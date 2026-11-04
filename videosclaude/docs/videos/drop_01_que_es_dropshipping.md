# ¿Qué es el dropshipping? (spoiler: 3,44 €)

**Archivo de guion:** `guiones/drop_01_que_es_dropshipping.json` · **Ambiente:** `dia_tienda` · **Duración:** 45 s (270 frames de animación a 6 fps)

El tonto cree que el dropshipping es «vender sin tener nada, magia». Claude le explica cómo funciona, le enseña el envío de 18-35 días y, con una calculadora, que de 29,90 € le quedan 3,44 €. Y el ROAS mínimo para no perder.

**Gancho (primera frase):** «¡Voy a vender sin tener nada! ¡Magia!»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/drop_01_que_es_dropshipping.json salidas/drop_01_que_es_dropshipping.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_tienda/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.6 | Humano | ¡Voy a vender sin tener / nada! ¡Magia! | `general` | ilusionado | catalogo (7.31 s) |
| 2 | 2.6–5.9 | Claude | Magia no: dropshipping. / Tú vendes, otro envía. | `monitor` | feliz |  |
| 3 | 5.9–7.3 | Humano | ¿Y yo qué hago? | `humano` | confundido |  |
| 4 | 7.3–10.7 | Claude | La tienda y los anuncios. / El proveedor, el resto. | `pantalla_completa` | idle |  |
| 5 | 10.7–12.7 | Humano | ¡Esta taza me sale a 8 €! | `dos` | feliz, pose senalar | proveedor (8.64 s) |
| 6 | 12.7–15.1 | Claude | Mira el envío: / 18 a 35 días. Días. | `monitor_lateral` | idle |  |
| 7 | 15.1–17.0 | Humano | Son clientes pacientes. | `humano` | bobo |  |
| 8 | 17.0–19.4 | Claude | Quieren su taza ayer. / Y lo saben. | `claude_ojos` | mira_izq, empuje de cámara |  |
| 9 | 19.4–20.9 | Humano | La vendo a 29,90 €. | `dos` | ilusionado | margen (6.63 s) |
| 10 | 20.9–24.5 | Claude | 29,90 menos coste, anuncios, / comisión e IVA: 3,44 €. | `pantalla_completa` | idle |  |
| 11 | 24.5–26.0 | Humano | ¿¡3,44 €!? | `humano` | preocupado |  |
| 12 | 26.0–29.6 | Claude | Y si el anuncio cuesta 12 €. / Si cuesta más, pierdes. | `cenital` | mira_der |  |
| 13 | 29.6–31.3 | Humano | Pues la vendo a 99 €. | `dos` | bobo |  |
| 14 | 31.3–34.9 | Claude | Y yo me pongo traje: banquero. / Los clientes comparan. | `monitor` | feliz |  |
| 15 | 34.9–36.6 | Humano | ¿Cuánto margen busco? | `humano` | confundido |  |
| 16 | 36.6–40.5 | Claude | Que venda ≥3 veces su coste. / Pequeño, ligero y no frágil. | `monitor_lateral` | idle |  |
| 17 | 40.5–42.4 | Humano | Aburrido... ¡pero rico! | `humano` | feliz |  |
| 18 | 42.4–45.0 | Claude | Paciencia. Y números. / Muchos números. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Cuenta del ejemplo (ilustrativa): precio 29,90 € − coste 8,10 € − anuncio 12,00 € − comisión de cobro 1,17 € (2,9 % + 0,30 €) − IVA 21 % incluido 5,19 € = beneficio 3,44 €. ROAS mínimo = precio ÷ (precio − coste − comisión − IVA) = 1,94. Son cifras de ejemplo, no una promesa.
- Desde el 1 de julio de 2021 se paga IVA en todas las importaciones comerciales a la UE (se acabó la exención de 22 €).
  - Fuente: [Nuevas reglas de IVA para el comercio electrónico en la UE desde el 1/7/2021 (Organización Mundial de Aduanas)](https://www.wcoomd.org/es-es/media/newsroom/2021/june/the-european-union-introduces-new-value-added-tax-rules-for-e-commerce-from-1-july-202.aspx)
  - Fuente: [Fin de la exención de 22 € y ventanilla única de importación IOSS (Avalara)](https://www.avalara.com/vatlive/en/vat-news/eu-2021-ending--22-import-vat-exemption--new-ioss-return.html)

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
