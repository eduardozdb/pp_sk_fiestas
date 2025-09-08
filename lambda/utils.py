from ask_sdk_model.interfaces.alexa.presentation.apl import RenderDocumentDirective
import json


# Estructura de mensajes que la skill debe responder al usuario.
MENSAJES = {
    'bienvenida': '¡Bienvenido al Juego de Fiestas!.',
    'inst_inicial': (
        'Di la palabra "USUARIO" seguida de tu número de usuario para buscar tu información, por ejemplo: "USUARIO 1", '
        'o di: "QUIERO REGISTRARME".'
    )
}


# Configuaración del APL:
def get_directiva_apl(token, tipo='', archivo='JuegoFiestas.json', titulo='', texto=''):
    datasources = { 'preguntaData': {'text': titulo, 'subtext': texto}}

    try:
        with open(archivo, 'r') as apl_file:
            return RenderDocumentDirective(
                token=token,
                document= json.load(apl_file),
                datasources=datasources
            )
    except:
        return None



