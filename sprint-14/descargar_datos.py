#!/usr/bin/env python3
"""Error404: descarga y verificación de los cuatro CSV de centros educativos."""
import argparse
import csv
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

PORTAL = 'https://datos.canarias.es/catalogos/general'
DATASET = 'centros-educativos-de-canarias'
FUENTE = f'{PORTAL}/dataset/{DATASET}'
API = f'{PORTAL}/api/3/action/package_show?id={DATASET}'
LICENCIA = 'https://creativecommons.org/licenses/by/4.0/'
AVISO = 'https://datos.canarias.es/portal/aviso-legal-y-condiciones-de-uso'
REFERENCIAS = {
    'centros.csv': ('00c041f31202487fdd47989a8bb140c10013de0eeb9aeca937fd5a6052721156', 1472, 33, 'Codigo'),
    'ensenanzas-autorizadas-por-centro.csv': ('eb1aa8a70eb498c91ee839a0a3f1622b9ae34cf2dd47bc7378b5871b2f8fa37e', 14138, 22, 'CodigoCentro'),
    'ensenanzas-impartidas-por-centro.csv': ('409f547eb31d9d36fbaf7521000beaa0a17874c4db1ead2e9b717995223ae251', 18324, 11, 'CodigoCentro'),
    'servicios-complementarios-por-centro.csv': ('a85ee42f8b582ae1d5dbddf137ff1ea8d20992164c50444f1e2fe03767985b3c', 972, 5, 'CodigoCentro'),
}

def obtener(url):
    if not url.startswith('https://'):
        raise ValueError(f'URL no HTTPS: {url}')
    with urlopen(Request(url, headers={'User-Agent': 'Error404-OrientaFP/1.0'}), timeout=90) as r:
        return r.read()

def verificar(nombre, datos):
    esperado, filas_ref, cols_ref, clave = REFERENCIAS[nombre]
    lector = csv.reader(io.StringIO(datos.decode('utf-8-sig')), strict=True)
    columnas = next(lector)
    if clave not in columnas or len(columnas) != cols_ref:
        raise ValueError(f'{nombre}: esquema inesperado')
    filas = 0
    for fila in lector:
        if len(fila) != len(columnas):
            raise ValueError(f'{nombre}: fila irregular {lector.line_num}')
        filas += 1
    if not filas:
        raise ValueError(f'{nombre}: CSV vacío')
    sha = hashlib.sha256(datos).hexdigest()
    return dict(archivo=nombre, bytes=len(datos), filas=filas, columnas=len(columnas), sha256=sha,
                sha256_referencia=esperado, filas_referencia=filas_ref, coincide_referencia=sha == esperado)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--destino', type=Path, default=Path(__file__).resolve().parent)
    p.add_argument('--solo-verificar', action='store_true', help='Comprueba copias locales sin conexión')
    p.add_argument('--aceptar-version-nueva', action='store_true', help='Permite descargar datos distintos a la referencia en una carpeta nueva')
    args = p.parse_args()
    destino = args.destino.resolve()
    recursos = {}
    meta = {}
    if not args.solo_verificar:
        respuesta = json.loads(obtener(API))
        if not respuesta.get('success'):
            raise ValueError('La API no devolvió el conjunto solicitado')
        meta = respuesta['result']
        for nombre in REFERENCIAS:
            candidatos = [r for r in meta['resources'] if r.get('name','').strip().lower() == nombre]
            if len(candidatos) != 1:
                raise ValueError(f'No se identificó un recurso único: {nombre}')
            recursos[nombre] = candidatos[0]
    resultados = []
    pendientes = {}
    for nombre in REFERENCIAS:
        ruta = destino / nombre
        recurso = recursos.get(nombre, {})
        datos = ruta.read_bytes() if args.solo_verificar else obtener(recurso['url'])
        info = verificar(nombre, datos)
        info.update(url_descarga=recurso.get('url'), fecha_actualizacion_recurso=recurso.get('last_modified'))
        resultados.append(info)
        print(f"{nombre}: {info['filas']} filas | SHA-256 {'OK' if info['coincide_referencia'] else 'DISTINTO'}")
        if not args.solo_verificar:
            if ruta.exists() and ruta.read_bytes() != datos:
                raise ValueError(f'No se sobrescribe {ruta}; elige otra carpeta con --destino')
            pendientes[ruta] = datos
    coincide = all(r['coincide_referencia'] for r in resultados)
    if not args.solo_verificar and not coincide and not args.aceptar_version_nueva:
        raise ValueError('La fuente ha cambiado. No se guardan CSV; revisa la versión o usa --aceptar-version-nueva en otra carpeta.')
    destino.mkdir(parents=True, exist_ok=True)
    for ruta, datos in pendientes.items():
        if not ruta.exists():
            with ruta.open('xb') as f:
                f.write(datos)
    informe = dict(proyecto='Error404 – OrientaFP Canarias', fuente=FUENTE, organismo='Gobierno de Canarias',
                   licencia_referencia=LICENCIA, condiciones=AVISO, licencia_catalogo=meta.get('license_title'),
                   fecha_actualizacion_catalogo=meta.get('metadata_modified'),
                   fecha_control=datetime.now(timezone.utc).isoformat(),
                   modo='verificacion_local' if args.solo_verificar else 'descarga', archivos=resultados)
    ruta_informe = destino / ('registro_datos_' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '.json')
    with ruta_informe.open('x', encoding='utf-8') as f:
        json.dump(informe, f, ensure_ascii=False, indent=2)
    print(f'Registro: {ruta_informe}')
    return 0 if coincide or args.aceptar_version_nueva else 1

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, csv.Error) as error:
        raise SystemExit(f'Error: {error}')
