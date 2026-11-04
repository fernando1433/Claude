# Tu primer pedido (y la realidad)

**Archivo de guion:** `guiones/drop_03_primer_pedido.json` · **Ambiente:** `atardecer_tienda` · **Duración:** 45 s (270 frames de animación a 6 fps)

¡Primer pedido! El tonto se cree rico… hasta que el cliente espera 25 días y escribe en mayúsculas. Claude le enseña a contestar, el derecho de desistimiento de 14 días, el contracargo y el IVA de importación. Humor y datos reales.

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/drop_03_primer_pedido.json salidas/drop_03_primer_pedido.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/atardecer_tienda/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–1.7 | Humano | ¡CLAUDE! ¡PRIMER PEDIDO! | `general` | ilusionado | pedido (9.04 s) |
| 2 | 1.7–4.3 | Claude | Enhorabuena. Ahora pídeselo / al proveedor. | `monitor` | feliz |  |
| 3 | 4.3–5.6 | Humano | ¿Ya soy rico? | `dos` | bobo |  |
| 4 | 5.6–8.6 | Claude | Eres rico: 3,44 €. / Si nada falla. Spoiler: falla. | `pantalla_completa` | idle |  |
| 5 | 8.6–11.1 | Claude | Y tu cliente espera / 25 días. Por barco. | `monitor_lateral` | idle | tracking (7.07 s) |
| 6 | 11.1–12.9 | Humano | Pero en la web puse 3 días. | `dos` | confundido |  |
| 7 | 12.9–15.7 | Claude | Eso tiene nombre: / prometer lo que no puedes. | `claude_ojos` | mira_izq, empuje de cámara |  |
| 8 | 15.7–17.5 | Humano | Uy. Ha escrito el cliente. | `humano` | preocupado | cliente (5.1 s) |
| 9 | 17.5–20.8 | Claude | En mayúsculas. Mala señal. / Responde con calma y datos. | `pantalla_completa` | idle |  |
| 10 | 20.8–22.1 | Humano | ¿Y si no contesto? | `dos` | preocupado, pose hombros |  |
| 11 | 22.1–25.4 | Claude | Pedirá el dinero a su banco: / contracargo. Y te cuesta. | `cenital` | mira_der |  |
| 12 | 25.4–27.4 | Humano | ¿Puede devolverlo sin motivo? | `humano` | bobo | ley (5.94 s) |
| 13 | 27.4–30.6 | Claude | Sí: 14 días naturales. / Y le devuelves hasta el envío. | `pantalla_completa` | idle |  |
| 14 | 30.6–32.1 | Humano | ¿Y el IVA que pagué? | `dos` | preocupado |  |
| 15 | 32.1–36.0 | Claude | Desde 2021, IVA desde el primer / euro importado. Revisa márgenes. | `monitor` | feliz |  |
| 16 | 36.0–37.5 | Humano | ¿Entonces me conviene? | `humano` | confundido |  |
| 17 | 37.5–41.0 | Claude | Si cuidas envíos y atención, sí. / Si no, es un hobby caro. | `claude_ojos` | feliz |  |
| 18 | 41.0–42.5 | Humano | ¡Voy a hacerlo bien! | `dos` | ilusionado |  |
| 19 | 42.5–45.0 | Claude | Primera frase sensata. / La voy a apuntar. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Derecho de desistimiento: 14 días naturales para devolver compras a distancia en la UE sin dar motivos (Directiva 2011/83/UE); el vendedor devuelve el dinero, incluido el coste de entrega estándar. Hay excepciones (p. ej. productos personalizados o precintados abiertos).
  - Fuente: [Plazo de 14 días para devolver compras online en la UE (Consumer.es)](https://www.consumer.es/tecnologia/el-plazo-de-devolucion-para-las-compras-por-internet-en-la-ue-sera-de-14-dias.html)
  - Fuente: [Derecho de desistimiento en compras online (Legálitas)](https://www.legalitas.com/actualidad/derecho-la-devolucion-de-tu-compra-online)
- IVA en importaciones: desde el 1/7/2021 se paga IVA desde el primer euro (adiós a la exención de 22 €); IOSS opcional hasta 150 €.
  - Fuente: [Nuevas reglas de IVA para el comercio electrónico en la UE desde el 1/7/2021 (Organización Mundial de Aduanas)](https://www.wcoomd.org/es-es/media/newsroom/2021/june/the-european-union-introduces-new-value-added-tax-rules-for-e-commerce-from-1-july-202.aspx)
  - Fuente: [Fin de la exención de 22 € y ventanilla única de importación IOSS (Avalara)](https://www.avalara.com/vatlive/en/vat-news/eu-2021-ending--22-import-vat-exemption--new-ioss-return.html)
- Contracargo: el cliente puede reclamar a su banco/tarjeta el cobro de un pedido que no recibió; suele implicar una tarifa para el comercio.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
