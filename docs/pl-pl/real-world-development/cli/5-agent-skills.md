---
title: "Ćwiczenie 5 - Dostosuj i użyj skillu quality-checks"
description: "Poznaj istniejący skill quality-checks, dostosuj format raportu i użyj go do walidacji filtrowania."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-29
---

Pisanie kodu to coś więcej niż samo pisanie kodu. Zweryfikowaliśmy już działanie kodu ręcznie i użyliśmy plików instrukcji, aby zapewnić zgodność ze standardami. A co z testowaniem? Lintowaniem? Pozostałymi elementami ciągłej integracji (CI)?

Do tego typu zadań najlepiej pasują **skille agenta (agent skills)**! Skille pomagają Copilotowi zrozumieć, jak poprawnie wykonywać takie operacje.

W tym ćwiczeniu:

- przejrzysz istniejący skill `quality-checks`.
- dostosujesz format jego wyników.
- przeładujesz i uruchomisz skill.

## Scenariusz

Tailspin Toys używa skillu `quality-checks` do testów jednostkowych, lintu i sprawdzania typów. Zespół chce ulepszyć raport, żeby wyniki były łatwiejsze do odczytania.

## Instrukcje, skrypty i zasoby

Skille agenta pakują wielokrotnego użytku instrukcje zadań, wykonywalne skrypty i zasoby pomocnicze, które agent wczytuje na żądanie. W istocie to folder o nazwie skillu z plikiem Markdown o nazwie `SKILL.md`. Markdown zawiera frontmatter z nazwą i opisem definiującymi, czym jest skill, przegląd tego, co robi, oraz wskazówki, kiedy powinien zostać wywołany. Folder może też zawierać podfoldery ze skryptami i innymi zasobami używanymi przez skill przy wywołaniu.

> [!NOTE]
> Dodatkowe foldery i pliki nie są wymagane dla skillu. Skill `quality-checks` w Tailspin Toys zawiera tylko `SKILL.md`, ponieważ korzysta z istniejących poleceń projektu.

Skille mogą znajdować się w folderze `.github/skills` projektu, aby stać się zasobem repozytorium współdzielonym i wielokrotnie używanym przez zespół, albo w folderze skilli użytkownika pod `~/.copilot/skills`.

## Przejrzyj skill

Przejrzyjmy skill utworzony przez zespół Tailspin Toys do uruchamiania testów jednostkowych, lintu i sprawdzania typów, o nazwie `quality-checks`.

1. Wróć do Codespace. W edytorze Codespaces otwórz `.github/skills/quality-checks/SKILL.md`.
2. Przeczytaj `name` i `description` na górze. Opis pomaga Copilotowi zrozumieć, kiedy wywołać skill.
3. Przeczytaj instrukcje i zwróć uwagę, jak prowadzą Copilota przez proces testowania i lintowania.
4. Zwróć uwagę, że skill nie zawiera jeszcze sekcji **Results output formatting**.

## Uruchom skill przed wprowadzeniem zmiany

Skille można wywoływać bezpośrednio przez Copilot CLI albo językiem naturalnym. Poprośmy Copilota o uruchomienie trzech sprawdzeń skillu.

1. Wróć do rozmowy o filtrowaniu w trybie Interactive.
2. Użyj poniższego polecenia:

   ```plaintext
   Run the quality-checks skill for unit tests, lint, and type checks.
   ```

3. Zwróć uwagę na raport na końcu.

## Dostosuj raport

OK, chcemy lepszego raportu, który powie, co zostało uruchomione, czy się powiodło i co faktycznie zgłosiły narzędzia. Zaktualizujmy skill, żeby tworzył taki raport!

1. Wróć do `.github/skills/quality-checks/SKILL.md`.
2. Dodaj poniższą sekcję na końcu pliku:

   ```markdown
   ## Results output formatting

   Upon completion, report each command that ran and whether it passed, failed, or was blocked. Include test counts, durations, errors, warnings, and other metrics only when the tool reports them. Identify the next action for any failure or blocker, and never describe a skipped or incomplete check as passed.
   ```

3. Plik zostanie zapisany automatycznie.

## Uruchom zaktualizowany skill

Po wprowadzeniu zmiany zobaczmy ją w działaniu! Copilot CLI może przeładować edytowane skille bez restartowania rozmowy.

1. Wpisz:

   ```plaintext
   /skills reload
   ```

2. Użyj dokładnie tego samego polecenia co wcześniej:

   ```plaintext
   Run the quality-checks skill for unit tests, lint, and type checks.
   ```

3. Zwróć uwagę na raport na końcu i porównaj go z pierwszym raportem.

## Podsumowanie i kolejne kroki

Dostosowałeś i użyłeś istniejącego skillu agenta. W tym ćwiczeniu:

- przejrzałeś skill `quality-checks` do testów jednostkowych, lintu i sprawdzania typów.
- dostosowałeś format jego wyników.
- przeładowałeś i uruchomiłeś skill.

Ta zmiana towarzyszy filtrowaniu w PR funkcji. Następnie pozwolisz Copilotowi wchodzić w interakcję z witryną bezpośrednio [przez serwer Playwright MCP][next-lesson].

## Więcej przykładów skilli

Te przykłady społecznościowe to materiały referencyjne, a nie dodatkowe zadania:

- [Agent Skills specification][skill-spec]
- [Contribution workflow: `make-repo-contribution`][contribution-example]
- [Requirements documents: `prd`][prd-example]
- [Diagrams and a bundled export script: `drawio`][drawio-example]
- [Browser testing: `webapp-testing`][browser-example]

[previous-lesson]: ../4-custom-instructions/
[next-lesson]: ../6-mcp-playwright/
[skill-spec]: https://agentskills.io/specification
[contribution-example]: https://github.com/github/awesome-copilot/tree/main/skills/make-repo-contribution
[prd-example]: https://github.com/github/awesome-copilot/tree/main/skills/prd
[drawio-example]: https://github.com/github/awesome-copilot/tree/main/skills/drawio
[browser-example]: https://github.com/github/awesome-copilot/tree/main/skills/webapp-testing
