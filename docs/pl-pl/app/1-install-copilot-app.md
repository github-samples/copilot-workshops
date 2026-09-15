---
title: "Lekcja 1 - Instalacja aplikacji GitHub Copilot"
description: "Zainstaluj aplikację GitHub Copilot, podłącz właśnie utworzone repozytorium, zapoznaj się z obszarem roboczym i wypróbuj szybki czat."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-09
---

**[Aplikacja GitHub Copilot][about-copilot-app]** to aplikacja desktopowa pozwalająca budować oprogramowanie za pomocą agentów. Jest zbudowana na bazie GitHub Copilot CLI i integruje się natywnie z GitHubem, więc repozytoria, gałęzie i potoki CI działają od samego początku. Jest zaprojektowana pod przepływy, w których kierujesz kilkoma agentami równolegle, każdy we własnym izolowanym obszarze roboczym — zamiast robić całą pracę samodzielnie oraz pod automatyzację powtarzalnych zadań. Jeżeli Node.js jest już zainstalowany, a kopia projektu gotowa, kolejnym krokiem jest instalacja aplikacji i podłączenie tego repozytorium.

Podczas tej lekcji:

- zainstalujesz aplikację GitHub Copilot i zalogujesz się do niej.
- dodasz projekt do aplikacji wykorzystując swoje repozytorium na GitHubie.
- zapoznasz się z obszarem roboczym, w tym z backlogiem, który szablon dla Ciebie przygotował.
- wypróbujesz szybki czat, aby dowiedzieć się więcej o samej aplikacji.

## Scenariusz

Twój zespół wdraża agentów AI, aby przerabiać rosnący backlog. Aplikacja Copilot gwarantuje centralne miejsce do kierowania tą pracą — podejmowanie zgłoszeń (issues), uruchamianie agentów, przeglądanie zmian i scalanie pull requestów. W ramach tej lekcji zainstalujesz aplikację, podłączysz się i swobodnie rozpoczniesz rozmowę o projekcie z agentami.

> [!NOTE]
> Wymagany jest odpowiedni plan Copilot — Copilot Student lub dowolny płatny plan (Pro, Pro+, Business lub Enterprise). Jeśli korzystasz z Copilot Business lub Copilot Enterprise, administrator musi włączyć dostęp do **Copilot CLI**, zanim będziesz w stanie poprawnie skorzystać z aplikacji.

## Zainstaluj i skonfiguruj aplikację GitHub Copilot

Aby korzystać z aplikacji GitHub Copilot, pierwszym krokiem — jak można się spodziewać — jest jej instalacja. Dostępne są wersje dla Windows, macOS i Linux. Zainstalujmy aplikację, uwierzytelnijmy się i dodajmy nasze repozytorium Tailspin Toys.

1. W przeglądarce otwórz [stronę startową aplikacji GitHub Copilot][download-app].
2. Pobierz aplikację dla swojej platformy i zainstaluj ją zgodnie z instrukcjami na stronie startowej.
3. Otwórz aplikację po instalacji.
4. Wybierz **Sign in to GitHub** i postępuj zgodnie z instrukcjami, aby się uwierzytelnić. Jeśli używasz GitHub Enterprise Server, wybierz **Use GitHub Enterprise** i wprowadź adres serwera, gdy zostaniesz o to poproszony.
5. Po uwierzytelnieniu zostaniesz zapytany o podłączenie repozytoriów. Wybierz właśnie utworzone repozytorium Tailspin Toys, które powinno mieć nazwę `<YOUR_GITHUB_HANDLE>/tailspin-toys`.
6. Wybierz **Continue**, aby kontynuować wprowadzenie.
7. Gdy zostaniesz poproszony o motyw, wybierz ten, który najbardziej Ci odpowiada, a następnie wciśnij **Finish**.

> [!NOTE]
> Jeśli Twoja kopia Tailspin Toys nie pojawiła się na liście automatycznie, możesz dodać ją po zakończeniu procesu konfiguracji aplikacji. Po zakończeniu aplikacja Copilot przeniesie Cię na ekran główny. Stamtąd możesz wybrać **Choose from GitHub**, wyszukać repozytorium po nazwie (\<YOUR_GITHUB_HANDLE\>/tailspin-toys), a następnie je wybrać. Repozytorium zostanie dodane do aplikacji Copilot!

## Zapoznaj się z obszarem roboczym

