import random
from datetime import datetime

responses = {

    "hello": [
        "Hello! How can I help you?",
        "Hi! Nice to meet you!",
        "Hello! What can I do for you?"
    ],

    "how are you": [
        "I'm doing great!",
        "I'm fine. Thanks for asking!",
        "I'm doing well!"
    ],

    "name": [
        "I'm a Python AI chatbot.",
        "You can call me PyBot."
    ],

    "bye": [
        "Goodbye!",
        "See you later!",
        "Have a nice day!"
    ]
}


def chatbot(message):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return random.choice(responses["hello"])

    elif "how are you" in message:
        return random.choice(
            responses["how are you"]
        )

    elif "your name" in message:
        return random.choice(
            responses["name"]
        )

    elif "time" in message:
        return "Current time: " + datetime.now().strftime("%H:%M:%S")

    elif "bye" in message:
        return random.choice(responses["bye"])

    else:
        return "Sorry, I don't understand that."


print("===== PYBOT =====")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ")

    reply = chatbot(user)

    print("Bot:", reply)

    if "bye" in user.lower():
        break
