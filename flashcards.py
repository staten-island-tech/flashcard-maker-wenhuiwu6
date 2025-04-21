import json

def save_flashcards(flashcards):
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
    print("Flashcards saved")


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



