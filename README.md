Chatbot with ChatterBot, React Native, and FastAPI
This project showcases a chatbot system developed using the ChatterBot library for natural language processing, React Native for the mobile app, and FastAPI for the backend. The chatbot is designed to assist users by providing information from a CSV file, which includes item details and their corresponding shelf numbers. Additionally, it can answer general questions and provide specific shelf details to customers.

Features
Natural Language Understanding: Utilizes the ChatterBot library to understand and respond to user inputs with a high degree of accuracy.
Mobile Application: Built with React Native, allowing users to interact with the chatbot on both iOS and Android devices.
FastAPI Backend: Serves as the backend, handling requests and managing data interactions efficiently.
Dynamic Data Management: Reads item details and shelf numbers from a CSV file, with the ability to update this information.
General Knowledge Responses: Capable of answering general questions beyond just item and shelf details.
Getting Started
Prerequisites
Python 3.x
Node.js
Expo CLI
FastAPI
ChatterBot
React Native
Setup
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Backend Setup

Navigate to the backend directory and install the required Python packages:

bash
Copy code
cd backend

Start the FastAPI server:

bash
Copy code
uvicorn main:app --reload
Frontend Setup

Navigate to the React Native project directory and install dependencies:

bash
Copy code
cd frontend
npm install
Start the Expo development server:

bash
Copy code
expo start
Update CSV File

Place your CSV file with item details and shelf numbers in the appropriate location as specified in the backend code.

Usage
Open the React Native app on your device or emulator.
Interact with the chatbot to get item and shelf information or to ask general questions.
Screenshots
Add your screenshots here.


Demonstration
View the demonstration video to see the chatbot in action:


GIFs
You can add GIFs to show the chatbot in action:


Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
ChatterBot: ChatterBot Documentation
React Native: React Native Documentation
FastAPI: FastAPI Documentation
