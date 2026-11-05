# Claude, ¿soy muy mayor para empezar de cero?

![vista previa](img/micro_07_empezar_de_cero.jpg)

**Archivo de guion:** `guiones/micro_07_empezar_de_cero.json` · **Ambiente:** `dia_casa` · **Duración:** 20 s (120 frames de animación a 6 fps)

Micro-vídeo de humor de ~20 s, sin datos reales.

**Gancho (primera frase):** «Claude, ¿soy muy mayor para empezar de cero?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/micro_07_empezar_de_cero.json salidas/micro_07_empezar_de_cero.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–4.8 | Humano | Claude, ¿soy muy mayor para / empezar de cero? | `humano` | preocupado | mensajes (20.0 s) |
| 2 | 4.8–7.3 | Claude | Depende. ¿Para qué? | `monitor` | mira_izq |  |
| 3 | 7.3–9.6 | Humano | Para todo. | `dos` | bobo |  |
| 4 | 9.6–13.4 | Claude | Entonces no. Todo / es un buen plan. | `claude_ojos` | feliz |  |
| 5 | 13.4–15.7 | Humano | ¿De verdad? | `humano` | ilusionado |  |
| 6 | 15.7–20.0 | Claude | Empieza por uno. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
