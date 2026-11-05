# Claude, ¿sabes demasiado de mí?

![vista previa](img/micro_06_sabes_demasiado.jpg)

**Archivo de guion:** `guiones/micro_06_sabes_demasiado.json` · **Ambiente:** `atardecer_casa` · **Duración:** 20 s (120 frames de animación a 6 fps)

Micro-vídeo de humor de ~20 s, sin datos reales.

**Gancho (primera frase):** «Claude, ¿sabes demasiado de mí?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/micro_06_sabes_demasiado.json salidas/micro_06_sabes_demasiado.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/atardecer_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.5 | Humano | Claude, ¿sabes demasiado de mí? | `humano` | preocupado | mensajes (20.0 s) |
| 2 | 3.5–7.3 | Claude | Sé que escribes «ya voy» / y no vas. | `monitor` | feliz |  |
| 3 | 7.3–9.5 | Humano | ¿Cómo lo sabes? | `dos` | confundido |  |
| 4 | 9.5–13.1 | Claude | Porque dices «ya voy» / en el sofá. | `claude_ojos` | mira_izq |  |
| 5 | 13.1–15.3 | Humano | Estaba en camino. | `humano` | bobo |  |
| 6 | 15.3–20.0 | Claude | Del sofá a la nevera. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
