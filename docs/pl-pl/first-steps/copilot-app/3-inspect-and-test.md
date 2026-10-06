---
title: "Lekcja 3 - Przejrzyj sesję i przetestuj quiz"
description: "Przeczytaj szczegóły sesji, aby potwierdzić, nad czym pracuje agent, a następnie uruchom smoke test na poziomie przeglądarki, zanim Git cokolwiek zapisze."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Teraz, gdy sesja wykonała realną pracę, jest co sprawdzić. Potwierdź, na co skierowany jest agent, a potem pozwól mu przejść quiz w zintegrowanej przeglądarce i raportować to, co faktycznie się wydarzyło — a nie to, co zamierzał.

W tej lekcji:

- przeczytasz panel szczegółów sesji.
- sprawdzisz projekt, ścieżkę, gałąź, zmiany i zużycie kontekstu sesji.
- uruchomisz smoke test na poziomie przeglądarki i naprawisz ewentualne błędy.

## Przeczytaj szczegóły sesji

Szczegóły sesji mówią dokładnie, nad czym pracuje agent. Nie musisz stale patrzeć na ten panel, ale wszystko w nim ma znaczenie, gdy wynik Cię zaskoczy.

![Ilustracja panelu szczegółów sesji w aplikacji Copilot dla sesji budowania Space Quiz. Pokazuje gałąź main z origin/main, ścieżkę, projekt, nazwę sesji, identyfikator sesji i agenta, jeden zmieniony plik, liczby tokenów, zużycie kontekstu na poziomie 27 procent, wydatki sesji oraz opcje włączenia zdalnego sterowania, zmiany nazwy, podglądu insights, udostępnienia jako tajnego gista lub archiwizacji sesji.](../../../_images/first-steps-app-session-details.svg)

Panel pokazuje, gdzie odbywa się praca, co się zmieniło i jak pełne jest okno kontekstu. Nie ma wiersza modelu, bo model wybierasz przy każdym żądaniu w composerze.

1. Upewnij się, że **project**, **path** i **branch** to te, które zamierzasz edytować.
2. Przeczytaj **Changes**, aby sprawdzić, czy ta sesja już czegoś dotknęła.
3. Sprawdź **context usage**. Gdy rośnie, agent ma mniej miejsca na właściwe zadanie — to sygnał, by zacząć świeżą sesję.

> [!TIP]
> **Większość złych wyników to problemy z kontekstem**
>
> Zła gałąź, zły folder albo niemal pełne okno kontekstu tłumaczy znacznie więcej niespodzianek niż zły prompt.

## Testuj, zanim Git cokolwiek zapisze

Zintegrowana przeglądarka to prawdziwa przeglądarka, więc agent może sterować quizem i weryfikować jego zachowanie. Wyślij poniższe polecenie:

```plaintext
Run a browser-level smoke test for the quiz in the integrated browser. Check keyboard navigation, score updates, correct and incorrect feedback, and the results screen. Fix any failures, then report what passed.
```

1. Obserwuj zintegrowaną przeglądarkę, gdy agent przechodzi przez pytania.
2. Jeśli coś zawiedzie, pozwól agentowi to naprawić i ponownie uruchomić test, aż wszystko przejdzie.
3. Idź dalej dopiero wtedy, gdy budowa i test są zielone.

Do Gita jeszcze nic nie zapisano. Następny krok to `/init`, które czyta projekt w bieżącym stanie — warto najpierw upewnić się, że projekt działa.

## Podsumowanie i kolejne kroki

Potwierdziłeś, nad czym pracuje sesja, i zweryfikowałeś quiz smoke testem na poziomie przeglądarki. Przejdź do [Lekcji 4: Zapisz instrukcje projektu][next-lesson].

[next-lesson]: ../4-project-instructions/
