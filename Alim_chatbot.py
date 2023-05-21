from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
chatbot = ChatBot('Terminal')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hello Alim, I have an appointment today",
    "Can I have your medical file number ?",
    "Sure, its 461432",
    "Good morning Ahmad, what is the reson for your visit today?",
    "I want to check The results of my recent medical tests",
    "Sure , Here's your medical assessment: all vital signs are in good condition."
])

print('Hello, my name is Alim,'+'\n '+'How can I help you ?')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break