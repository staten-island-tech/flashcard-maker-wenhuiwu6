import json

try:
    with open("flashcards_data.json", 'r') as file:
        flashcards_data = json.load(file)
except FileNotFoundError:
    flashcards_data = []
except json.JSONDecodeError:
    flashcards_data = []

class Flashcard:
    def __init__(self, phrase, answer):
        self.phrase = phrase
        self.answer = answer

    def create_dict(self):
        return {self.phrase: self.answer}

create = input("Do you want to create a new flashcard? (Yes or No): ")
while create == "Yes":
    word_phrase = input("Give word or phrase: ")
    answer = input("Give answer: ")

    new_card = Flashcard(word_phrase, answer)
    print(new_card.create_dict())
    flashcards_data.append(new_card.__dict__)

    print(flashcards_data)
    create = input("Do you want to create flashcard? (Yes or No): ")

with open("flashcards_data.json", "w") as file:
    json.dump(flashcards_data, file, indent=4)

class Student: 
    def __init__(self, name, score=0, streak=0):
        self.name = name
        self.score = score
        self.streak = streak

    def points(self):
        self.score += 1
        return self.score

    def streaks(self):
        self.streak += 1
        return self.streak

    def reset(self):
        self.streak = 0

    def show(self):
        return self.score

lina = Student("Lina", 0, 0)
mode = input("Switch to student mode? (Yes or No): ")
while mode == "Yes":
    for flashcard in flashcards_data:
        print(flashcard["question"])
        attempt = input("Type your answer: ")
        if attempt.strip().lower() == flashcard["key"].strip().lower():
            print(f"Correct! Score right now: {lina.points()}, Streak: {lina.streaks()}")
        else:
            lina.reset()
            print(f"Incorrect. Score now: {lina.show()}")
        switch = input("Another round? (Yes or No): ")
        if switch != "Yes":
            mode = "No"
            break
