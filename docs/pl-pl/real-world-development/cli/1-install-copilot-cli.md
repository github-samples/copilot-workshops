---
title: "Ćwiczenie 1 - Instalacja GitHub Copilot CLI"
description: "Zainstaluj i uwierzytelnij Copilot CLI w Codespace, zapoznaj się z narzędziem i znajdź przygotowane zgłoszenie o filtrowaniu."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-18
---

[GitHub Copilot CLI][about-copilot-cli] to potężny asystent programowania oparty na agentach, działający w terminalu. Pozwala eksplorować bazy kodu, generować kod, uruchamiać polecenia i korzystać z zewnętrznych narzędzi — wszystko z linii poleceń. Możesz zlecać zadania, prosić o zmiany i pozostawać w flow. Pierwszy krok, jak można się spodziewać, to instalacja narzędzia! Na szczęście da się to zrobić za pomocą narzędzi, które już znasz.

W tym ćwiczeniu:

- zainstalujesz GitHub Copilot CLI za pomocą npm.
- uwierzytelnisz się kontem GitHuba.
- zaufasz repozytorium warsztatowemu i przeprowadzisz krótką rozmowę.
- znajdziesz zgłoszenie o filtrowaniu przez wbudowany serwer GitHub MCP.

## Scenariusz

Twój zespół zaczyna używać agentów AI do pracy nad rosnącym backlogiem. Copilot CLI przenosi tę możliwość do terminala, w którym wielu deweloperów i tak spędza czas. To ćwiczenie doprowadzi Cię do instalacji, uwierzytelnienia i gotowości do korzystania z narzędzia w dalszej części warsztatu.

## Zainstaluj Copilot CLI

Copilot CLI możesz zainstalować przez [npm][install-cli], WinGet i Homebrew. Ponieważ GitHub Codespaces mają wstępnie zainstalowany Node.js, użyjesz npm.

1. Wróć do Codespace i otwórz terminal.
2. Sprawdź, czy Node.js jest zainstalowany i spełnia wymaganie wersji:

   ```bash
   node --version
   ```

   Powinieneś zobaczyć wersję 24 lub nowszą.

3. Zainstaluj Copilot CLI globalnie:

   ```bash
   npm install -g @github/copilot
   ```

4. Zweryfikuj instalację:

   ```bash
   copilot --version
   ```

   Powinieneś zobaczyć numer wersji.

## Uwierzytelnij się w GitHubie

Przy pierwszym uruchomieniu Copilot CLI poprosi Cię o uwierzytelnienie kontem GitHuba.

1. Uruchom Copilot CLI:

   ```bash
   copilot
   ```

2. Jeśli zostaniesz o to poproszony, postępuj zgodnie z instrukcjami kodu urządzenia, aby uwierzytelnić i autoryzować Copilot CLI.
3. Copilot CLI wyświetli następujący komunikat:

   ```plaintext
   Copilot can read files in this folder and, with your permission, edit them or run code and shell commands. It will remember your permissions for the rest of this session.

   Do you trust the files in this folder?
   ```

4. Upewnij się, że ścieżka wskazuje Twoje repozytorium Tailspin Toys, a następnie potwierdź, wybierając **Yes, and remember this folder for future sessions**.

> [!NOTE]
> W Codespace możesz być już uwierzytelniony przez sesję GitHuba. Jeśli Copilot CLI uruchomi się bez prośby o uwierzytelnienie, wszystko jest w porządku!

## Zapoznaj się z narzędziem

Polecenia w zwykłym prompcie powłoki uruchamiają się bezpośrednio w Codespace. Po starcie Copilot CLI język naturalny trafia do agenta, a polecenia slash sterują rozmową.

