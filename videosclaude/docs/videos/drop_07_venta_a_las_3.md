# Claude, ¡tengo una venta a las 3 de la mañana!

![vista previa](img/drop_07_venta_a_las_3.jpg)

**Archivo de guion:** `guiones/drop_07_venta_a_las_3.json` · **Ambiente:** `noche_tienda` · **Duración:** 40 s (240 frames de animación a 6 fps)

Una venta de madrugada: celebración, sospecha y revisión de señales de fraude con calma.

**Gancho (primera frase):** «¡Claude! ¡Tengo una venta a las 3 de la mañana!»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/drop_07_venta_a_las_3.json salidas/drop_07_venta_a_las_3.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/noche_tienda/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–4.0 | Humano | ¡Claude! ¡Tengo una venta / a las 3 de la mañana! | `humano` | ilusionado | pedido (13.21 s) |
| 2 | 4.0–7.1 | Claude | Enhorabuena. ¿De dónde / es el pedido? | `monitor` | mira_izq |  |
| 3 | 7.1–9.0 | Humano | Mira, eso da igual. | `dos` | bobo |  |
| 4 | 9.0–12.6 | Claude | No da igual. Mira país, / email y dirección. | `claude_ojos` | idle |  |
| 5 | 12.6–16.1 | Humano | Un email con números / y una dirección rara. | `humano` | confundido |  |
| 6 | 16.1–20.4 | Claude | Pedido grande, urgente, / con email raro. Sospechoso. | `cenital` | mira_der |  |
| 7 | 20.4–22.1 | Humano | ¿Fraude? | `dos` | preocupado |  |
| 8 | 22.1–25.9 | Claude | Puede. Verifica el pago antes / de enviar nada. | `monitor` | feliz |  |
| 9 | 25.9–27.9 | Humano | ¿Y cómo lo verifico? | `humano` | confundido |  |
| 10 | 27.9–33.5 | Claude | Pasarela de pagos: revisa el / estado del cobro y la alerta de riesgo. | `claude_ojos` | idle, empuje de cámara |  |
| 11 | 33.5–36.8 | Humano | Vale, espero a que / el pago se confirme. | `dos` | ilusionado |  |
| 12 | 36.8–40.0 | Claude | Eso. Y duerme. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Vídeo de humor, sin datos reales.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
