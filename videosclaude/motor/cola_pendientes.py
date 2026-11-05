"""DEMONIO de montaje: cada 30 s mira guiones/*.json y monta (con montar_video.py) todo video cuyo ambiente ya este renderizado
(marcador LISTO_<ambiente> en la carpeta de logs) y cuyo mp4 no exista o sea mas viejo que su guion. Asi, al editar un guion se remonta solo.
Uso: python3 -I motor/cola_pendientes.py <logdir>      (parar: crear <logdir>/PARAR_MONTAJE)"""
import os, sys, json, time, subprocess, glob
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); LOG = sys.argv[1]
FALLIDOS = set()
def pendientes():
    out = []
    for f in sorted(glob.glob(f'{RAIZ}/guiones/*.json')):
        vid = os.path.basename(f)[:-5]
        if vid.startswith('ejemplo_') or vid in FALLIDOS: continue
        try: amb = json.load(open(f)).get('ambiente', 'noche_trading')
        except Exception: continue
        mp4 = f'{RAIZ}/salidas/{vid}.mp4'
        if not os.path.exists(f'{LOG}/LISTO_{amb}'): continue
        if os.path.exists(mp4) and os.path.getmtime(mp4) >= os.path.getmtime(f): continue
        out.append((os.path.exists(mp4), vid, f, mp4))     # primero los que NO existen, luego los desactualizados
    return sorted(out)

while not os.path.exists(f'{LOG}/PARAR_MONTAJE'):
    cola = pendientes()
    if not cola: time.sleep(30); continue
    _, vid, f, mp4 = cola[0]
    with open(f'{LOG}/montaje.log', 'a') as lg:
        lg.write(f'montando {vid} ({time.strftime("%H:%M:%S")})\n'); lg.flush()
        r = subprocess.run([sys.executable, '-I', f'{RAIZ}/motor/montar_video.py', f, mp4], stdout=lg, stderr=lg)
        lg.write(f'{"listo" if r.returncode == 0 else "ERROR"} {vid} ({time.strftime("%H:%M:%S")})\n')
    open(f'{LOG}/VIDEO_{vid}', 'w').close()
    if r.returncode != 0: FALLIDOS.add(vid)      # no bloquea al resto; se reintenta al reiniciar el demonio