1. Wpisz `/model`, klawiszami strzałek wybierz **Auto**, wciśnij <kbd>Enter</kbd>, a następnie ponownie <kbd>Enter</kbd>, aby potwierdzić.
2. Wpisz `/help`, aby zobaczyć polecenia dostępne w zainstalowanej wersji, a następnie wciśnij <kbd>Esc</kbd>, aby zamknąć ekran pomocy.
3. Zadaj Copilotowi proste pytanie, aby sprawdzić, czy wszystko działa:

   ```plaintext
   What are the key files in this project?
   ```

4. Przeczytaj odpowiedź i zwróć uwagę, jak Copilot eksploruje repozytorium przed udzieleniem odpowiedzi.
5. Wpisz `/mcp list` i upewnij się, że wbudowany serwer GitHub MCP jest dostępny.
6. Poproś Copilota o znalezienie zgłoszenia o filtrowaniu:

   ```plaintext
   Using GitHub MCP, find the issue in this repository titled "Allow users to filter games by category and publisher." Give me its URL and a short summary. Don't change anything.
   ```

7. Otwórz URL i przeczytaj zgłoszenie. Użyjesz go po wykonaniu szybkiej pierwszej zmiany.

> [!TIP]
> Zwykła sesja Copilot CLI działa na gałęzi aktualnie aktywnej w terminalu; nie tworzy automatycznie worktree. Przed każdą zmianą utworzysz gałąź funkcji.

## Użyj skrótu warsztatowego

Copilot CLI zwykle pyta przed użyciem narzędzi poza ustalonymi uprawnieniami. W tym warsztacie uruchomisz go ponownie z `--yolo` — zatwierdzonym przez użytkownika skrótem, który usuwa te prośby o zatwierdzenie w Codespace, żebyś mógł skupić się na ćwiczeniach.

> [!CAUTION]
> `--yolo` włącza pełne automatyczne uprawnienia (`--allow-all-tools`, `--allow-all-paths` i `--allow-all-urls`). Używaj go tylko w izolowanym środowisku, takim jak Codespace lub maszyna wirtualna, i nigdy nie ustawiaj go jako domyślnego aliasu w codziennej pracy. Szczegóły znajdziesz w [Allowing and denying tool use][allow-all-warning].

W tym warsztacie `--enable-all-github-mcp-tools` włącza narzędzia GitHub MCP do odczytu i zapisu, których późniejsze ćwiczenia używają do pracy ze zgłoszeniami i pull requestami. Codespace ogranicza dostęp do lokalnego komputera, ale uwierzytelnione zasoby GitHuba pozostają rzeczywiste. Przeglądaj zmiany przed ich opublikowaniem lub scaleniem.

1. Wyjdź z Copilot CLI poleceniem `/exit`.
2. Uruchom go ponownie z katalogu głównego repozytorium:

   ```bash
   copilot --yolo --enable-all-github-mcp-tools
   ```

3. Zadaj kolejne krótkie pytanie o projekt, aby potwierdzić, że rozmowa działa, a następnie wyjdź poleceniem `/exit`.

Copilot zapisuje rozmowy automatycznie. Później, po zmianie instrukcji lub dodaniu agenta, użyjesz `copilot --resume`, aby wrócić do tej samej rozmowy o funkcji i tej samej gałęzi.

## Podsumowanie i kolejne kroki

Gratulacje! W tym ćwiczeniu:

- zainstalowałeś GitHub Copilot CLI za pomocą npm.
- uwierzytelniłeś się kontem GitHuba.
- zaufałeś repozytorium warsztatowemu i przeprowadziłeś krótką rozmowę.
- znalazłeś zgłoszenie o filtrowaniu przez wbudowany serwer GitHub MCP.

Następnie [rozpoczniesz pierwszą skoncentrowaną zmianę][next-lesson] i użyjesz Copilot CLI, aby wyświetlić ocenę gwiazdkową na kartach gier.

## Zasoby

- [Install GitHub Copilot CLI][install-cli]
- [About GitHub Copilot CLI][about-copilot-cli]
- [Copilot CLI command reference][cli-reference]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[install-cli]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[allow-all-warning]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli#allowing-and-denying-tool-use
