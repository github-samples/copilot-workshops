---
title: "Lekcja 5 - Zaplanuj przed edycją"
description: "Przełącz Copilot Chat na Plan mode, aby zbadał obszar roboczy i zaproponował podejście, zanim zmieni jakiekolwiek pliki."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Tryb planowania bada obszar roboczy i przygotowuje plan implementacji, nie ruszając Twoich plików.

W tej lekcji:

- przełączysz Copilot Chat z Agent na Plan.
- przejrzysz i dopracujesz zaproponowany plan.
- wrócisz do Agent, aby wdrożyć plan.

## Uzgodnij podejście przed jakimikolwiek zmianami

1. Otwórz Copilot Chat i użyj **mode dropdown** nad polem wprowadzania.
2. Przełącz z **Agent** na **Plan**.
3. Opisz kolejną funkcję poniższym poleceniem i pozwól Copilotowi zbadać obszar roboczy:

   ```plaintext
   Plan how to add a review screen that shows every question with the answer I chose. Investigate the existing quiz, list the changes you would make, call out accessibility and single-file risks, and stop before editing.
   ```

4. Przeczytaj plan i poproś o zmiany, a następnie wróć do **Agent**, aby go wdrożyć.

> [!TIP]
> **Kiedy tryb planowania się opłaca**
>
> Używaj Plan mode przy wszystkim, co jest niejednoznaczne, przecina wiele części projektu albo jest kosztowne do cofnięcia. Najtaniej poprawisz złe podejście przed pierwszą edycją.

## Podsumowanie i kolejne kroki

Uzgodniłeś podejście z Copilotem, zanim napisał jakikolwiek kod. Przejdź do [Lekcji 6: Wyposaż Copilota w narzędzia GitHub][next-lesson].

[next-lesson]: ../6-github-mcp/
