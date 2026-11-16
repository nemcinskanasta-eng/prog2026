"""Обчислення Word Error Rate на рівні слів."""

import re


def tokenize(text: str) -> list[str]:
    """Перетворює текст на послідовність слів, ігноруючи регістр і пунктуацію."""
    return re.findall(r"\b[\w’'-]+\b", text.lower(), flags=re.UNICODE)


def calculate_wer(reference: str, hypothesis: str) -> dict:
    """
    Обчислює WER за допомогою динамічного програмування.

    reference — еталонний текст;
    hypothesis — текст для порівняння.
    """
    ref = tokenize(reference)
    hyp = tokenize(hypothesis)

    if not ref:
        raise ValueError("Еталонний текст не може бути порожнім.")

    rows, cols = len(ref) + 1, len(hyp) + 1
    dp = [[0] * cols for _ in range(rows)]
    back = [[None] * cols for _ in range(rows)]

    for i in range(1, rows):
        dp[i][0] = i
        back[i][0] = "D"
    for j in range(1, cols):
        dp[0][j] = j
        back[0][j] = "I"

    for i in range(1, rows):
        for j in range(1, cols):
            if ref[i - 1] == hyp[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                back[i][j] = "C"
            else:
                choices = [
                    (dp[i - 1][j - 1] + 1, "S"),
                    (dp[i - 1][j] + 1, "D"),
                    (dp[i][j - 1] + 1, "I"),
                ]
                dp[i][j], back[i][j] = min(choices, key=lambda item: item[0])

    substitutions = deletions = insertions = correct = 0
    i, j = len(ref), len(hyp)

    while i > 0 or j > 0:
        operation = back[i][j]
        if operation == "C":
            correct += 1
            i -= 1
            j -= 1
        elif operation == "S":
            substitutions += 1
            i -= 1
            j -= 1
        elif operation == "D":
            deletions += 1
            i -= 1
        elif operation == "I":
            insertions += 1
            j -= 1
        else:
            break

    n = len(ref)
    wer = (substitutions + deletions + insertions) / n

    return {
        "WER": round(wer, 4),
        "WER_percent": round(wer * 100, 2),
        "S": substitutions,
        "D": deletions,
        "I": insertions,
        "N": n,
        "C": correct,
        "reference_words": len(ref),
        "hypothesis_words": len(hyp),
    }
