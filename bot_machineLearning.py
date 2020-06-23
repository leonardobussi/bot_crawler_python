from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("test")

conversa = ChatBot('ola', 'oie', 'como vai', 'vou bem e voce?', 'bem tambem', 'qual é o seu nome', 'nao tenho nome')
conversa2 = ['qual é o seu filme favorito', 'batman']

bot.set_trainer(ListTrainer)

bot.train(conversa)
bot.train(conversa2)


while True:
    questao = input("Voce: ")
    resposta = bot.get_response(questao)

    if float(response.confidence) > 8.5:
        print("Bot: ", resposta)
    else:
        print("Bot: Eu não sei")