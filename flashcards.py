import json
try:
    with open("FlashCards.json", 'r') as file:
        flashcards_data = json.load(file)
except FileNotFoundError:
    flashcards_data = []
except json.JSONDecodeError:
    flashcards_data=[]







class flashcards:
    def __init__(card, phrase, answer):
        card.phrase = phrase
        card. answer = answer
    def create_dict(card):
        print(card.phrase, card.answer)
        x = {card.phrase : card.answer}
        return x
    
create = input("Do you want to create a new flashcard? (Yes or No): ")
while create == "Yes" :
    word_phrase = input("Give word or phrase: ")
    answer = input("Give answer: ")

    hehe = flashcards(word_phrase,answer)
    print(hehe.create_dict())
    

""" def save_flashcards(flashcards):
    with open("FlashCards.json", 'w') as file:
        json.dump(flashcards, file, indent=4)
        print("Saved")

def add_flashcards():
    try:
        with open("FlashCards.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def teacher_mode():
    flashcards = add_flashcards()
    while True:
        word_phrase = input("Enter a word/phrase or 'exit' to leave): ")
        if word_phrase.lower() == 'exit':
            break
        answer = input("Enter the answer: ")
        flashcards[word_phrase] = answer
    save_flashcards(flashcards)
teacher_mode() """

































""" def save_flashcards(flashcards):
    with open("FlashCards.json", 'w') as file:
        json.dump(flashcards, file, indent=4)
        print("Saved")

def add_flashcards():
    try:
        with open("FlashCards.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def teacher_mode():
    flashcards = add_flashcards()
    print("Teacher Mode")
    while True:
        key = input("Enter a word/phrase or 'exit' to leave): ")
        if key.lower() == 'exit':
            break
        value = input("Enter the answer: ")
        flashcards[key] = value
    save_flashcards(flashcards)
    print("Flashcards saved") """


""" def student_mode():
    flashcards = add_flashcards()
    if not flashcards:
        print("No flashcards found. Please ask a teacher to add some.")
        return

    print("=== Student Mode ===")
    score = 0
    streak = 0

    for question, answer in flashcards.items():
        user_answer = input(f"What is the answer to: '{question}'? ")
        if user_answer.strip().lower() == answer.strip().lower():
            streak += 1
            points = 1 + (streak - 1)
            print(f"Correct! +{points} point(s). Streak: {streak}") """



