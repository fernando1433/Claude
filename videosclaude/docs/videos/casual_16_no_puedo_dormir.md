# Claude, no puedo dormir

**Archivo de guion:** `guiones/casual_16_no_puedo_dormir.json` · **Ambiente:** `noche_casa` · **Duración:** 38 s (228 frames de animación a 6 fps)

Insomnio de madrugada: pensamientos absurdos, contar ovejas y un Claude que por una vez te dice que cierres los ojos.

**Gancho (primera frase):** «Claude, no puedo dormir.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_16_no_puedo_dormir.json salidas/casual_16_no_puedo_dormir.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.6 | Humano | Claude, no puedo dormir. | `humano` | preocupado | mensajes (32.86 s) |
| 2 | 2.6–4.6 | Claude | ¿Qué hora es? | `monitor` | idle |  |
| 3 | 4.6–6.6 | Humano | Las 3:47. | `dos` | bobo |  |
| 4 | 6.6–8.7 | Claude | ¿En qué piensas? | `claude_ojos` | mira_izq |  |
| 5 | 8.7–12.3 | Humano | En por qué los patos no tienen frío. | `humano` | confundido |  |
| 6 | 12.3–16.3 | Claude | Es una gran pregunta. / Pero no a las 3:47. | `cenital` | mira_der |  |
| 7 | 16.3–18.6 | Humano | ¿Y si cuento ovejas? | `dos` | ilusionado |  |
| 8 | 18.6–22.6 | Claude | Cuéntalas. Pero no / las pongas a negociar. | `monitor` | feliz |  |
| 9 | 22.6–24.6 | Humano | Llevo 400. | `humano` | bobo |  |
| 10 | 24.6–26.6 | Claude | Qué rebaño. | `claude_ojos` | idle |  |
| 11 | 26.6–28.6 | Humano | ¿Qué hago? | `dos` | preocupado |  |
| 12 | 28.6–32.9 | Claude | Pantalla fuera. Luz fuera. / Yo me quedo aquí. | `pantalla_completa` | idle |  |
| 13 | 32.9–34.9 | Humano | ¿Seguro? | `humano` | confundido |  |
| 14 | 34.9–38.0 | Claude | Siempre. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
