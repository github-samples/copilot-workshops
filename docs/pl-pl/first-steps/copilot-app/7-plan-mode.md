---
title: "Lekcja 7 - Zaplanuj przed edycją"
description: "Użyj trybu Plan przy drugim zgłoszeniu, aby agent zbadał projekt i zaproponował podejście, zanim zmieni jakiekolwiek pliki."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Nie każde zgłoszenie powinno zaczynać się od edycji. Tryb Plan bada projekt, proponuje podejście i czeka na Twoją zgodę, zanim pojawią się jakiekolwiek zmiany w kodzie.

W tej lekcji:

- uruchomisz sesję dla drugiego zgłoszenia w trybie Plan.
- przejrzysz i dopracujesz plan zaproponowany przez agenta.
- zatwierdzisz plan i wybierzesz, jak sesja ma dalej działać.

## Uzgodnij podejście przed zmianami w kodzie

1. Otwórz **drugie zgłoszenie** z **My work** i wybierz **New session**.
2. W konfiguracji sesji wybierz **Plan** zamiast **Interactive** lub **Autopilot**.
3. Wyślij poniższe polecenie i pozwól agentowi zbadać projekt bez zmiany plików:

   ```plaintext
   Plan how to implement this issue. Investigate the existing quiz, list the files you would change, call out risks to accessibility and the single-file constraint, and stop before making any edits.
   ```

4. Przeczytaj zaproponowany plan i poproś o zmiany, jeśli czegoś brakuje.
5. Zatwierdź plan.
6. Gdy zostaniesz o to poproszony, wybierz, czy sesja ma kontynuować w trybie **Interactive**, czy **Autopilot**.

> [!TIP]
> **Kiedy tryb Plan się opłaca**
>
> Używaj trybu Plan przy wszystkim, co jest niejednoznaczne, przecina wiele obszarów albo jest kosztowne do cofnięcia. Najtańsze miejsce na poprawienie złego podejścia to moment przed pierwszą edycją.

## Podsumowanie i kolejne kroki

Uzgodniłeś podejście z agentem, zanim ten napisał jakikolwiek kod. Przejdź do [Lekcji 8: Dokończ pętlę przeglądu Copilot][next-lesson].

[next-lesson]: ../8-review-loop/
