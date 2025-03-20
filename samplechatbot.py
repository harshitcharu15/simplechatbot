class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "help": "I can respond to basic greetings, list my capabilities, and handle simple interactions.",
            "capabilities": "I can greet you, list my capabilities, and respond to basic prompts.",
            "bye": "Goodbye! Have a great day!"
        }

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "I'm not sure how to respond to that. Try asking 'help' to see what I can do."

# Simple interaction loop
def chat():
    bot = SimpleChatbot()
    print("Chatbot: Hello! Type 'help' to see what I can do, or 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "bye":
            print("Chatbot: Goodbye!")
            break
        print(f"Chatbot: {bot.get_response(user_input)}")

if __name__ == "__main__":
    chat()

