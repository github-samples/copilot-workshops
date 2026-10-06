---
title: "Lekcja 5 - Dostosowanie i użycie skillu quality-checks"
description: "Poznaj istniejący skill quality-checks, dostosuj format jego raportu i użyj go do walidacji filtrowania."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-29
---

Pisanie kodu to coś więcej niż samo pisanie kodu. Udało nam się ręcznie zweryfikować, że kod działa, i użyliśmy plików instrukcji, by zapewnić zgodność ze standardami. A co z testami? Lintingiem? Wszystkimi innymi częściami ciągłej integracji (CI)?

Do takich zadań najlepiej pasują **skille agenta (agent skills)**! Skille pomagają Copilotowi zrozumieć, jak prawidłowo uruchamiać tego typu operacje.

Podczas tej lekcji:

- poznasz istniejący skill `quality-checks`.
- dostosujesz format jego wyników.
- uruchomisz skill i przejrzysz jego wynik.

## Scenariusz

Tailspin Toys używa skillu `quality-checks` do testów jednostkowych, lintu i sprawdzeń typów. Zespół chce ulepszyć raport, aby wyniki były łatwiejsze do odczytania.

## Instrukcje, skrypty i zasoby

Skille agenta pakują wielokrotnego użytku instrukcje zadań, wykonywalne skrypty i zasoby pomocnicze, które agent ładuje na żądanie. W istocie to folder o nazwie skillu z plikiem markdown o nazwie `SKILL.md`. Markdown zawiera frontmatter z nazwą i opisem, które definiują, czym jest skill, przegląd tego, co robi, oraz wskazówki, kiedy należy go wywołać. Folder może też zawierać podfoldery ze skryptami i innymi zasobami używanymi przez skill przy wywołaniu.

> [!NOTE]
> Dodatkowe foldery i pliki nie są wymagane dla skillu! W naszym przykładzie skill będzie uruchamiał polecenia `npm`, by uruchomić testy i lintery. Dlatego nie potrzebujemy dodatkowych plików pomocniczych.

Skille mogą znajdować się w folderze `.github/skills` projektu, by stać się zasobem repozytorium współdzielonym i wielokrotnie używanym przez zespół, albo w folderze głównym Copilota, zwykle `~/.copilot/skills`.

## Zbadaj skill

Zbadajmy skill, który zespół Tailspin Toys utworzył do uruchamiania testów jednostkowych, lintu i sprawdzeń typów — o nazwie `quality-checks`.

1. Jeśli nie masz jeszcze otwartej kanwy **Files**, w panelu przeglądu wybierz **+**, a następnie **File**
2. Wyszukaj `.github/skills/quality-checks/SKILL.md`.
3. Przeczytaj `name` i `description` na górze. Zwróć uwagę na opis, który pomaga Copilotowi zrozumieć, kiedy wywołać skill.
4. Przeczytaj instrukcje i zwróć uwagę, jak prowadzą Copilota przez proces testowania i lintingu.

## Uruchom skill przed wprowadzeniem zmiany

Skille można wywoływać bezpośrednio poleceniem slash (`/`) albo językiem naturalnym. Poprośmy Copilota o uruchomienie trzech sprawdzeń skillu.

1. Upewnij się, że Copilot jest w trybie **Interactive**, wybierając go z listy rozwijanej trybu.
2. Użyj poniższego polecenia, aby wywołać skill:

    ```plaintext
    Run the quality-checks skill for unit tests, lint, and type checks.
    ```

3. Zwróć uwagę na raport na końcu.

## Dostosuj raport

OK, chcemy lepszego raportu, który powie, co zostało uruchomione, czy zakończyło się sukcesem i co faktycznie zgłosiły narzędzia. Zaktualizujmy skill, aby taki raport tworzył!

1. Wróć do kanwy **Files**.
2. Jeśli nie jest jeszcze otwarty, otwórz `.github/skills/quality-checks/SKILL.md`.
3. Dodaj poniższą sekcję na końcu pliku:

    ```markdown
    ## Results output formatting

    Upon completion, report each command that ran and whether it passed, failed, or was blocked. Include test counts, durations, errors, warnings, and other metrics only when the tool reports them. Identify the next action for any failure or blocker, and never describe a skipped or incomplete check as passed.
    ```

Plik zostanie automatycznie zapisany.

## Uruchom zaktualizowany skill

Gdy zmiana jest gotowa, zobaczmy ją w działaniu! Użyjemy dokładnie tego samego polecenia co wcześniej.

1. Upewnij się, że Copilot jest w trybie **Interactive**, wybierając go z listy rozwijanej trybu.
2. Użyj poniższego polecenia, aby wywołać skill:

    ```plaintext
    Run the quality-checks skill for unit tests, lint, and type checks.
    ```

3. Zwróć uwagę na raport na końcu.

## Podsumowanie i kolejne kroki

Dostosowałeś i użyłeś istniejącego skillu agenta. Podczas tej lekcji:

- zbadałeś skill `quality-checks` do testów jednostkowych, lintu i sprawdzeń typów.
- dostosowałeś format jego wyników.
- uruchomiłeś skill i przejrzałeś jego wynik.

Ta zmiana towarzyszy filtrowaniu w PR funkcji. Następnie pozwolisz Copilotowi wchodzić w interakcję z witryną bezpośrednio [przez serwer Playwright MCP][next-lesson].

## Więcej przykładów skilli

Te przykłady społecznościowe to odniesienia, a nie dodatkowe zadania. Przed przyjęciem przejrzyj ich wymagania wstępne i zachowanie:

- [Specyfikacja Agent Skills][skill-spec].
- [Przepływ wkładu: `make-repo-contribution`][contribution-example].
- [Dokumenty wymagań: `prd`][prd-example].
- [Diagramy i dołączony skrypt eksportu: `drawio`][drawio-example].
- [Testowanie w przeglądarce: `webapp-testing`][browser-example].

Przykład wkładu upstream nazywa się `make-repo-contribution`; starsze szablony Tailspin używały innej nazwy, `make-contribution`. Ten warsztat nie zależy od żadnego z tych skilli wkładu.

[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
