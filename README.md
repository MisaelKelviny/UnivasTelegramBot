# UNIVAS PYTHON TELEGRAM BOT


### É necessário ter alguns pré requisitos:

O python precisa estar instalado na máquina, caso não tenha é econtrado em:
https://www.python.org/

O repositório oficial do bot é encontrado em:
https://github.com/python-telegram-bot/python-telegram-bot

Com o python instalado é necessário instalar os pacotes utilizando o gerenciador PIP.


## Iniciando o bot pelo telegram

precisaremos conseguir o token para que o chatbot possa interagir com a plataforma.
- 1 — Abra o Telegram;
- 2 — Inicie uma conversa com o The BotFather;
- 3 — Utilize o comando /newbot para criar um novo bot;
- 4 — Escolha um nome de exibição para o chatbot. Neste trabalho foi utilizado o nome "UnivasBot"
- 5 — Escolha um nome de usuario para o chatbot. Este será utilizado para que outras pessoas possam fazer menções, e também, se conectarem com o chatbot via o telegram.me. O nome de usuario deve necessariamente ser único na plataforma e terminar com “bot”. O utilizado aqui foi o Univasbot
- 6 — Se tudo ocorrer certo, o The BotFather irá enviar um Token de acesso, que é bem parecido com: “591201733:BCDdqQcvAY1vGWYxaCieFZAq95SPKSza”. É exatamente isso que permitirá que o nosso chatbot envie requisições para o Telegram Bot API.


## Em seguida
Instale os pacotes do bot na sua maquina

```
pip install python-telegram-bot --upgrade
```

### Para fazer o bot rodar

Baixar este repositorio
Abrir o prompt de comando
E rodar o comando dentro do diretorio baixado

```
python core.py
```

# NOTAS
Para tentar entender o projeto e sobre como funciona a maior parte do código foi encontrado na documentação 
do próprio python-telegram-bot
https://core.telegram.org/bots/api 


O Tolken é utilizado nesta linha de código dentro do core.py
```
updater = Updater(token='866382424:AAGVE7O492Xzak3OEwqKUojYF2TR7tNhb6A')
dispatcher = updater.dispatcher
```

É necessário ter uma resposta para a palavra chave esperada, então é preciso criar uma função da seguinte forma:
```
def filtro(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Olha!")
```

Para filtrar o palavras chaves dentro das mensagens lidas é só seguir o determinado código, que é basicamente
declarar um handler que pega aquela palavra chave:
```
filtro_handler = MessageHandler((Filters.regex(re.compile(r'filtro', re.IGNORECASE))), filtro)
```

adiciona a resposta ao dispensador do telegram para que ele possa responder ao servidor do telegram:
```
dispatcher.add_handler(filtro_handler)
```

E ao final é importante adicionar as funções que pausam o servidor local, com o comando de CTRL+C:
```
# Start search for updates
updater.start_polling(clean=True)
# Stop the bot, if Ctrl + C were pressed
updater.idle()
```