import json
def add_flashcard():
    try:
        with open("FlashCards.json", "r") as file:
            flash_card = json.load(file)
    except FileNotFoundError:
        flash_card = []

    word = input("Enter a word/phrase: ")
    answer = input("Enter the answer: ")

def teacher_mode():
    while True:
        print("\nTeacher Mode:")
        print("1. Add Flashcard")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_flashcard()
        elif choice == "2":
            break
        else:
            print("Invalid")

def student_mode():
    flashcards = load_flashcards()
    if not flashcards:
        return
    
    correct_answers = 0
    streak = 0
    total = len(flashcards)
    
    random.shuffle(flashcards)  # Shuffle the flashcards for random order
    
    for card in flashcards:
        print(f"\nWhat is the answer to: {card['word']}")
        answer = input("Your answer: ").strip()
        
        if answer.lower() == card['answer'].lower():
            print("Correct!")
            correct_answers += 1
            streak += 1
            if streak >= 3:
                print(f"Bonus points! Streak of {streak} correct answers!")
        else:
            print(f"Incorrect! The correct answer is: {card['answer']}")
            streak = 0  # Reset streak on incorrect answer

    # Display the final score
    print(f"\nYour score: {correct_answers}/{total}")
    print(f"Bonus Streak Points: {streak}")
    print(f"Total Score: {correct_answers + streak}")




