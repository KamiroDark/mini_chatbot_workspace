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