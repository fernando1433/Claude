# Claude, dime la verdad: ¿canto mal?

![vista previa](img/micro_10_dime_la_verdad.jpg)

**Archivo de guion:** `guiones/micro_10_dime_la_verdad.json` · **Ambiente:** `noche_casa` · **Duración:** 20 s (120 frames de animación a 6 fps)

Micro-vídeo de humor de ~20 s, sin datos reales.

**Gancho (primera frase):** «Claude, dime la verdad: ¿canto mal?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/micro_10_dime_la_verdad.json salidas/micro_10_dime_la_verdad.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–4.3 | Humano | Claude, dime la verdad: / ¿canto mal? | `humano` | ilusionado | mensajes (20.0 s) |
| 2 | 4.3–8.7 | Claude | Tu vecino tiene una nota / sobre eso. | `monitor` | mira_izq |  |
| 3 | 8.7–11.2 | Humano | ¿Es un cumplido? | `dos` | bobo |  |
| 4 | 11.2–13.7 | Claude | Es una nota. | `claude_ojos` | feliz |  |
| 5 | 13.7–16.2 | Humano | Seguiré cantando. | `humano` | feliz |  |
| 6 | 16.2–20.0 | Claude | Bajito. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
