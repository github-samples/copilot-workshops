---
title: "Ćwiczenie 7 - Wznawianie i praca zdalna"
description: "Opuść sesję Copilot CLI i wróć do niej później poleceniem copilot --resume lub /resume, a opcjonalnie kontynuuj ją na GitHubie z /remote."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Sesje można wstrzymać bez utraty rozmowy ani kontekstu obszaru roboczego. Opuść sesję, wróć do niej później i opcjonalnie kontynuuj ją w miejscu, do którego dotrzesz z dowolnego urządzenia.

W tym ćwiczeniu:

- wyjdziesz z sesji i wznowisz ją z terminala.
- przełączysz się między sesjami bez opuszczania CLI.
- opcjonalnie kontynuujesz sesję zdalnie.

## Opuść sesję i wróć później

1. Wyjdź z bieżącej sesji Copilot CLI, gdy będziesz gotowy przełączyć się na inne zadanie.
2. Z terminala uruchom `copilot --resume`, aby wybrać poprzednią sesję.
3. Wewnątrz Copilot CLI użyj `/resume`, aby przełączać się między sesjami bez opuszczania CLI.
4. Upewnij się, że przywrócona sesja nadal ma oczekiwane pliki, kontekst zgłoszenia i model.

## Opcjonalnie: Kontynuuj sesję zdalnie

Załóżmy, że jesteś głęboko w jednej z tych sesji i chcesz kontynuować po zamknięciu laptopa. Uruchom `/remote`, aby kontynuować *tę samą sesję* na GitHubie, a następnie wybierz zwrócony link, aby otworzyć i przeglądać sesję w przeglądarce.

> [!NOTE]
> `/remote` to nie delegowanie i nie jest wymagane w tym warsztacie. Wypróbuj je, gdy lokalna pętla stanie się naturalna.

## Podsumowanie i kolejne kroki

Potrafisz wstrzymywać, wznawiać i kontynuować sesje tam, gdzie pracujesz. Przejdź do [ćwiczenia 8: Tworzenie, przegląd i scalanie z CLI][next-lesson].

[next-lesson]: ../8-pull-request/
