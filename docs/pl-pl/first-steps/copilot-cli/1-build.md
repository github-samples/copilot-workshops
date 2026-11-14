---
title: "Ćwiczenie 1 - Budowa quizu z terminala"
description: "Poproś Copilot CLI o cały Space Quiz w jednym szczegółowym poleceniu, a następnie wprowadź jedno skupione dopracowanie."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Poproś o cały projekt w jednym szczegółowym poleceniu, przejrzyj propozycję agenta zanim ją zatwierdzisz, a następnie wprowadź jedną małą, ograniczoną zmianę.

W tym ćwiczeniu:

- zbudujesz quiz bez zależności w `index.html`.
- otworzysz quiz w przeglądarce z sesji.
- wprowadzisz jedną skupioną zmianę i zweryfikujesz ją.

## Zbuduj quiz

Wyślij poniższe polecenie w sesji Copilot CLI:

```plaintext
Create a space exploration quiz with 10 questions, a progress bar, score counter, and colorful animated feedback (green for correct, red shake for wrong). Show a results screen with an emoji reaction at the end. Single index.html, no server or dependencies. Accessible, keyboard-navigable, and respects prefers-color-scheme.
```

1. Przeczytaj zaproponowany plan i zatwierdź zmiany w plikach.
2. Otwórz `index.html` w przeglądarce i rozwiąż kilka pytań. Aby uruchomić go z sesji, użyj `!open index.html` na macOS, `!start index.html` na Windows albo `!xdg-open index.html` na Linux.

## Wprowadź małą zmianę, potem ją sprawdź

Poproś o jedno skupione dopracowanie, żeby zobaczyć, jak zachowuje się ograniczone polecenie:

```plaintext
The results screen feels flat. Give it a stronger sense of arrival: animate the score counting up and make the emoji reaction larger. Change nothing else.
```

1. Odśwież stronę w przeglądarce i przejdź quiz do końca.
2. Zwróć uwagę, że nic nie jest jeszcze w Gicie, więc nie ma względem czego zrobić diff. To się zmieni po opublikowaniu projektu.

## Podsumowanie i kolejne kroki

Zbudowałeś quiz i dopracowałeś go ograniczonym poleceniem. Przejdź do [ćwiczenia 2: Zapisanie instrukcji projektu][next-lesson].

[next-lesson]: ../2-project-instructions/
