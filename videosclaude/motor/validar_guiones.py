"""Valida todos los guiones: ambiente, planos disponibles en esa sala, tipos de pantalla, emociones/poses/estados, anchos de subtitulo.
Uso: python3 -I motor/validar_guiones.py"""
import os, sys, json, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pantallas import PANTALLAS
from PIL import ImageFont
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FUENTE = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 44)
LITE = {'humano', 'dos', 'general', 'monitor', 'monitor_espalda', 'monitor_lateral', 'claude_ojos', 'cenital', 'pantalla_completa'}
PLANOS = {'noche_trading': LITE | {'claude', 'espalda'}}
EMO = {'neutral', 'feliz', 'preocupado', 'burlon', 'bobo', 'ilusionado', 'confundido'}
POSES = {'type', 'pensar', 'senalar', 'hombros', 'mira'}; CL = {'idle', 'feliz', 'mira_izq', 'mira_der', 'mira_arriba'}
mal = 0
for f in sorted(glob.glob(f'{RAIZ}/guiones/*.json')):
    G = json.load(open(f)); n = os.path.basename(f); amb = G.get('ambiente', 'noche_trading'); ok = PLANOS.get(amb, LITE); er = []
    for i, L in enumerate(G['lineas'], 1):
        if L['plano'] not in ok: er.append(f'l{i}: plano {L["plano"]} no existe en {amb}')
        if L['quien'] == 'humano' and L.get('emocion', 'neutral') not in EMO: er.append(f'l{i}: emocion {L.get("emocion")}')
        if L.get('pose') and L['pose'] not in POSES: er.append(f'l{i}: pose {L["pose"]}')
        if L.get('claude_estado') and L['claude_estado'] not in CL: er.append(f'l{i}: estado {L["claude_estado"]}')
        if L.get('pantalla'):
            t = L['pantalla']['tipo'] if isinstance(L['pantalla'], dict) else L['pantalla']
            if t not in PANTALLAS and not os.path.exists(f'{RAIZ}/biblioteca/pantallas/{t}.png'): er.append(f'l{i}: pantalla {t}')
        for ln in L['texto'].split('\n'):
            if FUENTE.getlength(ln) > 1000: er.append(f'l{i}: subtitulo ancho "{ln}"')
    if G['lineas'][-1]['fin'] < G['duracion'] - 0.05: er.append('la ultima linea acaba antes que el video')
    print(('OK   ' if not er else 'FALLA'), n, G['duracion'], 's', '; '.join(er)); mal += bool(er)
sys.exit(1 if mal else 0)
