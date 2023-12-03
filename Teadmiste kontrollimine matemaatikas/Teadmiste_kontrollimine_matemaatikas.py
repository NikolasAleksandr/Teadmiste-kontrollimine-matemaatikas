import random

print("Valige ülesande raskusaste:")
print("1. Task 1 (numbrid 1 kuni 10)")
print("2. Task 2 (numbrid 10 kuni 50)")
print("3. Task 3 (numbrid 50 kuni 100)")

raskus = int(input("Sisestage raskusastme number (1, 2, 3): "))

if raskus not in {1, 2, 3}:
    print("Viga: vale raskusastme valik.")
else:
    total_questions = int(input("Sisestage näidete arv: "))
    correct_answers = 0

    for _ in range(total_questions):
        num_range = (1, 10) if raskus == 1 else (10, 50) if raskus == 2 else (50, 100)
        num1 = random.randint(*num_range)
        num2 = random.randint(*num_range)
        operation = random.choice(['+', '-', '*', '/'])

        result = eval(f"{num1} {operation} {num2}")
        expression = f"{num1} {operation} {num2}"

        user_answer = float(input(f"Lahendage näide: {expression} = "))

        if user_answer == result:
            print("Õige!")
            correct_answers += 1
        else:
            print(f"Vale. Õige vastus: {result}")

    percentage_correct = (correct_answers / total_questions) * 100
    print(f"\nHinne: {'Hinne 2' if percentage_correct < 60 else ('Hinne 3' if percentage_correct < 75 else ('Hinne 4' if percentage_correct < 90 else 'Hinne 5'))}")
    print(f"Õiged vastused: {correct_answers}/{total_questions} ({percentage_correct:.2f}%)")


