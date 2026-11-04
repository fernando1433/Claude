# Claude, ¿le escribo a mi ex?

**Archivo de guion:** `guiones/casual_15_escribir_al_ex.json` · **Ambiente:** `noche_casa` · **Duración:** 40 s (240 frames de animación a 6 fps)

Las 2 de la madrugada y el dedo sobre el chat de la ex. Claude intenta evitarlo con lógica, ternura y mucha paciencia.

**Gancho (primera frase):** «Claude... ¿le escribo a mi ex?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/casual_15_escribir_al_ex.json salidas/casual_15_escribir_al_ex.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.8 | Humano | Claude... ¿le escribo a mi ex? | `humano` | preocupado | mensajes (40.0 s) |
| 2 | 2.8–4.7 | Claude | ¿Qué hora es? | `monitor` | mira_izq |  |
| 3 | 4.7–7.0 | Humano | Las dos de la madrugada. | `dos` | bobo |  |
| 4 | 7.0–8.8 | Claude | No. | `claude_ojos` | idle |  |
| 5 | 8.8–10.7 | Humano | Solo un «hola». | `humano` | confundido |  |
| 6 | 10.7–15.2 | Claude | Nadie escribe «hola» a las 2 / para decir solo «hola». | `cenital` | mira_der |  |
| 7 | 15.2–17.9 | Humano | Lo hago con buena intención. | `dos` | ilusionado |  |
| 8 | 17.9–22.4 | Claude | Las buenas intenciones se / envían a las 2 de la tarde. | `monitor` | feliz |  |
| 9 | 22.4–24.3 | Humano | ¿Y si me contesta? | `humano` | preocupado |  |
| 10 | 24.3–29.0 | Claude | Entonces tendrás una / conversación a las 2 de la mañana. | `claude_ojos` | mira_arriba, empuje de cámara |  |
| 11 | 29.0–30.9 | Humano | Tienes razón. | `dos` | confundido |  |
| 12 | 30.9–33.9 | Claude | Deja el móvil. Bebe agua. / Duerme. | `pantalla_completa` | idle |  |
| 13 | 33.9–36.0 | Humano | ¿Y mañana le escribo? | `humano` | bobo |  |
| 14 | 36.0–40.0 | Claude | Mañana hablamos de eso. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
