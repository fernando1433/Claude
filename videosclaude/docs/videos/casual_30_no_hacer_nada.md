# Claude, si no hago nada, ¿es meditar?

**Archivo de guion:** `guiones/casual_30_no_hacer_nada.json` · **Ambiente:** `noche_casa` · **Duración:** 36 s (216 frames de animación a 6 fps)

Filosofía de sofá: ¿mirar el techo es meditación? Claude responde con más cariño que rigor.

**Gancho (primera frase):** «Claude, si no hago nada, ¿es meditar?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_30_no_hacer_nada.json salidas/casual_30_no_hacer_nada.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.6 | Humano | Claude, si no hago nada, / ¿es meditar? | `humano` | confundido | mensajes (36.0 s) |
| 2 | 3.6–6.8 | Claude | Depende. ¿Qué haces / exactamente? | `monitor` | mira_izq |  |
| 3 | 6.8–8.8 | Humano | Mirar el techo. | `dos` | bobo |  |
| 4 | 8.8–10.9 | Claude | ¿Y piensas en algo? | `claude_ojos` | idle |  |
| 5 | 10.9–13.7 | Humano | En si he apagado el horno. | `humano` | preocupado |  |
| 6 | 13.7–17.4 | Claude | Eso es más preocupación / que meditación. | `cenital` | mira_der |  |
| 7 | 17.4–20.6 | Humano | ¿Y si lo apago y miro el techo? | `dos` | ilusionado |  |
| 8 | 20.6–24.1 | Claude | Ahora sí. Es meditación. / Con extras. | `monitor` | feliz |  |
| 9 | 24.1–26.1 | Humano | ¿Y cuánto tiempo? | `humano` | bobo |  |
| 10 | 26.1–29.7 | Claude | El que quieras. / El techo es paciente. | `claude_ojos` | mira_arriba, empuje de cámara |  |
| 11 | 29.7–32.1 | Humano | Voy a meditar un rato. | `dos` | feliz |  |
| 12 | 32.1–36.0 | Claude | Y apaga el horno. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
