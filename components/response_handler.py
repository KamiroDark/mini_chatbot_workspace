"""
Response Hnadler Component
Manages chatbot responses and interactions.
"""

import json
from datatime import datetime

class ResponseHandler:
    def __init__(self):
        self.responses = {
            'hello' : 'Hello There! How can I assist you today?',
            'help' : 'Im here to help you! with information and support I can assist you?',
            'bye' : 'Goodbye! See you later!',
            'time' : f'Current time is {datetime.now().strftime("%H:%M:%S")}',
            'date' : f'Today is {datetime.now().strftime("%Y-%m-%d")}'
        }
    
    def get_response(self, user_input):
        """Return appropriate response based on user input."""
        user_input = user_input.lower().strip()

        if user_input in self.responses:
            return self.responses[user_input]
        
        for key in self.responses:
            if key in user_input:
                return self.responses[key]
            
        return "I'm sorry, I'm not sure how to respond to that. Try help for assistence"
    
    def add_response(self, trigger, response):

        self.responses[trigger.lower()] = response
        return True
    
    def main():
        print("=" * 50)
        print("Welcome to the Chatbot Response Handler!")
        print("=" * 50)

        handler = ResponseHandler()

        test_inputs = ['hello', 'help', 'time', 'whats your name?', 'bye']

        for user_input in test_inputs:
            response = handler.get_response(user_input)
            print(f"User: {user_input}")
            print(f"Bot: {response}")

        print("\n" + "=" * 50)
        print("Response Handler is Ready!")

    if __name__ == "__main__":
        main()

        