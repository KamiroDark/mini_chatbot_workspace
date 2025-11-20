#!/usr/bin/env python3
"""
Intent Classifier Component
Classifies user intent from input text using keyword matching
"""

import json
from collections import defaultdict

class IntentClassifier:
    def __init__(self):
        # Define intents and their associated keywords
        self.intents = {
            'greeting': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon'],
            'farewell': ['bye', 'goodbye', 'see you', 'farewell', 'exit', 'quit'],
            'help': ['help', 'assist', 'support', 'guide', 'how to', 'what can'],
            'question': ['what', 'when', 'where', 'why', 'how', 'who', '?'],
            'thanks': ['thank', 'thanks', 'appreciate', 'grateful'],
            'complaint': ['problem', 'issue', 'error', 'not working', 'broken', 'wrong']
        }
        
        self.intent_responses = {
            'greeting': 'I detected a greeting! Starting conversation...',
            'farewell': 'I detected a farewell. Ending conversation...',
            'help': 'I detected a help request. Providing assistance...',
            'question': 'I detected a question. Searching for answer...',
            'thanks': 'I detected gratitude. You\'re welcome!',
            'complaint': 'I detected a complaint. Escalating to support...',
            'unknown': 'Intent unclear. Please rephrase.'
        }
    
    def classify(self, user_input):
        """
        Classify the intent of user input
        Returns: dict with intent, confidence, and keywords matched
        """
        user_input = user_input.lower().strip()
        
        if not user_input:
            return {
                'intent': 'unknown',
                'confidence': 0.0,
                'matched_keywords': [],
                'response': self.intent_responses['unknown']
            }
        
        # Count keyword matches for each intent
        intent_scores = defaultdict(int)
        matched_keywords = defaultdict(list)
        
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in user_input:
                    intent_scores[intent] += 1
                    matched_keywords[intent].append(keyword)
        
        # If no matches found
        if not intent_scores:
            return {
                'intent': 'unknown',
                'confidence': 0.0,
                'matched_keywords': [],
                'response': self.intent_responses['unknown']
            }
        
        # Get intent with highest score
        best_intent = max(intent_scores, key=intent_scores.get)
        max_score = intent_scores[best_intent]
        
        # Calculate confidence (simple approach)
        total_keywords = len(self.intents[best_intent])
        confidence = min(max_score / total_keywords, 1.0)
        
        return {
            'intent': best_intent,
            'confidence': round(confidence, 2),
            'matched_keywords': matched_keywords[best_intent],
            'response': self.intent_responses[best_intent]
        }
    
    def add_intent(self, intent_name, keywords, response):
        """Add a new intent dynamically"""
        self.intents[intent_name] = keywords
        self.intent_responses[intent_name] = response
        return True
    
    def get_all_intents(self):
        """Return all available intents"""
        return list(self.intents.keys())

def main():
    """Demo the Intent Classifier"""
    print("=" * 60)
    print("INTENT CLASSIFIER COMPONENT - DEMO")
    print("=" * 60)
    
    classifier = IntentClassifier()
    
    # Test cases
    test_inputs = [
        "Hello, how are you?",
        "Can you help me with something?",
        "Thanks for your assistance!",
        "I have a problem with my account",
        "What is the weather today?",
        "Goodbye, see you later!",
        "blah blah random text"
    ]
    
    print("\nClassifying user inputs:\n")
    
    for user_input in test_inputs:
        result = classifier.classify(user_input)
        print(f"Input: '{user_input}'")
        print(f"  → Intent: {result['intent']}")
        print(f"  → Confidence: {result['confidence']}")
        print(f"  → Keywords: {result['matched_keywords']}")
        print(f"  → Response: {result['response']}")
        print()
    
    # Show all available intents
    print("Available intents:")
    for intent in classifier.get_all_intents():
        print(f"  • {intent}")
    
    print("\n" + "=" * 60)
    print("Intent Classifier is ready!")

if __name__ == "__main__":
    main()