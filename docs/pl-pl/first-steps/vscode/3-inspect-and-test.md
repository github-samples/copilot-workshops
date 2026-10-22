---
title: "Lekcja 3 - Sprawdź kontekst i przetestuj"
description: "Sprawdź kontekst dołączony do żądania Copilot Chat, a następnie uruchom smoke test na poziomie przeglądarki, zanim Git cokolwiek zapisze."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Zanim cokolwiek opublikujesz, sprawdź, co Copilot widzi, i upewnij się, że quiz działa.

W tej lekcji:

- przejrzysz kontekst dołączony do żądania w czacie.
- uruchomisz smoke test na poziomie przeglądarki.
- naprawisz błędy, zanim przejdziesz do Gita.

## Sprawdź kontekst w prawym dolnym rogu

VS Code pokazuje aktywny kontekst w prawym dolnym rogu pola wprowadzania Copilot Chat.

1. Otwórz wskaźnik kontekstu w **prawym dolnym rogu** pola czatu.
2. Przejrzyj pliki, instrukcje niestandardowe i symbole dołączone do żądania.
3. Usuń nieistotny kontekst albo dołącz plik quizu, zanim przejdziesz dalej.

## Zbuduj i przetestuj, zanim Git coś zapisze

Użyj zintegrowanej przeglądarki i polecenia smoke testu, zanim zainicjalizujesz repozytorium lub cokolwiek scommitujesz:

```plaintext
Run a browser-level smoke test for the quiz. Check keyboard navigation, score updates, correct and incorrect feedback, and the results screen. Fix any failures, then report what passed.
```

1. Uruchom smoke test i sprawdź zintegrowaną przeglądarkę.
2. Napraw błędy i powtarzaj test, aż wszystko przejdzie.
3. Dopiero gdy budowa i test przejdą, przejdź do Gita.

## Podsumowanie i kolejne kroki

Potwierdziłeś, co Copilot widzi, i przetestowałeś quiz przed publikacją. Przejdź do [Lekcji 4: Opublikuj projekt][next-lesson].

[next-lesson]: ../4-publish/
