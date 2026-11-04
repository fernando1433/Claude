# Las señales VIP de Telegram

**Archivo de guion:** `guiones/trading_02_senales_vip.json` · **Ambiente:** `dia_trading` · **Duración:** 45 s (270 frames de animación a 6 fps)

El trader paga 49 €/mes por un canal de señales. Claude le enseña cómo funciona un «pump & dump»: el admin compra antes, anuncia, el precio sube, él vende y tú te quedas con la pérdida. Claude le salva 380 € a tiempo.

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/trading_02_senales_vip.json salidas/trading_02_senales_vip.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_trading/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.7 | Humano | ¡Me he metido en un grupo / VIP de señales! | `general` | ilusionado | telegram (9.26 s) |
| 2 | 2.7–4.8 | Claude | Déjame adivinar: / 49 € al mes. | `monitor` | mira_izq |  |
| 3 | 4.8–6.7 | Humano | ¡El admin gana un 3.000 %! | `dos` | feliz, pose senalar |  |
| 4 | 6.7–9.3 | Claude | Casualmente, solo enseña / las que ganan. | `monitor_lateral` | idle |  |
| 5 | 9.3–11.0 | Humano | Hoy dice: compra $PERRO. | `humano` | bobo | telegram (10.56 s) |
| 6 | 11.0–12.9 | Claude | Un perro. Muy serio todo. | `monitor_lateral` | feliz |  |
| 7 | 12.9–14.6 | Humano | ¡Va a subir un 1.000 %! | `dos` | ilusionado |  |
| 8 | 14.6–18.3 | Claude | Sube porque lo dice el admin. / Cuando tú compras, él vende. | `cenital` | mira_der |  |
| 9 | 18.3–19.7 | Humano | ¿Eso es legal? | `humano` | confundido |  |
| 10 | 19.7–22.6 | Claude | Se llama pump & dump: / lo inflan y tú pagas. | `pantalla_completa` | idle |  |
| 11 | 22.6–24.2 | Humano | Yo ya compré... 400 €. | `dos` | preocupado, pose hombros |  |
| 12 | 24.2–26.4 | Claude | Vende YA. Aún recuperas 380 €. | `monitor` | feliz |  |
| 13 | 26.4–27.7 | Humano | ¿Cómo vendo? | `humano` | confundido |  |
| 14 | 27.7–31.2 | Claude | Botón rojo. Y adiós al VIP: / mira cómo luce tu cartera. | `pantalla_completa` | idle | cartera (3.68 s) |
| 15 | 31.2–32.6 | Humano | ¡Me quedan 380 €! | `dos` | preocupado |  |
| 16 | 32.6–35.5 | Claude | 380 € más de los que / habrías tenido sin mí. | `claude_ojos` | feliz, empuje de cámara |  |
| 17 | 35.5–37.2 | Humano | ¡Eres un genio, Claude! | `humano` | ilusionado |  |
| 18 | 37.2–40.5 | Claude | Dato real: 97 % de day traders / con +300 días pierde. | `pantalla_completa` | idle | verdad (3.38 s) |
| 19 | 40.5–42.4 | Humano | Pero yo soy del 3 %, ¿no? | `dos` | bobo |  |
| 20 | 42.4–45.0 | Claude | Claro. Seguro. / Yo traigo las palomitas. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- 97 % de los day traders brasileños que persistieron más de 300 días perdió dinero; solo el 0,5 % (8 de 1.551) ganó más que un sueldo básico de banca (estudio de la CVM de Brasil, 2013-2015).
  - Fuente: [Chague, De-Losso y Giovannetti — «Day Trading for a Living?» (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101)
  - Fuente: [Resumen del estudio (Quantpedia)](https://quantpedia.com/retail-day-trading-is-an-uphill-battle/)

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
