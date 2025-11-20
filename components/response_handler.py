"""
Response Hnadler Component
Manages chatbot responses and interactions.
"""

import json
from datetime import datetime


class ResponseHandler:
    def __init__(self):
        self.responses = {
            # Saludos
            "hello": "Hi there! How can I help you today?",
            "hi": "Hello! What can I do for you?",
            "hey": "Hey! How are you doing?",
            "good morning": "Good morning! Hope you're having a great day!",
            "good afternoon": "Good afternoon! What brings you here?",
            # Despedidas
            "bye": "Goodbye! Have a great day!",
            "goodbye": "See you later! Take care!",
            "see you": "See you soon! Have a wonderful day!",
            # Ayuda
            "help": "I can assist you with information and answer questions. Try asking me about the weather, time, or just chat!",
            "what can you do": "I can chat with you, answer questions, tell you the time, and more! What would you like to know?",
            "how can you help": "I'm here to assist you! You can ask me questions, chat, or request information.",
            # Tiempo
            "time": f'Current time is {datetime.now().strftime("%H:%M:%S")}',
            "what time is it": f'It\'s {datetime.now().strftime("%H:%M:%S")} right now.',
            # Fecha
            "date": f'Today is {datetime.now().strftime("%Y-%m-%d")}',
            "what day is it": f'Today is {datetime.now().strftime("%A, %B %d, %Y")}',
            "today": f'Today is {datetime.now().strftime("%A, %B %d, %Y")}',
            # Agradecimientos
            "thank": "You're welcome! Happy to help!",
            "thanks": "No problem! Anytime!",
            "thank you": "You're very welcome!",
            # Información del bot
            "who are you": "I'm a simple chatbot built with modular Python components!",
            "what are you": "I'm an AI chatbot designed to demonstrate component-based architecture.",
            "your name": "I'm a demonstration chatbot. You can call me ChatBot!",
            # Clima (simulado)
            "weather": "I don't have live weather data, but I hope it's nice where you are!",
            "how is the weather": "I can't check the weather right now, but I hope it's pleasant!",
            # Preguntas personales
            "how are you": "I'm doing great, thanks for asking! How about you?",
            "are you ok": "I'm functioning perfectly! Thanks for checking!",
            # Humor
            "tell me a joke": "Why did the chatbot go to therapy? It had too many issues! 😄",
            "joke": "What do you call a chatbot that sings? A-dell! 🎵",
            # Capacidades
            "what can you tell me": "I can chat about various topics, tell you the time and date, and answer questions!",
            "can you help me": "Absolutely! I'm here to help. What do you need?",
        }

        # Patrones de respuesta para palabras clave
        self.keyword_responses = {
            "python": "Python is awesome! I'm actually built using Python components.",
            "programming": "Programming is fascinating! Are you learning to code?",
            "code": "I love talking about code! What programming language interests you?",
            "chatbot": "Chatbots like me are built using various components working together!",
            "component": "I'm made of modular components: response handler, logger, data processor, and intent classifier!",
            "learn": "Learning is important! What would you like to learn about?",
            "project": "This chatbot is actually a demonstration project! Pretty cool, right?",
        }

    def get_response(self, user_input):
        """Return appropriate response based on user input"""
        user_input_lower = user_input.lower().strip()

        # Actualizar respuestas de tiempo/fecha en tiempo real
        self.responses["time"] = (
            f'Current time is {datetime.now().strftime("%H:%M:%S")}'
        )
        self.responses["what time is it"] = (
            f'It\'s {datetime.now().strftime("%H:%M:%S")} right now.'
        )
        self.responses["date"] = f'Today is {datetime.now().strftime("%Y-%m-%d")}'
        self.responses["what day is it"] = (
            f'Today is {datetime.now().strftime("%A, %B %d, %Y")}'
        )
        self.responses["today"] = f'Today is {datetime.now().strftime("%A, %B %d, %Y")}'

        # Buscar coincidencia exacta primero
        if user_input_lower in self.responses:
            return self.responses[user_input_lower]

        # Buscar coincidencias parciales en respuestas predefinidas
        for key in self.responses.keys():
            if key in user_input_lower:
                return self.responses[key]

        # Buscar palabras clave
        for keyword, response in self.keyword_responses.items():
            if keyword in user_input_lower:
                return response

        # Respuestas contextuales basadas en palabras
        if "?" in user_input:
            return "That's a great question! I'm still learning, but I'll do my best to help."

        if any(word in user_input_lower for word in ["love", "like", "enjoy"]):
            return "That's wonderful! I'm glad you shared that with me."

        if any(
            word in user_input_lower for word in ["sad", "upset", "angry", "frustrated"]
        ):
            return (
                "I'm sorry you're feeling that way. Is there anything I can help with?"
            )

        if any(
            word in user_input_lower
            for word in ["happy", "great", "awesome", "excited"]
        ):
            return "That's fantastic! I'm happy to hear that!"

        # Respuesta por defecto
        return "I'm not sure how to respond to that. Try asking me about the time, date, or just say hello!"

    def add_response(self, trigger, response):
        """Add a new response pattern"""
        self.responses[trigger.lower()] = response
        return True


def main():
    print("=" * 50)
    print("Welcome to the Chatbot Response Handler!")
    print("=" * 50)

    handler = ResponseHandler()

    test_inputs = ["hello", "help", "time", "whats your name?", "bye"]

    for user_input in test_inputs:
        response = handler.get_response(user_input)
        print(f"User: {user_input}")
        print(f"Bot: {response}")

    print("\n" + "=" * 50)
    print("Response Handler is Ready!")


if __name__ == "__main__":
    main()
