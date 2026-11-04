# Claude, ¿va a llover?

**Archivo de guion:** `guiones/casual_21_va_a_llover.json` · **Ambiente:** `dia_casa` · **Duración:** 28 s (168 frames de animación a 6 fps)

Preguntarle a Claude por la lluvia cuando tienes ventana. Un clásico.

**Gancho (primera frase):** «Claude, ¿va a llover?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_21_va_a_llover.json salidas/casual_21_va_a_llover.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.5 | Humano | Claude, ¿va a llover? | `humano` | confundido | mensajes (28.0 s) |
| 2 | 2.5–4.7 | Claude | No tengo ventana. | `monitor` | mira_izq |  |
| 3 | 4.7–6.9 | Humano | Yo sí. | `dos` | bobo |  |
| 4 | 6.9–9.2 | Claude | Pues mira por ella. | `claude_ojos` | idle |  |
| 5 | 9.2–11.4 | Humano | Está nublado. | `humano` | confundido |  |
| 6 | 11.4–13.6 | Claude | Entonces, quizás. | `cenital` | mira_der |  |
| 7 | 13.6–15.7 | Humano | ¿Cojo paraguas? | `dos` | preocupado |  |
| 8 | 15.7–21.2 | Claude | Si dudas, cógelo. Si no llueve, / es un bastón elegante. | `monitor` | feliz |  |
| 9 | 21.2–23.4 | Humano | Muy sabio. | `humano` | ilusionado |  |
| 10 | 23.4–28.0 | Claude | Lo sé. Y sin ventana. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
