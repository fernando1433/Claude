# Indice de la biblioteca `noche_trading`

Tamano de cada capa: 720x1280 (vertical). Todas las capas de un plano comparten camara: se apilan en este orden: **fondo -> pantalla del monitor (opcional) -> humano -> claude**.


## Plano `humano` - Primer plano del humano

- Fondo: `humano/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[716.4, 319.2], [2424.7, 134.9], [2295.0, 1022.1], [703.2, 834.8]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_humano.png`
- Capas del humano (RGBA, fondo transparente + sombra): `humano_neutral_cerrada.png`, `humano_neutral_media.png`, `humano_neutral_abierta.png`, `humano_feliz_cerrada.png`, `humano_feliz_media.png`, `humano_feliz_abierta.png`, `humano_preocupado_cerrada.png`, `humano_preocupado_media.png`, `humano_preocupado_abierta.png`, `humano_burlon_cerrada.png`, `humano_burlon_media.png`, `humano_burlon_abierta.png`, `humano_bobo_cerrada.png`, `humano_bobo_media.png`, `humano_bobo_abierta.png`, `humano_ilusionado_cerrada.png`, `humano_ilusionado_media.png`, `humano_ilusionado_abierta.png`, `humano_confundido_cerrada.png`, `humano_confundido_media.png`, `humano_confundido_abierta.png`, `humano_neutral_parpadeo.png`, `humano_pensar_neutral_cerrada.png`, `humano_pensar_neutral_media.png`, `humano_pensar_neutral_abierta.png`, `humano_pensar_preocupado_cerrada.png`, `humano_pensar_preocupado_media.png`, `humano_pensar_preocupado_abierta.png`, `humano_senalar_neutral_cerrada.png`, `humano_senalar_neutral_media.png`, `humano_senalar_neutral_abierta.png`, `humano_senalar_feliz_cerrada.png`, `humano_senalar_feliz_media.png`, `humano_senalar_feliz_abierta.png`, `humano_hombros_neutral_cerrada.png`, `humano_hombros_neutral_media.png`, `humano_hombros_neutral_abierta.png`, `humano_hombros_preocupado_cerrada.png`, `humano_hombros_preocupado_media.png`, `humano_hombros_preocupado_abierta.png`, `humano_mira_neutral_cerrada.png`, `humano_mira_neutral_media.png`, `humano_mira_neutral_abierta.png`, `humano_mira_feliz_cerrada.png`, `humano_mira_feliz_media.png`, `humano_mira_feliz_abierta.png`
- Vista rapida de todas las capas: `humano/_contacto.png`

## Plano `dos` - Plano de los dos: humano y Clawd en el escritorio

- Fondo: `dos/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[662.8, 302.3], [1777.1, 116.6], [1714.6, 706.3], [654.6, 662.1]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_humano.png`, `sombra_claude.png`
- Capas del humano (RGBA, fondo transparente + sombra): `humano_neutral_cerrada.png`, `humano_neutral_media.png`, `humano_neutral_abierta.png`, `humano_feliz_cerrada.png`, `humano_feliz_media.png`, `humano_feliz_abierta.png`, `humano_preocupado_cerrada.png`, `humano_preocupado_media.png`, `humano_preocupado_abierta.png`, `humano_burlon_cerrada.png`, `humano_burlon_media.png`, `humano_burlon_abierta.png`, `humano_bobo_cerrada.png`, `humano_bobo_media.png`, `humano_bobo_abierta.png`, `humano_ilusionado_cerrada.png`, `humano_ilusionado_media.png`, `humano_ilusionado_abierta.png`, `humano_confundido_cerrada.png`, `humano_confundido_media.png`, `humano_confundido_abierta.png`, `humano_neutral_parpadeo.png`, `humano_pensar_neutral_cerrada.png`, `humano_pensar_neutral_media.png`, `humano_pensar_neutral_abierta.png`, `humano_pensar_preocupado_cerrada.png`, `humano_pensar_preocupado_media.png`, `humano_pensar_preocupado_abierta.png`, `humano_senalar_neutral_cerrada.png`, `humano_senalar_neutral_media.png`, `humano_senalar_neutral_abierta.png`, `humano_senalar_feliz_cerrada.png`, `humano_senalar_feliz_media.png`, `humano_senalar_feliz_abierta.png`, `humano_hombros_neutral_cerrada.png`, `humano_hombros_neutral_media.png`, `humano_hombros_neutral_abierta.png`, `humano_hombros_preocupado_cerrada.png`, `humano_hombros_preocupado_media.png`, `humano_hombros_preocupado_abierta.png`, `humano_mira_neutral_cerrada.png`, `humano_mira_neutral_media.png`, `humano_mira_neutral_abierta.png`, `humano_mira_feliz_cerrada.png`, `humano_mira_feliz_media.png`, `humano_mira_feliz_abierta.png`
- Capas de Clawd (RGBA): `claude_idle.png`, `claude_parpadeo.png`, `claude_feliz.png`, `claude_mira_izq.png`, `claude_mira_der.png`, `claude_mira_arriba.png`
- Vista rapida de todas las capas: `dos/_contacto.png`

