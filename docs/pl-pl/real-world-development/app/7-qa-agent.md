---
title: "Lekcja 7 - Tworzenie i użycie agenta QA"
description: "Utwórz profil QA wychodzący od wymagań, łączący pokrycie testami, skill quality-checks i bezpośrednie dowody z przeglądarki."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-17
---

Użyłeś skillu `quality-checks` do uruchamiania automatycznych sprawdzeń oraz Playwright MCP do obserwacji filtrowania w przeglądarce. Teraz połączysz te możliwości w agencie niestandardowym z jasno zdefiniowanym procesem QA.

W tej lekcji:

- poznasz, jak agent niestandardowy współpracuje z instrukcjami, skillami i narzędziami MCP.
- utworzysz i przejrzysz wielokrotnego użytku profil zapewnienia jakości (QA).
- wybierzesz agenta QA i przejrzysz jego ustalenia względem zgłoszenia o filtrowaniu.

## Scenariusz

Tailspin Toys chce spójnego przeglądu wymagań, jakości kodu, automatycznych sprawdzeń, pokrycia testami i zachowania w przeglądarce przed otwarciem pull requesta (PR). Agent niestandardowy może koordynować ten proces QA i dostarczać wielokrotnego użytku raport.

## Czym jest agent niestandardowy?

Agent niestandardowy to wyspecjalizowana wersja Copilota zdefiniowana w profilu Markdown. Profil opisuje cel agenta, instrukcje i dostępne narzędzia. W tym warsztacie zdefiniujesz rolę QA w `.github/agents/qa.agent.md` i wybierzesz ją w aplikacji.

Używane przez Ciebie personalizacje mają różne zadania. Instrukcje repozytorium opisują standardy zespołu. Skill `quality-checks` pakuje powtarzalne sprawdzenia. Playwright MCP dostarcza narzędzia przeglądarki. Profil QA mówi Copilotowi, jak używać tych możliwości do oceny wymagań i raportowania wyników. Nie zastępuje ich ani nie wymaga kolejnej sesji.

## Utwórz profil QA

Zanim otworzysz PR funkcji, poprosisz Copilota o utworzenie wielokrotnego użytku profilu QA. Profil zdefiniuje zarówno sprawdzenia wykonywane przez QA, jak i granice, których musi przestrzegać.

1. Upewnij się, że sesja jest w trybie **Interactive**.
2. Wyślij poniższe polecenie do Copilota, by utworzyć nowego agenta niestandardowego:

    ```plaintext
    Create a custom agent named QA in .github/agents/qa.agent.md. It should check features against their issues and agreed requirements, follow the repository instructions, run the quality-checks skill, use Playwright MCP to verify behavior, and add tests when coverage is missing.

    Have it report each requirement as pass, fail, or blocked with supporting evidence. It must ask before changing implementation code, and it must not commit changes or open pull requests. Use the current model and available tools. Just create the profile for now so I can review it.
    ```

## Przejrzyj profil

Zanim użyjesz nowego agenta, przejrzyj jego profil i upewnij się, że Copilot uchwycił zamierzony przepływ QA oraz granice uprawnień. Dzięki temu niepełny lub zbyt szeroki agent nie zmieni funkcji, gdy chcesz ją tylko zweryfikować.

1. Otwórz **Changes** i wybierz `.github/agents/qa.agent.md`.
2. Przeczytaj frontmatter. Pole `description` jest wymagane; `name` jest opcjonalne, ale jego podanie daje agentowi czytelną nazwę wyświetlaną.
3. Przeczytaj instrukcje profilu i upewnij się, że QA zaczyna od wymagań, stosuje instrukcje repozytorium, uruchamia skill `quality-checks` i używa Playwright MCP.
4. Upewnij się, że QA raportuje dowody, pyta przed zmianą kodu implementacji oraz nie tworzy commitów ani nie otwiera pull requestów.
5. Jeśli wygenerowany profil pomija którąkolwiek z tych odpowiedzialności lub granic, poproś ogólnego agenta Copilot o poprawki, zanim przejdziesz dalej.

## Uruchom QA względem zgłoszenia

Po przejrzeniu profilu wybierz QA w bieżącej sesji, żeby mógł skorzystać ze zgłoszenia o filtrowaniu i decyzji z planowania już obecnych w kontekście. Przed wysłaniem polecenia uruchomienia upewnij się, który agent jest aktywny.

1. W bieżącej sesji otwórz selektor agenta w polu monitu.
2. Wybierz **QA** i sprawdź, że aplikacja wyraźnie wskazuje **QA** jako aktywnego agenta, zanim wyślesz polecenie uruchomienia.
3. Wyślij poniższe polecenie, by poprosić QA o przegląd funkcji:

    ```plaintext
    Review the filtering feature against the issue and the decisions in our plan. Is it ready for a PR?
    ```

4. Upewnij się, że QA korzysta z właściwego zgłoszenia i decyzji z planowania. Podaj URL zgłoszenia lub brakujący kontekst, jeśli o to poprosi.
5. Przeczytaj raport, gdy skończy pracę!

## Podsumowanie i kolejne kroki

Dodałeś do przepływu pracy wielokrotnego użytku rolę specjalisty i przejrzałeś jej pracę. W tej lekcji:

- poznałeś, jak agent niestandardowy współpracuje z instrukcjami, skillami i narzędziami MCP.
- utworzyłeś i przejrzałeś wielokrotnego użytku profil QA wychodzący od wymagań.
- wybrałeś agenta QA i przejrzałeś jego ustalenia względem zgłoszenia o filtrowaniu.

Masz już implementację, aktualizację skillu, profil QA, testy i raport weryfikacji gotowe do przeglądu. Następnie [zbierzesz je w PR funkcji i użyjesz Agent Merge][next-lesson].

## Zasoby

- [Customizing the GitHub Copilot app, including selecting custom agents][customize-app]

[next-lesson]: ../8-create-pull-request/
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
