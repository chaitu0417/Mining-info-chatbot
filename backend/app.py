from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Predefined responses for the chatbot
responses = {
    "mining_act": "The primary mining act in India is the Coal Mines Act, 1952.",
    "explosives_act": "The Indian Explosives Act, 1884, governs the use of explosives in mining.",
    "wages_rules": "The Payment of Wages (Mines) Rules, 1956, specify wage-related regulations in mining.",
    "colliery_control": "The Colliery Control Order, 2000, and Colliery Control Rules, 2004, contain safety regulations for collieries.",
    "coal_regulations": "The Coal Mines Regulations, 2017, provide detailed regulations for coal mining.",
    "default": "I'm sorry, I couldn't understand your query. Please ask again.",
    "largest_mine":"b naaat hearttttt ",
    "dinesh":"Pedda konda errri zooogu, nidumolu lowdesh , condom baba , ardamainda rajaaa",
}

# Function to generate a response based on user input
def generate_response(user_input):
    user_input = user_input.lower()

    # Check if the user's input contains keywords related to topics
    if "mines act" in user_input:
        return responses["mining_act"]
    elif "explosives act" in user_input:
        return responses["explosives_act"]
    elif "wages rules" in user_input:
        return responses["wages_rules"]
    elif "colliery control" in user_input:
        return responses["colliery_control"]
    elif "coal regulations" in user_input:
        return responses["coal_regulations"]
    elif "largest mine in a.p" in user_input:
        return responses["largest_mine"]
    elif "dinesh" in user_input:
        return responses["dinesh"]

    # Check if the user's input contains any keyword
    for topic in responses.keys():
        if topic in user_input:
            return responses[topic]

    # If no specific keywords are found, provide a default response
    return responses["default"]
@app.route("/", methods=["GET"])
def index():
    # This route handles requests to the root URL
    return "Welcome to MiningInfoBot!"

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_input = request.json["user_input"]
    bot_response = generate_response(user_input)
    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
