---
title: "Lekcja 2 - Zbuduj i dopracuj quiz"
description: "Zbuduj jednoplikowy Space Quiz i dopracuj go w zintegrowanej przeglądarce oraz za pomocą element pickera."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Użyj jednego szczegółowego polecenia, aby zbudować Space Quiz, sprawdzić jego działanie w zintegrowanej przeglądarce i wprowadzić poprawkę wizualną za pomocą element pickera.

W tej lekcji:

- utworzysz quiz bez zależności w pliku `index.html`.
- przetestujesz quiz w zintegrowanej przeglądarce.
- przejrzysz wygenerowany kod.
- dopracujesz wybrany element, zachowując dostępność.

## Zbuduj quiz

Wyślij poniższe polecenie w sesji `space-quiz`:

```plaintext
Create a space exploration quiz with 10 questions, a progress bar, score counter, and colorful animated feedback (green for correct, red shake for wrong). Show a results screen with emoji reaction at the end. Center in a narrow column. Single index.html, no server/dependencies. Polished, sans-serif, 14–16px body, prefers-color-scheme. Open in the integrated browser.
```

Gdy agent skończy, zagraj kilka pytań i upewnij się, że:

- pasek postępu się przesuwa.
- wynik się aktualizuje.
- poprawne odpowiedzi pokazują stan zielony.
- błędne odpowiedzi używają czerwonej animacji wstrząsu.
- ekran wyników pojawia się po ostatnim pytaniu.

## Przejrzyj wygenerowany kod

Zwiń lewy pasek boczny i prawy panel przeglądarki, a następnie przejrzyj `index.html` w rozszerzonym obszarze kodu. Zwróć uwagę, jak HTML, CSS i JavaScript współdziałają w jednym pliku. Przywróć oba panele, gdy skończysz.

## Dopracuj z element pickerem

1. Wybierz element picker na pasku narzędzi przeglądarki.
2. Wybierz nagłówek quizu lub obszar odpowiedzi.
3. Wyślij poniższe polecenie:

   ```plaintext
   Make the selected element feel more like a mission-control display. Keep it accessible and preserve the existing light and dark themes.
   ```

4. Obserwuj odświeżenie zintegrowanej przeglądarki i sprawdź zmianę.

## Opcjonalne dopracowania

Jeśli chcesz dalej eksperymentować, poproś agenta, aby:

- dodał subtelne tło z polem gwiazd, które respektuje `prefers-reduced-motion`.
- uczynił ekran wyników bardziej celebracyjnym przy wyniku 8 lub wyższym.
- poprawił stany fokusu klawiatury, a następnie zweryfikował quiz bez myszy.

## Podsumowanie i kolejne kroki

Zbudowałeś, przejrzałeś i dopracowałeś Space Quiz. Przejdź do [Lekcji 3: Przejrzyj sesję i przetestuj quiz][next-lesson].

[next-lesson]: ../3-inspect-and-test/
