---
title: "Ćwiczenie 3 - Dodawanie nowych funkcji z GitHub Copilot CLI"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-10
---

Jak można się spodziewać, podstawowe zadania, które możesz wykonać za pomocą GitHub Copilot CLI, to dodawanie nowych funkcji i kodu do projektu. Weźmy jedno ze zgłoszeń z backlogu i poprośmy Copilota o pomoc w implementacji.

## Scenariusz

Nadszedł czas, aby dokończyć implementację filtrowania w projekcie. Masz już zgłoszenie o filtrowaniu w backlogu oraz fundament helpera z poprzedniego ćwiczenia. Niech Copilot pobierze szczegóły zgłoszenia, uwzględni istniejącą pracę i zbuduje pozostałą funkcjonalność.

Podczas tego ćwiczenia:

- użyjesz trybu planowania do wygenerowania planu implementacji filtrowania.
- wygenerujesz kod potrzebny do dodania filtrowania do witryny, wykorzystując Copilota.

Po zakończeniu tego ćwiczenia dodasz nową funkcjonalność do projektu.

## Użyj trybu planowania

Jednym z najlepszych zastosowań AI jest planowanie. Często masz dobrą koncepcję tego, co chcesz zbudować, ale chciałbyś z kimś przedyskutować swoje pomysły. Narzędzia AI pomagają skrystalizować myśli, zadając pytania uzupełniające i przechodząc przez pułapki lub brakujące elementy. Copilot CLI oferuje tryb planowania. Czas spędzony na planowaniu pomoże też Copilotowi wygenerować kod lepiej dopasowany do wymagań.

Zacznijmy tworzenie nowej funkcjonalności od trybu planowania w Copilot CLI.

1. Wróć do codespace. Jeśli go zamknąłeś, przejdź do repozytorium na GitHub.com, wybierz **Code** > **Codespaces**, a następnie ponownie otwórz istniejący codespace.
2. Wróć do otwartej sesji Copilot CLI. Jeśli terminal jest zamknięty lub wyszedłeś z Copilot CLI, otwórz terminal. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>\`</kbd>, a następnie uruchom go z katalogu głównego repozytorium poleceniem `copilot --yolo --enable-all-github-mcp-tools`. Zaufaj folderowi projektu, jeśli zostaniesz o to poproszony, potem uruchom `/models` i wybierz **Auto**.
3. Użyj poniższego polecenia w Copilot CLI, aby utworzyć plan na podstawie zgłoszenia o filtrowaniu:

    ```
    /plan Retrieve the issue on the repository related to adding filtering. We already added a publishers helper in src/lib/publishers.ts, so treat that as existing work and plan the remaining updates (games filtering logic, UI, and tests).
    ```

4. Copilot może zadawać pytania uzupełniające podczas budowania planu. Odpowiadaj na nie zgodnie z tym, jak zbudowałbyś funkcjonalność.
5. Gdy plan zostanie wygenerowany, przejrzyj go. Powinieneś zauważyć rekomendacje pozostałych zmian w warstwie danych i UI oraz generowanie testów.
6. Copilot CLI pozwoli Ci przekazać dodatkową opinię do planu. Możesz przejść kursorem w dół do wskazanej sekcji i wpisać sugestie. Copilot uwzględni je w nowej wersji planu.
7. Gdy będziesz zadowolony, wybierz opcję oferowaną przez Copilota, aby rozpocząć budowanie nowej funkcji!

> [!NOTE]
> Ponieważ Copilot jest probabilistyczny, dokładny tekst i opcje będą się różnić. Powinieneś zobaczyć opcję rozpoczęcia budowania podobną do:
>
> `Yes, and switch to autopilot mode`.
>
> Copilot może zaproponować włączenie [trybu autopilot](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot), jak w przykładzie powyżej. Tryb autopilot pozwala Copilot CLI pracować nad zadaniem bez czekania na Twoje dane wejściowe po każdym kroku. Po początkowej instrukcji Copilot CLI przechodzi przez kolejne kroki autonomicznie, aż uzna zadanie za ukończone. Ponieważ działamy w izolowanym środowisku, możemy uruchomić autopilot i zezwolić na wszystkie narzędzia.

8. Copilot zabierze się do generowania plików!

> [!NOTE]
> Ta operacja prawdopodobnie zajmie kilka minut. Zobaczysz, jak Copilot edytuje i tworzy pliki, aktualizuje i generuje testy oraz uruchamia wszystkie testy, aby upewnić się, że wszystko przechodzi. To dobry moment, by zastanowić się nad tym, co już poznałeś na warsztatach, albo napić się czegoś.

## Przejrzyj kod

Każdy kod AI należy przejrzeć przed scaleniem do głównej gałęzi. Poświęćmy teraz czas na przejrzenie plików utworzonych i zmodyfikowanych przez Copilota przy implementacji nowej funkcji.

1. Użyj Copilot CLI, aby wyświetlić „diff” lub zmiany w kodzie, wpisując w Copilot CLI:

    ```
    /diff
    ```

2. Zwróć uwagę na zmienione pliki. Użyj klawiszy strzałek w lewo i w prawo, aby przeglądać różne pliki. Powinieneś zobaczyć zmiany m.in. na stronie listy gier (gdzie wyświetlamy nowe elementy interfejsu sterujące filtrem i filtrowanie po stronie klienta) oraz w `src/lib/games.ts`, a także testy takie jak `games.test.ts`. Możesz też zobaczyć zmiany w `publishers.ts`, jeśli Copilot dopracuje istniejący helper pod pełną implementację.

## Podsumowanie i kolejne kroki

Dodałeś filtrowanie do witryny za pomocą Copilot CLI! Konkretnie:

- użyłeś trybu planowania do wygenerowania planu implementacji filtrowania.
- wygenerowałeś kod potrzebny do dodania filtrowania do witryny, wykorzystując Copilota.

W następnym kroku sprawdzisz, czy działa. [Przetestujmy funkcję serwerem Playwright MCP][next-lesson], zanim otworzysz pull request.

## Zasoby

- [Korzystanie z Copilot CLI][using-copilot-cli]
- [O Copilot CLI][about-copilot-cli]
- [Zarządzanie kontekstem w Copilot CLI][context-management]

[previous-lesson]: ../2-custom-instructions/
[next-lesson]: ../4-mcp/
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
