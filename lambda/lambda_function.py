from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type
from ask_sdk_core.skill_builder import CustomSkillBuilder

import intents_logic as il


# ================================ INICIO DEL JUEGO ================================
class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type('LaunchRequest')(handler_input)
    
    def handle(self, handler_input):
        speech_text, directiva_apl = il.iniciar_juego(handler_input.attributes_manager.session_attributes)
        return responder(handler_input,speech_text, directiva_apl)      


# ================================ CONFIGURACIÓN DE HANDLERS ================================
def responder(handler_input,speech_text, directiva_apl):
    if directiva_apl:
        handler_input.response_builder.add_directive(directiva_apl)
    return handler_input.response_builder.speak(speech_text).ask(speech_text).response


sb = CustomSkillBuilder()

sb.add_request_handler(LaunchRequestHandler())

lambda_handler = sb.lambda_handler()