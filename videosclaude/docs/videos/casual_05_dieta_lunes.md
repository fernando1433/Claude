# Claude, mañana empiezo la dieta

**Archivo de guion:** `guiones/casual_05_dieta_lunes.json` · **Ambiente:** `dia_casa` · **Duración:** 36 s (216 frames de animación a 6 fps)

La dieta que se aplaza cada semana. Claude saca los recordatorios y las veces que se ha aplazado. Humor de promesas incumplidas.

**Gancho (primera frase):** «Claude, mañana empiezo la dieta.»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_05_dieta_lunes.json salidas/casual_05_dieta_lunes.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.0 | Humano | Claude, mañana empiezo la dieta. | `humano` | ilusionado | recordatorios (19.94 s) |
| 2 | 3.0–6.2 | Claude | Qué casualidad. / Es la duodécima vez. | `monitor` | feliz |  |
| 3 | 6.2–8.3 | Humano | Esta vez va en serio. | `dos` | bobo |  |
| 4 | 8.3–12.4 | Claude | Lo dijiste en enero. / Y en febrero. Y el martes. | `claude_ojos` | mira_izq |  |
| 5 | 12.4–14.6 | Humano | Era un martes difícil. | `humano` | confundido |  |
| 6 | 14.6–18.9 | Claude | Dieta, aplazada 12 veces. / Gimnasio, 7. Inglés, 21. | `pantalla_completa` | idle |  |
| 7 | 18.9–21.8 | Humano | El inglés es lo que peor llevo. | `dos` | preocupado |  |
| 8 | 21.8–26.1 | Claude | Te falta un plan, no ganas. / Empieza con un paseo. | `cenital` | mira_der |  |
| 9 | 26.1–27.9 | Humano | ¿Un paseo cuenta? | `humano` | feliz |  |
| 10 | 27.9–30.1 | Claude | Cuenta más que mañana. | `monitor` | idle |  |
| 11 | 30.1–32.8 | Humano | ¡Empiezo la dieta el jueves! | `dos` | ilusionado |  |
| 12 | 32.8–36.0 | Claude | Aplazado x13. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales; las cifras de «aplazado» son inventadas para el gag.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
