import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import time

# Lee el token de un archivo o proporciona directamente el token aquí
with open('/home/alumno/token.txt', 'r') as token_file:
    TOKEN = token_file.read().strip()

# Crea un Updater y pasa el token del bot
updater = Updater(TOKEN, use_context=True)

# Lee la contraseña y el tiempo máximo de sesión desde archivos
with open('/home/alumno/pass.txt', 'r') as pass_file:
    PASSWORD = pass_file.read().strip()

with open('/home/alumno/tiempo.txt', 'r') as time_file:
    MAX_SESSION_TIME = int(time_file.read().strip())

# Guarda el último mensaje en el chat
LAST_MESSAGE = ""

# Función para manejar el comando /start
def start(update, context):
    # Verifica la contraseña
    if len(context.args) > 0 and context.args[0] == PASSWORD:
        context.user_data['session_start_time'] = time.time()
        update.message.reply_text("Sesión iniciada. Puedes enviar mensajes.")
    else:
        update.message.reply_text("Contraseña incorrecta. Sesión no iniciada.")

# Función para manejar el comando /stop
def stop(update, context):
    context.user_data.clear()
    update.message.reply_text("Sesión finalizada. Gracias por usar el bot.")

# Función para manejar los mensajes del usuario
def handle_messages(update, context):
    global LAST_MESSAGE
    LAST_MESSAGE = update.message.text
    # Actualiza el tiempo de la sesión cada vez que se recibe un mensaje
    if 'session_start_time' in context.user_data:
        elapsed_time = time.time() - context.user_data['session_start_time']
        if elapsed_time > MAX_SESSION_TIME:
            context.user_data.clear()
            update.message.reply_text("Sesión finalizada debido a inactividad.")
    else:
        update.message.reply_text("Debes iniciar sesión con /start password antes de enviar mensajes.")

# Función para escribir el último mensaje en un archivo
def write_last_message_to_file(context: CallbackContext):
    if LAST_MESSAGE:
        with open('/home/alumno/chat.txt', 'w') as chat_file:
            chat_file.write(LAST_MESSAGE)

# Agrega los manejadores de comandos y mensajes
updater.dispatcher.add_handler(CommandHandler('start', start, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_messages))

# Agrega un job que se ejecuta cada minuto para escribir el último mensaje en un archivo
updater.job_queue.run_repeating(write_last_message_to_file, interval=60, first=0)

# Inicia el bot
updater.start_polling()
updater.idle()
