from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
import apiai, json, re

# Settings
updater = Updater(token='866382424:AAGVE7O492Xzak3OEwqKUojYF2TR7tNhb6A') # Telegram API Token
dispatcher = updater.dispatcher

# Command processing
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Olá, Bem vindo ao chat da UNIVAS! Em que posso ajudar ?')

def boleto(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Seu boleto pode ser encontrado dentro do portal do aluno')

def contato(bot, update):
    msg = "0800 039 0010 (Ligação Gratuita)\n\n\n"
    msg += "Reitoria: \n Avenida Pref. Tuany Toledo, 470 - CEP 37554-210 - Pouso Alegre, MG \n Telefone: (35) 3449 9211\n E-mail: reitoria@univas.edu.br \n\n"
    msg += "Unidade Central: \n Avenida Cel. Alfredo Custódio de Paula, 320 - CEP 37553-068 - Pouso Alegre, MG \n Telefone: (35) 3449 8772 \n E-mail: facimpa@univas.edu.br\n\n"
    msg += "Unidade Fátima: \n Avenida Pref. Tuany Toledo, 470 - CEP 37554-210 - Pouso Alegre, MG \n Telefone: (35) 3449 9257 \n E-mail: fafiep@univas.edu.br\n\n"
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Desculpe não entendi o que você quiz dizer")

# Handlers
start_command_handler = CommandHandler("start", startCommand)
#re.compile e re.ignorecase é para ignorar o case sensitive para letras maiusculas e minusculas
boleto_handler = MessageHandler(Filters.regex(re.compile(r'boleto', re.IGNORECASE)), boleto)
contato_handler = MessageHandler(Filters.regex(re.compile(r'contato', re.IGNORECASE)), contato)
#para comandas ou palavras nao reconhecidas
unknown_handler = MessageHandler(Filters.command, unknown)

# Here we add the handlers to the dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(boleto_handler)
dispatcher.add_handler(contato_handler)
dispatcher.add_handler(unknown_handler)

# Start search for updates
updater.start_polling(clean=True)

# Stop the bot, if Ctrl + C were pressed
updater.idle()
