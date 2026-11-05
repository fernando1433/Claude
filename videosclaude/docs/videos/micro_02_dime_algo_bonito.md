# Claude, dime algo bonito

![vista previa](img/micro_02_dime_algo_bonito.jpg)

**Archivo de guion:** `guiones/micro_02_dime_algo_bonito.json` · **Ambiente:** `dia_casa` · **Duración:** 20 s (120 frames de animación a 6 fps)

Micro-vídeo de humor de ~20 s, sin datos reales.

**Gancho (primera frase):** «Claude, dime algo bonito.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/micro_02_dime_algo_bonito.json salidas/micro_02_dime_algo_bonito.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.5 | Humano | Claude, dime algo bonito. | `humano` | ilusionado | mensajes (20.0 s) |
| 2 | 3.5–6.8 | Claude | Tu wifi es muy estable. | `monitor` | feliz |  |
| 3 | 6.8–9.4 | Humano | ¿Eso es bonito? | `dos` | confundido |  |
| 4 | 9.4–12.0 | Claude | En lunes, sí. | `claude_ojos` | mira_izq |  |
| 5 | 12.0–14.6 | Humano | Dime algo más. | `humano` | bobo |  |
| 6 | 14.6–20.0 | Claude | Hoy has bebido agua. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
