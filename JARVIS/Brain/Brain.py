import nltk
from nltk.chat.util import Chat, reflections

# file downlaod
# import nltk
# nltk.download('punkt')


# Define the chat pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"who i am",
        ["You are creator of me. The BAIVAS called Buddy an Artificial Intelligence based Voice Assistant System",]
    ],
    [
        r"who is saad",
        ["Saad is a creator of me. The BAIVAS called Buddy an Artificial Intelligence based Voice Assistant System",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["You can call me Buddy.", "my name is buddy"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"quit",
        ["Bye-bye. Take care!", "Nice talking to you. Goodbye!"]
    ],

    [
        r"what is my name",
        ["You are Saad Akhtar", "Nice to meet you"]
    ],
]


# Preprocess the text
# Replace the 'text_file_path' with the path to your large text file
# with open('text_file_path', 'r') as file:
#     text = file.read()

# Perform any required text preprocessing steps
# Tokenization, cleaning, lowercasing, etc.

# Prepare the training data
# Extract patterns and responses from the preprocessed text
# Structure them as pairs

# Train the chatbot
chatbot = Chat(pairs, reflections)

# libraries for path (sys, os) and for Speak ank talk (Speak, Take_command)
import sys, os
sys.path.append(os.path.abspath("C:/JARVIS"))
from Body.Speak import Speak
from Body.Take_Command import take_command 

# Test the chatbot
def main():
    Speak("Welcome to the Chatting Area. What can I do for you today?")
    while True:
        # user_input = input("> ")
        # if user_input.lower() == "quit":
        input = take_command('eng')
        if 'quit' in input.lower or 'bye-bye' in input.lower or 'bye bye' in input.lower or 'end this' in input.lower:
            Speak("Leaving the chatting area. Now you can use other functions available in system.")
            break
        response = chatbot.respond(input)
        Speak(response)


# main()








