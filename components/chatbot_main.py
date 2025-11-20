#!/usr/bin/env python3
"""
Simple Interactive Chatbot
Integrates all components: Response Handler, Logger, Data Processor, Intent Classifier
"""

import sys
import os

# Import our components
from response_handler import ResponseHandler
from logger import ConversationLogger
from data_processor import DataProcessor
from intent_classifier import IntentClassifier

class SimpleChatbot:
    def __init__(self):
        print("🤖 Initializing chatbot components...")
        self.response_handler = ResponseHandler()
        self.logger = ConversationLogger('chatbot_conversation.txt')
        self.data_processor = DataProcessor()
        self.intent_classifier = IntentClassifier()
        print("✅ All components loaded!\n")
    
    def process_input(self, user_input):
        """Process user input through all components"""
        
        # 1. Clean and validate input
        cleaned_input = self.data_processor.clean_input(user_input)
        
        # 2. Classify intent
        intent_result = self.intent_classifier.classify(cleaned_input)
        
        # 3. Get appropriate response
        response = self.response_handler.get_response(cleaned_input)
        
        # 4. Log the conversation
        self.logger.log_conversation(user_input, response)
        
        return {
            'response': response,
            'intent': intent_result['intent'],
            'confidence': intent_result['confidence']
        }
    
    def chat(self):
        """Main chat loop"""
        print("=" * 60)
        print("  SIMPLE CHATBOT - Type 'quit' or 'exit' to end")
        print("=" * 60)
        print("\nBot: Hello! I'm a simple chatbot. How can I help you?\n")
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print("\nBot: Goodbye! Have a great day! 👋\n")
                    self.logger.log_message("SYSTEM", "Chat session ended")
                    break
                
                # Process input through all components
                result = self.process_input(user_input)
                
                # Display response with intent info
                print(f"\nBot: {result['response']}")
                print(f"[Intent: {result['intent']} | Confidence: {result['confidence']}]\n")
                
            except KeyboardInterrupt:
                print("\n\nBot: Interrupted. Goodbye! 👋\n")
                break
            except Exception as e:
                print(f"\nBot: Sorry, I encountered an error: {e}\n")

def main():
    """Run the chatbot"""
    chatbot = SimpleChatbot()
    chatbot.chat()
    
    print("\n" + "=" * 60)
    print("Chat session completed!")
    print("Check 'chatbot_conversation.txt' for the conversation log.")
    print("=" * 60)

if __name__ == "__main__":
    main()