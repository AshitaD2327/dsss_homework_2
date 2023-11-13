import random

def generate_random_integer(minimum, maximum):
    """
    Generates a random integer between the specified minimum and maximum values (inclusive).
    """
    return random.randint(minimum, maximum)

def generate_random_operator():
    """
    Generates a random mathematical operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])

def calculate_result(number1, number2, operator):
    """
    Calculates the result of the mathematical expression.
    """
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    expression = f"{number1} {operator} {number2}"
    return expression, result

def math_quiz():
    """
    Conducts a math quiz game where the user needs to provide correct answers to math problems.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = calculate_result(number1, number2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
