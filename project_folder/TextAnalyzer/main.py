
import re
from pathlib import Path


def get_words(text):
    """Отримує список слів із тексту."""
    return re.findall(
        r"[а-яіїєґ]+(?:[’ʼ'-][а-яіїєґ]+)*",
        text.lower()
    )


def word_frequency_percent(text):
    """Повертає частоту кожного слова у відсотках."""
    words = get_words(text)
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    total = len(words)

    if total == 0:
        return {}

    frequencies = {}

    for word, count in word_counts.items():
        frequencies[word] = round(count / total * 100, 2)

    return frequencies


def shortest_words(text):
    """Повертає список найкоротших слів."""
    words = get_words(text)

    if not words:
        return []

    min_length = min(len(word) for word in words)

    return sorted(set(
        word for word in words if len(word) == min_length
    ))


def longest_words(text):
    """Повертає список найдовших слів."""
    words = get_words(text)

    if not words:
        return []

    max_length = max(len(word) for word in words)

    return sorted(set(
        word for word in words if len(word) == max_length
    ))


def unique_words_count(text):
    """Повертає кількість унікальних слів."""
    return len(set(get_words(text)))


def words_count(text):
    """Повертає загальну кількість слів."""
    return len(get_words(text))


def used_letters(text):
    """Повертає всі літери, використані в тексті."""
    letters = set(re.findall(r"[а-яіїєґ]", text.lower()))
    return sorted(letters)


def most_frequent_letter(text):
    """Повертає літеру або літери, які трапляються найчастіше."""
    letters = re.findall(r"[а-яіїєґ]", text.lower())
    letter_counts = {}

    for letter in letters:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    if not letter_counts:
        return []

    max_count = max(letter_counts.values())

    return sorted(
        letter for letter, count in letter_counts.items()
        if count == max_count
    )



file_path = Path(__file__).parent / "text.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

print("АНАЛІЗ УКРАЇНСЬКОГО ТЕКСТУ")
print("=" * 40)

print("\n1. Частотний словник у відсотках:")
for word, frequency in sorted(
    word_frequency_percent(text).items(),
    key=lambda item: (-item[1], item[0])
):
    print(f"{word}: {frequency}%")

print("\n2. Найкоротші слова:")
print(shortest_words(text))

print("\n3. Найдовші слова:")
print(longest_words(text))

print("\n4. Кількість унікальних слів:")
print(unique_words_count(text))

print("\n5. Загальна кількість слів:")
print(words_count(text))

print("\n6. Літери, використані в тексті:")
print(used_letters(text))

print("\n7. Найчастіша літера:")
print(most_frequent_letter(text))
