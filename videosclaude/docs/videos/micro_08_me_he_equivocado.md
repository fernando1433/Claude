# Claude, me he equivocado muchísimo

![vista previa](img/micro_08_me_he_equivocado.jpg)

**Archivo de guion:** `guiones/micro_08_me_he_equivocado.json` · **Ambiente:** `noche_casa` · **Duración:** 20 s (120 frames de animación a 6 fps)

Micro-vídeo de humor de ~20 s, sin datos reales.

**Gancho (primera frase):** «Claude, me he equivocado muchísimo.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/micro_08_me_he_equivocado.json salidas/micro_08_me_he_equivocado.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–4.1 | Humano | Claude, me he equivocado / muchísimo. | `humano` | preocupado | mensajes (20.0 s) |
| 2 | 4.1–7.1 | Claude | Cuéntame. Con detalles. | `monitor` | mira_izq |  |
| 3 | 7.1–11.7 | Humano | Mandé el correo sin adjunto. / Tres veces. | `dos` | bobo |  |
| 4 | 11.7–14.0 | Claude | Tres veces. | `claude_ojos` | idle |  |
| 5 | 14.0–16.4 | Humano | ¿Soy tonto? | `humano` | confundido |  |
| 6 | 16.4–20.0 | Claude | Humano. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
