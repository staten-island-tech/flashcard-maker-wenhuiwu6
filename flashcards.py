import json

try:
    with open("FlashCards.json", "r") as file:
        flash_card = json.load(file)
except FileNotFoundError:
    
    flash_card = []

class flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def display_info(self):
        return f"question: {self.question}, answer: {self.answer}"
