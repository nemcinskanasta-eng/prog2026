import random


# Список студентів групи
students = [
    "Акберова Шафіга",
    "Бабич Софія",
    "Вагіна Аліна",
    "Дмитрієва Анна",
    "Іщенко Карина",
    "Клименко Наталія",
    "Крамаренко Ганна",
    "Карпова Христина",
    "Коржикова Софія",
    "Кучін Ілля",
    "Леонова Поліна",
    "Міняйлик Аліна",
    "Наталуша Тетяна",
    "Немчинська Анастасія",
    "Поліщук Єлизавета",
    "Роменський Микита",
    "Ткачук Поліна",
    "Фесюк Вікторія",
    "Хмельницька Олександра",
    "Хміль Катерина",
    "Чомахашвілі Евеліна",
]


def demonstrate_random_functions():
    """Демонструє різницю між random(), randint() і choice()."""
    print("\n0. РІЗНИЦЯ МІЖ ФУНКЦІЯМИ МОДУЛЯ RANDOM")
    print("-" * 55)

    print("random.random():", random.random())
    print("Повертає випадкове дійсне число від 0.0 (включно) до 1.0 (не включно).")

    print("random.randint(1, 10):", random.randint(1, 10))
    print("Повертає випадкове ціле число від 1 до 10 включно.")

    options = ["яблуко", "груша", "слива"]
    print("random.choice(options):", random.choice(options))
    print("Вибирає один випадковий елемент зі списку або іншої послідовності.")


def choose_one_student():
    """Випадково обирає одного студента кілька разів."""
    print("\n1. ВИПАДКОВИЙ ВИБІР ОДНОГО СТУДЕНТА")
    print("-" * 55)

    for attempt in range(1, 6):
        student = random.choice(students)
        print(f"{attempt}. Обрано: {student}")


def choose_several_students():
    """Випадково обирає п'ятьох різних студентів."""
    print("\n2. ВИПАДКОВИЙ ВИБІР КІЛЬКОХ СТУДЕНТІВ")
    print("-" * 55)

    selected_students = random.sample(students, 5)
    print("Випадково обрані 5 студентів:")
    for number, student in enumerate(selected_students, start=1):
        print(f"{number}. {student}")


def flip_coin(number_of_flips):
    """Підкидає монету задану кількість разів і рахує результати."""
    results = []
    counts = {"орел": 0, "решка": 0}

    for _ in range(number_of_flips):
        result = random.choice(["орел", "решка"])
        results.append(result)
        counts[result] += 1

    print(f"\nРезультати {number_of_flips} підкидань:")
    # Виводимо всі результати, по 20 у рядку, щоб їх було зручно читати.
    for start in range(0, len(results), 20):
        print(", ".join(results[start:start + 20]))

    print(f"Орел випав: {counts['орел']} разів")
    print(f"Решка випала: {counts['решка']} разів")
    print(f"Перевірка: {counts['орел']} + {counts['решка']} = {number_of_flips}")


def coin_game():
    """Проводить експеримент із підкиданням монети 100 і 1000 разів."""
    print("\n3. ГРА З МОНЕТКОЮ")
    print("-" * 55)
    flip_coin(100)
    flip_coin(1000)


def rock_paper_scissors():
    """Гра користувача з комп'ютером у камінь, ножиці, папір."""
    print("\n4. ВЛАСНА ГРА: КАМІНЬ, НОЖИЦІ, ПАПІР")
    print("-" * 55)

    choices = ["камінь", "ножиці", "папір"]

    print("Оберіть свій варіант:")
    print("1 — камінь")
    print("2 — ножиці")
    print("3 — папір")

    user_input = input("Ваш вибір (1/2/3): ").strip()
    variants = {"1": "камінь", "2": "ножиці", "3": "папір"}

    if user_input not in variants:
        print("Помилка: введіть 1, 2 або 3. Гру завершено.")
        return

    user_choice = variants[user_input]
    computer_choice = random.choice(choices)

    print(f"Ваш вибір: {user_choice}")
    print(f"Вибір комп'ютера: {computer_choice}")

    if user_choice == computer_choice:
        print("Результат: нічия!")
    elif (
        (user_choice == "камінь" and computer_choice == "ножиці")
        or (user_choice == "ножиці" and computer_choice == "папір")
        or (user_choice == "папір" and computer_choice == "камінь")
    ):
        print("Результат: ви перемогли!")
    else:
        print("Результат: переміг комп'ютер!")


def main():
    print("=" * 55)
    print("ПРАКТИЧНА РОБОТА: РОБОТА З МОДУЛЕМ RANDOM")
    print("=" * 55)

    demonstrate_random_functions()
    choose_one_student()
    choose_several_students()
    coin_game()
    rock_paper_scissors()

    print("\nРоботу завершено.")


if __name__ == "__main__":
    main()
