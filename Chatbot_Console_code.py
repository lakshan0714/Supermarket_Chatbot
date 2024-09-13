
##This is Python code for Chatbot you can use chatbot in console by running It.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import Backend.TrainingData as TrainingData


# Create a new instance of a ChatBot
chatbot = ChatBot('Charlie', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)


# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train(TrainingData.training_data)

# Chat with the user
def chat():
    print("Welcome to the Supermarket! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        else:
            print(f"Bot: {chatbot.get_response(user_input)}")

if __name__ == "__main__":
    chat()



