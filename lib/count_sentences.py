#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''
        if isinstance(value, str):
            self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  # Print instead of raising ValueError
    
    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self):
        if not self._value:
            return 0
            
        # Replace multiple punctuation marks with a single period
        text = self._value.replace('!', '.').replace('?', '.')
        
        # Split by period and filter out empty strings
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        return len(sentences)