## Plano `claude` - Clawd sobre los libros, la pantalla detras

- Fondo: `claude/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[-655.7, -42.6], [532.9, -153.4], [518.6, 631.2], [-584.8, 615.1]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_claude.png`
- Capas de Clawd (RGBA): `claude_idle.png`, `claude_parpadeo.png`, `claude_feliz.png`, `claude_mira_izq.png`, `claude_mira_der.png`, `claude_mira_arriba.png`
- Vista rapida de todas las capas: `claude/_contacto.png`

## Plano `espalda` - Clawd de espaldas mirando el monitor

- Fondo: `espalda/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[159.7, 343.8], [917.5, 251.0], [917.5, 739.8], [159.7, 716.0]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_claude.png`
- Capas de Clawd (RGBA): `claude_idle.png`
- Vista rapida de todas las capas: `espalda/_contacto.png`

## Plano `monitor` - Monitor centrado y de frente; Clawd pequeno al pie mirando a camara

- Fondo: `monitor/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[30.9, 388.3], [690.6, 388.2], [690.6, 759.9], [30.9, 759.8]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_claude.png`
- Capas de Clawd (RGBA): `claude_idle.png`, `claude_parpadeo.png`, `claude_feliz.png`, `claude_mira_izq.png`, `claude_mira_der.png`, `claude_mira_arriba.png`
- Vista rapida de todas las capas: `monitor/_contacto.png`

## Plano `monitor_espalda` - Monitor centrado; Clawd de espaldas mirandolo en primer plano

- Fondo: `monitor_espalda/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[29.7, 409.6], [692.1, 409.3], [687.4, 780.4], [34.4, 780.1]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_claude.png`
- Capas de Clawd (RGBA): `claude_idle.png`
- Vista rapida de todas las capas: `monitor_espalda/_contacto.png`

## Plano `general` - Plano general: humano, monitor y Clawd en el escritorio

- Fondo: `general/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[331.4, 487.0], [711.4, 462.1], [706.6, 699.2], [331.7, 682.3]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_humano.png`, `sombra_claude.png`
- Capas del humano (RGBA, fondo transparente + sombra): `humano_neutral_cerrada.png`, `humano_neutral_media.png`, `humano_neutral_abierta.png`, `humano_feliz_cerrada.png`, `humano_feliz_media.png`, `humano_feliz_abierta.png`, `humano_bobo_cerrada.png`, `humano_bobo_media.png`, `humano_bobo_abierta.png`, `humano_ilusionado_cerrada.png`, `humano_ilusionado_media.png`, `humano_ilusionado_abierta.png`, `humano_neutral_parpadeo.png`, `humano_senalar_neutral_cerrada.png`, `humano_senalar_neutral_media.png`, `humano_senalar_neutral_abierta.png`
- Capas de Clawd (RGBA): `claude_idle.png`, `claude_parpadeo.png`, `claude_feliz.png`
- Vista rapida de todas las capas: `general/_contacto.png`

## Plano `cenital` - Cenital sobre el escritorio (teclado, raton, taza, libros) con Clawd

- Fondo: `cenital/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[219.3, 105.6], [1096.1, 289.2], [801.9, 611.4], [266.9, 440.1]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_claude.png`
- Capas de Clawd (RGBA): `claude_idle.png`, `claude_parpadeo.png`, `claude_feliz.png`, `claude_mira_izq.png`, `claude_mira_der.png`, `claude_mira_arriba.png`
- Vista rapida de todas las capas: `cenital/_contacto.png`

## Plano `claude_ojos` - Primerisimo plano de Clawd (reacciones: parpadeo, mirada)

- Fondo: `claude_ojos/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[-713.5, -111.0], [642.1, -658.4], [619.0, 717.1], [-663.6, 643.5]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_claude.png`
- Capas de Clawd (RGBA): `claude_idle.png`, `claude_parpadeo.png`, `claude_feliz.png`, `claude_mira_izq.png`, `claude_mira_der.png`, `claude_mira_arriba.png`
- Vista rapida de todas las capas: `claude_ojos/_contacto.png`

## Plano `monitor_lateral` - Monitor en tres cuartos desde la derecha, Clawd al pie

- Fondo: `monitor_lateral/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[203.1, 417.6], [808.3, 248.0], [776.1, 933.5], [208.5, 740.6]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_claude.png`
- Capas de Clawd (RGBA): `claude_idle.png`, `claude_parpadeo.png`, `claude_feliz.png`
- Vista rapida de todas las capas: `monitor_lateral/_contacto.png`

## Pantallas del monitor (`biblioteca/pantallas/`, 1280x720)
- `vacia` (por defecto, neutra) y ejemplos de trading: `chart`, `chat`, `order`. Se pueden anadir mas: cualquier PNG 1280x720.
