from fastapi import FastAPI,Request
import uvicorn
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import TrainingData


# Create a new instance of a ChatBot
chatbot = ChatBot('Charlie', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train(TrainingData.training_data)

app=FastAPI()

@app.post('/response')
async def response(requst:Request):

    
        data =await requst.json()
        print(data['Input'])
        userinput=data['Input']

        if userinput.lower() == "exit":
            response="GoodBye"
            

        else:
            response=chatbot.get_response(userinput)
            response=str(response)

        return {"response":response}


if __name__=="__main__":
   uvicorn.run(app,host='0.0.0.0',port=8010)
  #response()

