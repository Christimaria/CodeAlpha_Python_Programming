
def chatbot_response(message):
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks! How are you?"

    elif message == "what is your name":
        return "I'm a simple Python chatbot."

    elif message == "help":
        return "You can greet me, ask how I am, or say bye."

    elif message == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Type 'help' for options."


print("===== Welcome to Python Chatbot =====")
print("Type 'help' to see what you can ask.")
print("Type 'bye' to end the conversation.\n")

while True:
    user_message = input("You: ")

    response = chatbot_response(user_message)
    print("Chatbot:", response)

    if user_message.lower().strip() == "bye":
        break
