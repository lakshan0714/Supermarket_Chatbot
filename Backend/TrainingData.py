# training_data.py
import pandas as pd

# Load data from CSV
Data = pd.read_csv('supermarket.csv')

good_names=Data['good'].to_list()




# Generate descriptions
Data['description'] = Data.apply(
    lambda row: f"Sorry! {row['good']} is currently Not available." if row['shelf'] == 0 else f"{row['good']} is located on shelf {row['shelf']}.",
    axis=1
)

# Print the generated text
sentences = list(Data['description'])

# Create training data dynamically
training_data = [   

]

# Generate training data from the DataFrame
for index, row in Data.iterrows():
    training_data.extend([
         "Hello",
         "Hello! How can i help you?.",

         "Hi",
         "Hi! How can i assist you?.",

          "Hii",
         "Hi! How can i assist you?.",

         "What is your name?" ,
         "I'm Atlas, your supermarket assistant chatbot.",
          "What's your name?" ,
         "I'm Atlas, your supermarket assistant chatbot.",
          "Who are you?" ,
         "I'm Atlas, your supermarket assistant chatbot.",

          "Thankyou",
          "You're welcome! If you need any more help, just ask.",
            "Thanks",
          "You're welcome! If you need any more help, just ask.",
            "Okay Thankyou",
          "You're welcome! If you need any more help, just ask.",

        "Where is the cart?",
        "Shopping carts are located at the entrance of the supermarket.",
        "Good morning!",
        "Good morning!How can i assist you?",
        "Good affternoon!",
        "Good afternoon!How can i assist you?",
         "Good evening!",
         "Good evening!How can i assist you?",

         "How are you!",
         "I'm just a bot, but I'm here to help you with your shopping needs.",

         "What can you do!",
         "I can help you find the location of items in the supermarket.",

          "Bye",
          "Good Bye! Have a nice Day",
          "okay Bye",
          "Good Bye! Have a nice Day"
           "See You!",
           "See You Soon"]

       
    )
    
    training_data.extend([
           f"Where is the {row['good']}?",
           row['description']

    ]   
    )
    
    training_data.extend([
        f"Can you tell me where the {row['good']} are?",
        "sure"+row['description']]     
    )
    training_data.extend([
        f"Can i have {row['good']}",
         row['description']]      
    )
    training_data.extend([
        f"do you have {row['good']}",
        row['description']]      
    )

    training_data.extend([
         f"I need some {row['good']}.where is it?",
           row['description']]
    )

    training_data.extend([
          f"Where can i find {row['good']}.",
           row['description']]
    )
    training_data.extend([
          f"Do you have {row['good']}.",
           row['description']]
    )



    training_data.extend([
          f"Where can i find bun.",
          "I'm sorry, but we currently don't have bun available in our supermarket.",
           "Do you have cake?",
           "I'm sorry, but we don't have cake at the moment."]

    )



#print(training_data)