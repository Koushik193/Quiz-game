def display_welcome_message():
    print("Welcome to the Python Quiz Game!")
    print("Answer the following questions to the best of your ability.")
    print("Let's get started!")

def ask_question(question, options, correct_answer):
    print("\n" + question)
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    
    while True:
        try:
            answer = int(input("Please enter the number of your answer: "))
            if 1 <= answer <= len(options):
                return options[answer - 1] == correct_answer
            else:
                print("Invalid choice. Please choose a number from the options.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    display_welcome_message()

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "correct_answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_answer": "4"
        },
        {
            "question": "Which language is this code written in?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "correct_answer": "Python"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "Jupiter"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
            "correct_answer": "Harper Lee"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["Oxygen", "Gold", "Osmium", "Oganesson"],
            "correct_answer": "Oxygen"
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1912", "1905", "1898", "1923"],
            "correct_answer": "1912"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Gold", "Iron", "Diamond", "Platinum"],
            "correct_answer": "Diamond"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["0", "1", "2", "3"],
            "correct_answer": "2"
        },
        {
            "question": "Which programming language is known as the 'mother of all languages'?",
            "options": ["Python", "Java", "C", "Assembly"],
            "correct_answer": "C"
        }
    ]

    score = 0

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['correct_answer']}.")

    print(f"\nQuiz finished! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    main()