Gdy projekt jest już pobrany, poświęć chwilę na rozpoznanie, co jest gdzie w wyświetlanym interfejsie. Aplikacja dzieli wszystko na kilka obszarów na pasku bocznym:

- **Sessions** — miejsce, w którym agenci wykonują pracę. Każda sesja działa we własnym izolowanym obszarze roboczym, więc możesz uruchomić kilka sesji naraz bez kolizji zmian. Pierwszą sesję rozpoczniesz w następnej lekcji.
- **Quick chats** — lekkie rozmowy do pytań i burzy mózgów, które nie potrzebują własnej gałęzi ani obszaru roboczego. Wypróbujesz jedną na końcu tej lekcji.
- **My work** — Twoje zgłoszenia i pull requesty, udostępnione dzięki **natywnej integracji z GitHubem**. Stąd możesz przeglądać i filtrować zgłoszenia oraz pull requesty, sprawdzać status CI, uruchamiać sesję ze zgłoszenia i przeglądać pull requesty — bez opuszczania aplikacji.
- **Automations** — zapisane zadania agenta uruchamiane według harmonogramu lub na żądanie. Jedną utworzysz pod koniec warsztatu.

### Znajdź przygotowany backlog

Ponieważ aplikacja integruje się natywnie z GitHubem, praca czekająca w repozytorium pojawia się bezpośrednio w aplikacji. Gdy utworzyłeś repozytorium, backlog zgłoszeń został dla Ciebie złożony — potwierdźmy, że tam jest.

1. Wybierz **My work** na pasku bocznym.
2. Szablon przygotował osiem zgłoszeń w backlogu. To środowisko skupia się na poniższych trzech — potwierdź, że je widzisz:

   - Allow users to filter games by category and publisher
   - Update our repository coding standards
   - Implement pagination on the game list page

3. Wybierz zgłoszenie, aby przeczytać szczegóły. Każde zgłoszenie jest też punktem startowym sesji agenta — rozpoczniesz pracę z tych zgłoszeń później w trakcie zadań.

> [!NOTE]
> Lista elementów w My work jest automatycznie filtrowana, aby pokazywać tylko elementy z repozytoriów dodanych do aplikacji Copilot. Chcesz zobaczyć elementy pracy z innych repozytoriów? Dodaj je do aplikacji!

## Wypróbuj szybki czat

Dobry sposób, by oswoić się z aplikacją, to użyć jej do nauki o *samej aplikacji* — a **szybki czat** jest do tego idealnym narzędziem. Szybkie czaty pozwalają zadać pytanie lub zrobić burzę mózgów bez tworzenia gałęzi ani worktree, więc są doskonałe do szybkiego, jednorazowego pytania — bez sesji.

1. Na pasku bocznym wybierz **+** obok **Quick chats**, aby otworzyć nowy czat.
2. Zapytaj aplikację, jak działają jej własne sesje:

   ```plaintext
   How does the GitHub Copilot app use worktrees?
   ```

3. Przeczytaj odpowiedź w widoku rozmowy. Zobaczysz, że każda sesja działa we własnym izolowanym git worktree — to właśnie pozwala uruchamiać kilku agentów równolegle bez kolizji zmian. Możesz kontynuować rozmowę lub w dowolnym momencie rozpocząć nowy czat.

## Podsumowanie i kolejne kroki

Gratulacje! Zainstalowałeś aplikację GitHub Copilot, podłączyłeś projekt i zbadałeś obszar roboczy. Nauczyłeś się:

- instalować aplikację i logować się do GitHuba.
- dodawać projekt z jego repozytorium na GitHubie.
- jak używać interfejsu i znajdować przygotowany backlog w **My work**.
- używać szybkiego czatu do szybkiego, jednorazowego pytania.

W następnym kroku rozpoczniesz pierwszą sesję agenta i wprowadzisz pierwszą zmianę w projekcie — wyświetlenie oceny za pomocą gwiazdek na kartach gier. Przejdź do [Lekcji 2 - Uruchomienie pierwszej sesji agenta][next-lesson].

## Zasoby

- [O aplikacji GitHub Copilot][about-copilot-app]
- [Pierwsze kroki z aplikacją GitHub Copilot][getting-started]
- [Praca z sesjami agenta w aplikacji GitHub Copilot][agent-sessions]

[ex0]: ../0-prerequisites/
[next-lesson]: ../2-add-star-rating/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[download-app]: https://gh.io/app
