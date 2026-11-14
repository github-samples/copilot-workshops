---
title: "Lekcja 9 - Zautomatyzuj triage zgłoszeń"
description: "Utwórz i uruchom cotygodniową automatyzację, która podsumowuje niedawne otwarte zgłoszenia."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Użyj automatyzacji, aby zamienić powtarzalne zadanie triage zgłoszeń w zaplanowany przepływ pracy agenta.

W tej lekcji:

- utworzysz cotygodniową automatyzację.
- połączysz automatyzację z projektem Space Quiz.
- uruchomisz automatyzację od razu i przejrzysz jej wynik.

## Utwórz automatyzację

![Ilustracja widoku Automations w aplikacji Copilot z filtrami All, Local i Cloud, polem wyszukiwania, przyciskami Templates i New automation oraz dwiema kartami cotygodniowych automatyzacji dla projektu space-quiz: Issue triage i Accessibility audit.](../../../_images/first-steps-app-automations.svg)

Automatyzacje uruchamiają to samo polecenie według harmonogramu, każda we własnej sesji, więc automatyzacja nigdy nie zakłóca Twojej pracy. Możesz filtrować według **All**, **Local** lub **Cloud** i uruchamiać dowolną automatyzację na żądanie.

1. Otwórz **Automations**.
2. Wybierz szablon nowej cotygodniowej automatyzacji.
3. Wpisz poniższe polecenie:

   ```plaintext
   Review the latest GitHub issues created and still open in the last week, and provide a summary table ranked by severity and priority.
   ```

4. Ustaw tryb sesji na **Autopilot**.
5. Ustaw model na **Auto**.
6. Wybierz projekt `space-quiz`.
7. Otwórz listę rozwijaną **Create**, a następnie wybierz **Create and run**.

Przejrzyj wygenerowane podsumowanie i upewnij się, że odwołuje się do niedawnych otwartych zgłoszeń w Twoim repozytorium.

## Podsumowanie i kolejne kroki

Utworzyłeś wielokrotnego użytku przepływ pracy agenta, który działa według harmonogramu. Przejdź do [Lekcji 10: Kontynuuj sesję zdalnie][next-lesson].

[next-lesson]: ../10-remote/
