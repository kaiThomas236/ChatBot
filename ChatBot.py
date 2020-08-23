from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



def training(chatbot):
    conversation1 = [
        "Hey",
        "What's up?",
        "How are you?",
        "I'm great!",
        "That's awesome. Why so great?",
        "I got a new job!",
        "Wow! Congratulations!",
        "Thank you! I'm super excited to start.",
        "When do you start?",
        "Tomorrow!",
        "Great job!",
        "Thank you.",
        "Of course."
    ]

    trainer = ListTrainer(chatbot)

    trainer.train(conversation1)

def reply(userIn, chatbot):
    response = chatbot.get_response("Good morning!")

    print(response)



def initBot():
    chatbot = ChatBot("Danny")
    return chatbot


def main():
    print("Hi! Welcome to Kai's little chatbot. You'll be talking to Danny today, hopefully it passes the Turing test!")
    danny = initBot()
    training(danny)
    print("Danny is ready to talk to you now! When you want to end the conversation, just say 'Good bye'")
    userIn = input()
    while userIn != "Good bye":
        reply(userIn, danny)
        userIn = input()
    print("Bye!")
    exit()



if __name__ == "__main__":
    main()
