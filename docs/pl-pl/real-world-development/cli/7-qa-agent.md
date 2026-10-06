---
title: "Ćwiczenie 7 - Tworzenie i użycie agenta QA"
description: "Utwórz agenta niestandardowego QA, który łączy wymagania ze zgłoszenia, skill quality-checks i Playwright MCP."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-18
---

Użyłeś skillu `quality-checks` do uruchamiania automatycznych sprawdzeń oraz Playwright MCP do obserwacji filtrowania w przeglądarce. Teraz połączysz te możliwości w agencie niestandardowym z jasno zdefiniowanym procesem QA.

W tym ćwiczeniu:

- poznasz, jak agent niestandardowy współpracuje z instrukcjami, skillami i narzędziami MCP.
- utworzysz i przejrzysz profil zapewnienia jakości wielokrotnego użytku.
- wybierzesz agenta QA i przejrzysz jego ustalenia względem zgłoszenia o filtrowaniu.

## Scenariusz

Tailspin Toys chce spójnego przeglądu wymagań, jakości kodu, automatycznych sprawdzeń, pokrycia testami i zachowania w przeglądarce przed otwarciem pull requesta (PR). Agent niestandardowy może koordynować ten proces QA i dostarczać raport wielokrotnego użytku.

## Czym jest agent niestandardowy?

Agent niestandardowy to wyspecjalizowana wersja Copilota zdefiniowana w profilu Markdown. Profil opisuje cel agenta, instrukcje i dostępne narzędzia. W tych warsztatach zdefiniujesz rolę QA w `.github/agents/qa.agent.md` i wybierzesz ją w Copilot CLI.

Używane wcześniej dostosowania mają różne zadania. Instrukcje repozytorium opisują standardy zespołu. Skill `quality-checks` pakuje powtarzalne sprawdzenia. Playwright MCP dostarcza narzędzia przeglądarki. Profil QA mówi Copilotowi, jak użyć tych możliwości do oceny wymagań i raportowania ustaleń. Nie zastępuje ich i nie wymaga osobnej rozmowy.

## Utwórz profil QA

Zanim otworzysz PR funkcji, poprosisz Copilota o utworzenie profilu QA wielokrotnego użytku. Profil zdefiniuje zarówno sprawdzenia wykonywane przez QA, jak i granice, których musi przestrzegać.

1. Wróć do Codespace i upewnij się, że rozmowa o filtrowaniu jest w trybie Interactive.
2. Poproś domyślnego agenta o utworzenie nowego agenta niestandardowego:

   ```plaintext
   Create a custom agent named QA in .github/agents/qa.agent.md. It should check features against their issues and agreed requirements, follow the repository instructions, run the quality-checks skill, use Playwright MCP to verify behavior, and add tests when coverage is missing.

   Have it report each requirement as pass, fail, or blocked with supporting evidence. It must ask before changing implementation code, and it must not commit changes or open pull requests.

   Just create the profile for now so I can review it.
   ```

## Przejrzyj profil

Zanim użyjesz nowego agenta, przejrzyj jego profil i upewnij się, że Copilot uchwycił zamierzony przepływ QA oraz jego granice. Zapobiega to sytuacji, w której niepełny lub zbyt szeroki agent zmienia funkcję, gdy chcesz ją tylko zweryfikować.

1. Wpisz `/diff` i otwórz `.github/agents/qa.agent.md`.
2. Przeczytaj frontmatter. Pole `description` jest wymagane; `name` jest opcjonalne, ale jego obecność daje agentowi czytelną nazwę wyświetlaną.
3. Przeczytaj instrukcje profilu i upewnij się, że QA zaczyna od wymagań, stosuje instrukcje repozytorium, uruchamia skill `quality-checks` i używa Playwright MCP.
4. Upewnij się, że QA raportuje dowody, pyta przed zmianą kodu implementacji oraz nie commituje zmian ani nie otwiera pull requestów.
5. Jeśli wygenerowany profil pomija któreś z tych obowiązków lub granic, poproś domyślnego agenta o poprawkę, zanim przejdziesz dalej.

## Uruchom QA względem zgłoszenia

Copilot CLI ładuje agentów projektu przy starcie rozmowy. Wznów tę samą rozmowę o filtrowaniu po utworzeniu profilu, a następnie wybierz QA, żeby mógł skorzystać ze zgłoszenia i decyzji planowania już obecnych w kontekście.

1. Włącz agenta poniższym poleceniem:

   ```plaintext
   /agent QA
   ```

> [!NOTE]
> Ponieważ właśnie utworzyłeś agenta, może nie pojawić się na liście dostępnych agentów. Jest tam — powyższe polecenie go aktywuje.

2. Użyj poniższego polecenia, by poprosić agenta QA o przegląd funkcji:

   ```plaintext
   Review the filtering feature against the issue and the decisions in our plan. Is it ready for a PR?
   ```

3. Agent QA zabiera się do pracy!
4. Przeczytaj raport, gdy skończy pracę!

## Podsumowanie i kolejne kroki

Dodałeś do przepływu rolę specjalisty wielokrotnego użytku i przejrzałeś jej pracę. W tym ćwiczeniu:

- poznałeś, jak agent niestandardowy współpracuje z instrukcjami, skillami i narzędziami MCP.
- utworzyłeś i przejrzałeś profil zapewnienia jakości wielokrotnego użytku.
- wybrałeś agenta QA i przejrzałeś jego ustalenia względem zgłoszenia o filtrowaniu.

Masz teraz implementację, aktualizację skillu, profil QA, testy i raport weryfikacji gotowe do przeglądu. Następnie [połączysz je w PR funkcji i użyjesz Agent Merge][next-lesson].

## Zasoby

- [Create custom agents for Copilot CLI][create-agents]
- [Custom agent configuration][agent-config]

[previous-lesson]: ../6-mcp-playwright/
[next-lesson]: ../8-create-pull-request/
[create-agents]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli
[agent-config]: https://docs.github.com/copilot/reference/custom-agents-configuration
