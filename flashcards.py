import json

try:
    with open("FlashCards.json", "r") as file:
        flash_card = json.load(file)
except FileNotFoundError:
    
    flash_card = []

class flashcard:
    def __init__(self, question, key):
        self.question = question
        self.key = key
    def display_info(self):
        return f"question: {self.question}, answer: {self.key}"
    
class Student:
    def __init__(self, name, answer):
        self.name = name
        self.answer = answer 

    def display_info(self):
        return f"Student: {self.name}, Question: {self.answer}"


