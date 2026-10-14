---
title: "Lekcja 6 - Praca ze zgłoszeniami i sesjami"
description: "Utwórz skupiony backlog, wybierz zgłoszenie, zaimplementuj je w izolowanym worktree i samodzielnie przejrzyj diff."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Poproś agenta o propozycje skupionych ulepszeń produktu, zamień te pomysły w zgłoszenia GitHub i zaimplementuj jedno zgłoszenie w izolowanej sesji.

W tej lekcji:

- utworzysz trzy skupione zgłoszenia dla Space Quiz.
- przejrzysz zgłoszenia w **My work**.
- uruchomisz sesję na podstawie zgłoszenia w nowym worktree.
- przejrzysz diff w zakładce **Changes** i zweryfikujesz funkcję.

## Zbuduj backlog w My work

Wyślij poniższe polecenie:

```plaintext
Review the space quiz and suggest three focused feature ideas that could each be completed in a short session. Create a separate GitHub issue for each idea with a clear title, user-focused description, and acceptance criteria. Do not implement them yet.
```

Otwórz **My work**, przejrzyj trzy zgłoszenia i wybierz jedno, które ma jasną wartość i zarządzalny zakres.

![Ilustracja widoku My work w aplikacji Copilot. Pasek boczny zawiera New, My work, Automations, Customize oraz projekt space-quiz. Główny obszar ma filtry All, Active, Review requests i Done nad listą pull requestów.](../../../_images/first-steps-app-my-work.svg)

**My work** wciąga do aplikacji Twoje zgłoszenia i pull requesty z GitHuba, z filtrami **All**, **Active**, **Review requests** i **Done**.

## Zaimplementuj zgłoszenie

1. Otwórz wybrane zgłoszenie w **My work**.
2. Wybierz **New session**.
3. Gdy zostaniesz o to poproszony, wybierz **new worktree**.
4. Użyj trybu **Interactive** i preferowanego modelu.
5. Wyślij poniższe polecenie:

   ```plaintext
   Implement this issue completely. Keep the single-file, dependency-free design, test the behavior in the integrated browser, and summarize the changes when finished.
   ```

Nowy worktree utrzymuje tę funkcję w izolacji od domyślnej gałęzi, dopóki nie będziesz gotowy do przeglądu i scalenia.

## Samodzielnie przejrzyj diff

Gdy agent się zgłosi, nie bierz jego słów za pewnik.

1. Otwórz wysuwany panel po prawej i wybierz zakładkę **Changes**.
2. Przeczytaj diff każdego pliku, którego sesja dotknęła.
3. Przetestuj funkcję w zintegrowanej przeglądarce i upewnij się, że spełnia kryteria akceptacji zgłoszenia.

![Ilustracja sesji w aplikacji Copilot z otwartą zakładką Changes w prawym wysuwanym panelu. Pokazuje jeden zmieniony plik, index.html, z 142 dodanymi i 8 usuniętymi wierszami oraz wbudowane linie diff obok rozmowy w sesji.](../../../_images/first-steps-app-changes-tab.svg)

Zakładka **Changes** wymienia każdy plik, którego sesja dotknęła, z diffem wbudowanym w widok.

## Podsumowanie i kolejne kroki

Utworzyłeś backlog, zaimplementowałeś jedno zgłoszenie w izolowanej sesji i przejrzałeś diff. Przejdź do [Lekcji 7: Zaplanuj przed edycją][next-lesson].

[next-lesson]: ../7-plan-mode/
