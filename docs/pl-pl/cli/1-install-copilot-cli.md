---
title: "Ćwiczenie 1 - Instalacja GitHub Copilot CLI"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-10
---

[GitHub Copilot CLI][about-copilot-cli] to wielozadaniowy oparty na pracy agentów asystent programowania działający w terminalu. Pozwala eksplorować kod źródłowy, generować nowy, uruchamiać polecenia i korzystać z zewnętrznych narzędzi — wszystko za pomocą linii poleceń. Możesz zlecać zadania i prosić o zmiany, samemu skupiając się na zadaniach wysokiego poziomu. Pierwszy krok, jak można się spodziewać, to instalacja narzędzia! Na szczęście da się to zrobić za pomocą innych narzędzi, które już znasz.

Podczas tego ćwiczenia:

- zainstalujesz GitHub Copilot CLI za pomocą npm.
- uwierzytelnisz się kontem GitHuba.
- zweryfikujesz instalację.

## Scenariusz

Twój zespół zaczyna używać agentów AI do pracy nad rosnącym backlogiem. Copilot CLI przenosi tę możliwość do terminala, w którym wielu deweloperów i tak spędza czas. To ćwiczenie doprowadzi Cię do instalacji, uwierzytelnienia i gotowości do korzystania z narzędzia w dalszej części tych warsztatów.

## Otwórz terminal w codespace

Przed instalacją Copilot CLI otwórz okno terminala w codespace.

1. Wróć do codespace, jeśli jeszcze go nie masz otwartego.
2. Otwórz okno terminala. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
3. Na dole okna VS Code powinien pojawić się panel terminala.

## Zainstaluj Copilot CLI

Copilot CLI możesz zainstalować przez [npm][install-npm], [WinGet][install-winget] i [Homebrew][install-homebrew]. Ponieważ GitHub Codespaces mają wstępnie zainstalowany Node.js, użyjesz npm do instalacji Copilot CLI.

1. W terminalu sprawdź, czy Node.js jest zainstalowany i spełnia wymaganie wersji:

   ```bash
   node --version
   ```

   Powinieneś zobaczyć wersję 22 lub nowszą (np. `v22.x.x`).

2. Zainstaluj Copilot CLI globalnie w codespace za pomocą npm:

   ```bash
   npm install -g @github/copilot
   ```

3. Zweryfikuj instalację, sprawdzając wersję:

   ```bash
   copilot --version
   ```

   Powinieneś zobaczyć numer wersji (np. `v1.0.XX`).

> [!TIP]
> Jeśli napotkasz błędy związane z uprawnieniami, na niektórych systemach może być potrzebne `sudo npm install -g @github/copilot`. W GitHub Codespaces zwykle nie jest to konieczne.

## Uwierzytelnij się w GitHubie

Przy pierwszym uruchomieniu Copilot CLI poprosi Cię o uwierzytelnienie kontem GitHuba.

1. Uruchom Copilot CLI:

   ```bash
   copilot
   ```

2. Jeśli nie jesteś zalogowany, zobaczysz prośbę o uwierzytelnienie. Copilot CLI wyświetli kod urządzenia i poprosi o odwiedzenie adresu URL.
3. Postępuj zgodnie z instrukcjami na ekranie:
   - Otwórz podany adres URL w przeglądarce
   - Wprowadź kod urządzenia, gdy zostaniesz o to poproszony
   - Autoryzuj Copilot CLI do dostępu do konta GitHuba
4. Po uwierzytelnieniu zobaczysz interfejs Copilot CLI, gotowy na pytania i polecenia.

> [!NOTE]
> W codespace możesz być już uwierzytelniony przez sesję GitHuba. Jeśli Copilot CLI uruchomi się bez prośby o uwierzytelnienie, wszystko jest w porządku!

## Zaufaj katalogowi i sprawdź, czy wszystko działa

Skoro jesteś po raz pierwszy w interfejsie Copilot CLI, gdy wyświetli się stosowne powiadomienie, zaufaj temu repozytorium i upewnij się, że Copilot CLI jest poprawnie zainstalowany i połączony.

1. Gdy Copilot CLI poprosi o potwierdzenie, że ufasz plikom w tym folderze, zobaczysz trzy opcje:
   - **Yes, proceed**: Zaufaj tylko w tej sesji
   - **Yes, and remember this folder for future sessions**: Zaufaj na stałe
   - **No, exit (Esc)**: Nie zezwalaj na dostęp do plików
2. Na potrzeby tych warsztatów wybierz **Yes, and remember this folder for future sessions**, ponieważ będziesz pracować w tym repozytorium przez cały czas.
3. Zadaj Copilotowi proste pytanie, aby sprawdzić, czy działa:

   ```
   What files are in this project?
   ```

4. Copilot zbada repozytorium i podsumuje strukturę projektu.
5. Wypróbuj polecenie `/help`, aby zobaczyć dostępne polecenia slash:

   ```
   /help
   ```

6. Wyjdź z Copilot CLI, wprowadzając w terminalu poniższe polecenie. Wrócimy do Copilot CLI w kolejnym ćwiczeniu!

   ```
   exit
   ```

## Podsumowanie i kolejne kroki

Gratulacje! Pomyślnie zainstalowałeś i uwierzytelniłeś GitHub Copilot CLI. Nauczyłeś się:

- instalować Copilot CLI za pomocą npm.
- uwierzytelniać się kontem GitHuba.
- ufać katalogowi, z którym ma pracować Copilot CLI.
- weryfikować, że instalacja działa poprawnie.

W następnym kroku dasz Copilotowi kontekst projektu. Przejdź do [Ćwiczenia 2 - Instrukcje niestandardowe (Copilot CLI)][next-lesson].

## Zasoby

- [Instalacja GitHub Copilot CLI][install-copilot-cli]
- [O Copilot CLI][about-copilot-cli]
- [Korzystanie z Copilot CLI][using-copilot-cli]

[previous-lesson]: ../0-prerequisites/
[next-lesson]: ../2-custom-instructions/
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
