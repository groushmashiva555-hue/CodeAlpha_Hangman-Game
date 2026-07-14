def get_bot_response(user_input):
    
    user_input = user_input.lower().strip()
    
    
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm doing great, thanks for asking! How are you?",
        "what is your name": "I am a simple Python chatbot created for my internship.",
        "bye": "Goodbye! Have a great day!"
    }
    
    
    return responses.get(user_input, "I'm sorry, I don't understand that. Could you try asking something else?")

def run_chatbot():
    print("Chatbot initialized! (Type 'bye' to exit)")
    
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print(f"Bot: {response}")
        
        
        if user_input.lower().strip() == "bye":
            break

if __name__ == "__main__":
    run_chatbot()
