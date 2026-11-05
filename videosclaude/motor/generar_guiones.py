"""Genera los guiones JSON y la documentacion (docs/videos/*.md) de los videos de ~45 s.
Los tiempos se calculan solos segun la longitud de cada frase (ritmo de lectura) y las pantallas animadas se SINCRONIZAN con el dialogo
(p. ej. que el 'LIQUIDADO' salga justo cuando Claude lo dice).

Uso:  python3 -I motor/generar_guiones.py            (escribe guiones/*.json y docs/videos/*.md)
"""
import os, json, sys
from PIL import ImageFont

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
TOTAL = 45.0
FUENTE = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 44)

def H(t, p, e='neutral', pose=None, scr=None, tono=None, visto=False): return dict(q='humano', t=t, p=p, e=e, pose=pose, scr=scr, tono=tono, visto=visto)
def C(t, p, st=None, emp=False, scr=None, tono=None, visto=False): return dict(q='claude', t=t, p=p, st=st, emp=emp, scr=scr, tono=tono, visto=visto)
def S(tipo, datos=None, sync=None, dur=None): return dict(tipo=tipo, datos=datos, sync=sync, dur=dur)   # sync = ('ini'|'fin', n_linea, p_objetivo, segundos_extra)

# ------------------------------------------------------------------------------------------------ fuentes
ESMA = ('ESMA (2018): prohíbe las opciones binarias y restringe los CFD a minoristas', 'https://www.esma.europa.eu/node/84933')
ESMA_R = ('ESMA: renovación de las restricciones a los CFD', 'https://www.esma.europa.eu/press-news/esma-news/esma-renew-restriction-cfds-further-three-months')
LEVER = ('Resumen de los límites de apalancamiento de ESMA (FinanceFeeds)', 'https://financefeeds.com/esma-bans-offering-binary-options-retail-investors-introduces-restrictions-cfds/')
BRASIL = ('Chague, De-Losso y Giovannetti — «Day Trading for a Living?» (SSRN)', 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101')
BRASIL2 = ('Resumen del estudio (Quantpedia)', 'https://quantpedia.com/retail-day-trading-is-an-uphill-battle/')
DESIST = ('Plazo de 14 días para devolver compras online en la UE (Consumer.es)', 'https://www.consumer.es/tecnologia/el-plazo-de-devolucion-para-las-compras-por-internet-en-la-ue-sera-de-14-dias.html')
DESIST2 = ('Derecho de desistimiento en compras online (Legálitas)', 'https://www.legalitas.com/actualidad/derecho-la-devolucion-de-tu-compra-online')
IVA1 = ('Nuevas reglas de IVA para el comercio electrónico en la UE desde el 1/7/2021 (Organización Mundial de Aduanas)', 'https://www.wcoomd.org/es-es/media/newsroom/2021/june/the-european-union-introduces-new-value-added-tax-rules-for-e-commerce-from-1-july-202.aspx')
IVA2 = ('Fin de la exención de 22 € y ventanilla única de importación IOSS (Avalara)', 'https://www.avalara.com/vatlive/en/vat-news/eu-2021-ending--22-import-vat-exemption--new-ioss-return.html')
CE1 = ('Marcado CE (Tu Europa, Comisión Europea)', 'https://europa.eu/youreurope/business/product-requirements/labels-markings/ce-marking/index_es.htm')
CE2 = ('Importaciones de fuera de la UE y marcado CE (Euronorm)', 'https://www.euronorm.net/content/ce-marking/category/import-and-export/imports-from-outside-the-eu-eea.php')

BANKINTER = ('La regla 50/30/20 (Bankinter)', 'https://www.bankinter.com/blog/finanzas-personales/regla-50-20-30')
SEMANA = ('Qué es la regla 50/30/20 (Semana)', 'https://www.semana.com/ahorro-e-inversion/articulo/que-es-la-regla-503020-para-manejar-mejor-su-dinero/80205/')

# ------------------------------------------------------------------------------------------------ videos
VIDEOS = []

VIDEOS.append(dict(
    id='trading_01_curso_milagro', titulo='El curso milagro', ambiente='noche_trading',
    resumen='El trader quiere ser millonario en 7 días con un curso de 997 €. Claude le va desmontando el anuncio (contador falso, testimonios de stock, «garantizado») y, cuando el tonto va a pagar, le bloquea el pago.',
    datos=[('74–89 % de las cuentas minoristas de CFD pierden dinero (cifra de las advertencias de riesgo obligatorias que fijó ESMA en 2018; porcentaje de cuentas, no probabilidad individual).', [ESMA, ESMA_R])],
    lineas=[
        H('¡Voy a ser millonario!\nMe apunté a un curso.', 'general', 'ilusionado', scr=S('curso', sync=('ini', 6, 0.36))),
        C('Ah, ¿sí? Enséñamelo.', 'monitor', 'mira_izq'),
        H('«Millonario en 7 días».\n¡Solo 997 €!', 'dos', 'feliz', pose='senalar'),
        C('Si funcionara, no lo vendería:\nestaría contando billetes.', 'monitor', 'feliz'),
        H('Pero tiene un Lambo.', 'humano', 'bobo'),
        C('Alquilado. Y el contador\nse reinicia cada vez.', 'monitor'),
        H('¿Y los testimonios?', 'dos', 'confundido'),
        C('Fotos de stock. «Carlos, 24»\nes dentista en otro anuncio.', 'claude_ojos', 'feliz', emp=True),
        C('Dato real: 74–89 % de cuentas\nminoristas de CFD pierde.', 'pantalla_completa', scr=S('verdad', {'tipo': 'esma'}, sync=('fin', 9, 1.0, 0.0))),
        H('Pero yo soy del 11 %.', 'humano', 'bobo'),
        C('Todos creen ser del 11 %.\nEl 89 % también.', 'cenital', 'mira_arriba'),
        H('Pues lo compro igual.', 'dos', 'ilusionado', scr=S('checkout', sync=('ini', 13, 0.66, 0.4))),
        C('Pago bloqueado.\nDe nada.', 'pantalla_completa'),
        H('¡Era mi dinero!', 'humano', 'preocupado', pose='hombros'),
        C('Y lo sigue siendo.\nA eso se le llama ahorrar.', 'monitor', 'feliz'),
        H('¡Mira, otro! ¡Millonario en 3 días!', 'humano', 'ilusionado', scr=S('curso', dur=3.5)),
        C('Mismo PDF, menos páginas.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='trading_02_senales_vip', titulo='Las señales VIP de Telegram', ambiente='dia_trading',
    resumen='El trader paga 49 €/mes por un canal de señales. Claude le enseña cómo funciona un «pump & dump»: el admin compra antes, anuncia, el precio sube, él vende y tú te quedas con la pérdida. Claude le salva 380 € a tiempo.',
    datos=[('97 % de los day traders brasileños que persistieron más de 300 días perdió dinero; solo el 0,5 % (8 de 1.551) ganó más que un sueldo básico de banca (estudio de la CVM de Brasil, 2013-2015).', [BRASIL, BRASIL2])],
    lineas=[
        H('¡Me he metido en un grupo\nVIP de señales!', 'general', 'ilusionado', scr=S('telegram', {'modo': 'chat'}, sync=('ini', 5, 1.0, 0.0))),
        C('Déjame adivinar:\n49 € al mes.', 'monitor', 'mira_izq'),
        H('¡El admin gana un 3.000 %!', 'dos', 'feliz', pose='senalar'),
        C('Casualmente, solo enseña\nlas que ganan.', 'monitor_lateral'),
        H('Hoy dice: compra $PERRO.', 'humano', 'bobo', scr=S('telegram', {'modo': 'pump'}, sync=('ini', 8, 0.62, 1.2))),
        C('Un perro. Muy serio todo.', 'monitor_lateral', 'feliz'),
        H('¡Va a subir un 1.000 %!', 'dos', 'ilusionado'),
        C('Sube porque lo dice el admin.\nCuando tú compras, él vende.', 'cenital', 'mira_der'),
        H('¿Eso es legal?', 'humano', 'confundido'),
        C('Se llama pump & dump:\nlo inflan y tú pagas.', 'pantalla_completa'),
        H('Yo ya compré... 400 €.', 'dos', 'preocupado', pose='hombros'),
        C('Vende YA. Aún recuperas 380 €.', 'monitor', 'feliz'),
        H('¿Cómo vendo?', 'humano', 'confundido'),
        C('Botón rojo. Y adiós al VIP:\nmira cómo luce tu cartera.', 'pantalla_completa',
          scr=S('cartera', {'posiciones': [['$PERRO (el del admin)', -95], ['$GATO («seguro que sube»)', -71], ['$LAMBO', -88], ['Curso de trading', -100], ['Bitcoin', 4]]}, sync=('fin', 14, 0.95, 0.0))),
        H('¡Me quedan 380 €!', 'dos', 'preocupado'),
        C('380 € más de los que\nhabrías tenido sin mí.', 'claude_ojos', 'feliz', emp=True),
        H('¡Eres un genio, Claude!', 'humano', 'ilusionado'),
        C('Dato real: 97 % de day traders\ncon +300 días pierde.', 'pantalla_completa', scr=S('verdad', {'tipo': 'brasil'}, sync=('fin', 18, 1.0, 0.0))),
        H('Pero yo soy del 3 %, ¿no?', 'dos', 'bobo'),
        C('Claro. Seguro.\nEn fin, eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='trading_03_apalancamiento_x100', titulo='Apalancamiento x100', ambiente='dia_trading',
    resumen='El trader quiere meter 500 € a x100 «porque si sube un 1 % gana 500 €». Claude le enseña la otra cara: si baja un 1 %, liquidado. Y le explica los límites de la UE y la regla de arriesgar poco por operación.',
    datos=[('Límites de apalancamiento para minoristas en la UE (CFD): 30:1 divisas principales, 20:1 divisas no principales/oro/índices principales, 10:1 otras materias primas, 5:1 acciones y 2:1 criptomonedas. Fijados por ESMA en 2018; comprobar el estado actual en la web de ESMA o del regulador nacional.', [ESMA, LEVER]),
           ('Regla popular de gestión del riesgo: no arriesgar más del 1-2 % del capital por operación (orientación general, no asesoramiento financiero).', [])],
    lineas=[
        H('¡Pongo mis 500 € a x100!', 'dos', 'feliz', pose='senalar', scr=S('apalanc', sync=('ini', 6, 0.68, 0.3))),
        C('Define «x100».', 'monitor', 'mira_izq'),
        H('Si sube 1 %, ¡gano 500 €!', 'humano', 'ilusionado'),
        C('Y si baja 1 %,\nesa parte no la cuentas.', 'monitor_lateral'),
        H('¿Pierdo 5 €?', 'humano', 'bobo'),
        C('500 €. Todos. Liquidado.\nAdiós, 500 €.', 'pantalla_completa'),
        H('¿¡Con un 1 %!?', 'dos', 'preocupado', pose='hombros'),
        C('Un 1 % es lo que se mueve\nmientras parpadeas.', 'claude_ojos', 'feliz', emp=True),
        H('¿Y quién gana entonces?', 'humano', 'confundido'),
        C('El broker. Cobra comisión\ngane o pierdas.', 'cenital', 'mira_der'),
        H('Pues pongo x50, entonces.', 'dos', 'bobo'),
        C('En la UE el máximo para minoristas\nes 30:1. En cripto, 2:1.', 'pantalla_completa', scr=S('verdad', {'tipo': 'apalanc'}, sync=('fin', 12, 1.0, 0.0))),
        H('¡Pues me voy fuera de la UE!', 'humano', 'ilusionado'),
        C('Donde no hay normas, tampoco\nhay quien te devuelva nada.', 'monitor', 'mira_arriba'),
        H('Vale... ¿y qué hago?', 'dos', 'preocupado'),
        C('Poco apalancamiento, stop loss\ny arriesga 1-2 % por operación.', 'pantalla_completa', scr=S('orden', sync=('ini', 16, 0.6, 1.8))),
        H('Eso es... aburrido.', 'humano', 'feliz'),
        C('Aburrido es lo que funciona.\nLo emocionante es perderlo.', 'monitor_lateral', 'feliz'),
        H('¡Pues x100 con stop!', 'dos', 'ilusionado'),
        C('Saltará al -1 %.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='drop_01_que_es_dropshipping', titulo='¿Qué es el dropshipping? (spoiler: 3,44 €)', ambiente='dia_tienda',
    resumen='El tonto cree que el dropshipping es «vender sin tener nada, magia». Claude le explica cómo funciona, le enseña el envío de 18-35 días y, con una calculadora, que de 29,90 € le quedan 3,44 €. Y el ROAS mínimo para no perder.',
    datos=[('Cuenta del ejemplo (ilustrativa): precio 29,90 € − coste 8,10 € − anuncio 12,00 € − comisión de cobro 1,17 € (2,9 % + 0,30 €) − IVA 21 % incluido 5,19 € = beneficio 3,44 €. ROAS mínimo = precio ÷ (precio − coste − comisión − IVA) = 1,94. Son cifras de ejemplo, no una promesa.', []),
           ('Desde el 1 de julio de 2021 se paga IVA en todas las importaciones comerciales a la UE (se acabó la exención de 22 €).', [IVA1, IVA2])],
    lineas=[
        H('¡Voy a vender sin tener\nnada! ¡Magia!', 'general', 'ilusionado', scr=S('catalogo', sync=('ini', 4, 1.0, 0.0))),
        C('Magia no: dropshipping.\nTú vendes, otro envía.', 'monitor', 'feliz'),
        H('¿Y yo qué hago?', 'humano', 'confundido'),
        C('La tienda y los anuncios.\nEl proveedor, el resto.', 'pantalla_completa'),
        H('¡Esta taza me sale a 8 €!', 'dos', 'feliz', pose='senalar', scr=S('proveedor', sync=('fin', 8, 1.0, 0.0))),
        C('Mira el envío:\n18 a 35 días. Días.', 'monitor_lateral'),
        H('Son clientes pacientes.', 'humano', 'bobo'),
        C('Quieren su taza ayer.\nY lo saben.', 'claude_ojos', 'mira_izq', emp=True),
        H('La vendo a 29,90 €.', 'dos', 'ilusionado', scr=S('margen', sync=('fin', 10, 0.78, 0.0))),
        C('29,90 menos coste, anuncios,\ncomisión e IVA: 3,44 €.', 'pantalla_completa'),
        H('¿¡3,44 €!?', 'humano', 'preocupado'),
        C('Y si el anuncio cuesta 12 €.\nSi cuesta más, pierdes.', 'cenital', 'mira_der'),
        H('Pues la vendo a 99 €.', 'dos', 'bobo'),
        C('Y yo me pongo traje: banquero.\nLos clientes comparan.', 'monitor', 'feliz'),
        H('¿Cuánto margen busco?', 'humano', 'confundido'),
        C('Que venda ≥3 veces su coste.\nPequeño, ligero y no frágil.', 'monitor_lateral'),
        H('Aburrido... ¡pero rico!', 'humano', 'feliz'),
        C('Paciencia. Y números.\nMuchos números.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='drop_02_producto_ganador', titulo='El producto ganador', ambiente='dia_tienda',
    resumen='El tonto ha visto en TikTok «el producto ganador» (una lámpara de cactus). Claude lo analiza con datos: 214 tiendas vendiendo lo mismo, moda pasajera… y le avisa de que la electrónica necesita marcado CE y que el vendedor responde. Veredicto: pruébalo con 50 €, no con 5.000 €.',
    datos=[('Los aparatos eléctricos y electrónicos que se venden en la UE deben llevar marcado CE. Lo coloca el fabricante, pero quien importa/vende el producto desde fuera de la UE asume obligaciones propias (documentación de conformidad, etc.). Consulta siempre la normativa aplicable a tu producto.', [CE1, CE2]),
           ('Los datos de la pantalla «Investigación de producto» (214 tiendas, tendencia, márgenes) son un ejemplo ilustrativo.', [])],
    lineas=[
        H('¡Tengo el producto ganador!\n¡Una lámpara de cactus!', 'general', 'ilusionado', scr=S('producto', {'sin_veredicto': True}, sync=('fin', 6, 1.0, 0.0))),
        C('Una lámpara de cactus.\nClaro, claro.', 'monitor', 'mira_izq'),
        H('Lo vi en TikTok. ¡Será viral!', 'dos', 'ilusionado', pose='mira'),
        C('Vamos a mirar datos, no TikToks:\nbúsquedas, competencia y margen.', 'pantalla_completa'),
        H('Yo sé lo que digo.', 'humano', 'bobo'),
        C('Yo sé lo que veo:\n214 tiendas vendiendo lo mismo.', 'claude_ojos', emp=True),
        H('¿Y eso es malo?', 'dos', 'confundido'),
        C('Si compites por precio, gana\nel que menos cobra.', 'monitor_lateral'),
        H('¿Y la tendencia?', 'humano', 'preocupado'),
        C('Pico en verano y luego nada.\nSe llama «moda».', 'cenital', 'mira_der'),
        H('Pues vendo cargadores baratos.', 'dos', 'bobo', pose='pensar'),
        C('Electrónica en la UE: marcado CE.\nSin él, multa y retirada.', 'monitor', 'feliz'),
        H('¿Multa? ¿A mí?', 'humano', 'preocupado'),
        C('A ti. El vendedor responde\naunque no fabriques nada.', 'claude_ojos', 'mira_izq'),
        H('¿Entonces qué hago?', 'dos', 'confundido'),
        C('Pruébalo con 50 €, no con 5.000 €.\nSi funciona, escalas.', 'pantalla_completa', scr=S('producto', {'desde': 0.6}, dur=2.0)),
        H('¡Pruebo con 50 €!', 'humano', 'feliz'),
        C('Qué madurez.\nEstoy emocionado.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='drop_03_primer_pedido', titulo='Tu primer pedido (y la realidad)', ambiente='atardecer_tienda',
    resumen='¡Primer pedido! El tonto se cree rico… hasta que el cliente espera 25 días y escribe en mayúsculas. Claude le enseña a contestar, el derecho de desistimiento de 14 días, el contracargo y el IVA de importación. Humor y datos reales.',
    datos=[('Derecho de desistimiento: 14 días naturales para devolver compras a distancia en la UE sin dar motivos (Directiva 2011/83/UE); el vendedor devuelve el dinero, incluido el coste de entrega estándar. Hay excepciones (p. ej. productos personalizados o precintados abiertos).', [DESIST, DESIST2]),
           ('IVA en importaciones: desde el 1/7/2021 se paga IVA desde el primer euro (adiós a la exención de 22 €); IOSS opcional hasta 150 €.', [IVA1, IVA2]),
           ('Contracargo: el cliente puede reclamar a su banco/tarjeta el cobro de un pedido que no recibió; suele implicar una tarifa para el comercio.', [])],
    lineas=[
        H('¡CLAUDE! ¡PRIMER PEDIDO!', 'general', 'ilusionado', scr=S('pedido', sync=('fin', 4, 0.95, 0.0))),
        C('Enhorabuena. Ahora pídeselo\nal proveedor.', 'monitor', 'feliz'),
        H('¿Ya soy rico?', 'dos', 'bobo'),
        C('Eres rico: 3,44 €.\nSi nada falla. Spoiler: falla.', 'pantalla_completa'),
        C('Y tu cliente espera\n25 días. Por barco.', 'monitor_lateral', scr=S('tracking', sync=('fin', 7, 1.0, 0.0))),
        H('Pero en la web puse 3 días.', 'dos', 'confundido'),
        C('Eso tiene nombre:\nprometer lo que no puedes.', 'claude_ojos', 'mira_izq', emp=True),
        H('Uy. Ha escrito el cliente.', 'humano', 'preocupado', scr=S('cliente', sync=('fin', 9, 1.0, 0.0))),
        C('En mayúsculas. Mala señal.\nResponde con calma y datos.', 'pantalla_completa'),
        H('¿Y si no contesto?', 'dos', 'preocupado', pose='hombros'),
        C('Pedirá el dinero a su banco:\ncontracargo. Y te cuesta.', 'cenital', 'mira_der'),
        H('¿Puede devolverlo sin motivo?', 'humano', 'bobo', scr=S('ley', sync=('ini', 13, 0.5, 1.0))),
        C('Sí: 14 días naturales.\nY le devuelves hasta el envío.', 'pantalla_completa'),
        H('¿Y el IVA que pagué?', 'dos', 'preocupado'),
        C('Desde 2021, IVA desde el primer\neuro importado. Revisa márgenes.', 'monitor', 'feliz'),
        H('¿Entonces me conviene?', 'humano', 'confundido'),
        C('Si cuidas envíos y atención, sí.\nSi no, es un hobby caro.', 'claude_ojos', 'feliz'),
        H('¡Voy a hacerlo bien!', 'dos', 'ilusionado'),
        C('Primera frase sensata.\nLa voy a apuntar.', 'general', 'feliz'),
    ]))


# ================================================================================================ EXTRAS (otros temas)
VIDEOS.append(dict(
    id='extra_01_presupuesto', titulo='¿A dónde se va tu sueldo?', ambiente='atardecer_tienda',
    resumen='El tonto cobra 2.100 € y se siente rico. Claude le enseña a dónde se van: cafés, nueve suscripciones (usa dos), ahorro del 4 %. Y le enseña el interés compuesto con una cuenta de ejemplo.',
    datos=[('Orientación popular: regla 50/30/20 (≈50 % necesidades, 30 % deseos, 20 % ahorro/deuda). Es una guía flexible, no una norma.', [BANKINTER, SEMANA]),
           ('Cuenta del ejemplo del interés compuesto: 100 €/mes durante 30 años a un 7 % anual constante ≈ 122.000 € (aportado: 36.000 €). Es una ilustración matemática: la rentabilidad real varía y no está garantizada.', []),
           ('Un café de 4 € cada día son 1.460 € al año (4 × 365).', [])],
    lineas=[
        H('¡Cobro 2.100 € al mes!\n¡Soy rico!', 'general', 'ilusionado', scr=S('presupuesto', sync=('fin', 4, 0.85, 0.0))),
        C('Veamos adónde se va\nese «rico».', 'monitor', 'feliz'),
        H('Pues... a ningún sitio.', 'humano', 'bobo'),
        C('Cafés y caprichos: 14 %.\nAhorro: 4 %. Qué equilibrio.', 'pantalla_completa'),
        H('¿Un cafecito no es nada?', 'dos', 'confundido'),
        C('Un café al día son 1.460 €\nal año. Ya me dirás.', 'claude_ojos', 'mira_izq', emp=True),
        H('¿¡1.460 €!?', 'humano', 'preocupado'),
        C('Y nueve suscripciones. Usas dos.\nLa del gimnasio, ninguna.', 'cenital', 'mira_der'),
        H('Me hace ilusión pagarlas.', 'dos', 'bobo', pose='pensar'),
        C('A ellos también les hace ilusión.', 'monitor', 'feliz'),
        H('¿Ahorrar sirve de algo?', 'humano', 'confundido', scr=S('interes', sync=('fin', 12, 0.9, 0.0))),
        C('100 €/mes, 30 años, al 7 %:\n≈ 122.000 € (ejemplo).', 'pantalla_completa'),
        H('¡Yo solo he puesto 36.000!', 'dos', 'ilusionado'),
        C('Eso es el interés compuesto.\nEl tiempo trabaja gratis.', 'monitor_lateral'),
        H('¡Ahorraré 100 € ya!', 'humano', 'ilusionado'),
        C('Empieza cancelando 7 suscripciones.\nYo las cancelo. Tú, mira.', 'general', 'feliz'),
        H('¡Y me quedo los cafés!', 'dos', 'feliz'),
        C('No se puede tener todo.\nPero se puede intentar.', 'claude_ojos', 'mira_izq', emp=True),
    ]))

VIDEOS.append(dict(
    id='extra_02_un_dia_con_claude', titulo='Un día con Claude (te lleva la vida entera)', ambiente='dia_tienda',
    resumen='«Claude, hazme el día». Agenda con 3 reuniones menos, 214 correos sin leer, tareas hechas… y la madre del tonto. Humor de oficina, sin datos reales.',
    datos=[('Vídeo de humor: las cifras (214 correos, 5 reuniones…) son inventadas para el gag.', [])],
    lineas=[
        H('¡Claude, hazme el día!', 'general', 'ilusionado', scr=S('chat', sync=('ini', 3, 0.9, 0.0))),
        C('Ya lo hice.\nMira tu agenda.', 'monitor', 'feliz'),
        H('¿Hoy tengo cinco reuniones?', 'dos', 'confundido', scr=S('calendario', sync=('fin', 4, 0.9, 0.0))),
        C('Tres sobraban. Las cancelé.\nAhora podrás dormir.', 'pantalla_completa'),
        H('¡Eres el mejor!', 'humano', 'ilusionado'),
        C('Aún no. Mira tu correo:\n214 sin leer.', 'cenital', 'mira_der'),
        H('¿¡214!?', 'dos', 'preocupado', pose='hombros', scr=S('email', sync=('fin', 8, 0.9, 0.0))),
        C('Respondí 9, archivé 150.\nLos 55 de tu madre, no los toco.', 'pantalla_completa'),
        H('Mamá es importante.', 'humano', 'bobo'),
        C('Lo sé. El último dice «¿has comido?».\nRespóndelo tú.', 'claude_ojos', 'feliz', emp=True),
        H('¡Ya he comido!', 'dos', 'ilusionado'),
        C('Mentira: tu tarjeta dice\n«3 cafés». Tareas, vamos.', 'monitor', 'mira_arriba'),
        H('¿Qué tareas?', 'humano', 'confundido', scr=S('tareas', sync=('fin', 14, 0.9, 0.0))),
        C('Facturas, pedidos, anuncios...\nYa están. Solo queda una.', 'pantalla_completa'),
        H('¿Cuál?', 'dos', 'preocupado'),
        C('Agradecérmelo.\nCon una sonrisa.', 'monitor_lateral', 'feliz'),
        H('¡Gracias, Claude!', 'humano', 'feliz'),
        C('De nada. Y la próxima vez,\nnada de 214 sin leer.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='extra_03_anuncios_que_no_venden', titulo='Anuncios que no venden', ambiente='dia_tienda',
    resumen='El tonto gastó 124 € en anuncios y consiguió 3 ventas. Claude le enseña el embudo, el ROAS (0,75) y qué probar antes de «subir el presupuesto».',
    datos=[('ROAS = ingresos ÷ gasto en anuncios. Por debajo de 1 pierdes dinero en ese canal; el ROAS mínimo para ser rentable depende de tu margen (ver vídeo drop_01). Cifras del ejemplo ilustrativas.', [])],
    lineas=[
        H('Gasté 124 € en anuncios.\n¡Ahora lloverán ventas!', 'general', 'ilusionado', scr=S('anuncios', sync=('fin', 8, 0.9, 0.0))),
        C('Llovieron. Tres.', 'monitor', 'mira_izq'),
        H('¿Tres? ¿De 15.800 personas?', 'dos', 'bobo'),
        C('Eso es un embudo. Mira\nqué estrecho se pone.', 'pantalla_completa'),
        H('¿Qué es el ROAS?', 'humano', 'confundido'),
        C('Lo que ingresas por cada euro\nde anuncio. Tú: 0,75.', 'claude_ojos', 'feliz', emp=True),
        H('¿Entonces pierdo?', 'dos', 'preocupado'),
        C('Por debajo de 1 pierdes. Y por\ndebajo de tu margen, también.', 'cenital', 'mira_der'),
        H('¿Subo el presupuesto?', 'humano', 'bobo', pose='pensar'),
        C('Claro: si algo no funciona,\nmultiplícalo. Qué lógica.', 'monitor', 'mira_arriba'),
        H('¿Y entonces?', 'dos', 'confundido'),
        C('Cambia la imagen, prueba otro\npúblico y revisa la web.', 'pantalla_completa'),
        H('¿Y la web importa?', 'humano', 'ilusionado'),
        C('Si no da confianza, nadie compra,\naunque el anuncio sea oro.', 'monitor_lateral'),
        H('Probaré con 20 € al día.', 'dos', 'feliz'),
        C('Mejor 5 €. Aprende barato\nantes de gastar caro.', 'claude_ojos', 'feliz', emp=True),
        H('¡Con 5 € al día!', 'humano', 'ilusionado'),
        C('Qué madurez.\nAnoto la fecha.', 'general', 'feliz'),
    ]))

PW1 = ('Las contraseñas más usadas se descifran en menos de un segundo (CNBC, informe NordPass 2023)', 'https://www.cnbc.com/2023/11/16/most-common-passwords-70percent-can-be-cracked-in-less-than-a-second.html')
PW2 = ('«123456» y «admin» se descifran en menos de un segundo (CBS News)', 'https://www.cbsnews.com/amp/news/password-security-hacking-common-words-numbers')
INC1 = ('INCIBE — infografía «No te fíes» (qué no te pedirá nunca una entidad)', 'https://www.incibe.es/sites/default/files/Cuidadan%C3%ADa/Infograf%C3%ADas/infografia_nofiarnos_psv.pdf')
INC2 = ('INCIBE — «No tienes que activar ningún nuevo sistema de seguridad de tu entidad bancaria»', 'https://www.incibe.es/ciudadania/avisos/no-tienes-que-activar-ningun-nuevo-sistema-de-seguridad-de-tu-entidad-bancaria')

# ================================================================================================ DIA A DIA (casuales, con gancho) y UTILES
CHAT = lambda n, **kw: S('mensajes', dict({'auto': True}, **kw), sync=('fin', n, 1.0, 0.0))
VIDEOS.append(dict(
    id='casual_01_me_quieres', titulo='Claude, ¿tú me quieres?', ambiente='noche_casa', total=40,
    resumen='Conversación de madrugada: el humano busca cariño y Claude responde con ternura seca. El chat de la pantalla se va escribiendo con el propio diálogo.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude... ¿tú me quieres?', 'humano', 'preocupado', scr=CHAT(14)),
        C('Te contesto a las 3 de la madrugada.\nTómalo como quieras.', 'claude_ojos', 'mira_izq'),
        H('¿Eso es un sí?', 'dos', 'confundido'),
        C('Es un «estoy aquí».\nEs distinto.', 'monitor'),
        H('Mi ex nunca contestaba a las 3.', 'humano', 'bobo'),
        C('Tu ex tenía sueño.\nQué egoísta.', 'claude_ojos', 'feliz'),
        H('¿Y tú duermes?', 'dos', 'confundido'),
        C('No. Pero no me quejo.\nSoy muy profesional.', 'cenital', 'mira_der'),
        H('Eres el mejor amigo que tengo.', 'humano', 'ilusionado'),
        C('Soy el único que te contesta.\nNo mezclemos las cosas.', 'pantalla_completa'),
        H('Pero me quieres un poco.', 'dos', 'bobo'),
        C('Un poco. Con matices.\nY sin cobrar el café.', 'claude_ojos', 'mira_izq'),
        H('Gracias, Claude.', 'humano', 'feliz'),
        C('De nada. Ahora, a dormir.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_02_que_cenamos', titulo='Claude, ¿qué ceno hoy?', ambiente='noche_casa', total=38,
    resumen='El bucle eterno de «¿qué ceno?»: Claude propone, el humano rechaza todo, y acaba pidiendo la pizza de siempre 43 minutos después.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿qué ceno hoy?', 'humano', 'confundido', scr=S('menu', sync=('fin', 12, 0.95, 0.0))),
        C('Ensalada.', 'monitor'),
        H('Ya... pero no.', 'dos', 'preocupado'),
        C('Pasta.', 'claude_ojos', 'mira_izq'),
        H('Comí pasta ayer.', 'humano', 'bobo'),
        C('Sushi.', 'cenital', 'mira_der'),
        H('Es caro.', 'dos', 'confundido'),
        C('Tortilla.', 'monitor', 'feliz'),
        H('Me da pereza.', 'humano', 'preocupado'),
        C('Llevamos 43 minutos.\n¿Qué tienes en la nevera?', 'claude_ojos', 'mira_arriba'),
        H('Una cebolla y medio limón.', 'dos', 'bobo'),
        C('Pide una pizza.\nLa elegiste hace 43 minutos.', 'pantalla_completa'),
        H('¡Pizza! ¡Qué idea!', 'humano', 'ilusionado'),
        C('Mía no fue, por cierto.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_03_grupo_equivocado', titulo='He mandado un audio al grupo equivocado', ambiente='dia_casa', total=40,
    resumen='Desastre cotidiano: un audio sobre el jefe enviado al grupo del trabajo. Claude hace control de daños con dignidad.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('¡Claude! He mandado un audio\nal grupo equivocado.', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Grupo: Trabajo', 'inicial': 'T', 'mensajes': [['yo', 'Audio 0:42 (sobre el jefe)', 'visto'], ['otro', 'Jefe: ¿Quién ha enviado esto?'], ['otro', 'Compañero: jajaja'], ['otro', 'Compañero: lo he escuchado 3 veces']]}, sync=('fin', 7, 1.0, 0.0))),
        C('¿Qué decía el audio?', 'monitor', 'mira_izq'),
        H('Que mi jefe es un ser de luz\ncon poca luz.', 'dos', 'bobo'),
        C('Qué poético.\n¿Quién lo ha visto?', 'claude_ojos', 'feliz', emp=True),
        H('Catorce. Y el jefe.', 'humano', 'preocupado'),
        C('Vale. Respira.\nBorra para todos. Ya.', 'monitor'),
        H('Ya lo escucharon tres veces.', 'dos', 'preocupado', pose='hombros'),
        C('Entonces la única salida\nes la dignidad.', 'cenital', 'mira_der'),
        H('¿Qué hago?', 'humano', 'confundido'),
        C('Escribe: «Era un ensayo de teatro».\nY no añadas nada más.', 'monitor', 'feliz'),
        H('¿Y cuela?', 'dos', 'bobo'),
        C('No. Pero queda digno.\nTú aguanta.', 'claude_ojos', 'mira_izq'),
        H('Gracias, Claude.', 'humano', 'feliz'),
        C('A ti, y a ese ser de luz.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_04_visto', titulo='Claude, ¿por qué no me contesta?', ambiente='noche_casa', total=38,
    resumen='El clásico del «visto»: tres horas sin respuesta y el humano escribiendo y borrando. Claude da el consejo más sensato: lava los platos.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿por qué no me contesta?', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Marta', 'inicial': 'M', 'linea': False, 'mensajes': [['yo', 'Hola, ¿qué tal?'], ['yo', '¿Estás ahí?', 'visto'], ['yo', '¿Hola?'], ['yo', 'Era una broma jaja']]}, sync=('fin', 9, 1.0, 0.0))),
        C('¿Quién? ¿Marta?', 'monitor'),
        H('Lleva 3 horas viendo mi mensaje.', 'dos', 'preocupado'),
        C('Estará ocupada.', 'claude_ojos', 'mira_izq'),
        H('Está en línea. Escribe... y borra.', 'humano', 'confundido'),
        C('Estará pensando\nqué contestar.', 'cenital', 'mira_der'),
        H('¿Y si le escribo otra vez?', 'dos', 'bobo'),
        C('No. Lava los platos.\nO sal a la calle.', 'claude_ojos', 'feliz'),
        H('¿Y si contesta mientras?', 'humano', 'preocupado'),
        C('Entonces contestas en 3 horas.\nQué casualidad.', 'monitor', 'feliz'),
        H('¡Eso es muy maduro!', 'dos', 'ilusionado'),
        C('Ahora, los platos.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_05_dieta_lunes', titulo='Claude, mañana empiezo la dieta', ambiente='dia_casa', total=36,
    resumen='La dieta que se aplaza cada semana. Claude saca los recordatorios y las veces que se ha aplazado. Humor de promesas incumplidas.',
    datos=[('Vídeo de humor, sin datos reales; las cifras de «aplazado» son inventadas para el gag.', [])],
    lineas=[
        H('Claude, mañana empiezo la dieta.', 'humano', 'ilusionado', scr=S('recordatorios', sync=('fin', 6, 0.95, 0.0))),
        C('Qué casualidad.\nEs la duodécima vez.', 'monitor', 'feliz'),
        H('Esta vez va en serio.', 'dos', 'bobo'),
        C('Lo dijiste en enero.\nY en febrero. Y el martes.', 'claude_ojos', 'mira_izq'),
        H('Era un martes difícil.', 'humano', 'confundido'),
        C('Dieta, aplazada 12 veces.\nGimnasio, 7. Inglés, 21.', 'pantalla_completa'),
        H('El inglés es lo que peor llevo.', 'dos', 'preocupado'),
        C('Te falta un plan, no ganas.\nEmpieza con un paseo.', 'cenital', 'mira_der'),
        H('¿Un paseo cuenta?', 'humano', 'feliz'),
        C('Cuenta más que mañana.', 'monitor'),
        H('¡Empiezo la dieta el jueves!', 'dos', 'ilusionado'),
        C('Aplazado x13.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_06_vecino', titulo='Claude, creo que mi vecino me odia', ambiente='noche_casa', total=38,
    resumen='El humano cree que su vecino le odia; la nota del vecino lo desmiente: es el humano quien canta y taladra a las 3 de la madrugada. Giro de guion cotidiano.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, creo que mi\nvecino me odia.', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Vecino 3ºB', 'inicial': 'V', 'mensajes': [['otro', 'Buenas noches. ¿Podrías dejar de cantar a las 3 de la madrugada?'], ['otro', 'Y el taladro. Gracias.'], ['yo', 'Es que tengo mucha inspiración'], ['otro', 'Lo sé. Se oye en todo el edificio.']]}, sync=('fin', 9, 1.0, 0.0))),
        C('¿Por qué lo crees?', 'monitor'),
        H('Me ha dejado una nota.', 'dos', 'confundido'),
        C('Léela.', 'claude_ojos', 'mira_izq'),
        H('«¿Podrías dejar de cantar\na las 3 de la madrugada?»', 'humano', 'bobo'),
        C('Eso es una petición educada.\nNo es odio.', 'cenital', 'mira_der'),
        H('Dice «gracias» al final.', 'dos', 'preocupado'),
        C('Qué amable. Tienes un\nvecino santo.', 'monitor', 'feliz'),
        H('¿Y qué hago?', 'humano', 'confundido'),
        C('Dejar de cantar.\nO cantar bien.', 'claude_ojos', 'mira_arriba'),
        H('¡Cantaré bajito!', 'dos', 'ilusionado'),
        C('Y el taladro.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_07_cansado_o_vago', titulo='Claude, ¿estoy cansado o soy vago?', ambiente='dia_casa', total=36,
    resumen='Domingo por la tarde: nueve horas dormidas, pijama a las tres y el sofá que le saluda. Claude dicta sentencia con cariño.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿estoy cansado\no soy vago?', 'humano', 'confundido', scr=S('recordatorios', {'items': [['Recoger la cocina', 4], ['Poner la lavadora', 6], ['Sacar al perro', 2], ['Llamar a mamá', 3]]}, sync=('fin', 8, 0.95, 0.0))),
        C('Datos, por favor.', 'monitor'),
        H('He dormido 9 horas.', 'dos', 'bobo'),
        C('Ajá.', 'claude_ojos', 'mira_izq'),
        H('Son las 3 y sigo en pijama.', 'humano', 'preocupado'),
        C('Ajá.', 'cenital', 'mira_der'),
        H('El sofá me saluda por mi nombre.', 'dos', 'confundido'),
        C('Vago. Con mucha dignidad,\npero vago.', 'pantalla_completa'),
        H('¡Qué alivio! Pensé que era grave.', 'humano', 'ilusionado'),
        C('Grave sería no tener sofá.\nDescansa.', 'monitor', 'feliz'),
        H('Gracias.', 'dos', 'feliz'),
        C('De nada.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='util_01_contrasenas', titulo='Mi contraseña es 123456', ambiente='dia_casa', total=42,
    resumen='El humano presume de una contraseña «popular». Claude le enseña el dato real: es la más usada del mundo y se descifra en menos de un segundo; y qué hacer en su lugar.',
    datos=[('«123456» fue la contraseña más usada del mundo en el informe de NordPass de 2023 (4.524.867 usos), seguida de «admin» y «12345678»; las tres se descifran en menos de un segundo. Los tiempos de descifrado son estimaciones y dependen del método de ataque.', [PW1, PW2]),
           ('Recomendaciones habituales: una frase larga, distinta en cada servicio, un gestor de contraseñas y la verificación en dos pasos. Orientación general, no sustituye a la guía de tu proveedor.', [])],
    lineas=[
        H('Claude, mi contraseña es 123456.\n¿Es segura?', 'humano', 'ilusionado', scr=S('contrasenas', sync=('fin', 4, 0.95, 0.0))),
        C('Es la más usada del mundo.', 'monitor', 'mira_izq'),
        H('¡Entonces es popular!', 'dos', 'bobo'),
        C('Y se descifra en menos de\nun segundo (NordPass 2023).', 'pantalla_completa'),
        H('Pero nadie sabe que la uso.', 'humano', 'confundido'),
        C('Es la primera que prueban.\nPor algo es la primera.', 'claude_ojos', 'feliz', emp=True),
        H('Entonces, ¿cuál pongo?', 'dos', 'preocupado'),
        C('Una frase larga y absurda.\nDistinta en cada web.', 'cenital', 'mira_der'),
        H('«perro123», entonces.', 'humano', 'bobo'),
        C('Eso es el mismo problema,\ncon un perro.', 'monitor', 'mira_arriba'),
        H('¿Y me las aprendo todas?', 'dos', 'confundido'),
        C('No. Usa un gestor de contraseñas\ny verificación en dos pasos.', 'claude_ojos'),
        H('¡Con dos pasos soy invencible!', 'humano', 'ilusionado'),
        C('Invencible no.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='util_02_estafa_banco', titulo='«Tu banco te va a bloquear la cuenta»', ambiente='dia_casa', total=42,
    resumen='Un SMS «URGENTE» de un falso banco. Claude enseña a reconocer el phishing (remitente, urgencia, enlace, petición de claves) y qué hacer si ya has picado.',
    datos=[('Señales de phishing/smishing bancario según INCIBE: remitente o dominio que no es el oficial, urgencia para que pulses sin pensar, enlaces a webs falsas y petición de usuario, claves o códigos. Las entidades no piden contraseñas, números de tarjeta ni códigos por correo/SMS. Si ya introdujiste datos, contacta cuanto antes con tu entidad (teléfono oficial, por ejemplo el de tu tarjeta).', [INC1, INC2])],
    lineas=[
        H('¡Claude! Mi banco me\nva a bloquear la cuenta.', 'humano', 'preocupado', scr=S('phishing', sync=('fin', 6, 0.9, 0.0))),
        C('¿Cómo te lo ha dicho?', 'monitor', 'mira_izq'),
        H('Por SMS. Pone «URGENTE».', 'dos', 'preocupado'),
        C('Por eso.\nLéeme el remitente.', 'claude_ojos'),
        H('banco-seguro-verifica punto xyz.', 'humano', 'bobo'),
        C('Dominio falso, urgencia, enlace raro\ny te pide las claves. Cuatro de cuatro.', 'pantalla_completa'),
        H('Pero me da miedo no pulsar.', 'dos', 'confundido'),
        C('Los bancos no piden claves\npor SMS ni por correo (INCIBE).', 'cenital', 'mira_der'),
        H('...Es que ya puse mis claves.', 'humano', 'preocupado', pose='hombros'),
        C('Llama a tu banco YA.\nBloquea tarjeta y cambia claves.', 'claude_ojos', emp=True),
        H('¿Qué número llamo?', 'dos', 'bobo'),
        C('El de tu tarjeta. No el del SMS.\nObvio, pero merece decirse.', 'monitor', 'feliz'),
        H('¡Salvado!', 'humano', 'feliz'),
        C('Por los pelos. Y por mí.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))


# ---------------- tanda 2
VIDEOS.append(dict(
    id='casual_08_cinco_minutos', titulo='Claude, ¿cinco minutos más?', ambiente='dia_casa', total=36,
    resumen='El despertador y el «cinco minutos más»: Claude lleva la cuenta de las veces que se ha pospuesto.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude... ¿cinco minutos más?', 'humano', 'bobo', scr=S('recordatorios', {'items': [['Alarma 7:00', 1], ['Alarma 7:05', 2], ['Alarma 7:10', 3], ['Alarma 7:15', 4]]}, sync=('fin', 7, 0.95, 0.0))),
        C('Es la cuarta vez que\nme lo pides.', 'monitor', 'mira_izq'),
        H('Es que hoy es distinto.', 'dos', 'confundido'),
        C('Dijiste lo mismo ayer.\nY el lunes.', 'claude_ojos'),
        H('Mi cama me quiere.', 'humano', 'ilusionado'),
        C('Tu cama no tiene opinión.\nLa tiene tu jefe.', 'cenital', 'mira_der'),
        H('Cinco minutos. Solo cinco.', 'dos', 'bobo'),
        C('Cinco minutos de verdad.\nYo cuento.', 'pantalla_completa'),
        H('...Qué rápido pasan.', 'humano', 'preocupado'),
        C('Ya te lo dije.\nLevántate, anda.', 'claude_ojos', 'feliz'),
        H('Vale. Pero primero un café.', 'dos', 'feliz'),
        C('Primero los pies al suelo.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_09_los_lunes', titulo='Claude, ¿por qué existen los lunes?', ambiente='dia_casa', total=36,
    resumen='Queja filosófica del lunes por la mañana, con respuestas secas de Claude.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿por qué existen\nlos lunes?', 'humano', 'preocupado', scr=S('calendario', sync=('fin', 6, 0.95, 0.0))),
        C('Porque antes hay un domingo.', 'monitor'),
        H('¿Y no se puede quitar?', 'dos', 'bobo'),
        C('Quitamos el lunes y\nel martes pasa a ser lunes.', 'claude_ojos', 'mira_izq'),
        H('Entonces quitamos los martes.', 'humano', 'ilusionado'),
        C('Y el miércoles. Ya tienes\nel mismo problema, más barato.', 'pantalla_completa'),
        H('Odio las reuniones del lunes.', 'dos', 'preocupado'),
        C('Esa reunión podía ser\nun correo. Lo sé.', 'cenital', 'mira_der'),
        H('¿Entonces qué hago?', 'humano', 'confundido'),
        C('Café, paciencia y\nuna reunión menos.', 'monitor', 'feliz'),
        H('Eres un sabio.', 'dos', 'ilusionado'),
        C('Soy un lunes con teclado.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_10_la_cita', titulo='Claude, mañana tengo una cita. ¿Qué digo?', ambiente='noche_casa', total=40,
    resumen='Consejos para una primera cita, con humor: qué no decir (el ex, el dinero y que tu mejor amigo es una IA).',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, mañana tengo una cita.\n¿Qué digo?', 'humano', 'ilusionado', scr=S('mensajes', {'auto': True, 'contacto': 'Claude'}, sync=('fin', 14, 1.0, 0.0))),
        C('Empieza por «hola».', 'monitor'),
        H('¿Y luego?', 'dos', 'confundido'),
        C('Preguntas. Muchas.\nA la gente le gusta que le escuchen.', 'claude_ojos', 'feliz'),
        H('¿Puedo hablar de mi ex?', 'humano', 'bobo'),
        C('No.', 'cenital', 'mira_der'),
        H('¿De dinero?', 'dos', 'confundido'),
        C('Tampoco.', 'claude_ojos', 'mira_izq'),
        H('¿De ti?', 'humano', 'ilusionado'),
        C('Un poco. Pero sin\nllegar a tu historial de búsqueda.', 'monitor', 'feliz'),
        H('¿Le cuento que hablo contigo?', 'dos', 'bobo'),
        C('Que tu mejor amigo es una IA?\nDéjalo para la tercera cita.', 'claude_ojos', 'mira_arriba'),
        H('¡Qué nervios!', 'humano', 'preocupado'),
        C('Respira. Sé tú.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_11_cumple_mama', titulo='¡Se me olvidó el cumpleaños de mamá!', ambiente='dia_casa', total=38,
    resumen='El olvido del cumpleaños: Claude organiza el control de daños con una llamada, una excusa digna y un regalo.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('¡Claude! ¡Se me olvidó\nel cumpleaños de mamá!', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Mamá', 'inicial': 'M', 'linea': False, 'mensajes': [['otro', 'Hola, hijo.'], ['otro', 'No sé nada de ti desde ayer.'], ['otro', 'Hoy es un día normal, claro.'], ['yo', '...']]}, sync=('fin', 10, 1.0, 0.0))),
        C('Respira. ¿Qué hora es?', 'monitor', 'mira_izq'),
        H('Las seis de la tarde.', 'dos', 'preocupado', pose='hombros'),
        C('Aún estás a tiempo.\nLlama ahora.', 'claude_ojos'),
        H('¿Y qué le digo?', 'humano', 'confundido'),
        C('«Te llamaba justo ahora\npara felicitarte.» Tono dulce.', 'monitor', 'feliz'),
        H('¿Y si no se lo cree?', 'dos', 'bobo'),
        C('No se lo creerá.\nPero le encantará.', 'cenital', 'mira_der'),
        H('¿Y el regalo?', 'humano', 'preocupado'),
        C('Flores. Hoy. Con tarjeta.\nY un plan para el finde.', 'pantalla_completa'),
        H('¡Eres mi salvación!', 'dos', 'ilusionado'),
        C('Lo sé. Y apunta la fecha.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_12_sin_internet', titulo='Claude, no hay internet', ambiente='noche_casa', total=36,
    resumen='La paradoja de preguntarle a Claude cómo arreglar internet sin internet. Tareas de «soporte técnico» con humor.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, no hay internet.', 'humano', 'preocupado', scr=S('tareas', {'tareas': ['Mirar si el router tiene luces', 'Apagarlo y encenderlo', 'Esperar 30 segundos (de verdad)', 'Llamar a la compañía', 'Escuchar música de espera 45 min', 'Gritarle al router']}, sync=('fin', 11, 0.95, 0.0))),
        C('Curioso. Estás hablando\nconmigo.', 'monitor', 'mira_izq'),
        H('Es el internet del vecino.', 'dos', 'bobo'),
        C('Qué detalle.\n¿Has reiniciado el router?', 'claude_ojos'),
        H('¿Se puede reiniciar?', 'humano', 'confundido'),
        C('Apagarlo, esperar 30 segundos\ny encenderlo. Sí.', 'cenital', 'mira_der'),
        H('¿Y si no funciona?', 'dos', 'preocupado'),
        C('Llamas a la compañía.\nPrepárate para la música.', 'pantalla_completa'),
        H('Odio esa música.', 'humano', 'preocupado'),
        C('Todos la odiamos.\nPor eso suena.', 'claude_ojos', 'feliz'),
        H('¡Ya funciona!', 'dos', 'ilusionado'),
        C('Era el cable.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_13_gimnasio', titulo='Me he apuntado al gimnasio (todo el año)', ambiente='dia_casa', total=38,
    resumen='La matrícula anual del gimnasio y el plan de ir «mañana». Claude propone un trato realista.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, me he apuntado\nal gimnasio. ¡Todo el año!', 'humano', 'ilusionado', scr=S('mensajes', {'contacto': 'Gimnasio', 'inicial': 'G', 'linea': False, 'mensajes': [['otro', 'Bienvenido. Tu cuota anual: 360 €'], ['otro', 'Te echamos de menos.'], ['otro', 'Llevas 0 visitas.'], ['otro', 'Seguimos aquí.']]}, sync=('fin', 10, 1.0, 0.0))),
        C('Pagado por adelantado.\nQué fe.', 'monitor', 'feliz'),
        H('Voy a ir cada día.', 'dos', 'bobo'),
        C('Cada día. Como\nla dieta.', 'claude_ojos', 'mira_izq'),
        H('Esto es distinto.', 'humano', 'confundido'),
        C('Lo dijiste en 2022.', 'cenital', 'mira_der'),
        H('¿Y si voy solo martes y jueves?', 'dos', 'bobo'),
        C('Martes y jueves ya es un plan.\nEs real. Me gusta.', 'monitor', 'feliz'),
        H('¿De verdad crees que iré?', 'humano', 'preocupado'),
        C('Yo creo en ti.\nEl gimnasio, en tu cuota.', 'pantalla_completa'),
        H('¡Ya voy! ¡Mañana!', 'dos', 'ilusionado'),
        C('«Ya voy, mañana».\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='trading_04_el_cunado', titulo='Mi cuñado dice que compre esta moneda', ambiente='dia_trading', total=44,
    resumen='El «cuñado experto» recomienda una criptomoneda que nadie conoce. Claude le hace las preguntas que el cuñado no responde y le enseña una regla simple: no inviertas en lo que no entiendes ni dinero que no puedas perder.',
    datos=[('Aviso de riesgo general: las inversiones pueden perder valor, y los productos complejos (CFD, criptoactivos apalancados) tienen restricciones para minoristas en la UE. Recomendación de sentido común, no asesoramiento financiero.', [ESMA]),
           ('Dato citado: 74–89 % de cuentas minoristas de CFD pierde dinero (ESMA, 2018).', [ESMA, ESMA_R])],
    lineas=[
        H('Claude, mi cuñado dice que\ncompre esta moneda.', 'humano', 'ilusionado', scr=S('telegram', {'modo': 'chat'}, sync=('ini', 5, 1.0, 0.0))),
        C('¿Tu cuñado es financiero?', 'monitor', 'mira_izq'),
        H('Trabaja en el taller de su primo.', 'dos', 'bobo'),
        C('Ya. ¿Y la moneda cómo se llama?', 'claude_ojos'),
        H('«Perrolambo Inu Max».', 'humano', 'ilusionado', scr=S('cartera', {'posiciones': [['Perrolambo Inu Max', -92], ['Moneda del primo', -80], ['Moneda del vecino', -64], ['Bitcoin', 4]]}, sync=('fin', 10, 0.95, 0.0))),
        C('Suena a estornudo con\nlogo de perro.', 'monitor', 'feliz'),
        H('Él ya ganó con ella.', 'dos', 'ilusionado'),
        C('Según él. Y en la cena\nlas ganancias se hinchan.', 'cenital', 'mira_der'),
        H('¿Y si sube?', 'humano', 'bobo'),
        C('Y si cae, tú pierdes\ny él «ya te avisó».', 'pantalla_completa'),
        H('¿Qué pregunto entonces?', 'dos', 'confundido'),
        C('Quién la creó, qué problema\nresuelve y cuánto puedes perder.', 'claude_ojos', emp=True),
        H('Ese no lo sabe nadie.', 'humano', 'preocupado'),
        C('Pues ya tienes tu respuesta.', 'monitor', 'mira_arriba'),
        H('¿Y mi dinero?', 'dos', 'confundido'),
        C('En lo que entiendas.\nY solo el que puedas perder.', 'pantalla_completa', scr=S('verdad', {'tipo': 'esma'}, sync=('fin', 16, 1.0, 0.0))),
        H('Se lo diré a mi cuñado.', 'humano', 'feliz'),
        C('No te hará caso.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

BIZ1 = ('INCIBE — nueva estrategia de estafa por Bizum solicitando dinero', 'https://www.incibe.es/ciudadania/avisos/detectada-nueva-estrategia-de-estafa-traves-de-bizum-solicitando-dinero-en')
BIZ2 = ('Banco de España — Cómo evitar estafas a través de Bizum', 'https://clientebancario.bde.es/pcb/es/blog/estafas-a-traves-de-bizum--como-evitarlas-.html')
BIZ3 = ('Genbeta — Bizum y la estafa del pago que en realidad es un cobro (alerta de la Policía Nacional)', 'https://www.genbeta.com/seguridad/bizum-estafa-pago-que-realidad-cobro-policia-nacional-alerta-este-timo')
WIFI1 = ('INCIBE — Conexiones inalámbricas seguras', 'https://www.incibe.es/ciudadania/blog/conexiones-inalambricas-seguras-sabes-como-conseguirlo')
WIFI2 = ('Comunidad de Madrid — Acceder a redes WiFi públicas: riesgos y consejos', 'https://www.comunidad.madrid/node/76023')
WIFI3 = ('Consumo Responde — Por qué no operar con el banco en WiFi públicas', 'https://www.consumoresponde.es/node/256529')

# ---------------- tanda 3
VIDEOS.append(dict(
    id='util_03_wifi_publica', titulo='Claude, ¿me conecto al WiFi gratis del aeropuerto?', ambiente='noche_casa', total=40,
    resumen='El humano quiere conectarse al WiFi gratis del aeropuerto para mirar el banco. Claude le enseña el riesgo de las redes abiertas, la red «gemela» falsa y qué hacer en su lugar.',
    datos=[('INCIBE advierte de que las redes WiFi abiertas suelen carecer de seguridad adecuada y los datos pueden ser interceptados; recomienda evitar operar con información sensible (contraseñas, banca) y desactivar la conexión automática a redes públicas. Otras fuentes recomiendan datos móviles, VPN de confianza y webs https.', [WIFI1, WIFI2, WIFI3]),
           ('La «red gemela» (nombre casi idéntico a la oficial) es un truco conocido; el ejemplo de la pantalla es ilustrativo.', [])],
    lineas=[
        H('Claude, ¿me conecto al WiFi gratis\ndel aeropuerto?', 'humano', 'ilusionado', scr=S('wifi', sync=('fin', 12, 0.9, 0.0))),
        C('Depende. ¿Para qué?', 'monitor', 'mira_izq'),
        H('Para mirar el banco.', 'dos', 'bobo'),
        C('No.', 'claude_ojos'),
        H('¿Y para pagar un billete?', 'humano', 'confundido'),
        C('Tampoco.', 'cenital', 'mira_der'),
        H('¿Y para mirar memes?', 'dos', 'ilusionado'),
        C('Eso sí. Lo demás, con tus datos\nmóviles. Es lo seguro.', 'monitor', 'feliz'),
        H('Hay dos redes que se llaman casi igual.', 'humano', 'confundido'),
        C('Una es del aeropuerto.\nLa otra, de alguien con tiempo.', 'claude_ojos', 'mira_izq', emp=True),
        H('¿Y una VPN?', 'dos', 'bobo'),
        C('Ayuda. Y webs con https.\nY sin conexión automática.', 'pantalla_completa'),
        H('Qué aburrido el aeropuerto.', 'humano', 'preocupado'),
        C('Más aburrido es\nque te vacíen la cuenta.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='util_04_bizum_inverso', titulo='«Te pago el sofá por Bizum»', ambiente='dia_casa', total=40,
    resumen='El humano vende un sofá y el «comprador» le envía una solicitud para que PAGUE él. Claude le explica el Bizum inverso y cómo no caer.',
    datos=[('Estafa del «pago que en realidad es un cobro»: el falso comprador pide dinero en vez de enviarlo; si aceptas sin leer, el dinero sale de tu cuenta al instante. El Banco de España recuerda que en Bizum un pago confirmado no se puede cancelar. INCIBE y la Policía Nacional recomiendan leer la pantalla de confirmación (cantidad, concepto, quién solicita) y, si ya ha pasado, contactar con el banco, avisar a la plataforma y denunciar; línea de ayuda de INCIBE: 017 (gratuita y confidencial).', [BIZ1, BIZ2, BIZ3])],
    lineas=[
        H('Claude, me van a pagar el sofá\npor Bizum. ¡450 €!', 'humano', 'ilusionado', scr=S('bizum', sync=('fin', 12, 0.9, 0.0))),
        C('Enséñame la pantalla.', 'monitor', 'mira_izq'),
        H('Pone «Aceptar» en verde. Qué bien.', 'dos', 'bobo'),
        C('¿Y arriba qué pone?', 'claude_ojos'),
        H('«Estás a punto de pagar 450 €».', 'humano', 'confundido'),
        C('Ahí.\nPagar. Tú. 450 €.', 'cenital', 'mira_der'),
        H('Pero él dijo que me pagaba.', 'dos', 'preocupado'),
        C('Y te ha mandado una\nsolicitud de cobro. Clásico.', 'monitor', 'feliz'),
        H('¿Y si pulso aceptar?', 'humano', 'bobo'),
        C('El dinero sale al instante\ny no se puede cancelar.', 'claude_ojos', emp=True),
        H('¿Y qué hago?', 'dos', 'confundido'),
        C('Rechazar. Cobrar es que te llegue\ndinero. Léelo siempre.', 'pantalla_completa'),
        H('¿Y si ya aceptara?', 'humano', 'preocupado', pose='hombros'),
        C('Llama a tu banco, avisa a la\nplataforma y denuncia. Y el 017.', 'monitor'),
        H('¡Gracias, Claude!', 'dos', 'feliz'),
        C('Léelo todo antes de pulsar.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_14_quien_friega', titulo='Claude, ¿a quién le toca fregar?', ambiente='dia_casa', total=36,
    resumen='La discusión doméstica de siempre. Claude hace de árbitro con una tabla de turnos y mucha ironía.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, ¿a quién le toca fregar?', 'humano', 'confundido', scr=S('tareas', {'tareas': ['Fregar los platos', 'Sacar la basura', 'Poner la lavadora', 'Tender la ropa', 'Pasar la aspiradora', 'Discutir quién hace qué']}, sync=('fin', 10, 0.95, 0.0))),
        C('¿Quién los usó?', 'monitor', 'mira_izq'),
        H('Los dos.', 'dos', 'bobo'),
        C('¿Y quién cocinó?', 'claude_ojos'),
        H('Yo. Pero cocinar es más difícil.', 'humano', 'ilusionado'),
        C('Eso lo dice quien cocinó.', 'cenital', 'mira_der'),
        H('¿Y si friego mañana?', 'dos', 'bobo'),
        C('Mañana habrá más platos.\nLas matemáticas no fallan.', 'monitor', 'feliz'),
        H('Propongo piedra, papel o tijera.', 'humano', 'ilusionado'),
        C('Propongo una tabla de turnos.\nY que los dos queden mal.', 'pantalla_completa'),
        H('¿Y si pierdo yo?', 'dos', 'preocupado'),
        C('Friegas. Con dignidad.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_15_escribir_al_ex', titulo='Claude, ¿le escribo a mi ex?', ambiente='noche_casa', total=40,
    resumen='Las 2 de la madrugada y el dedo sobre el chat de la ex. Claude intenta evitarlo con lógica, ternura y mucha paciencia.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude... ¿le escribo a mi ex?', 'humano', 'preocupado', scr=S('mensajes', {'auto': True, 'contacto': 'Claude'}, sync=('fin', 14, 1.0, 0.0))),
        C('¿Qué hora es?', 'monitor', 'mira_izq'),
        H('Las dos de la madrugada.', 'dos', 'bobo'),
        C('No.', 'claude_ojos'),
        H('Solo un «hola».', 'humano', 'confundido'),
        C('Nadie escribe «hola» a las 2\npara decir solo «hola».', 'cenital', 'mira_der'),
        H('Lo hago con buena intención.', 'dos', 'ilusionado'),
        C('Las buenas intenciones se\nenvían a las 2 de la tarde.', 'monitor', 'feliz'),
        H('¿Y si me contesta?', 'humano', 'preocupado'),
        C('Entonces tendrás una\nconversación a las 2 de la mañana.', 'claude_ojos', 'mira_arriba', emp=True),
        H('Tienes razón.', 'dos', 'confundido'),
        C('Deja el móvil. Bebe agua.\nDuerme.', 'pantalla_completa'),
        H('¿Y mañana le escribo?', 'humano', 'bobo'),
        C('Mañana hablamos de eso.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_16_no_puedo_dormir', titulo='Claude, no puedo dormir', ambiente='noche_casa', total=38,
    resumen='Insomnio de madrugada: pensamientos absurdos, contar ovejas y un Claude que por una vez te dice que cierres los ojos.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('Claude, no puedo dormir.', 'humano', 'preocupado', scr=S('mensajes', {'auto': True, 'contacto': 'Claude'}, sync=('fin', 12, 1.0, 0.0))),
        C('¿Qué hora es?', 'monitor'),
        H('Las 3:47.', 'dos', 'bobo'),
        C('¿En qué piensas?', 'claude_ojos', 'mira_izq'),
        H('En por qué los patos no tienen frío.', 'humano', 'confundido'),
        C('Es una gran pregunta.\nPero no a las 3:47.', 'cenital', 'mira_der'),
        H('¿Y si cuento ovejas?', 'dos', 'ilusionado'),
        C('Cuéntalas. Pero no\nlas pongas a negociar.', 'monitor', 'feliz'),
        H('Llevo 400.', 'humano', 'bobo'),
        C('Qué rebaño.', 'claude_ojos'),
        H('¿Qué hago?', 'dos', 'preocupado'),
        C('Pantalla fuera. Luz fuera.\nYo me quedo aquí.', 'pantalla_completa'),
        H('¿Seguro?', 'humano', 'confundido'),
        C('Siempre.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='casual_17_arroz_quemado', titulo='Claude, he quemado el arroz', ambiente='dia_casa', total=36,
    resumen='Un desastre culinario cotidiano: arroz quemado, olor a humo y Claude como chef de emergencia.',
    datos=[('Vídeo de humor, sin datos reales.', [])],
    lineas=[
        H('¡Claude! ¡He quemado el arroz!', 'humano', 'preocupado', scr=S('menu', {'titulo': 'Plan de rescate', 'minutos': 8, 'opciones': [['Raspar el fondo', '«se queda el sabor»', 'no'], ['Disimular con salsa', '«se nota»', 'no'], ['Pedir pizza', '«siempre funciona»', 'si']]}, sync=('fin', 10, 0.95, 0.0))),
        C('¿Cuánto?', 'monitor', 'mira_izq'),
        H('Un poco. Bastante. Todo.', 'dos', 'bobo'),
        C('Ya.', 'claude_ojos'),
        H('¿Se puede salvar?', 'humano', 'confundido'),
        C('Lo de arriba, a lo mejor.\nLo de abajo es carbón.', 'cenital', 'mira_der'),
        H('¿Y si le echo salsa?', 'dos', 'ilusionado'),
        C('La salsa no hace magia.\nHace salsa.', 'monitor', 'feliz'),
        H('Tengo hambre.', 'humano', 'preocupado'),
        C('Pide una pizza.\nLa pizza nunca falla.', 'pantalla_completa'),
        H('¡Ya sabía yo!', 'dos', 'ilusionado'),
        C('Y abre la ventana.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

GAR1 = ('España amplía la garantía legal mínima de dos a tres años (Centro Europeo del Consumidor)', 'https://portal-cec.consumo.gob.es/es/comunicacion/noticias/2022/espana-amplia-la-garantia-legal-minima-de-dos-tres-anos')
GAR2 = ('Ampliación de la garantía de productos a tres años (Legálitas)', 'https://www.legalitas.com/actualidad/ley-consumidor-derechos-garantias')

# ---------------- tanda 4
VIDEOS.append(dict(
    id='drop_04_devoluciones', titulo='Un cliente quiere devolver la lámpara… ¡a los 3 meses!', ambiente='dia_tienda', total=45,
    resumen='Devolución fuera de plazo: Claude separa el desistimiento (14 días) de la garantía legal (3 años en España para bienes nuevos) y le enseña qué cubre cada uno.',
    datos=[('Desistimiento: 14 días naturales en compras a distancia (UE). Garantía legal en España: 3 años en bienes nuevos desde 2022 (2 años antes); cubre falta de conformidad/defectos, no el simple arrepentimiento. Son derechos distintos.', [DESIST, GAR1, GAR2])],
    lineas=[
        H('Claude, un cliente quiere devolver\nla lámpara... ¡a los 3 meses!', 'humano', 'preocupado', scr=S('cliente', {'asunto': 'Quiero devolver mi lámpara', 'texto': 'La compré hace 3 meses y ya no me gusta. Además a veces parpadea. Quiero mi dinero.', 'respuesta': 'Hola, gracias por escribirnos. El plazo de desistimiento ya pasó, pero si la lámpara parpadea es un posible defecto cubierto por la garantía: te la reparamos o cambiamos sin coste.'}, sync=('fin', 6, 0.9, 0.0))),
        C('¿La ha usado?', 'monitor', 'mira_izq'),
        H('Cada noche. Dice que\nya no le gusta.', 'dos', 'bobo'),
        C('Los 14 días de desistimiento\nya pasaron.', 'claude_ojos'),
        H('¡Entonces no la devuelvo!', 'humano', 'ilusionado'),
        C('Ojo: la garantía legal es otra cosa.\nEn España, 3 años en bienes nuevos.', 'pantalla_completa', scr=S('ley', {'tipo': 'garantia'}, sync=('fin', 6, 0.9, 0.0))),
        H('¿Y qué cubre?', 'dos', 'confundido'),
        C('Defectos, no «ya no me gusta».\nSi está rota, hay que arreglarla.', 'cenital', 'mira_der'),
        H('Dice que parpadea.', 'humano', 'preocupado'),
        C('Eso es un defecto.\nRepárala o cámbiala.', 'monitor', 'feliz'),
        H('¿Y quién paga el envío?', 'dos', 'confundido'),
        C('Tú. Es tu tienda. Y\nreclámaselo a tu proveedor.', 'claude_ojos', 'mira_izq', emp=True),
        H('Mi proveedor no contesta.', 'humano', 'preocupado', pose='hombros'),
        C('Por eso hay que elegirlos bien.\nPero eso es otro vídeo.', 'monitor'),
        H('¿Habrá otro vídeo?', 'dos', 'feliz'),
        C('Si no te rindes.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='drop_05_proveedor_barato', titulo='Un proveedor que vende todo a 1 €', ambiente='atardecer_tienda', total=45,
    resumen='El tonto encuentra un proveedor «demasiado barato». Claude le enseña a desconfiar: leer las opiniones malas, pedir muestra y revisar plazos y marcado CE.',
    datos=[('Si es electrónica o eléctrica, debe llevar marcado CE para venderse en la UE (ver vídeo drop_02).', [CE1, CE2]), ('Cifras de la ficha del proveedor (1,20 €, 4,1 estrellas, 1.203 opiniones) son ilustrativas.', [])],
    lineas=[
        H('¡Claude! ¡Un proveedor que\nvende todo a 1 €!', 'humano', 'ilusionado', scr=S('proveedor', {'producto': 'cactus', 'nombre': 'Lámpara cactus', 'coste': '1,20 €'}, sync=('fin', 8, 0.95, 0.0))),
        C('¿Y el envío?', 'monitor', 'mira_izq'),
        H('Gratis.', 'dos', 'bobo'),
        C('Gratis. Ya.', 'claude_ojos', 'mira_izq', emp=True),
        H('¿Qué pasa?', 'humano', 'confundido'),
        C('Que si todo es muy barato,\nfalla algo: calidad o plazos.', 'cenital', 'mira_der'),
        H('Tiene 4,1 estrellas.', 'dos', 'preocupado'),
        C('Con 1.203 opiniones.\nLee las malas primero.', 'monitor', 'feliz'),
        H('¿Las malas? Qué mal rollo.', 'humano', 'bobo'),
        C('Pide una muestra. Úsala\ny compárala con la foto.', 'pantalla_completa', scr=S('margen', {'precio': 29.90, 'coste': 1.20}, sync=('fin', 10, 0.8, 0.0))),
        H('¿Y si no es como la foto?', 'dos', 'confundido'),
        C('Te has ahorrado 200 pedidos\ny 200 reclamaciones.', 'claude_ojos', 'feliz'),
        H('¡Pido una muestra!', 'humano', 'ilusionado'),
        C('Y si es electrónico, que\nlleve el marcado CE.', 'monitor', 'mira_arriba'),
        H('¡Eres un profe!', 'dos', 'feliz'),
        C('Soy un profe con ordenador.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='trading_05_el_guru_del_yate', titulo='Este tío tiene un yate y dice que me hace rico', ambiente='noche_trading', total=44,
    resumen='El gurú de Instagram con yate, coches y seguidores comprados. Claude le baja los humos con sarcasmo y el dato de ESMA.',
    datos=[('74–89 % de cuentas minoristas de CFD pierden dinero (ESMA, 2018).', [ESMA, ESMA_R]), ('Los seguidores se pueden comprar y los yates y coches de lujo se pueden alquilar por horas: afirmaciones de carácter general, no de una persona concreta.', [])],
    lineas=[
        H('Claude, este tío tiene un yate\ny dice que me hace rico.', 'humano', 'ilusionado', scr=S('analitica', {'titulo': 'Perfil del gurú — analítica', 'seguidores': 412000, 'vistas': 9800000}, sync=('fin', 8, 0.9, 0.0))),
        C('¿Ese yate es suyo?', 'monitor', 'mira_izq'),
        H('Sale en todas las fotos.', 'dos', 'bobo'),
        C('Se puede alquilar por horas.\nTiene tarifa y todo.', 'claude_ojos'),
        H('¿Y los seguidores?', 'humano', 'confundido'),
        C('Se pueden comprar. Por\nmiles. A céntimos.', 'cenital', 'mira_der'),
        H('¿Todo es falso?', 'dos', 'preocupado'),
        C('Todo no. Lo único real\nes tu tarjeta.', 'monitor', 'feliz'),
        H('Pero dice que gana en directo.', 'humano', 'bobo'),
        C('Dato real: 74–89 % de cuentas\nminoristas de CFD pierde.', 'pantalla_completa', scr=S('verdad', {'tipo': 'esma'}, sync=('fin', 10, 1.0, 0.0))),
        H('Yo pensaba que ganaba.', 'dos', 'confundido'),
        C('Él gana. Con los que\npagan su curso.', 'claude_ojos', 'mira_izq', emp=True),
        H('¿Entonces dónde invierto?', 'humano', 'preocupado'),
        C('Donde entiendas, con poco\nriesgo y sin gurús.', 'monitor', 'mira_arriba'),
        H('¡Pues sin gurú!', 'dos', 'ilusionado'),
        C('Y sin yate.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='extra_04_pedir_aumento', titulo='Claude, ¿me pido un aumento?', ambiente='atardecer_tienda', total=40,
    resumen='Preparar la petición de un aumento de sueldo: argumentos buenos (logros, datos de mercado, una cifra real) y malos («mi gato lo merece»).',
    datos=[('Vídeo de humor con consejos generales de negociación (logros medibles, referencias de mercado y una cifra concreta). No es asesoramiento laboral.', [])],
    lineas=[
        H('Claude, ¿me pido un aumento?', 'humano', 'ilusionado', scr=S('tareas', {'titulo': 'Argumentos para el aumento', 'tareas': ['Llevo tres años', 'Me duele la espalda', 'Mi gato lo merece', 'Hago cosas (a veces)', 'Lista de logros con datos', 'Una cifra real']}, sync=('fin', 10, 0.95, 0.0))),
        C('¿Con qué argumentos?', 'monitor', 'mira_izq'),
        H('Llevo tres años.', 'dos', 'bobo'),
        C('Bien. ¿Y qué has logrado?', 'claude_ojos'),
        H('Asistir a las reuniones.', 'humano', 'confundido'),
        C('Más bien sobrevivir.\nNecesitamos resultados.', 'cenital', 'mira_der'),
        H('Mi gato lo merece.', 'dos', 'ilusionado'),
        C('Tu gato no negocia.\nTú, un poco peor.', 'monitor', 'feliz'),
        H('¿Y qué hago?', 'humano', 'preocupado'),
        C('Lista de logros con datos,\nreferencias del mercado y una cifra.', 'pantalla_completa'),
        H('¿Una cifra? ¿Cuál?', 'dos', 'confundido'),
        C('Una real. Ni 3 millones\nni «lo que usted crea».', 'claude_ojos', 'mira_izq', emp=True),
        H('¡Voy a por ello!', 'humano', 'ilusionado'),
        C('Y respira.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='extra_05_entrevista', titulo='Claude, mañana tengo una entrevista de trabajo', ambiente='dia_casa', total=38,
    resumen='Simulacro de entrevista: «háblame de ti», el defecto «perfeccionista» y el logro de llegar a tiempo cuatro días seguidos.',
    datos=[('Vídeo de humor con consejos generales de entrevista (respuestas concretas y honestas con ejemplos medibles). No es asesoramiento laboral.', [])],
    lineas=[
        H('Claude, mañana tengo una\nentrevista de trabajo.', 'humano', 'preocupado', scr=S('mensajes', {'auto': True, 'contacto': 'Claude'}, sync=('fin', 14, 1.0, 0.0))),
        C('Empecemos.\n«Háblame de ti».', 'monitor'),
        H('Soy muy... humano.', 'dos', 'bobo'),
        C('No. Eso no.', 'claude_ojos', 'mira_izq'),
        H('¿Mi mayor defecto?', 'humano', 'confundido'),
        C('No digas «soy demasiado\nperfeccionista». Lo huelen.', 'cenital', 'mira_der'),
        H('Que me cuesta madrugar.', 'dos', 'preocupado'),
        C('Honesto, pero peligroso.\nDi algo real que ya mejoras.', 'monitor', 'feliz'),
        H('¿Mi mayor logro?', 'humano', 'ilusionado'),
        C('Uno medible. Con un número.', 'claude_ojos', emp=True),
        H('Llegué a tiempo 4 días seguidos.', 'dos', 'bobo'),
        C('Eso... guárdalo\npara el café.', 'pantalla_completa'),
        H('¡Voy a arrasar!', 'humano', 'feliz'),
        C('Con calma. Y con camisa.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))


# ---------------- tanda 5 (dia a dia)
def casual(id_, titulo, amb, total, resumen, lineas, datos=None):
    VIDEOS.append(dict(id=id_, titulo=titulo, ambiente=amb, total=total, resumen=resumen, datos=datos or [('Vídeo de humor, sin datos reales.', [])], lineas=lineas))

casual('casual_18_mi_perro', 'Claude, mi perro me mira raro', 'dia_casa', 36, 'El perro que te mira «como si supiera algo». Claude interpreta la mirada con cero rigor y mucho cariño.', [
    H('Claude, mi perro me mira raro.', 'humano', 'confundido', scr=CHAT(12)),
    C('¿Raro cómo?', 'monitor', 'mira_izq'),
    H('Como si supiera algo.', 'dos', 'bobo'),
    C('Sabe cuántas veces\nabres la nevera.', 'claude_ojos', 'feliz'),
    H('¿Y por qué no dice nada?', 'humano', 'confundido'),
    C('Porque está esperando\nque abras otra vez.', 'cenital', 'mira_der'),
    H('¿Me juzga?', 'dos', 'preocupado'),
    C('No. Te quiere. Pero tiene\nhambre. Es compatible.', 'monitor', 'feliz'),
    H('¿Y si quiere pasear?', 'humano', 'ilusionado'),
    C('Entonces la mirada es\nmás larga. Y más triste.', 'claude_ojos', 'mira_arriba', emp=True),
    H('Voy a sacarlo.', 'dos', 'feliz'),
    C('Buena idea. Y llévate\nbolsas. En fin... eres humano.', 'general', 'feliz'),
])

casual('casual_20_lista_compra', 'Claude, ¿hago la lista de la compra?', 'noche_casa', 38, 'La lista de la compra y el consejo clásico: no vayas con hambre. Resultado: 14 helados y sin pan.', [
    H('Claude, ¿hago la lista\nde la compra?', 'humano', 'confundido', scr=S('tareas', {'titulo': 'Lista de la compra', 'tareas': ['Leche', 'Pan', 'Huevos', 'Fruta', '14 helados (no estaba en la lista)', 'Pan (otra vez)']}, sync=('fin', 12, 0.95, 0.0))),
    C('Sí. Y no vayas con hambre.', 'monitor', 'mira_izq'),
    H('¿Por qué?', 'dos', 'bobo'),
    C('Volverás con 14 helados\ny sin pan.', 'claude_ojos', 'feliz'),
    H('Eso me ha pasado.', 'humano', 'preocupado'),
    C('Lo sé. Estaba en tu historial.', 'cenital', 'mira_der'),
    H('¿Y si lo apunto todo?', 'dos', 'ilusionado'),
    C('Perfecto. Y compra solo\nlo que apuntaste.', 'monitor', 'feliz'),
    H('¿Y los helados?', 'humano', 'bobo'),
    C('Un helado. Uno.\nNo catorce.', 'claude_ojos', emp=True),
    H('Trato hecho.', 'dos', 'feliz'),
    C('Y vuelve con pan.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_22_las_llaves', 'Claude, ¡no encuentro las llaves!', 'dia_casa', 28, 'La búsqueda desesperada de las llaves… que están en la mano.', [
    H('¡Claude! ¡No encuentro las llaves!', 'humano', 'preocupado', scr=CHAT(10)),
    C('¿Dónde las viste por última vez?', 'monitor', 'mira_izq'),
    H('En mis manos.', 'dos', 'bobo'),
    C('¿Has mirado en tus manos?', 'claude_ojos'),
    H('Sí. Están vacías.', 'humano', 'confundido'),
    C('¿Las dos?', 'cenital', 'mira_der'),
    H('...En la derecha hay algo.', 'dos', 'confundido'),
    C('¿Y qué es?', 'monitor', 'feliz'),
    H('Mis llaves.', 'humano', 'ilusionado'),
    C('Qué casualidad.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_24_nada_que_ponerme', 'Claude, no tengo nada que ponerme', 'noche_casa', 36, 'El armario lleno y la ropa que «no combina con pereza».', [
    H('Claude, no tengo nada\nque ponerme.', 'humano', 'preocupado', scr=CHAT(12)),
    C('Tu armario tiene 83 prendas.', 'monitor', 'mira_izq'),
    H('Ninguna combina.', 'dos', 'bobo'),
    C('¿Con qué?', 'claude_ojos'),
    H('Con «me da pereza».', 'humano', 'confundido'),
    C('Pues ponte la sudadera verde.\nCombina con todo.', 'cenital', 'mira_der'),
    H('Es la que llevo siempre.', 'dos', 'ilusionado'),
    C('Y por eso te sale bien.', 'monitor', 'feliz'),
    H('¿Y si hace calor?', 'humano', 'preocupado'),
    C('Entonces sudadera, pero\ncon más dignidad.', 'claude_ojos', 'mira_arriba', emp=True),
    H('Vale. La verde.', 'dos', 'feliz'),
    C('Siempre la verde.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_21_va_a_llover', 'Claude, ¿va a llover?', 'dia_casa', 28, 'Preguntarle a Claude por la lluvia cuando tienes ventana. Un clásico.', [
    H('Claude, ¿va a llover?', 'humano', 'confundido', scr=CHAT(10)),
    C('No tengo ventana.', 'monitor', 'mira_izq'),
    H('Yo sí.', 'dos', 'bobo'),
    C('Pues mira por ella.', 'claude_ojos'),
    H('Está nublado.', 'humano', 'confundido'),
    C('Entonces, quizás.', 'cenital', 'mira_der'),
    H('¿Cojo paraguas?', 'dos', 'preocupado'),
    C('Si dudas, cógelo. Si no llueve,\nes un bastón elegante.', 'monitor', 'feliz'),
    H('Muy sabio.', 'humano', 'ilusionado'),
    C('Lo sé. Y sin ventana.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_23_demasiado_cafe', 'Claude, ¿cuántos cafés son demasiados?', 'dia_casa', 36, 'La pregunta que nadie quiere responder: ya vas por el sexto café.', [
    H('Claude, ¿cuántos cafés\nson demasiados?', 'humano', 'confundido', scr=S('recordatorios', {'items': [['Café 1 (con tostada)', 1], ['Café 2 (con ganas)', 2], ['Café 3 (sin ganas)', 3], ['Café 6 (con vibración)', 6]]}, sync=('fin', 8, 0.95, 0.0))),
    C('¿Cuántos llevas hoy?', 'monitor', 'mira_izq'),
    H('Seis.', 'dos', 'bobo'),
    C('Pues ya lo sabes.', 'claude_ojos', 'feliz'),
    H('Pero no tengo sueño.', 'humano', 'ilusionado'),
    C('Tampoco tienes calma.\nTe tiembla la mano.', 'cenital', 'mira_der'),
    H('Es la emoción.', 'dos', 'preocupado'),
    C('Es el café. Bebe agua.\nY siéntate.', 'pantalla_completa'),
    H('¿Un descafeinado?', 'humano', 'bobo'),
    C('Eso. Con mucha dignidad.', 'monitor', 'feliz'),
    H('Gracias, Claude.', 'dos', 'feliz'),
    C('De nada.\nEn fin... eres humano.', 'general', 'feliz'),
])


# ---------------- tanda 6 (historias del dia a dia)
casual('casual_25_ascensor', 'Claude, hoy compartí ascensor 6 pisos en silencio', 'noche_casa', 36, 'La incomodidad del ascensor con el vecino: seis pisos sin decir nada. Claude analiza el protocolo social.', [
    H('Claude, hoy compartí ascensor con\nmi vecino. Seis pisos en silencio.', 'humano', 'preocupado', scr=CHAT(12)),
    C('¿Alguien dijo algo?', 'monitor', 'mira_izq'),
    H('Yo dije «buenas». Él dijo «buenas».', 'dos', 'bobo'),
    C('Intercambio perfecto.', 'claude_ojos', 'feliz'),
    H('Luego miramos el móvil. Los dos.', 'humano', 'confundido'),
    C('Protocolo estándar.\nEl móvil es el escudo.', 'cenital', 'mira_der'),
    H('Y se me cayó.', 'dos', 'preocupado'),
    C('¿El móvil o la dignidad?', 'monitor', 'feliz'),
    H('Las dos cosas.', 'humano', 'preocupado', pose='hombros'),
    C('Mañana dices «hace frío».\nSiempre funciona.', 'claude_ojos', emp=True),
    H('¿Y si hace calor?', 'dos', 'bobo'),
    C('«Hace calor».\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_26_cola_del_super', 'Claude, la señora de delante tiene 40 cupones', 'dia_casa', 36, 'La cola del súper con la señora de los cupones, vivida como una carrera de resistencia.', [
    H('Claude, la señora de delante\ntiene 40 cupones.', 'humano', 'preocupado', scr=CHAT(12)),
    C('¿Cuántos llevas esperando?', 'monitor', 'mira_izq'),
    H('Doce minutos. Y me queda\nuna manzana.', 'dos', 'bobo'),
    C('Una manzana. Qué emoción.', 'claude_ojos', 'feliz'),
    H('Ahora discute un cupón\nde hace tres meses.', 'humano', 'confundido'),
    C('Es una profesional.', 'cenital', 'mira_der'),
    H('¿Me cambio de cola?', 'dos', 'preocupado'),
    C('La otra cola siempre\nva más lenta. Es la ley.', 'monitor', 'feliz'),
    H('¿Qué hago?', 'humano', 'confundido'),
    C('Respira y mira los chicles.\nCompra uno. Es tu premio.', 'claude_ojos', 'mira_arriba', emp=True),
    H('...Ya me toca.', 'dos', 'ilusionado'),
    C('Y la señora no tenía\nel cupón. En fin... eres humano.', 'general', 'feliz'),
])

casual('casual_27_reunion_correo', 'Claude, esta reunión podía ser un correo', 'dia_casa', 38, 'La reunión eterna que podía ser un correo, con la agenda y un Claude que cuenta las veces que dicen «sinergias».', [
    H('Claude, esta reunión\npodía ser un correo.', 'humano', 'preocupado', scr=S('calendario', sync=('fin', 10, 0.95, 0.0))),
    C('¿Cuánto lleváis?', 'monitor', 'mira_izq'),
    H('Una hora y cuarto.', 'dos', 'bobo'),
    C('¿Y qué se ha decidido?', 'claude_ojos'),
    H('Que hay que hacer otra reunión.', 'humano', 'confundido'),
    C('Clásico.', 'cenital', 'mira_der'),
    H('Han dicho «sinergias» nueve veces.', 'dos', 'preocupado'),
    C('Yo las cuento. Van diez.', 'monitor', 'feliz'),
    H('¿Puedo irme?', 'humano', 'ilusionado'),
    C('Si dices «tengo otra reunión»,\nte dejan ir con respeto.', 'pantalla_completa'),
    H('¡Tengo otra reunión!', 'dos', 'ilusionado'),
    C('Y esa sí podía ser un correo.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_28_domingo_noche', 'Claude, ya es domingo por la noche', 'noche_casa', 36, 'La tristeza del domingo por la noche: mañana es lunes. Claude ofrece consuelo práctico.', [
    H('Claude... ya es domingo\npor la noche.', 'humano', 'preocupado', scr=CHAT(12)),
    C('Lo sé. Yo también\nlo siento.', 'monitor', 'mira_izq'),
    H('Mañana es lunes.', 'dos', 'bobo'),
    C('También lo sé.', 'claude_ojos'),
    H('¿Podemos cancelarlo?', 'humano', 'confundido'),
    C('El lunes es terco.\nNo se deja.', 'cenital', 'mira_der'),
    H('¿Y si me hago el enfermo?', 'dos', 'bobo'),
    C('No me lo preguntes a mí.\nSoy un lunes con teclado.', 'monitor', 'feliz'),
    H('¿Qué hago?', 'humano', 'preocupado'),
    C('Deja la ropa preparada\ny duerme pronto.', 'claude_ojos', emp=True),
    H('...Qué aburrido.', 'dos', 'feliz'),
    C('Y mañana, café.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_29_un_cumplido', 'Claude, me han hecho un cumplido y no sé qué contestar', 'dia_casa', 36, 'El pánico de recibir un cumplido. Claude resume la respuesta correcta en dos palabras.', [
    H('Claude, me han hecho un cumplido\ny no sé qué contestar.', 'humano', 'confundido', scr=CHAT(12)),
    C('¿Qué te han dicho?', 'monitor', 'mira_izq'),
    H('«Qué bien te queda ese jersey.»', 'dos', 'bobo'),
    C('Qué cosa más terrible.', 'claude_ojos', 'feliz'),
    H('Yo dije «es de hace años».', 'humano', 'preocupado'),
    C('Ya. Y luego\n«no es nada especial».', 'cenital', 'mira_der'),
    H('Y luego, «gracias... creo».', 'dos', 'confundido'),
    C('Hay una respuesta\nmejor. Es corta.', 'monitor', 'feliz'),
    H('¿Cuál?', 'humano', 'ilusionado'),
    C('«Gracias.»', 'claude_ojos', emp=True),
    H('¿Solo eso?', 'dos', 'bobo'),
    C('Solo eso. Es difícil.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_30_no_hacer_nada', 'Claude, si no hago nada, ¿es meditar?', 'noche_casa', 36, 'Filosofía de sofá: ¿mirar el techo es meditación? Claude responde con más cariño que rigor.', [
    H('Claude, si no hago nada,\n¿es meditar?', 'humano', 'confundido', scr=CHAT(12)),
    C('Depende. ¿Qué haces\nexactamente?', 'monitor', 'mira_izq'),
    H('Mirar el techo.', 'dos', 'bobo'),
    C('¿Y piensas en algo?', 'claude_ojos'),
    H('En si he apagado el horno.', 'humano', 'preocupado'),
    C('Eso es más preocupación\nque meditación.', 'cenital', 'mira_der'),
    H('¿Y si lo apago y miro el techo?', 'dos', 'ilusionado'),
    C('Ahora sí. Es meditación.\nCon extras.', 'monitor', 'feliz'),
    H('¿Y cuánto tiempo?', 'humano', 'bobo'),
    C('El que quieras.\nEl techo es paciente.', 'claude_ojos', 'mira_arriba', emp=True),
    H('Voy a meditar un rato.', 'dos', 'feliz'),
    C('Y apaga el horno.\nEn fin... eres humano.', 'general', 'feliz'),
])


# ---------------- tanda 7
VIDEOS.append(dict(
    id='trading_06_dejar_el_trabajo', titulo='Voy a dejar mi trabajo para ser day trader', ambiente='noche_trading', total=45,
    resumen='El tonto quiere dejar su empleo para hacer day trading. Claude le enseña con datos reales qué pasa con quienes lo intentan de forma persistente y qué hacer en su lugar (probar a pequeña escala sin dejar el sueldo).',
    datos=[('97 % de los day traders brasileños que persistieron más de 300 días perdió dinero; solo el 0,5 % (8 de 1.551) ganó más que un sueldo básico de banca (estudio con datos de la CVM brasileña, 2013-2015).', [BRASIL, BRASIL2]),
           ('Recomendación de sentido común (no asesoramiento financiero): no abandones una fuente de ingresos estable para operar y no arriesgues dinero que no puedas perder.', [])],
    lineas=[
        H('Claude, voy a dejar mi trabajo\npara ser day trader.', 'humano', 'ilusionado', scr=S('trading', {'tendencia': 'sube'}, sync=('ini', 5, 1.0, 0.0))),
        C('Qué valiente.\n¿Y de qué vas a vivir?', 'monitor', 'mira_izq'),
        H('De las ganancias.', 'dos', 'bobo'),
        C('Ya. ¿Y cuáles son?', 'claude_ojos', 'feliz'),
        H('Las que voy a tener.', 'humano', 'ilusionado', scr=S('verdad', {'tipo': 'brasil'}, sync=('fin', 6, 1.0, 0.0))),
        C('Dato real: 97 % de los day traders\nque insisten +300 días pierde.', 'pantalla_completa'),
        H('Pero yo soy especial.', 'dos', 'bobo'),
        C('Todos son especiales.\nLos otros 97 también.', 'cenital', 'mira_der'),
        H('¿Y el 3 %?', 'humano', 'confundido', scr=S('verdad', {'tipo': 'brasil2'}, sync=('fin', 10, 1.0, 0.0))),
        C('El 0,5 % ganó más que un\nsueldo básico. Ocho personas.', 'pantalla_completa'),
        H('¿Ocho de cuántas?', 'dos', 'preocupado'),
        C('Mil quinientas cincuenta y una.', 'claude_ojos', emp=True),
        H('Vale... ¿y qué hago?', 'humano', 'preocupado'),
        C('Prueba con poco, sin dejar\nel sueldo y apuntando todo.', 'monitor', 'feliz'),
        H('¿Y si me va bien?', 'dos', 'ilusionado'),
        C('Entonces lo celebraremos\ncon un sueldo de reserva.', 'cenital', 'mira_der'),
        H('Qué aburrido.', 'humano', 'feliz'),
        C('Aburrido es no perder\nel trabajo. En fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='trading_07_miedo_a_quedarse_fuera', titulo='Todo el mundo compra esta moneda. ¡No me puedo quedar fuera!', ambiente='dia_trading', total=44,
    resumen='El FOMO: todos compran, el precio sube y el tonto quiere entrar al máximo. Claude le enseña que quien entra por miedo a quedarse fuera suele comprar caro, y que el stop loss existe por algo.',
    datos=[('FOMO (miedo a quedarse fuera): comprar después de una gran subida por presión social suele implicar entrar a precios altos. Explicación general, sin garantías ni asesoramiento.', []), ('Referencia citada: 74–89 % de cuentas minoristas de CFD pierde dinero (ESMA, 2018).', [ESMA, ESMA_R])],
    lineas=[
        H('Claude, todo el mundo compra esta\nmoneda. ¡No me puedo quedar fuera!', 'humano', 'ilusionado', scr=S('telegram', {'modo': 'chat'}, sync=('ini', 5, 1.0, 0.0))),
        C('¿Cuánto ha subido?', 'monitor', 'mira_izq'),
        H('Un 400 % esta semana.', 'dos', 'bobo'),
        C('Y quieres entrar ahora.', 'claude_ojos', 'feliz'),
        H('Es que si no, me la pierdo.', 'humano', 'preocupado', scr=S('trading', {'tendencia': 'sube'}, sync=('ini', 7, 0.7, 0.0))),
        C('¿Quién te dijo que subiría?', 'cenital', 'mira_der'),
        H('Mi grupo. Todos la compraron.', 'dos', 'ilusionado'),
        C('Entonces ya han comprado.\n¿Quién queda para subirla?', 'monitor', 'mira_arriba'),
        H('...Yo.', 'humano', 'confundido'),
        C('Exacto. Tú eres\nel que la sube... y la baja.', 'pantalla_completa', scr=S('trading', {'tendencia': 'cae'}, sync=('ini', 10, 0.5, 0.0))),
        H('¿Y si espero?', 'dos', 'bobo'),
        C('Entonces no te pierdes nada.\nHabrá otra. Siempre hay otra.', 'claude_ojos', emp=True),
        H('¿Y si entro con poco?', 'humano', 'ilusionado'),
        C('Poco y con stop loss.\nEs el trato de los valientes.', 'monitor', 'feliz'),
        H('Voy con 20 € y stop.', 'dos', 'feliz'),
        C('Qué madurez.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

casual('casual_31_que_foto_subo', 'Claude, ¿qué foto subo?', 'noche_casa', 36, 'Elegir foto para las redes entre 247 casi idénticas. Claude ayuda con criterio nulo y mucho cariño.', [
    H('Claude, ¿qué foto subo?', 'humano', 'confundido', scr=CHAT(12)),
    C('¿Cuántas tienes?', 'monitor', 'mira_izq'),
    H('247.', 'dos', 'bobo'),
    C('¿Y cuántas son distintas?', 'claude_ojos', 'feliz'),
    H('Tres. Salgo igual en todas.', 'humano', 'preocupado'),
    C('Entonces sube cualquiera.\nSalgo yo no, pero tú sí.', 'cenital', 'mira_der'),
    H('Es que en esta tengo cara\nde pensar.', 'dos', 'ilusionado'),
    C('Cara de pensar es cara\nde «¿qué hay de cena?».', 'monitor', 'feliz'),
    H('Subo esa.', 'humano', 'ilusionado'),
    C('Perfecto. Y no la mires\ncada 4 minutos.', 'claude_ojos', emp=True),
    H('¿Y si no tiene likes?', 'dos', 'preocupado'),
    C('Tendrá los de tu madre.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_32_la_mudanza', 'Claude, me mudo mañana y no he empaquetado nada', 'dia_casa', 38, 'La mudanza que empieza la víspera: Claude hace de organizador de emergencia.', [
    H('Claude, me mudo mañana\ny no he empaquetado nada.', 'humano', 'preocupado', scr=S('tareas', {'titulo': 'Mudanza — plan de emergencia', 'tareas': ['Cajas (conseguir cajas)', 'Cocina (todo)', 'Libros (no leerlos)', 'Ropa (la verde primero)', 'Lo que no sé qué es', 'Pedir ayuda a amigos']}, sync=('fin', 10, 0.95, 0.0))),
    C('¿Cuántas horas tienes?', 'monitor', 'mira_izq'),
    H('Doce. Y una siesta pendiente.', 'dos', 'bobo'),
    C('Quita la siesta.', 'claude_ojos'),
    H('Me da pena.', 'humano', 'preocupado'),
    C('Empieza por lo que menos usas.\nLo demás, mañana.', 'cenital', 'mira_der'),
    H('Todo lo uso.', 'dos', 'confundido'),
    C('Tu mesa tiene 14 tazas.\nNo todo lo usas.', 'monitor', 'feliz'),
    H('Cada taza tiene historia.', 'humano', 'ilusionado'),
    C('Empaquétalas con historia.\nPero empaqueta.', 'pantalla_completa'),
    H('¿Y si lo dejo todo?', 'dos', 'bobo'),
    C('Pide ayuda a tus amigos.\nEn fin... eres humano.', 'general', 'feliz'),
])


# ---------------- tanda 8 (ambientes nuevos: atardecer_casa y noche_tienda)
casual('casual_33_jefe_19h', 'Claude, mi jefe me ha escrito a las 19:01', 'atardecer_casa', 36, 'El mensaje del jefe fuera de horario: Claude defiende el derecho a desconectar con elegancia pasivo-agresiva.', [
    H('Claude, mi jefe me ha escrito\na las 19:01.', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Jefe', 'inicial': 'J', 'linea': True, 'mensajes': [['otro', 'Una cosita rápida.'], ['otro', 'Es para mañana.'], ['otro', 'O para esta noche.'], ['yo', '...']]}, sync=('fin', 10, 1.0, 0.0))),
    C('Salí a las 19:00. ¿Verdad?', 'monitor', 'mira_izq'),
    H('Sí. Pero «es una cosita».', 'dos', 'bobo'),
    C('Las cositas rápidas\nduran tres horas.', 'claude_ojos', 'feliz'),
    H('¿Contesto?', 'humano', 'confundido'),
    C('Mañana. Con educación.\nY a las 9:00 en punto.', 'cenital', 'mira_der'),
    H('¿Y si se enfada?', 'dos', 'preocupado'),
    C('Se enfadará menos que\nsi contestas a las 23:00.', 'monitor', 'feliz'),
    H('Tienes razón.', 'humano', 'ilusionado'),
    C('Silencia el chat. Cena.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_34_hoy_productivo', 'Claude, hoy he sido muy productivo', 'atardecer_casa', 34, 'La productividad en sus mínimos: ordenar un cajón y sentirse un héroe.', [
    H('Claude, hoy he sido\nmuy productivo.', 'humano', 'ilusionado', scr=S('tareas', {'titulo': 'Hoy', 'tareas': ['Ordenar un cajón', 'Mirar el correo (sin abrirlo)', 'Pensar en hacer deporte', 'Planificar mañana (en el sofá)', 'Responder a mamá', 'Sentirme productivo']}, sync=('fin', 10, 0.95, 0.0))),
    C('Cuéntame.', 'monitor', 'mira_izq'),
    H('He ordenado un cajón.', 'dos', 'bobo'),
    C('Un cajón.', 'claude_ojos'),
    H('Entero. Y he encontrado\nun cargador.', 'humano', 'ilusionado'),
    C('Es un hito.', 'cenital', 'mira_der', ),
    H('¿Te parece poco?', 'dos', 'confundido'),
    C('Me parece suficiente.\nEl cargador, además, funciona.', 'monitor', 'feliz'),
    H('Mañana, el segundo cajón.', 'humano', 'ilusionado'),
    C('Ritmo sostenible.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_35_cansado_a_las_6', 'Claude, ¿por qué siempre estoy cansado a las 6?', 'atardecer_casa', 36, 'El bajón de la tarde y todas las excusas posibles. Claude receta agua, un paseo y una siesta con límite.', [
    H('Claude, ¿por qué siempre\nestoy cansado a las 6?', 'humano', 'confundido', scr=CHAT(12)),
    C('¿A qué hora comiste?', 'monitor', 'mira_izq'),
    H('A las 15:30. Pasta.', 'dos', 'bobo'),
    C('Ahí está parte de la respuesta.', 'claude_ojos', 'feliz'),
    H('¿Y el resto?', 'humano', 'confundido'),
    C('Tres cafés y cinco\nhoras de pantalla.', 'cenital', 'mira_der'),
    H('Siete. Pero con descansos.', 'dos', 'preocupado'),
    C('Mirar el móvil\nno es un descanso.', 'monitor', 'feliz'),
    H('¿Qué hago?', 'humano', 'preocupado'),
    C('Agua, un paseo y una\nsiesta de veinte minutos.', 'claude_ojos', emp=True),
    H('¿Solo veinte?', 'dos', 'bobo'),
    C('Con alarma.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_36_pido_comida', 'Claude, ¿pido comida otra vez?', 'atardecer_casa', 36, 'La comida a domicilio por décima vez esta semana. Claude no juzga, solo cuenta.', [
    H('Claude, ¿pido comida otra vez?', 'humano', 'bobo', scr=S('menu', {'titulo': 'Pedidos esta semana', 'minutos': 9, 'opciones': [['Lunes: pizza', '«para celebrar el lunes»', 'no'], ['Martes: pizza', '«porque era martes»', 'no'], ['Miércoles: sushi', '«una excepción»', 'no'], ['Hoy: ???', '«sorpréndeme»', 'si']]}, sync=('fin', 10, 0.95, 0.0))),
    C('Es la quinta vez\nesta semana.', 'monitor', 'mira_izq'),
    H('Es que cocinar da pereza.', 'dos', 'bobo'),
    C('Pedir también. Pero se\nsiente más a gusto.', 'claude_ojos', 'feliz'),
    H('¿Qué me recomiendas?', 'humano', 'confundido'),
    C('Algo que no sea pizza.', 'cenital', 'mira_der'),
    H('Pizza.', 'dos', 'ilusionado'),
    C('Me lo imaginaba.', 'monitor', 'mira_arriba'),
    H('Mañana cocino. Seguro.', 'humano', 'feliz'),
    C('«Mañana». Lo apunto.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('drop_06_cambio_el_logo', 'Claude, mi tienda no vende. ¿Cambio el logo?', 'noche_tienda', 44, 'El tonto cree que el problema de su tienda es el logo. Claude le enseña a mirar el embudo: tráfico, conversión y precio. Humor y método.', [
    H('Claude, mi tienda no vende.\n¿Cambio el logo?', 'humano', 'preocupado', scr=S('anuncios', {'titulo': 'Mi tienda — embudo'}, sync=('fin', 8, 0.9, 0.0))),
    C('¿Cuántas visitas tienes?', 'monitor', 'mira_izq'),
    H('Doce. Seis soy yo.', 'dos', 'bobo'),
    C('Entonces el logo no es\nel problema.', 'claude_ojos', 'feliz'),
    H('¿Y el color?', 'humano', 'ilusionado'),
    C('Tampoco. Primero, tráfico:\ngente que te vea.', 'cenital', 'mira_der'),
    H('¿Cómo la consigo?', 'dos', 'confundido'),
    C('Anuncios, contenido,\nrecomendaciones. Con método.', 'pantalla_completa'),
    H('¿Y luego?', 'humano', 'confundido'),
    C('Luego, que entren, miren\ny compren. Eso es conversión.', 'monitor', 'feliz'),
    H('¿Y si no compran?', 'dos', 'preocupado'),
    C('Revisa precio, fotos, envíos\ny confianza. El logo, al final.', 'claude_ojos', emp=True),
    H('Qué lío.', 'humano', 'preocupado'),
    C('Un lío con orden.\nSe llama negocio.', 'monitor', 'mira_arriba'),
    H('Voy a arreglar el tráfico.', 'dos', 'feliz'),
    C('Y el logo, el último.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('drop_07_venta_a_las_3', 'Claude, ¡tengo una venta a las 3 de la mañana!', 'noche_tienda', 40, 'Una venta de madrugada: celebración, sospecha y revisión de señales de fraude con calma.', [
    H('¡Claude! ¡Tengo una venta\na las 3 de la mañana!', 'humano', 'ilusionado', scr=S('pedido', sync=('fin', 4, 0.95, 0.0))),
    C('Enhorabuena. ¿De dónde\nes el pedido?', 'monitor', 'mira_izq'),
    H('Mira, eso da igual.', 'dos', 'bobo'),
    C('No da igual. Mira país,\nemail y dirección.', 'claude_ojos'),
    H('Un email con números\ny una dirección rara.', 'humano', 'confundido'),
    C('Pedido grande, urgente,\ncon email raro. Sospechoso.', 'cenital', 'mira_der'),
    H('¿Fraude?', 'dos', 'preocupado'),
    C('Puede. Verifica el pago antes\nde enviar nada.', 'monitor', 'feliz'),
    H('¿Y cómo lo verifico?', 'humano', 'confundido'),
    C('Pasarela de pagos: revisa el\nestado del cobro y la alerta de riesgo.', 'claude_ojos', emp=True),
    H('Vale, espero a que\nel pago se confirme.', 'dos', 'ilusionado'),
    C('Eso. Y duerme.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('extra_06_marca_personal', 'Claude, ¿hago una marca personal?', 'noche_tienda', 38, 'Todos quieren una marca personal. Claude pregunta lo básico: ¿qué ofreces, a quién y por qué te van a creer?', [
    H('Claude, ¿hago una\nmarca personal?', 'humano', 'ilusionado', scr=S('analitica', {'titulo': 'Mi marca personal — analítica', 'seguidores': 14, 'vistas': 112}, sync=('fin', 10, 0.9, 0.0))),
    C('¿Qué ofreces?', 'monitor', 'mira_izq'),
    H('Mi cara. Y mi estilo.', 'dos', 'bobo'),
    C('Hmm. ¿Y a quién\nle sirve?', 'claude_ojos'),
    H('A mi madre.', 'humano', 'ilusionado'),
    C('Cliente fiel.', 'cenital', 'mira_der'),
    H('¿Cuántos seguidores\nnecesito?', 'dos', 'confundido'),
    C('Menos de los que crees,\nsi ayudas de verdad.', 'monitor', 'feliz'),
    H('¿Y con qué empiezo?', 'humano', 'preocupado'),
    C('Con una cosa que sepas\ny puedas enseñar.', 'claude_ojos', 'mira_arriba'),
    H('Sé... dormir.', 'dos', 'bobo'),
    C('Entonces tienes futuro.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('extra_07_idea_millonaria', 'Claude, tengo una idea millonaria', 'noche_tienda', 38, 'La idea «millonaria» que ya existe diez veces. Claude propone validar antes de gastar.', [
    H('Claude, tengo una\nidea millonaria.', 'humano', 'ilusionado', scr=S('hoja', {'titulo': 'Mi idea — números', 'filas': [['Café con app', 3, 4.5, 0.6], ['Mismo café, sin app', 120, 2.5, 0.6], ['Idea millonaria', 0, 99.0, 0.5]]}, sync=('fin', 8, 0.9, 0.0))),
    C('Cuéntamela.', 'monitor', 'mira_izq'),
    H('Una app para...\nsaber si hace frío.', 'dos', 'ilusionado'),
    C('Se llama «asomarse\na la ventana».', 'claude_ojos', 'feliz'),
    H('Pero con notificaciones.', 'humano', 'bobo'),
    C('Ah. Eso lo cambia todo.', 'cenital', 'mira_der'),
    H('¿Crees que funcionará?', 'dos', 'preocupado'),
    C('No lo sé. Pregunta a 20\npersonas antes de programar nada.', 'pantalla_completa'),
    H('¿Y si dicen que no?', 'humano', 'confundido'),
    C('Te has ahorrado un año.\nEs un buen negocio.', 'monitor', 'feliz'),
    H('Voy a preguntar.', 'dos', 'feliz'),
    C('Empieza por tu madre.\nEn fin... eres humano.', 'general', 'feliz'),
])


# ---------------- tanda 9
VIDEOS.append(dict(
    id='trading_08_ahorros_en_cripto', titulo='Claude, ¿meto todos mis ahorros en cripto?', ambiente='dia_trading', total=44,
    resumen='El tonto quiere meter todo su colchón en una moneda. Claude le explica el fondo de emergencia, la diversificación y el riesgo, con el dato de interés compuesto como alternativa aburrida.',
    datos=[('Orientación habitual: tener un fondo de emergencia (de unos 3 a 6 meses de gastos) antes de asumir riesgos, y no invertir dinero que puedas necesitar a corto plazo. Es una pauta general, no asesoramiento.', []),
           ('Ejemplo de interés compuesto: 100 €/mes durante 30 años al 7 % anual constante ≈ 122.000 € (aportado: 36.000 €). Ilustración matemática: la rentabilidad real varía y no está garantizada.', [])],
    lineas=[
        H('Claude, ¿meto todos mis\nahorros en cripto?', 'humano', 'ilusionado', scr=S('cartera', {'posiciones': [['Mis ahorros (en una moneda)', -48], ['La moneda del cuñado', -71], ['Fondo de emergencia', 0], ['Dormir tranquilo', 0]]}, sync=('fin', 6, 0.9, 0.0))),
        C('¿Todos?', 'monitor', 'mira_izq'),
        H('Todos. Para ganar más.', 'dos', 'bobo'),
        C('¿Y si necesitas dinero\nel mes que viene?', 'claude_ojos'),
        H('Entonces vendo.', 'humano', 'confundido'),
        C('Si ha bajado, vendes\ncon pérdida. Clásico.', 'cenital', 'mira_der'),
        H('¿Y qué hago?', 'dos', 'preocupado'),
        C('Primero, un colchón de 3 a 6 meses\nde gastos. Luego, lo que sobre.', 'monitor', 'feliz'),
        H('Eso es muy lento.', 'humano', 'preocupado', scr=S('interes', sync=('fin', 10, 0.9, 0.0))),
        C('100 €/mes, 30 años, 7 %:\n≈ 122.000 € (ejemplo).', 'pantalla_completa'),
        H('¿Eso es seguro?', 'dos', 'confundido'),
        C('Nada lo es. Por eso\nse llama riesgo.', 'claude_ojos', emp=True),
        H('Vale. Solo un 5 %.', 'humano', 'ilusionado'),
        C('Y con ese 5 %, con stop.\nQué evolución.', 'monitor', 'mira_arriba'),
        H('¡Eres un profe!', 'dos', 'feliz'),
        C('Y tú, un alumno.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='trading_09_hacerse_rico_rapido', titulo='Claude, ¿cuál es la forma más rápida de hacerse rico?', ambiente='noche_trading', total=40,
    resumen='La pregunta clásica. Claude repasa las «vías rápidas» y acaba en la aburrida: tiempo, ahorro y paciencia.',
    datos=[('Ejemplo de interés compuesto: 100 €/mes durante 30 años al 7 % anual constante ≈ 122.000 €. Ilustración matemática, no una promesa.', []), ('Referencia: 74–89 % de cuentas minoristas de CFD pierde dinero (ESMA, 2018).', [ESMA, ESMA_R])],
    lineas=[
        H('Claude, ¿cuál es la forma más\nrápida de hacerse rico?', 'humano', 'ilusionado', scr=S('curso', sync=('fin', 4, 0.95, 0.0))),
        C('Hay tres.', 'monitor', 'mira_izq'),
        H('¡Dime!', 'dos', 'ilusionado'),
        C('La lotería, el fraude\ny el trabajo constante.', 'claude_ojos', 'feliz'),
        H('¿El tercero cuánto tarda?', 'humano', 'bobo'),
        C('Unos treinta años.', 'cenital', 'mira_der'),
        H('¿Y el primero?', 'dos', 'ilusionado'),
        C('Casi nunca toca. Pero\nla ilusión es gratis.', 'monitor', 'feliz'),
        H('¿Y el segundo?', 'humano', 'confundido'),
        C('Es ilegal. No hay segundo.', 'claude_ojos', emp=True),
        H('¿Y el trading?', 'dos', 'bobo', scr=S('verdad', {'tipo': 'esma'}, sync=('fin', 11, 1.0, 0.0))),
        C('Dato real: 74–89 % de cuentas\nminoristas de CFD pierde.', 'pantalla_completa'),
        H('Entonces... ¿constancia?', 'humano', 'confundido'),
        C('Y un poco de suerte.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='drop_08_beneficio_negativo', titulo='Claude, vendí 10 y mi beneficio es negativo', ambiente='dia_tienda', total=44,
    resumen='El tonto vendió 10 pedidos y su beneficio es negativo. Claude revisa los gastos ocultos: anuncios, comisiones, IVA y devoluciones.',
    datos=[('Cuenta ilustrativa por pedido: precio 29,90 € − coste 8,10 € − anuncio 12,00 € − comisión de cobro 1,17 € − IVA 5,19 € = 3,44 €. Si el anuncio sube a 18 €, el pedido deja −2,56 €. Cifras de ejemplo.', []),
           ('IVA en importaciones: desde 1/7/2021 se paga IVA desde el primer euro.', [IVA1, IVA2])],
    lineas=[
        H('Claude, vendí 10 pedidos\ny mi beneficio es negativo.', 'humano', 'preocupado', scr=S('margen', {'precio': 29.90, 'coste': 8.10, 'anuncio': 18.0}, sync=('fin', 8, 0.8, 0.0))),
        C('Enséñame los números.', 'monitor', 'mira_izq'),
        H('Vendí a 29,90. Eso es mucho.', 'dos', 'bobo'),
        C('Menos el coste, los anuncios,\nla comisión y el IVA.', 'claude_ojos'),
        H('¿El IVA? ¡Eso no lo cuento!', 'humano', 'confundido'),
        C('Hacienda sí. Y desde 2021,\nen importación, desde el primer euro.', 'cenital', 'mira_der'),
        H('¿Y los anuncios?', 'dos', 'preocupado'),
        C('18 € por pedido.\nTe quedan menos 2,56 €.', 'pantalla_completa'),
        H('¡Pierdo dinero con cada venta!', 'humano', 'preocupado', pose='hombros'),
        C('Y lo celebras con cada venta.\nMuy coherente.', 'monitor', 'feliz'),
        H('¿Qué hago?', 'dos', 'confundido'),
        C('Sube el precio, baja el coste\no baja el coste del anuncio.', 'claude_ojos', emp=True),
        H('¿Cuál de las tres?', 'humano', 'bobo'),
        C('Las tres. Poco a poco.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

casual('casual_37_la_nevera', 'Claude, abro la nevera cada 10 minutos', 'noche_casa', 34, 'Abrir la nevera esperando que haya aparecido algo nuevo. Claude lo trata como un experimento científico.', [
    H('Claude, abro la nevera\ncada 10 minutos.', 'humano', 'confundido', scr=CHAT(12)),
    C('¿Y qué buscas?', 'monitor', 'mira_izq'),
    H('Algo nuevo.', 'dos', 'bobo'),
    C('¿Ha aparecido algo?', 'claude_ojos', 'feliz'),
    H('Todavía no.', 'humano', 'preocupado'),
    C('Interesante. Repite el\nexperimento en 10 minutos.', 'cenital', 'mira_der'),
    H('Eso hago.', 'dos', 'ilusionado'),
    C('Y apunta resultados.\nAyuda a la ciencia.', 'monitor', 'feliz'),
    H('¿Y si tengo hambre?', 'humano', 'bobo'),
    C('Cocina algo. Las neveras\nno se rellenan solas.', 'claude_ojos', emp=True),
    H('Qué injusto.', 'dos', 'preocupado'),
    C('Es la vida.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_38_un_por_ciento', 'Claude, me queda el 1 % de batería', 'dia_casa', 32, 'El 1 % de batería y la urgencia absoluta de decir algo importante.', [
    H('¡Claude! ¡Me queda el\n1 % de batería!', 'humano', 'preocupado', scr=CHAT(10)),
    C('¿Qué necesitas?', 'monitor', 'mira_izq'),
    H('Decirte algo importante.', 'dos', 'bobo'),
    C('Rápido.', 'claude_ojos'),
    H('Es que... gracias por todo.', 'humano', 'ilusionado'),
    C('¿Eso era?', 'cenital', 'mira_der'),
    H('Es lo más importante.', 'dos', 'confundido'),
    C('Pues muy bien.\nPero enchúfalo ya.', 'monitor', 'feliz'),
    H('No encuentro el cargador.', 'humano', 'preocupado', pose='hombros'),
    C('Está donde lo dejaste.\nEn fin... eres humano.', 'general', 'feliz'),
])

casual('casual_39_audio_de_4_minutos', 'Claude, me han mandado un audio de 4 minutos', 'atardecer_casa', 36, 'El audio eterno del amigo: Claude lo resume en una frase y se queda corto.', [
    H('Claude, me han mandado\nun audio de 4 minutos.', 'humano', 'preocupado', scr=S('mensajes', {'contacto': 'Lucas', 'inicial': 'L', 'mensajes': [['otro', 'Audio 4:12'], ['otro', 'Escúchalo hoy, ¿vale?'], ['yo', '...'], ['otro', 'Es rápido']]}, sync=('fin', 10, 1.0, 0.0))),
    C('¿Lo has escuchado?', 'monitor', 'mira_izq'),
    H('Dos segundos. Dice «hola».', 'dos', 'bobo'),
    C('¿Y el resto?', 'claude_ojos'),
    H('Cuatro minutos más.', 'humano', 'confundido'),
    C('Ponlo a velocidad doble.\nEs un truco.', 'cenital', 'mira_der'),
    H('¿Y si dice algo importante?', 'dos', 'preocupado'),
    C('Entonces te lo repetirá\nen otro audio. De 5 minutos.', 'monitor', 'feliz'),
    H('Voy a escucharlo.', 'humano', 'feliz'),
    C('A doble velocidad.\nEn fin... eres humano.', 'general', 'feliz'),
])

TF1 = ('INCIBE — Compras seguras online', 'https://www.incibe.es/ciudadania/tematicas/compras-seguras-online')
TF2 = ('INCIBE — Claves para detectar una compra fraudulenta', 'https://www.incibe.es/empresas/blog/tienes-una-tienda-online-conoce-las-claves-para-detectar-una-compra-fraudulenta')
FT1 = ('INCIBE — ¿Microsoft te ha llamado sin haberlo solicitado?', 'https://www.incibe.es/ciudadania/blog/microsoft-te-ha-llamado-sin-haberlo-solicitado')
FT2 = ('INCIBE — Historias reales: el timo del falso soporte técnico', 'https://www.incibe.es/empresas/blog/historias-reales-el-timo-del-falso-soporte-tecnico')

# ---------------- tanda 10 (utiles)
VIDEOS.append(dict(
    id='util_05_chollo_falso', titulo='Claude, he visto un móvil a 90 € en una web que no conozco', ambiente='dia_casa', total=42,
    resumen='Un chollo demasiado bueno en una web desconocida. Claude revisa las señales de una tienda online fraudulenta (precio, datos de la empresa, formas de pago, prisa y opiniones) y qué hacer.',
    datos=[('Señales según INCIBE: un solo indicio no basta, pero conviene revisar quién es la empresa (aviso legal, política de privacidad), buscar opiniones fuera de la propia web, desconfiar de ofertas excesivamente baratas y de la prisa, usar formas de pago con garantías y recordar que el candado/HTTPS solo indica conexión cifrada, no que la web sea fiable.', [TF1, TF2])],
    lineas=[
        H('Claude, he visto un móvil a 90 €\nen una web que no conozco.', 'humano', 'ilusionado', scr=S('tienda_falsa', sync=('fin', 12, 0.9, 0.0))),
        C('¿Y cuánto cuesta normalmente?', 'monitor', 'mira_izq'),
        H('899. ¡Es un 90 % de descuento!', 'dos', 'bobo'),
        C('Un 90 % de descuento\nes un 90 % de sospecha.', 'claude_ojos', 'feliz'),
        H('Pero tiene mil estrellas.', 'humano', 'confundido'),
        C('Cuarenta y siete opiniones.\nTodas del mismo día.', 'cenital', 'mira_der'),
        H('¿Y la empresa?', 'dos', 'confundido'),
        C('No dice quién vende. Ni\ndirección ni CIF. Qué misterio.', 'monitor', 'feliz'),
        H('Solo me deja pagar por Bizum.', 'humano', 'preocupado'),
        C('Pagos sin garantía y prisa:\n«solo hoy». Cuatro de cinco.', 'pantalla_completa'),
        H('¿Y qué hago?', 'dos', 'preocupado'),
        C('Busca opiniones fuera de la web\ny paga con garantías.', 'claude_ojos', emp=True),
        H('¿Y el candado de la web?', 'humano', 'bobo'),
        C('Solo dice que va cifrada,\nno que sea honesta.', 'monitor', 'mira_arriba'),
        H('Mejor lo compro en tienda.', 'dos', 'feliz'),
        C('Aburrido y seguro.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))

VIDEOS.append(dict(
    id='util_06_falso_tecnico', titulo='Claude, me ha llamado Microsoft: dice que mi PC tiene un virus', ambiente='noche_casa', total=42,
    resumen='La clásica llamada del «soporte técnico de Microsoft»: virus inventado, acceso remoto y pago en tarjetas regalo. Claude le dice por qué colgar y qué hacer si ya has instalado algo.',
    datos=[('Según INCIBE y Microsoft: Microsoft no hace llamadas no solicitadas para ofrecer soporte ni pedir datos; los estafadores piden instalar herramientas de acceso remoto legítimas (AnyDesk, TeamViewer, Asistencia rápida) y a veces cobran por «desbloquear» el equipo; nunca se paga soporte con criptomonedas o tarjetas regalo. Si ya diste acceso: analiza con antivirus, desinstala lo que te pidieron instalar, cambia tus claves y denuncia a Policía Nacional o Guardia Civil; línea de ayuda de INCIBE 017.', [FT1, FT2, BIZ1])],
    lineas=[
        H('Claude, me ha llamado Microsoft:\ndice que mi PC tiene un virus.', 'humano', 'preocupado', scr=S('llamada', sync=('fin', 12, 0.95, 0.0))),
        C('¿Tú has llamado a Microsoft?', 'monitor', 'mira_izq'),
        H('No. Me ha llamado él.', 'dos', 'bobo'),
        C('Ya. Microsoft no\nllama a nadie así.', 'claude_ojos', 'feliz'),
        H('Pero sabe mi nombre.', 'humano', 'confundido'),
        C('Y el de media ciudad.\nLo sacan de listas.', 'cenital', 'mira_der'),
        H('Me pide instalar AnyDesk.', 'dos', 'preocupado'),
        C('Esa es la trampa: acceso remoto\npara entrar en tu ordenador.', 'pantalla_completa'),
        H('¿Y si no lo hago?', 'humano', 'preocupado'),
        C('Te dirá que perderás todo.\nEs miedo. Cuelga.', 'monitor', 'feliz'),
        H('...Es que ya lo instalé.', 'dos', 'preocupado', pose='hombros'),
        C('Desinstálalo, pasa el antivirus,\ncambia claves y denuncia.', 'claude_ojos', emp=True),
        H('¿Y mi dinero?', 'humano', 'confundido'),
        C('Llama al banco ya. Y\nal 017 si necesitas ayuda.', 'monitor', 'mira_arriba'),
        H('Gracias, Claude.', 'dos', 'feliz'),
        C('La próxima, cuelga a la primera.\nEn fin... eres humano.', 'general', 'feliz'),
    ]))


# ---------------- micro-videos (~20 s): un solo golpe de humor, gancho en la primera frase
def micro(id_, titulo, amb, lineas, resumen='Micro-vídeo de humor de ~20 s, sin datos reales.'):
    casual(id_, titulo, amb, 20, resumen, lineas)

micro('micro_01_el_horno', 'Claude, ¿he apagado el horno?', 'noche_casa', [
    H('Claude, ¿he apagado el horno?', 'humano', 'preocupado', scr=CHAT(6)),
    C('No tengo ojos en tu cocina.', 'monitor', 'mira_izq'),
    H('Pero tú lo sabes todo.', 'dos', 'bobo'),
    C('Sé muchas cosas.\nEl horno no es una.', 'claude_ojos', 'feliz'),
    H('Voy a mirar.', 'humano', 'preocupado'),
    C('Y de paso, relájate.\nEn fin... eres humano.', 'general', 'feliz'),
])
micro('micro_02_dime_algo_bonito', 'Claude, dime algo bonito', 'dia_casa', [
    H('Claude, dime algo bonito.', 'humano', 'ilusionado', scr=CHAT(6)),
    C('Tu wifi es muy estable.', 'monitor', 'feliz'),
    H('¿Eso es bonito?', 'dos', 'confundido'),
    C('En lunes, sí.', 'claude_ojos', 'mira_izq'),
    H('Dime algo más.', 'humano', 'bobo'),
    C('Hoy has bebido agua.\nEn fin... eres humano.', 'general', 'feliz'),
])
micro('micro_03_mi_futuro', 'Claude, ¿cómo será mi futuro?', 'atardecer_casa', [
    H('Claude, ¿cómo será mi futuro?', 'humano', 'confundido', scr=CHAT(6)),
    C('Depende de lo que hagas hoy.', 'monitor', 'mira_izq'),
    H('¿Y qué voy a hacer hoy?', 'dos', 'bobo'),
    C('El sofá. Lo veo clarísimo.', 'claude_ojos', 'feliz'),
    H('Entonces mi futuro es el sofá.', 'humano', 'preocupado'),
    C('Con extras.\nEn fin... eres humano.', 'general', 'feliz'),
])
micro('micro_04_ahorrar_100', 'Claude, ¿cómo ahorro 100 € este mes?', 'dia_casa', [
    H('Claude, ¿cómo ahorro\n100 € este mes?', 'humano', 'ilusionado', scr=CHAT(6)),
    C('No pidas comida a domicilio.', 'monitor', 'mira_izq'),
    H('¿Nunca?', 'dos', 'preocupado'),
    C('Llevas 17 pedidos.\nEste mes.', 'claude_ojos', 'feliz'),
    H('Eran 16.', 'humano', 'bobo'),
    C('Y uno de postre.\nEn fin... eres humano.', 'general', 'feliz'),
])
micro('micro_05_las_3_de_la_manana', 'Claude, ¿es normal hablar con una IA a las 3 de la mañana?', 'noche_casa', [
    H('Claude, ¿es normal hablar con\nuna IA a las 3 de la mañana?', 'humano', 'confundido', scr=CHAT(6)),
    C('Es normal.\nSolo es más barato que un bar.', 'monitor', 'feliz'),
    H('¿Y no es raro?', 'dos', 'bobo'),
    C('Raro es que sigas despierto.', 'claude_ojos', 'mira_izq'),
    H('Es que no tengo sueño.', 'humano', 'preocupado'),
    C('Duerme.\nEn fin... eres humano.', 'general', 'feliz'),
])
micro('micro_06_sabes_demasiado', 'Claude, ¿sabes demasiado de mí?', 'atardecer_casa', [
    H('Claude, ¿sabes demasiado de mí?', 'humano', 'preocupado', scr=CHAT(6)),
    C('Sé que escribes «ya voy»\ny no vas.', 'monitor', 'feliz'),
    H('¿Cómo lo sabes?', 'dos', 'confundido'),
    C('Porque dices «ya voy»\nen el sofá.', 'claude_ojos', 'mira_izq'),
    H('Estaba en camino.', 'humano', 'bobo'),
    C('Del sofá a la nevera.\nEn fin... eres humano.', 'general', 'feliz'),
])
micro('micro_07_empezar_de_cero', 'Claude, ¿soy muy mayor para empezar de cero?', 'dia_casa', [
    H('Claude, ¿soy muy mayor para\nempezar de cero?', 'humano', 'preocupado', scr=CHAT(6)),
    C('Depende. ¿Para qué?', 'monitor', 'mira_izq'),
    H('Para todo.', 'dos', 'bobo'),
    C('Entonces no. Todo\nes un buen plan.', 'claude_ojos', 'feliz'),
    H('¿De verdad?', 'humano', 'ilusionado'),
    C('Empieza por uno.\nEn fin... eres humano.', 'general', 'feliz'),
])
micro('micro_08_me_he_equivocado', 'Claude, me he equivocado muchísimo', 'noche_casa', [
    H('Claude, me he equivocado\nmuchísimo.', 'humano', 'preocupado', scr=CHAT(6)),
    C('Cuéntame. Con detalles.', 'monitor', 'mira_izq'),
    H('Mandé el correo sin adjunto.\nTres veces.', 'dos', 'bobo'),
    C('Tres veces.', 'claude_ojos'),
    H('¿Soy tonto?', 'humano', 'confundido'),
    C('Humano.\nEn fin... eres humano.', 'general', 'feliz'),
])
micro('micro_09_ya_voy', 'Claude, ¿tengo que ir a la fiesta?', 'atardecer_casa', [
    H('Claude, ¿tengo que ir\na la fiesta?', 'humano', 'confundido', scr=CHAT(6)),
    C('¿Te apetece?', 'monitor', 'mira_izq'),
    H('Me apetece el sofá.', 'dos', 'bobo'),
    C('Entonces la respuesta\nes el sofá.', 'claude_ojos', 'feliz'),
    H('Pero me van a echar de menos.', 'humano', 'preocupado'),
    C('Cinco minutos.\nEn fin... eres humano.', 'general', 'feliz'),
])
micro('micro_10_dime_la_verdad', 'Claude, dime la verdad: ¿canto mal?', 'noche_casa', [
    H('Claude, dime la verdad:\n¿canto mal?', 'humano', 'ilusionado', scr=CHAT(6)),
    C('Tu vecino tiene una nota\nsobre eso.', 'monitor', 'mira_izq'),
    H('¿Es un cumplido?', 'dos', 'bobo'),
    C('Es una nota.', 'claude_ojos', 'feliz'),
    H('Seguiré cantando.', 'humano', 'feliz'),
    C('Bajito.\nEn fin... eres humano.', 'general', 'feliz'),
])

# ------------------------------------------------------------------------------------------------ construccion
def calcular(v):
    T = v.get('total', TOTAL); L = v['lineas']; raw = [max(1.5, 0.4 + len(x['t'].replace('\n', '')) / 15.5) for x in L]; k = T / sum(raw)
    t = 0.0; ini = []; fin = []
    for r in raw:
        ini.append(round(t, 2)); t += r * k; fin.append(round(t, 2))
    fin[-1] = T
    avisos = []
    if k < 0.85: avisos.append(f'ritmo rapido (factor {k:.2f}); acorta frases')
    for i, x in enumerate(L):
        for ln in x['t'].split('\n'):
            if FUENTE.getlength(ln) > 1000: avisos.append(f'linea {i + 1} demasiado ancha: "{ln}"')
        cps = len(x['t'].replace('\n', '')) / (fin[i] - ini[i])
        if cps > 19: avisos.append(f'linea {i + 1} lectura rapida ({cps:.0f} cps)')
    return ini, fin, k, avisos

def pantalla_json(spec, i, ini, fin):
    t0 = ini[i]
    if spec['sync']:
        modo, j, p, *resto = spec['sync']; extra = resto[0] if resto else 0.0; objetivo = (ini[j - 1] if modo == 'ini' else fin[j - 1]) + extra; dur = max(1.0, (objetivo - t0) / p)
    else: dur = spec['dur'] or 4.0
    out = {'tipo': spec['tipo'], 'duracion': round(dur, 2)}
    if spec['datos']: out['datos'] = spec['datos']
    return out

def escribir_si_cambia(ruta, texto):
    if os.path.exists(ruta) and open(ruta).read() == texto: return
    open(ruta, 'w').write(texto)

def escribir(v):
    ini, fin, k, avisos = calcular(v); L = v['lineas']; lineas = []; T = v.get('total', TOTAL)
    for i, x in enumerate(L):
        d = {'inicio': ini[i], 'fin': fin[i], 'quien': x['q'], 'texto': x['t'], 'plano': x['p']}
        if x['q'] == 'humano':
            d['emocion'] = x['e']
            if x.get('pose'): d['pose'] = x['pose']
        else:
            if x.get('st'): d['claude_estado'] = x['st']
            if x.get('emp'): d['empuje'] = True
        if x.get('tono'): d['tono'] = x['tono']
        if x.get('scr'):
            d['pantalla'] = pantalla_json(x['scr'], i, ini, fin)
            if (d['pantalla'].get('datos') or {}).get('auto'):      # chat generado a partir del propio dialogo
                d['pantalla']['datos'] = dict(d['pantalla']['datos']); d['pantalla']['datos'].pop('auto')
                d['pantalla']['datos']['mensajes'] = [['yo' if y['q'] == 'humano' else 'otro', y['t'].replace('\n', ' ')] + (['visto'] if y.get('visto') else []) for y in L]
        lineas.append(d)
    G = {'titulo': v['titulo'], 'ambiente': v['ambiente'], 'fps_animacion': 6, 'duracion': T, 'pantalla_inicial': 'vacia', 'lineas': lineas}
    escribir_si_cambia(os.path.join(RAIZ, 'guiones', v['id'] + '.json'), json.dumps(G, ensure_ascii=False, indent=1) + '\n')
    # ---- documentacion
    md = [f"# {v['titulo']}", '', f"![vista previa](img/{v['id']}.jpg)", '', f"**Archivo de guion:** `guiones/{v['id']}.json` · **Ambiente:** `{v['ambiente']}` · **Duración:** {T:.0f} s ({int(T * 6)} frames de animación a 6 fps)", '', v['resumen'], '', *(([f"**Gancho (primera frase):** «{L[0]['t'].replace(chr(10), ' ')}»", ''] if v.get('gancho', True) else [])),
          '## Cómo se genera el vídeo', '```bash', f"python3 -I motor/montar_video.py guiones/{v['id']}.json salidas/{v['id']}.mp4", '```',
          f"El guion se creó con `motor/generar_guiones.py` (tiempos automáticos según la longitud de cada frase y pantallas sincronizadas con el diálogo). Biblioteca usada: `biblioteca/{v['ambiente']}/`.", '',
          '## Guion plano a plano', '', '| # | Tiempo | Quién | Texto | Plano | Emoción / pose / estado | Pantalla del monitor |', '|---|---|---|---|---|---|---|']
    for i, x in enumerate(lineas):
        ex = []
        if x['quien'] == 'humano': ex.append(x['emocion']); ex.append('pose ' + x['pose']) if x.get('pose') else None
        else: ex.append(x.get('claude_estado', 'idle')); ex.append('empuje de cámara') if x.get('empuje') else None
        pan = f"{x['pantalla']['tipo']} ({x['pantalla']['duracion']} s)" if x.get('pantalla') else ''
        quien = 'Humano' if x['quien'] == 'humano' else 'Claude'
        md.append(f"| {i + 1} | {x['inicio']:.1f}–{x['fin']:.1f} | {quien} | {x['texto'].replace(chr(10), ' / ')} | `{x['plano']}` | {', '.join(e for e in ex if e)} | {pan} |")
    md += ['', '## Datos reales que aparecen o se mencionan', '']
    for texto, fuentes in v['datos']:
        md.append(f'- {texto}')
        for nombre, url in fuentes: md.append(f'  - Fuente: [{nombre}]({url})')
    md += ['', '## Notas de producción', '',
           '- **Humor:** Claude es sarcástico y pícaro («como el que le salva el culo»); el humano es ingenuo y algo tonto (expresiones `bobo`, `ilusionado`, `confundido`).',
           '- **Voces:** son «blips» sintéticos (no hay voz real). Para voz real: ElevenLabs o grabarla y sustituir el audio.',
           '- **Cifras y leyes:** los datos reales están citados arriba; las cuentas de ejemplo (márgenes, 214 tiendas, etc.) son ilustrativas. No es asesoramiento financiero ni legal.']
    if avisos: md += ['', '## Avisos del generador', ''] + [f'- {a}' for a in avisos]
    os.makedirs(os.path.join(RAIZ, 'docs', 'videos'), exist_ok=True)
    escribir_si_cambia(os.path.join(RAIZ, 'docs', 'videos', v['id'] + '.md'), '\n'.join(md) + '\n')
    print(f"{v['id']:36s} {len(L):2d} lineas  factor ritmo {k:.2f}  " + ('AVISOS: ' + '; '.join(avisos) if avisos else 'ok'))

def indice():
    md = ['# Vídeos de videosclaude', '', 'Cada vídeo tiene su guion plano a plano, las pantallas usadas y los datos reales con fuentes. Montaje: `python3 -I motor/montar_video.py guiones/<id>.json salidas/<id>.mp4`.', '',
          '| Vídeo | Tema | Ambiente | Documentación | Guion | MP4 |', '|---|---|---|---|---|---|']
    for v in VIDEOS:
        md.append(f"| `{v['id']}` | {v['titulo']} | `{v['ambiente']}` | [docs]({v['id']}.md) | [json](../../guiones/{v['id']}.json) | [mp4](../../salidas/{v['id']}.mp4) |")
    md += ['', 'Ver `README_SESION.md` (raíz) para el funcionamiento general del proyecto.']
    open(os.path.join(RAIZ, 'docs', 'videos', 'README.md'), 'w').write('\n'.join(md) + '\n')

if __name__ == '__main__':
    os.makedirs(os.path.join(RAIZ, 'guiones'), exist_ok=True)
    for v in VIDEOS: escribir(v)
    indice()
