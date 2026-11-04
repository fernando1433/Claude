# Mi contraseña es 123456

**Archivo de guion:** `guiones/util_01_contrasenas.json` · **Ambiente:** `dia_casa` · **Duración:** 42 s (252 frames de animación a 6 fps)

El humano presume de una contraseña «popular». Claude le enseña el dato real: es la más usada del mundo y se descifra en menos de un segundo; y qué hacer en su lugar.

**Gancho (primera frase):** «Claude, mi contraseña es 123456. ¿Es segura?»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/util_01_contrasenas.json salidas/util_01_contrasenas.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.5 | Humano | Claude, mi contraseña es 123456. / ¿Es segura? | `humano` | ilusionado | contrasenas (12.65 s) |
| 2 | 3.5–5.9 | Claude | Es la más usada del mundo. | `monitor` | mira_izq |  |
| 3 | 5.9–7.8 | Humano | ¡Entonces es popular! | `dos` | bobo |  |
| 4 | 7.8–12.0 | Claude | Y se descifra en menos de / un segundo (NordPass 2023). | `pantalla_completa` | idle |  |
| 5 | 12.0–14.4 | Humano | Pero nadie sabe que la uso. | `humano` | confundido |  |
| 6 | 14.4–18.4 | Claude | Es la primera que prueban. / Por algo es la primera. | `claude_ojos` | feliz, empuje de cámara |  |
| 7 | 18.4–20.4 | Humano | Entonces, ¿cuál pongo? | `dos` | preocupado |  |
| 8 | 20.4–24.3 | Claude | Una frase larga y absurda. / Distinta en cada web. | `cenital` | mira_der |  |
| 9 | 24.3–26.2 | Humano | «perro123», entonces. | `humano` | bobo |  |
| 10 | 26.2–29.4 | Claude | Eso es el mismo problema, / con un perro. | `monitor` | mira_arriba |  |
| 11 | 29.4–31.6 | Humano | ¿Y me las aprendo todas? | `dos` | confundido |  |
| 12 | 31.6–36.4 | Claude | No. Usa un gestor de contraseñas / y verificación en dos pasos. | `claude_ojos` | idle |  |
| 13 | 36.4–39.0 | Humano | ¡Con dos pasos soy invencible! | `humano` | ilusionado |  |
| 14 | 39.0–42.0 | Claude | Invencible no. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- «123456» fue la contraseña más usada del mundo en el informe de NordPass de 2023 (4.524.867 usos), seguida de «admin» y «12345678»; las tres se descifran en menos de un segundo. Los tiempos de descifrado son estimaciones y dependen del método de ataque.
  - Fuente: [Las contraseñas más usadas se descifran en menos de un segundo (CNBC, informe NordPass 2023)](https://www.cnbc.com/2023/11/16/most-common-passwords-70percent-can-be-cracked-in-less-than-a-second.html)
  - Fuente: [«123456» y «admin» se descifran en menos de un segundo (CBS News)](https://www.cbsnews.com/amp/news/password-security-hacking-common-words-numbers)
- Recomendaciones habituales: una frase larga, distinta en cada servicio, un gestor de contraseñas y la verificación en dos pasos. Orientación general, no sustituye a la guía de tu proveedor.

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
