---
title: "Ćwiczenie 0 - Wymagania wstępne"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-10
---

Zanim zaczniesz ćwiczenia Copilot CLI, przygotuj środowisko. W ramach tego ćwiczenia utworzysz własną kopię repozytorium Tailspin Toys i uruchomisz [codespace][codespaces], wewnątrz którego za pomocą zintegrowanego terminala zainstalujesz i uruchomisz Copilot CLI w następnym ćwiczeniu.

## Skonfiguruj repozytorium

Warsztaty będą prowadzone na własnej kopii projektu Tailspin Toys. Utwórz ją teraz za pomocą [repozytorium szablonu][template-repository]. Nowe repozytorium zawiera wszystkie pliki potrzebne w warsztatach — w kolejnych ćwiczeniach będziesz z niego korzystać.

1. W nowym oknie przeglądarki przejdź do repozytorium tych warsztatów na GitHubie: `https://github.com/github-samples/tailspin-toys`.
2. Utwórz własną kopię repozytorium, wybierając przycisk **Use this template** na stronie repozytorium. Następnie wybierz **Create a new repository**.

    ![Przycisk Use this template z wybraną z listy rozwijanej opcją Create a new repository](../../_images/ex0-use-template.png)

3. Jeśli uczestniczysz w warsztacie w ramach wydarzenia prowadzonego przez GitHuba lub Microsoft, postępuj zgodnie z instrukcjami mentorów. W przeciwnym razie możesz utworzyć nowe repozytorium w organizacji, w której masz dostęp do GitHub Copilot.

    ![Formularz Create a new repository z github-samples/tailspin-toys wybranym jako szablon](../../_images/ex0-repository-settings.png)

4. Zanotuj ścieżkę utworzonego repozytorium (**organization-or-user-name/repository-name**) — będziesz się do niej odwoływać później w trakcie zadań.

> [!NOTE]
> Gdy tworzysz repozytorium z szablonu, backlog zgłoszeń (issues) GitHub jest tworzony automatycznie. Będziesz pracować na tych zgłoszeniach przez cały warsztat — nie musisz nic zgłaszać samodzielnie.

## Tworzenie codespace

Wykorzystasz codespace do wykonania ćwiczeń w ramach tych warsztatów.

[GitHub Codespaces][codespaces] to chmurowe środowisko deweloperskie, które pozwala pisać, uruchamiać i debugować kod bezpośrednio w przeglądarce. Zapewnia pełnoprawne IDE z obsługą wielu języków programowania, rozszerzeń i narzędzi.

1. Przejdź do nowo utworzonego repozytorium.
2. Wybierz zielony przycisk **Code**.

    ![Przycisk Code](../../_images/ex0-code-button.png)

3. Wybierz kartę **Codespaces**, a następnie przycisk **+**, aby utworzyć nowy Codespace.

    ![Tworzenie nowego codespace](../../_images/ex0-create-codespace.png)

Utworzenie codespace zajmie kilka minut, choć i tak jest to znacznie szybsze niż ręczne instalowanie wszystkich bibliotek lokalnie. Możesz wykorzystać ten czas na poznanie innych funkcji GitHub Copilot, do których przejdziemy dalej.

> [!CAUTION]
> Wrócisz do codespace w kolejnym ćwiczeniu. Na razie zostaw je otwarte w karcie przeglądarki.

> [!NOTE]
> Ten warsztat jest przeznaczony do uruchamiania w codespace lub lokalnym [kontenerze deweloperskim][dev-containers]. Oba rozwiązania zapewniają środowisko ze wszystkimi wymaganymi zależnościami. Jeśli wolisz pracować lokalnie, otwórz sklonowane repozytorium w VS Code i wybierz **Reopen in Container**, gdy zostaniesz o to poproszony — VS Code zbuduje ten sam kontener deweloperski, którego używa codespace.

## Podsumowanie

Gratulacje — utworzyłeś własną kopię repozytorium Tailspin Toys! Rozpocząłeś też tworzenie codespace, z którego skorzystasz, gdy zaczniesz pracę z Copilot CLI.

## Następny krok

W następnym kroku zainstalujesz Copilot CLI i uwierzytelnisz się za pomocą konta GitHub. Przejdź do [Ćwiczenia 1 - Instalacja GitHub Copilot CLI][next-lesson].

## Zasoby

- [Przegląd GitHub Codespaces][codespaces]
- [Tworzenie repozytorium z szablonu][template-repository]
- [Pierwsze kroki z Codespaces][codespaces-quickstart]

[template-repository]: https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository
[codespaces-quickstart]: https://docs.github.com/codespaces/getting-started/quickstart
[next-lesson]: ../1-install-copilot-cli/
[codespaces]: https://github.com/features/codespaces
[dev-containers]: https://code.visualstudio.com/docs/devcontainers/containers
