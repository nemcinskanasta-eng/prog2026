"""Запуск порівняння двох текстів та збереження метрик у JSON."""

import json
from pathlib import Path
from wer import calculate_wer

BASE_DIR = Path(__file__).resolve().parent


def read_text(filename: str) -> str:
    path = BASE_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Не знайдено файл: {filename}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    reference = read_text("reference.txt")
    hypothesis = read_text("hypothesis.txt")

    metrics = calculate_wer(reference, hypothesis)

    output_path = BASE_DIR / "results.json"
    output_path.write_text(
        json.dumps(metrics, ensure_ascii=False, indent=4),
        encoding="utf-8",
    )

    print("РЕЗУЛЬТАТИ ОБЧИСЛЕННЯ WORD ERROR RATE")
    print("-" * 42)
    print(f"WER: {metrics['WER']} ({metrics['WER_percent']}%)")
    print(f"S — заміни:       {metrics['S']}")
    print(f"D — видалення:    {metrics['D']}")
    print(f"I — вставлення:   {metrics['I']}")
    print(f"N — слів в еталоні: {metrics['N']}")
    print(f"C — правильні слова: {metrics['C']}")
    print("-" * 42)
    print(f"Результати збережено у файлі: {output_path.name}")


if __name__ == "__main__":
    main()
