from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from telegram import *
from functools import wraps
import apiai
import json
import re

# Settings
# Telegram API Token
updater = Updater(token='866382424:AAGVE7O492Xzak3OEwqKUojYF2TR7tNhb6A')
dispatcher = updater.dispatcher

def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func

@send_typing_action
def my_handler(update, context):
    pass # Will send 'typing' action while processing the request.


# Command processing
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Olá, Bem vindo ao chat da UNIVAS! Em que posso ajudar ?')


def boleto(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Seu boleto pode ser encontrado dentro do portal do aluno \n\n Acesse: http://portalaluno.univas.edu.br/SistemaWeb/mentornet/centralaluno/PA_Login_1.php \n\n')


def contato(bot, update):
    msg = "0800 039 0010 (Ligação Gratuita)\n\n"
    msg += "Reitoria: \n Avenida Pref. Tuany Toledo, 470 - CEP 37554-210 - Pouso Alegre, MG \n Telefone: (35) 3449 9211\n E-mail: reitoria@univas.edu.br \n\n"
    msg += "Unidade Central: \n Avenida Cel. Alfredo Custódio de Paula, 320 - CEP 37553-068 - Pouso Alegre, MG \n Telefone: (35) 3449 8772 \n E-mail: facimpa@univas.edu.br\n\n"
    msg += "Unidade Fátima: \n Avenida Pref. Tuany Toledo, 470 - CEP 37554-210 - Pouso Alegre, MG \n Telefone: (35) 3449 9257 \n E-mail: fafiep@univas.edu.br\n\n"
    bot.send_message(chat_id=update.message.chat_id, text=msg)


def incentivo(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Temos um texto especial sobre o incentivo do PROGRAMA DE INCENTIVO À PESQUISA: \n\n Veja mais em: https://www.univas.edu.br/docs/2018/pesquisa/incentivo.pdf \n\n")


def nucleo(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Temos um texto especial sobre NÚCLEOS DE PESQUISAS: \n\n Veja mais em: https://www.univas.edu.br/docs/2018/pesquisa/nucleoPesquisa.pdf \n\n")


def convenio(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Temos um texto especial sobre NÚCLEOS DE PESQUISAS: \n\n Veja mais em: https://www.univas.edu.br/docs/2018/pesquisa/convenios.pdf \n\n")


def grupoPesquisa(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Saiba mais sobre os grupos de pesquisa \n\n Veja mais em: https://www.univas.edu.br/docs/2019/pesquisa/gruposDePesquisa/Grupos%20de%20Pesquisa%20CNPq.pdf \n\n")


def pesquisa(bot, update):
    msg = "A Pesquisa Científica é uma das três áreas onde a Universidade deve atuar. A busca pelo conhecimento, de forma sistemática e contínua, difere uma verdadeira Universidade de outras instituições de ensino superior, impactando de maneira positiva o seu Ensino e as suas atividades de Extensão, aumentando assim sua relevância no contexto local, regional, nacional e internacional. \n\n \
    A Universidade do Vale do Sapucaí (Univás), ciente de sua participação e incentivo a pesquisa científica, coloca como meta principal a busca constante pelo conhecimento. Realizada por docentes qualificados e por seus acadêmicos, a Pesquisa Científica na Univás tem o seu gerenciamento centrado na Coordenadoria de Pesquisa, subordinada à Pró-Reitoria de Pós-Graduação e Pesquisa da Univás. \
    A Coordenadoria tem como missão estimular docentes e acadêmicos a se engajarem em projetos científicos cada vez com melhor qualidade e em maior número."
    bot.send_message(chat_id=update.message.chat_id, text=msg)


def etica(bot, update):
    msg = "Comissão de Ética \n\
    CEUA \n\
    Regulamento: \n\
    https://www.univas.edu.br/docs/2018/pesquisa/comiteDeEtica/CEUA_regulamento.pdf \n\n   \
    Calendário de Reunião \n\
    https://www.univas.edu.br/docs/2019/pesquisa/comiteDeEtica/CEUA_calendario.pdf  \n\n  \
    Resolução\n\
    https://www.univas.edu.br/docs/2018/pesquisa/comiteDeEtica/CEUA_resolucao.pdf \n\n \
    \
    Obs: O projeto de pesquisa deverá ser entregue na Secretária de Pós-graduação e Pesquisa, em 2 cópias impressas acompanhada do formulário unificado e autorização do biotério e 1 cópia digital - com o mesmo conteúdo para o e-mail abaixo: \
    \n\
    ceua@univas.edu.br \n\n"
    bot.send_message(chat_id=update.message.chat_id, text=msg)


def secretaria(bot, update):
    msg = "Endereço: \n\
    Avenida Prefeito Tuany Toledo, 470, Fátima I \
    CEP 37550-000 POUSO ALEGRE-MG  \n\n \
    Funcionamento: \n\
    Segundas-feiras às sextas-feiras das 8h às 11h30min e das 13h30min às 17h \
    E-mail: tassianac@fuvs.br \
    Tel. (35) 3449-9271"
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def vestibular(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Fique por dentro das datas dos nossos vestibulates em: \n\n http://portalvestibular.univas.edu.br/portalVestibular2020/index.asp?utm_source=site&utm_medium=botao&utm_campaign=vestibular2020")


# essa tem que ser sempre a ultima
def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Desculpe não entendi o que você quiz dizer")


# Handlers
start_command_handler = MessageHandler((Filters.regex(re.compile(r'oi', re.IGNORECASE)) | \
    (Filters.regex(re.compile(r'oi', re.IGNORECASE))) | \
    (Filters.regex(re.compile(r'ola', re.IGNORECASE))) | \
    (Filters.regex(re.compile(r'olá', re.IGNORECASE))) | \
    (Filters.regex(re.compile(r'opa', re.IGNORECASE))) | \
    (Filters.regex(re.compile(r'bom dia', re.IGNORECASE))) | \
    (Filters.regex(re.compile(r'boa tarde', re.IGNORECASE))) | \
    (Filters.regex(re.compile(r'boa noite', re.IGNORECASE)))), startCommand)
# re.compile e re.ignorecase é para ignorar o case sensitive para letras maiusculas e minusculas
boleto_handler=MessageHandler(Filters.regex(re.compile(r'boleto', re.IGNORECASE)), boleto)
contato_handler=MessageHandler(Filters.regex(re.compile(r'contato', re.IGNORECASE)), contato)
incentivo_handler=MessageHandler(Filters.regex(re.compile(r'incentivo', re.IGNORECASE)), incentivo)
nucleo_handler=MessageHandler(Filters.regex(re.compile(r'nucleo', re.IGNORECASE)), nucleo)
convenio_handler=MessageHandler(Filters.regex(re.compile(r'convenio', re.IGNORECASE)), convenio)
gp_handler=MessageHandler(Filters.regex(re.compile(r'grupo de pesquisa', re.IGNORECASE)), grupoPesquisa)
pesquisa_handler=MessageHandler(Filters.regex(re.compile(r'pesquisa', re.IGNORECASE)), pesquisa)
etica_handler=MessageHandler((Filters.regex(re.compile(r'etica', re.IGNORECASE)) | (Filters.regex(re.compile(r'ética', re.IGNORECASE)))), etica)
secretaria_handler=MessageHandler(Filters.regex(re.compile(r'secretaria', re.IGNORECASE)), secretaria)
vestibular_handler=MessageHandler(Filters.regex(re.compile(r'vestibular', re.IGNORECASE)), vestibular)

# para comandas ou palavras nao reconhecidas tem que ficar no final
unknown_handler=MessageHandler(Filters.command, unknown)

# Here we add the handlers to the dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(boleto_handler)
dispatcher.add_handler(contato_handler)
dispatcher.add_handler(incentivo_handler)
dispatcher.add_handler(nucleo_handler)
dispatcher.add_handler(convenio_handler)
dispatcher.add_handler(gp_handler)
dispatcher.add_handler(pesquisa_handler)
dispatcher.add_handler(etica_handler)
dispatcher.add_handler(secretaria_handler)
dispatcher.add_handler(vestibular_handler)
dispatcher.add_handler(unknown_handler)

# Start search for updates
updater.start_polling(clean=True)

# Stop the bot, if Ctrl + C were pressed
updater.idle()
