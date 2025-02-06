import nltk
from nltk.chat.util import Chat, reflections
import random

nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


pares = [
    [
        r"oi|ola|e aí|bom dia",
        ["Olá! Como posso ajudar?", "Oi! Em que posso ajudar hoje?", "E aí! Qual é a boa?"]
    ],
    [
        r"qual e o seu nome?",
        ["Me chamam de NeuroBot!", "Pode me chamar de Algoritmo Amigável!"]
    ],
    [
        r"como voce funciona\?",
        ["Sou um sistema de IA que usa processamento de linguagem natural e padrões pré-definidos para conversar!"]
    ],
    [
        r"(.*) clima (.*)",
        ["Desculpe, não tenho acesso a dados em tempo real. Que tal ver no seu app de previsão?"]
    ],
    [
        r"adeus|tchau|ate mais",
        ["Até logo! Foi bom conversar!", "Tchau! Volte sempre!"]
    ]
]


def resposta_padrao():
    return random.choice([
        "Interessante... Conte-me mais sobre isso.",
        "Não tenho certeza se entendi. Poderia reformular?",
        "Vou precisar aprender mais sobre isso!",
        "Como isso faz você se sentir?"
    ])


def preprocessar(texto):
    tokens = nltk.word_tokenize(texto.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

# Criar e iniciar o chatbot
chat = Chat(pares, reflections)
print("NeuroBot: Olá! Vamos conversar? (Digite 'sair' para encerrar)")
while True:
    entrada = input("Você: ")
    if entrada.lower() == "sair":
        print("NeuroBot: Até a próxima!")
        break
    resposta = chat.respond(entrada)
    if not resposta:
        resposta = resposta_padrao()
    print("NeuroBot:", resposta)