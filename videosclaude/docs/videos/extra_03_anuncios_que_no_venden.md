# Anuncios que no venden

**Archivo de guion:** `guiones/extra_03_anuncios_que_no_venden.json` · **Ambiente:** `dia_tienda` · **Duración:** 45 s (270 frames de animación a 6 fps)

El tonto gastó 124 € en anuncios y consiguió 3 ventas. Claude le enseña el embudo, el ROAS (0,75) y qué probar antes de «subir el presupuesto».

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/extra_03_anuncios_que_no_venden.json salidas/extra_03_anuncios_que_no_venden.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_tienda/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.3 | Humano | Gasté 124 € en anuncios. / ¡Ahora lloverán ventas! | `general` | ilusionado | anuncios (22.6 s) |
| 2 | 3.3–4.8 | Claude | Llovieron. Tres. | `monitor` | mira_izq |  |
| 3 | 4.8–6.8 | Humano | ¿Tres? ¿De 15.800 personas? | `dos` | bobo |  |
| 4 | 6.8–9.9 | Claude | Eso es un embudo. Mira / qué estrecho se pone. | `pantalla_completa` | idle |  |
| 5 | 9.9–11.3 | Humano | ¿Qué es el ROAS? | `humano` | confundido |  |
| 6 | 11.3–14.8 | Claude | Lo que ingresas por cada euro / de anuncio. Tú: 0,75. | `claude_ojos` | feliz, empuje de cámara |  |
| 7 | 14.8–16.3 | Humano | ¿Entonces pierdo? | `dos` | preocupado |  |
| 8 | 16.3–20.3 | Claude | Por debajo de 1 pierdes. Y por / debajo de tu margen, también. | `cenital` | mira_der |  |
| 9 | 20.3–22.0 | Humano | ¿Subo el presupuesto? | `humano` | bobo, pose pensar |  |
| 10 | 22.0–25.7 | Claude | Claro: si algo no funciona, / multiplícalo. Qué lógica. | `monitor` | mira_arriba |  |
| 11 | 25.7–27.1 | Humano | ¿Y entonces? | `dos` | confundido |  |
| 12 | 27.1–30.8 | Claude | Cambia la imagen, prueba otro / público y revisa la web. | `pantalla_completa` | idle |  |
| 13 | 30.8–32.3 | Humano | ¿Y la web importa? | `humano` | ilusionado |  |
| 14 | 32.3–36.4 | Claude | Si no da confianza, nadie compra, / aunque el anuncio sea oro. | `monitor_lateral` | idle |  |
| 15 | 36.4–38.2 | Humano | Probaré con 20 € al día. | `dos` | feliz |  |
| 16 | 38.2–41.5 | Claude | Mejor 5 €. Aprende barato / antes de gastar caro. | `claude_ojos` | feliz, empuje de cámara |  |
| 17 | 41.5–42.9 | Humano | ¡Con 5 € al día! | `humano` | ilusionado |  |
| 18 | 42.9–45.0 | Claude | Qué madurez. / Anoto la fecha. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- ROAS = ingresos ÷ gasto en anuncios. Por debajo de 1 pierdes dinero en ese canal; el ROAS mínimo para ser rentable depende de tu margen (ver vídeo drop_01). Cifras del ejemplo ilustrativas.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
