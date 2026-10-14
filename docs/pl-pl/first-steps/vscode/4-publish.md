---
title: "Lekcja 4 - Opublikuj projekt"
description: "Zainicjalizuj, scommituj i opublikuj Space Quiz wyłącznie przez wbudowaną integrację Source Control w VS Code."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Opublikuj przetestowany quiz na GitHub wyłącznie przez wbudowaną integrację Gita i pozwól Copilotowi przygotować treść commita na podstawie tego, co faktycznie się zmieniło.

W tej lekcji:

- zainicjalizujesz repozytorium z **Source Control**.
- wygenerujesz treść commita ze staged diffa.
- opublikujesz gałąź w nowym publicznym repozytorium GitHub.

## Zainicjalizuj, scommituj i opublikuj

1. Otwórz **Source Control** i wybierz **Initialize Repository**.
2. Dodaj pliki do stage.
3. Wybierz ikonę **sparkle pencil** w polu treści commita, aby Copilot napisał wiadomość na podstawie staged diffa. Przeczytaj wiadomość, popraw błędy, a następnie scommituj.
4. Wybierz **Publish Branch** i utwórz publiczne repozytorium `space-quiz` na GitHub.
5. Upewnij się, że przetestowany plik jest widoczny na GitHub.

![Ilustracja widoku Source Control w VS Code. Lista Changes pokazuje index.html oraz .github/copilot-instructions.md. Adnotacja przy przycisku sparkle w polu treści commita mówi Copilot wrote your message, a wiadomość brzmi Add per-question timer to the quiz. Pod przyciskiem Commit wyróżniony jest Create Pull Request z notatką Commit first, then this button appears right inside Source Control.](../../../_images/first-steps-vscode-commit.svg)

Przycisk sparkle przygotowuje treść commita na podstawie staged diffa. Po commitcie **Source Control** proponuje też utworzenie pull requesta.

## Podsumowanie i kolejne kroki

Twój przetestowany quiz jest teraz opublikowany na GitHub. Przejdź do [Lekcji 5: Zaplanuj przed edycją][next-lesson].

[next-lesson]: ../5-plan-mode/
