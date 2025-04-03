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



















def teacher_mode():
    flashcards = flash_card()
    
    while True:
        print("\nEnter 'exit' to quit Teacher Mode.")
        word = input("Enter the word/phrase: ")
        if word.lower() == 'exit':
            break
        answer = input("Enter the answer: ")

        flashcards[word] = answer
        save_flashcards(flashcards)
        print(f"Flashcard for '{word}' added successfully!")

    print("\nTeacher Mode has ended.")


class Teacher:
    def __init__(self, question, answer):
        self.answer = answer
        self.question = question
    
    def display_info(self):
        return f"Question: {self.question}, Answer: {self.answer}"
    
class Student:
    def __init__(self, name, answer):
        self.name = name
        self.answer = answer 

    def display_info(self):
        return f"Student: {self.name}, Question: {self.answer}"


