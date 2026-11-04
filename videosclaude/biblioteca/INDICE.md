# Indice de la biblioteca de capas

Tamano de cada capa: 720x1280 (vertical). Todas las capas de un plano comparten camara: se apilan en este orden: **fondo -> pantalla del monitor (opcional) -> humano -> claude**.


## Plano `humano` - Primer plano del humano

- Fondo: `humano/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[716.4, 319.2], [2424.7, 134.9], [2295.0, 1022.1], [703.2, 834.8]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_humano.png`
- Capas del humano (RGBA, fondo transparente + sombra): `humano_neutral_cerrada.png`, `humano_neutral_media.png`, `humano_neutral_abierta.png`, `humano_feliz_cerrada.png`, `humano_feliz_media.png`, `humano_feliz_abierta.png`, `humano_preocupado_cerrada.png`, `humano_preocupado_media.png`, `humano_preocupado_abierta.png`, `humano_burlon_cerrada.png`, `humano_burlon_media.png`, `humano_burlon_abierta.png`, `humano_neutral_parpadeo.png`
- Vista rapida de todas las capas: `humano/_contacto.png`

## Plano `dos` - Plano de los dos: humano y Clawd en el escritorio

- Fondo: `dos/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[662.8, 302.3], [1777.1, 116.6], [1714.6, 706.3], [654.6, 662.1]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_humano.png`, `sombra_claude.png`
- Capas del humano (RGBA, fondo transparente + sombra): `humano_neutral_cerrada.png`, `humano_neutral_media.png`, `humano_neutral_abierta.png`, `humano_feliz_cerrada.png`, `humano_feliz_media.png`, `humano_feliz_abierta.png`, `humano_preocupado_cerrada.png`, `humano_preocupado_media.png`, `humano_preocupado_abierta.png`, `humano_burlon_cerrada.png`, `humano_burlon_media.png`, `humano_burlon_abierta.png`, `humano_neutral_parpadeo.png`
- Capas de Clawd (RGBA): `claude_idle.png`, `claude_parpadeo.png`, `claude_feliz.png`
- Vista rapida de todas las capas: `dos/_contacto.png`

## Plano `claude` - Clawd sobre los libros, la pantalla detras

- Fondo: `claude/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[-655.7, -42.6], [532.9, -153.4], [518.6, 631.2], [-584.8, 615.1]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_claude.png`
- Capas de Clawd (RGBA): `claude_idle.png`, `claude_parpadeo.png`, `claude_feliz.png`
- Vista rapida de todas las capas: `claude/_contacto.png`

## Plano `espalda` - Clawd de espaldas mirando el monitor

- Fondo: `espalda/fondo.png` (habitacion sin personajes, monitor con pantalla `vacia`).
- Cuadrilatero del monitor (px, TL,TR,BR,BL): `[[159.7, 343.8], [917.5, 251.0], [917.5, 739.8], [159.7, 716.0]]`
- Sombras FIJAS (capas aparte, no se mueven): `sombra_claude.png`
- Capas de Clawd (RGBA): `claude_idle.png`
- Vista rapida de todas las capas: `espalda/_contacto.png`

## Pantallas del monitor (`biblioteca/pantallas/`, 1280x720)
- `vacia` (por defecto, neutra) y ejemplos de trading: `chart`, `chat`, `order`. Se pueden anadir mas: cualquier PNG 1280x720.
