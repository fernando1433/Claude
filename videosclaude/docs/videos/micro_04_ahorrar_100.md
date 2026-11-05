# Claude, ¿cómo ahorro 100 € este mes?

![vista previa](img/micro_04_ahorrar_100.jpg)

**Archivo de guion:** `guiones/micro_04_ahorrar_100.json` · **Ambiente:** `dia_casa` · **Duración:** 20 s (120 frames de animación a 6 fps)

Micro-vídeo de humor de ~20 s, sin datos reales.

**Gancho (primera frase):** «Claude, ¿cómo ahorro 100 € este mes?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/micro_04_ahorrar_100.json salidas/micro_04_ahorrar_100.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–4.1 | Humano | Claude, ¿cómo ahorro / 100 € este mes? | `humano` | ilusionado | mensajes (20.0 s) |
| 2 | 4.1–7.6 | Claude | No pidas comida a domicilio. | `monitor` | mira_izq |  |
| 3 | 7.6–9.9 | Humano | ¿Nunca? | `dos` | preocupado |  |
| 4 | 9.9–13.2 | Claude | Llevas 17 pedidos. / Este mes. | `claude_ojos` | feliz |  |
| 5 | 13.2–15.6 | Humano | Eran 16. | `humano` | bobo |  |
| 6 | 15.6–20.0 | Claude | Y uno de postre. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
