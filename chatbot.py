
customer_responses = {
    "hello": "Hello! How can I assist you today?",
    "bye": "Goodbye! Have a nice day!",
    "thank you": "You're welcome!",
    "name": "My Name is chatbot2.0",
    "default": "I'm sorry, I didn't understand. Can you simplify please?"
}

def chatbot():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        customer_input = input("Customer: ")

        if customer_input in customer_responses:
            print("Chatbot:", customer_responses[customer_input])
        else:
            print("Chatbot:", customer_responses["default"])

        if customer_input == "bye":
            break

chatbot()
