#!/usr/bin/env python3
"""
Logger Component
Logs all chatbot conversations to a file
"""

import json
from datetime import datetime
import os

class ConversationLogger:
    def __init__(self, log_file='chatbot_logs.txt'):
        self.log_file = log_file
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self._initialize_log()
    
    def _initialize_log(self):
        """Create log file if it doesn't exist"""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("CHATBOT CONVERSATION LOG\n")
                f.write("=" * 60 + "\n\n")
    
    def log_message(self, sender, message):
        """Log a message to the file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{self.session_id}] {sender}: {message}\n"
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        
        return True
    
    def log_conversation(self, user_input, bot_response):
        """Log a complete conversation turn"""
        self.log_message("USER", user_input)
        self.log_message("BOT", bot_response)
        return True
    
    def get_recent_logs(self, num_lines=10):
        """Retrieve recent log entries"""
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                return lines[-num_lines:]
        except FileNotFoundError:
            return []

def main():
    """Demo the Logger"""
    print("=" * 50)
    print("LOGGER COMPONENT - DEMO")
    print("=" * 50)
    
    logger = ConversationLogger()
    
    # Simulate some conversations
    conversations = [
        ("Hello!", "Hi there! How can I help you?"),
        ("What's the weather?", "I don't have weather data currently."),
        ("Thanks!", "You're welcome!")
    ]
    
    print("\nLogging conversations...")
    for user_msg, bot_msg in conversations:
        logger.log_conversation(user_msg, bot_msg)
        print(f"✓ Logged: User: '{user_msg}' | Bot: '{bot_msg}'")
    
    print(f"\n✓ All logs saved to: {logger.log_file}")
    print(f"✓ Session ID: {logger.session_id}")
    
    print("\n" + "=" * 50)
    print("Logger is ready!")

if __name__ == "__main__":
    main()