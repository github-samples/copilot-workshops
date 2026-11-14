---
title: "Lekcja 1 - Buduj w obszarze roboczym"
description: "Zbuduj Space Quiz w VS Code, podglądaj go w zintegrowanej przeglądarce i dopracuj wybrany element."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Trzymaj edytor, czat, pliki i podgląd razem. Zbudujesz quiz, przejdziesz go w zintegrowanej przeglądarce, a następnie przekażesz konkretny element prosto do czatu, aby wprowadzić precyzyjną zmianę.

W tej lekcji:

- zbudujesz quiz w pojedynczym pliku `index.html`.
- otworzysz podgląd quizu w zintegrowanej przeglądarce.
- wybierzesz element w przeglądarce i go dopracujesz.

## Zbuduj quiz

Wyślij poniższe polecenie w Copilot Chat:

```plaintext
Create a colorful, accessible space exploration quiz with 10 questions in a single index.html. Add a progress bar, score counter, animated correct and incorrect feedback, and a results screen. Use no server or dependencies. Open it in the VS Code integrated browser.
```

1. Przejrzyj wygenerowany plik w edytorze.
2. Otwórz zintegrowaną przeglądarkę i przejdź kilka pytań.
3. W dowolnym momencie otwórz **Source Control**, aby zobaczyć zmienione pliki i diff.

## Wybierz element i dopracuj go

Zintegrowana przeglądarka może przekazać konkretny element prosto do czatu, więc nie musisz opisywać, o który przycisk Ci chodzi.

1. Przy otwartym quizie w zintegrowanej przeglądarce rozpocznij wybór elementu z paska narzędzi przeglądarki.
2. Wybierz przyciski odpowiedzi, aby dołączyć ten element do kolejnej wiadomości w czacie.
3. Wyślij poniższe polecenie i obserwuj przeładowanie podglądu:

   ```plaintext
   Using the selected element, make the answer buttons feel more tactile: add a subtle press state, a clearer focus ring for keyboard users, and a smoother transition into the correct and incorrect colors. Change nothing else.
   ```

4. Przeczytaj diff w **Source Control**, zanim go zachowasz.
5. Wciśnij <kbd>Tab</kbd>, aby przejść między odpowiedziami, i upewnij się, że pierścień fokusu jest widoczny.

## Podsumowanie i kolejne kroki

Zbudowałeś, sprawdziłeś w podglądzie i dopracowałeś quiz bez opuszczania edytora. Przejdź do [Lekcji 2: Zapisz instrukcje projektu][next-lesson].

[next-lesson]: ../2-project-instructions/
