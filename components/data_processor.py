"""
Data Processor Modulo (Modulo de procesador de datos :D)
"""

#!/usr/bin/env python3
"""
Data Processor Component
Validates and processes user input data
"""

import re
import json

class DataProcessor:
    def __init__(self):
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.phone_pattern = r'^\+?1?\d{9,15}$'
    
    def clean_input(self, text):
        """Remove extra whitespace and normalize text"""
        if not text:
            return ""
        
        # Remove extra spaces
        cleaned = ' '.join(text.split())
        
        # Remove potentially harmful characters
        cleaned = re.sub(r'[<>{}]', '', cleaned)
        
        return cleaned.strip()
    
    def validate_email(self, email):
        """Check if email format is valid"""
        if re.match(self.email_pattern, email):
            return {"valid": True, "email": email}
        return {"valid": False, "error": "Invalid email format"}
    
    def validate_phone(self, phone):
        """Check if phone number format is valid"""
        # Remove common separators
        clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
        
        if re.match(self.phone_pattern, clean_phone):
            return {"valid": True, "phone": clean_phone}
        return {"valid": False, "error": "Invalid phone format"}
    
    def extract_keywords(self, text):
        """Extract important keywords from text"""
        # Remove common words
        stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        
        words = text.lower().split()
        keywords = [word for word in words if word not in stopwords and len(word) > 2]
        
        return keywords
    
    def process_user_input(self, user_input):
        """Complete processing pipeline"""
        result = {
            "original": user_input,
            "cleaned": self.clean_input(user_input),
            "length": len(user_input),
            "word_count": len(user_input.split()),
            "keywords": self.extract_keywords(user_input)
        }
        return result

def main():
    """Demo the Data Processor"""
    print("=" * 50)
    print("DATA PROCESSOR COMPONENT - DEMO")
    print("=" * 50)
    
    processor = DataProcessor()
    
    # Test input cleaning
    print("\n1. INPUT CLEANING:")
    test_text = "  Hello    world!   How   are you?  "
    cleaned = processor.clean_input(test_text)
    print(f"Original: '{test_text}'")
    print(f"Cleaned:  '{cleaned}'")
    
    # Test email validation
    print("\n2. EMAIL VALIDATION:")
    emails = ["user@example.com", "invalid.email", "test@domain.co"]
    for email in emails:
        result = processor.validate_email(email)
        print(f"{email}: {'✓ Valid' if result['valid'] else '✗ Invalid'}")
    
    # Test keyword extraction
    print("\n3. KEYWORD EXTRACTION:")
    text = "I want to book a flight to Paris for vacation"
    keywords = processor.extract_keywords(text)
    print(f"Text: {text}")
    print(f"Keywords: {keywords}")
    
    # Test complete processing
    print("\n4. COMPLETE PROCESSING:")
    user_input = "Can you help me find a good restaurant?"
    result = processor.process_user_input(user_input)
    print(json.dumps(result, indent=2))
    
    print("\n" + "=" * 50)
    print("Data Processor is ready!")

if __name__ == "__main__":
    main()