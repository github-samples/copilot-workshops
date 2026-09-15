---
title: "Lekcja 0 - Wymagania wstępne"
description: "Przygotuj się do warsztatów z GitHub Copilot: zainstaluj Node.js dla projektu Tailspin Toys i utwórz własną kopię repozytorium na podstawie szablonu."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-09
---

Aplikacja GitHub Copilot to aplikacja desktopowa — centralny hub zarówno dla Copilota, jak i GitHuba. Zapewnia szybki dostęp do zgłoszeń i pull requestów oraz oczywiście pozwala budować wykorzystując GitHub Copilot. Podczas tego warsztatu będziesz pracować lokalnie, korzystając zarówno z aplikacji Tailspin Toys opartej na Astro, jak i z aplikacji GitHub Copilot. Zanim zaczniesz, upewnijmy się, że Node.js jest zainstalowany na Twoim komputerze, a potem zainstalujemy aplikację Copilot.

Podczas tej lekcji:

- zainstalujesz Node.js, aby testy projektu mogły działać na Twoim komputerze.
- utworzysz własną kopię projektu Tailspin Toys wykorzystując szablon.

## Zainstaluj Node.js

W niektórych lekcjach agent buduje funkcje i uruchamia lokalnie zestaw testów Tailspin Toys, co wymaga **[Node.js][nodejs]** — jedynego środowiska uruchomieniowego (runtime), którego projekt potrzebuje. Zainstaluj wersję **22 lub nowszą**; bieżące wydanie **LTS** to bezpieczny wybór.

Najprostsza opcja na każdej platformie to oficjalny instalator:

1. W systemie operacyjnym otwórz okno terminala: Windows Terminal, terminal macOS lub to, czego zwykle używasz.
2. Uruchom poniższe polecenie, aby potwierdzić, że masz zainstalowany co najmniej Node.js 22 lub nowszy:

    ```shell
    node --version
    ```

3. Jeśli widzisz `v22` lub wyższy numer, możesz przejść do następnej sekcji!

> [!TIP]
> Te kroki wykonaj tylko wtedy, gdy nie masz zainstalowanego Node albo potrzebujesz aktualizacji.

4. Otwórz [stronę pobierania Node.js][node-download].
5. Pobierz wersję **LTS** dla swojego systemu operacyjnego.
6. Uruchom instalator i zaakceptuj domyślne ustawienia. W Windows pozostaw zaznaczoną opcję **Add to PATH**.
7. Po instalacji otwórz nowe okno terminala.
8. Potwierdź instalację w nowym oknie terminala, uruchamiając:

    ```bash
    node --version
    ```

9. Powinieneś zobaczyć `v22.x.x` lub wyższą wersję.

> [!TIP]
> Wolisz kontenery? Jeśli masz zainstalowanego **[Dockera][docker]**, możesz użyć [kontenera deweloperskiego][dev-containers] z repozytorium zamiast instalować Node.js lokalnie. W takim wypadku, nie instaluj go na lokalnym systemie operacyjnym.

## Skonfiguruj repozytorium

Warsztaty będą prowadzone na własnej kopii projektu Tailspin Toys. Utwórz ją teraz za pomocą [repozytorium szablonu][template-repository]. Nowe repozytorium zawiera wszystkie pliki potrzebne w tych warsztatach — w następnej lekcji podłączysz je do aplikacji.

1. W nowym oknie przeglądarki przejdź do repozytorium tych warsztatów na GitHubie: `https://github.com/github-samples/tailspin-toys`.
2. Utwórz własną kopię repozytorium, wybierając przycisk **Use this template** na stronie repozytorium. Następnie wybierz **Create a new repository**.

    ![Przycisk Use this template z wybraną z listy rozwijanej opcją Create a new repository](../../_images/app-0-use-template.png)

3. Jeśli uczestniczysz w warsztacie w ramach wydarzenia prowadzonego przez GitHuba lub Microsoft, postępuj zgodnie z instrukcjami mentorów. W przeciwnym razie możesz utworzyć nowe repozytorium w organizacji, w której masz dostęp do GitHub Copilot.

    ![Formularz Create a new repository z github-samples/tailspin-toys wybranym jako szablon i wypełnioną nazwą repozytorium](../../_images/app-0-create-repository.png)

4. Zanotuj ścieżkę utworzonego repozytorium (**organization-or-user-name/repository-name**) — będziesz się do niej odwoływać później w trakcie zadań.

> [!NOTE]
> Gdy tworzysz repozytorium z szablonu, backlog zgłoszeń (issues) GitHub jest tworzony automatycznie. Będziesz pracować na tych zgłoszeniach przez cały warsztat — nie musisz nic zgłaszać samodzielnie.

## Podsumowanie i kolejne kroki

Jesteś gotowy! Zainstalowałeś Node.js, aby projekt mógł się budować i być testowany na Twojej maszynie, oraz utworzyłeś własną kopię repozytorium Tailspin Toys.

W następnym kroku zainstalujesz aplikację GitHub Copilot, podłączysz właśnie utworzone repozytorium i zapoznasz się z interfejsem aplikacji. Przejdź do [Lekcji 1 - Instalacja aplikacji GitHub Copilot][next-lesson].

## Zasoby

- [Pobierz Node.js][node-download]
- [Tworzenie repozytorium z szablonu][template-repository]
- [O aplikacji GitHub Copilot][about-copilot-app]

[next-lesson]: ../1-install-copilot-app/
[nodejs]: https://nodejs.org/
[node-download]: https://nodejs.org/en/download
[docker]: https://www.docker.com/products/docker-desktop/
[dev-containers]: https://code.visualstudio.com/docs/devcontainers/containers
[template-repository]: https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
