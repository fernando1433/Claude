# «Te pago el sofá por Bizum»

**Archivo de guion:** `guiones/util_04_bizum_inverso.json` · **Ambiente:** `dia_casa` · **Duración:** 40 s (240 frames de animación a 6 fps)

El humano vende un sofá y el «comprador» le envía una solicitud para que PAGUE él. Claude le explica el Bizum inverso y cómo no caer.

**Gancho (primera frase):** «Claude, me van a pagar el sofá por Bizum. ¡450 €!»

## Cómo se genera el vídeo
```bash
python3 -I motor/montar_video.py guiones/util_04_bizum_inverso.json salidas/util_04_bizum_inverso.mp4
```
El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/dia_casa/`.

## Guion plano a plano

| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |
|---|---|---|---|---|---|---|
| 1 | 0.0–3.4 | Humano | Claude, me van a pagar el sofá / por Bizum. ¡450 €! | `humano` | ilusionado | bizum (32.58 s) |
| 2 | 3.4–5.2 | Claude | Enséñame la pantalla. | `monitor` | mira_izq |  |
| 3 | 5.2–7.7 | Humano | Pone «Aceptar» en verde. Qué bien. | `dos` | bobo |  |
| 4 | 7.7–9.3 | Claude | ¿Y arriba qué pone? | `claude_ojos` | idle |  |
| 5 | 9.3–11.6 | Humano | «Estás a punto de pagar 450 €». | `humano` | confundido |  |
| 6 | 11.6–13.4 | Claude | Ahí. / Pagar. Tú. 450 €. | `cenital` | mira_der |  |
| 7 | 13.4–15.5 | Humano | Pero él dijo que me pagaba. | `dos` | preocupado |  |
| 8 | 15.5–18.8 | Claude | Y te ha mandado una / solicitud de cobro. Clásico. | `monitor` | feliz |  |
| 9 | 18.8–20.5 | Humano | ¿Y si pulso aceptar? | `humano` | bobo |  |
| 10 | 20.5–24.0 | Claude | El dinero sale al instante / y no se puede cancelar. | `claude_ojos` | idle, empuje de cámara |  |
| 11 | 24.0–25.4 | Humano | ¿Y qué hago? | `dos` | confundido |  |
| 12 | 25.4–29.3 | Claude | Rechazar. Cobrar es que te llegue / dinero. Léelo siempre. | `pantalla_completa` | idle |  |
| 13 | 29.3–30.9 | Humano | ¿Y si ya aceptara? | `humano` | preocupado, pose hombros |  |
| 14 | 30.9–35.0 | Claude | Llama a tu banco, avisa a la / plataforma y denuncia. Y el 017. | `monitor` | idle |  |
| 15 | 35.0–36.5 | Humano | ¡Gracias, Claude! | `dos` | feliz |  |
| 16 | 36.5–40.0 | Claude | Léelo todo antes de pulsar. / En fin... eres humano. | `general` | feliz |  |

## Datos reales que aparecen o se mencionan

- Estafa del «pago que en realidad es un cobro»: el falso comprador pide dinero en vez de enviarlo; si aceptas sin leer, el dinero sale de tu cuenta al instante. El Banco de España recuerda que en Bizum un pago confirmado no se puede cancelar. INCIBE y la Policía Nacional recomiendan leer la pantalla de confirmación (cantidad, concepto, quién solicita) y, si ya ha pasado, contactar con el banco, avisar a la plataforma y denunciar; línea de ayuda de INCIBE: 017 (gratuita y confidencial).
  - Fuente: [INCIBE — nueva estrategia de estafa por Bizum solicitando dinero](https://www.incibe.es/ciudadania/avisos/detectada-nueva-estrategia-de-estafa-traves-de-bizum-solicitando-dinero-en)
  - Fuente: [Banco de España — Cómo evitar estafas a través de Bizum](https://clientebancario.bde.es/pcb/es/blog/estafas-a-traves-de-bizum--como-evitarlas-.html)
  - Fuente: [Genbeta — Bizum y la estafa del pago que en realidad es un cobro (alerta de la Policía Nacional)](https://www.genbeta.com/seguridad/bizum-estafa-pago-que-realidad-cobro-policia-nacional-alerta-este-timo)

## Notas de producción

- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).
- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.
- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.
