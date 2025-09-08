from utils import MENSAJES, get_directiva_apl


def iniciar_juego(session_attr):
    bienvenida = MENSAJES['bienvenida']
    inst_inicial = MENSAJES['inst_inicial']
    speech_text = f'{bienvenida} {inst_inicial}'

    return speech_text, get_directiva_apl('launch')