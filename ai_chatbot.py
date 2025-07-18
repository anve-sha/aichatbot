import nltk
import random
import string

from nltk.chat.util import Chat, reflections

# You can define your own pairs
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["what is your name?", ["I'm your friendly chatbot."]],
    ["how are you?", ["I'm doing well, thank you!", "All good. What about you?"]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]],
    ["(.*) your name?", ["My name is ChatBot."]],
    ["(.) help (.)", ["I can assist you with your queries. Ask me anything!"]],
    ["(.*) (location|city)", ["I'm in your imagination!"]],
    ["(.*)", ["Tell me more...", "Interesting...", "I'm listening."]],
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Run chatbot
def start_chat():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chatbot.converse()

start_chat()