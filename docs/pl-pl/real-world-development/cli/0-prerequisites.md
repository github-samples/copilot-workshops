---
title: "Ćwiczenie 0 - Wymagania wstępne"
description: "Utwórz własną kopię Tailspin Toys i przygotuj GitHub Codespace do warsztatu Copilot CLI."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-18
---

Zanim zaczniesz ćwiczenia Copilot CLI, przygotuj wszystko, czego potrzebujesz. Utworzysz własną kopię repozytorium Tailspin Toys i uruchomisz [codespace][codespaces], którego zintegrowanego terminala użyjesz do instalacji i uruchomienia Copilot CLI w następnym ćwiczeniu.

W tym ćwiczeniu:

- utworzysz własną kopię projektu Tailspin Toys z szablonu.
- utworzysz Codespace i potwierdzisz, że projekt jest gotowy.

## Skonfiguruj repozytorium warsztatowe

Będziesz pracować na własnej kopii projektu Tailspin Toys. Utwórz ją teraz z [repozytorium szablonu][tailspin-template]. Nowe repozytorium zawiera wszystkie pliki potrzebne w warsztacie.

1. W nowym oknie przeglądarki przejdź do [szablonu Tailspin Toys][tailspin-template].
2. Utwórz własną kopię repozytorium, wybierając **Use this template**, a następnie **Create a new repository**.
3. Jeśli uczestniczysz w warsztacie w ramach wydarzenia prowadzonego przez GitHuba lub Microsoft, postępuj zgodnie z instrukcjami mentorów. W przeciwnym razie utwórz nowe repozytorium w organizacji, w której masz dostęp do GitHub Copilot.
4. Zanotuj ścieżkę utworzonego repozytorium (`organization-or-user-name/repository-name`) — będziesz się do niej odwoływać później w warsztacie.

> [!NOTE]
> Gdy tworzysz repozytorium z szablonu, backlog zgłoszeń (issues) GitHub jest tworzony automatycznie. Będziesz pracować na tych zgłoszeniach przez cały warsztat — nie musisz nic zgłaszać samodzielnie.

Użyj świeżej kopii szablonu warsztatu. Zawiera instrukcje repozytorium, kod aplikacji, testy, skill `quality-checks` oraz backlog, z którego skorzystasz. Jeśli używasz starszej kopii, sprawdź u prowadzącego, czy ma pliki, których będziesz potrzebować.

## Utwórz Codespace

Następnie użyjesz Codespace do wykonania warsztatu.

[GitHub Codespaces][codespaces] to chmurowe środowisko deweloperskie, które pozwala pisać, uruchamiać i debugować kod bezpośrednio w przeglądarce. Zapewnia pełnoprawny edytor z obsługą wielu języków programowania, rozszerzeń i narzędzi.

1. Przejdź do nowo utworzonego repozytorium.
2. Wybierz **Code**.
3. Wybierz kartę **Codespaces**, a następnie **Create codespace on main**.
4. Poczekaj na zakończenie konfiguracji Codespace. Szablon instaluje za Ciebie zależności projektu, Playwright Chromium oraz lokalną bazę danych.
5. Jeśli pojawi się pytanie **Do you trust the authors of the files in this folder?**, wybierz **Trust Folder & Continue**.
6. Otwórz terminal w katalogu głównym repozytorium i uruchom aplikację:

   ```bash
   npm run dev
   ```

7. Gdy Codespaces zgłosi, że port `4321` jest dostępny, wybierz **Open in Browser** i upewnij się, że witryna Tailspin Toys się ładuje.
8. Wróć do terminala i zatrzymaj serwer deweloperski kombinacją <kbd>Ctrl</kbd>+<kbd>C</kbd>.

## Podsumowanie i kolejne kroki

Jesteś gotowy! W tym ćwiczeniu:

- utworzyłeś własną kopię projektu Tailspin Toys z szablonu.
- utworzyłeś Codespace i potwierdziłeś, że projekt jest gotowy.

Następnie [zainstalujesz GitHub Copilot CLI][next-lesson] w Codespace i uwierzytelnisz go kontem GitHuba.

## Zasoby

- [Przegląd GitHub Codespaces][codespaces]
- [Tworzenie repozytorium z szablonu][template-repository]
- [Pierwsze kroki z Codespaces][codespaces-quickstart]

[tailspin-template]: https://github.com/github-samples/tailspin-toys
[template-repository]: https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository
[codespaces-quickstart]: https://docs.github.com/codespaces/getting-started/quickstart
[next-lesson]: ../1-install-copilot-cli/
[codespaces]: https://github.com/features/codespaces
