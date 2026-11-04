# Un día con Claude (te lleva la vida entera)

**Archivo de guion:** `guiones/extra_02_un_dia_con_claude.json` · **Ambiente:** `dia_tienda` · **Duración:** 45 s (270 frames de animación a 6 fps)

«Claude, hazme el día». Agenda con 3 reuniones menos, 214 correos sin leer, tareas hechas… y la madre del tonto. Humor de oficina, sin datos reales.

**Gancho (primera frase):** «¡Claude, hazme el día!»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/extra_02_un_dia_con_claude.json salidas/extra_02_un_dia_con_claude.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_tienda/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–1.9 | Humano | ¡Claude, hazme el día! | `general` | ilusionado | chat (4.44 s) |
| 2 | 1.9–4.0 | Claude | Ya lo hice. / Mira tu agenda. | `monitor` | feliz |  |
| 3 | 4.0–6.2 | Humano | ¿Hoy tengo cinco reuniones? | `dos` | confundido | calendario (6.37 s) |
| 4 | 6.2–9.7 | Claude | Tres sobraban. Las cancelé. / Ahora podrás dormir. | `pantalla_completa` | idle |  |
| 5 | 9.7–11.3 | Humano | ¡Eres el mejor! | `humano` | ilusionado |  |
| 6 | 11.3–14.1 | Claude | Aún no. Mira tu correo: / 214 sin leer. | `cenital` | mira_der |  |
| 7 | 14.1–15.6 | Humano | ¿¡214!? | `dos` | preocupado, pose hombros | email (6.29 s) |
| 8 | 15.6–19.7 | Claude | Respondí 9, archivé 150. / Los 55 de tu madre, no los toco. | `pantalla_completa` | idle |  |
| 9 | 19.7–21.4 | Humano | Mamá es importante. | `humano` | bobo |  |
| 10 | 21.4–25.2 | Claude | Lo sé. El último dice «¿has comido?». / Respóndelo tú. | `claude_ojos` | feliz, empuje de cámara |  |
| 11 | 25.2–26.7 | Humano | ¡Ya he comido! | `dos` | ilusionado |  |
| 12 | 26.7–30.4 | Claude | Mentira: tu tarjeta dice / «3 cafés». Tareas, vamos. | `monitor` | mira_arriba |  |
| 13 | 30.4–31.9 | Humano | ¿Qué tareas? | `humano` | confundido | tareas (6.22 s) |
| 14 | 31.9–36.0 | Claude | Facturas, pedidos, anuncios... / Ya están. Solo queda una. | `pantalla_completa` | idle |  |
| 15 | 36.0–37.5 | Humano | ¿Cuál? | `dos` | preocupado |  |
| 16 | 37.5–39.9 | Claude | Agradecérmelo. / Con una sonrisa. | `monitor_lateral` | feliz |  |
| 17 | 39.9–41.5 | Humano | ¡Gracias, Claude! | `humano` | feliz |  |
| 18 | 41.5–45.0 | Claude | De nada. Y la próxima vez, / nada de 214 sin leer. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor: las cifras (214 correos, 5 reuniones…) son inventadas para el gag.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
