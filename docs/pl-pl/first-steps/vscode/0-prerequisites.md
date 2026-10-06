---
title: "Lekcja 0 - Wymagania wstępne i konfiguracja"
description: "Sprawdź wymagania wstępne warsztatu, potwierdź Copilot Chat w VS Code, dodaj rozszerzenie GitHub Pull Requests and Issues i wybierz model."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Wprowadź Copilota do edytora. Copilot jest wbudowany w VS Code, więc nie musisz nic instalować na potrzeby czatu. Dodaj rozszerzenie GitHub, a następnie otwórz pusty folder.

W tej lekcji:

- sprawdzisz wymagania wstępne warsztatu.
- potwierdzisz, że Copilot Chat odpowiada w VS Code.
- zainstalujesz rozszerzenie GitHub Pull Requests and Issues.
- otworzysz pusty folder projektu i wybierzesz model.

## Wymagania wstępne

Potrzebujesz:

- konta GitHub z [planem Copilot][copilot-plans].
- [Visual Studio Code][vscode].
- zainstalowanego [Git][git]. Uruchom `git --version` w terminalu, aby to sprawdzić.

## Skonfiguruj VS Code

1. Zainstaluj [VS Code][vscode] i zaloguj się do GitHub. Copilot i Copilot Chat są wbudowane, więc otwórz widok **Chat** z paska tytułu i upewnij się, że odpowiada.
2. Otwórz widok **Extensions** i zainstaluj oficjalne rozszerzenie [GitHub Pull Requests and Issues][pr-extension], aby zgłoszenia i pull requesty pojawiły się na pasku bocznym.
3. Utwórz pusty folder o nazwie `space-quiz`, a następnie wybierz **File** > **Open Folder** i otwórz go.
4. Wybierz model za pomocą selektora modeli w widoku **Chat**, według kolejności preferencji z następnej sekcji.

## Wybierz model

Wybierz pierwszą dostępną opcję:

1. **GPT-6-Luna** (zalecane).
2. **Auto**, jako zrównoważoną opcję zapasową.
3. Dowolny model z [listy aktywnych modeli][active-models].

Dostępność modeli zależy od planu, zasad organizacji i wersji produktu.

## Podsumowanie i kolejne kroki

VS Code jest gotowy: masz Copilot Chat, rozszerzenie GitHub i pusty folder `space-quiz`. Przejdź do [Lekcji 1: Buduj w obszarze roboczym][next-lesson].

[copilot-plans]: https://github.com/features/copilot/plans
[vscode]: https://code.visualstudio.com/
[git]: https://git-scm.com/downloads
[pr-extension]: https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github
[active-models]: https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing
[next-lesson]: ../1-build-and-polish/
