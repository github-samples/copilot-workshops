---
title: "Ćwiczenie 0 - Wymagania wstępne i konfiguracja"
description: "Sprawdź wymagania wstępne warsztatu, zainstaluj GitHub Copilot CLI, zaloguj się i wybierz model z pustego folderu projektu."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Umieść agenta w terminalu. Potwierdź, że masz to, czego potrzebujesz, zainstaluj GitHub Copilot CLI, zaloguj się i przygotuj się do pierwszej prośby z pustego folderu.

W tym ćwiczeniu:

- sprawdzisz wymagania wstępne warsztatu.
- zainstalujesz GitHub Copilot CLI i zalogujesz się.
- utworzysz folder projektu i zaufasz mu.
- wybierzesz model dla sesji.

## Wymagania wstępne

Potrzebujesz:

- konta GitHub z [planem Copilot][copilot-plans].
- zainstalowanego [Gita][git]. Uruchom `git --version`, aby to zweryfikować.
- komputera z macOS, Windows lub Linux.

[GitHub CLI][gh-cli] (`gh`) jest opcjonalne, ale zalecane, bo pozwala agentowi tworzyć za Ciebie repozytoria i pull requesty.

> [!NOTE]
> Jeśli korzystasz z Copilot Business lub Copilot Enterprise, administrator musi włączyć zasadę **Copilot CLI**, zanim sesje agenta zaczną działać.

## Skonfiguruj CLI

1. Zainstaluj [GitHub Copilot CLI][install-cli] dla swojej platformy.
2. Utwórz i wejdź do folderu projektu:

   ```bash
   mkdir space-quiz && cd space-quiz
   ```

3. Uruchom `copilot`, zaloguj się i zaufaj folderowi, gdy zostaniesz o to poproszony.
4. Uruchom `/model` i wybierz model według kolejności preferencji z następnej sekcji.
5. Opcjonalnie zainstaluj [GitHub CLI][gh-cli], jeśli jeszcze go nie masz.

![Ilustracja Copilot CLI w oknie terminala zatytułowanym space-quiz. Pyta, czy zaufać plikom w tym folderze, z wybraną opcją Yes, proceed, i sugeruje polecenie /model do wyboru modelu na tę sesję oraz /help, aby wyświetlić wszystkie polecenia slash. Linia promptu brzmi Create a space exploration quiz.](../../../_images/first-steps-cli-welcome.svg)

CLI otwiera się z prośbą o zaufanie i kilkoma poleceniami startowymi, w tym `/model`.

> [!TIP]
> W dowolnym momencie wpisz `/`, aby przeglądać dostępne polecenia, albo uruchom `/help`, aby zobaczyć pełną referencję.

## Wybierz model

Użyj poniższej kolejności preferencji przy uruchamianiu `/model` i wybierz pierwszą dostępną opcję:

1. **GPT-6-Luna** (zalecany).
2. **Auto**, jako zrównoważona rezerwa.
3. Dowolny model z [listy aktywnych modeli][active-models].

Dostępność modeli zależy od planu, zasad organizacji i wersji produktu.

## Podsumowanie i kolejne kroki

Copilot CLI jest zainstalowany, zalogowany i działa w pustym folderze `space-quiz`. Przejdź do [ćwiczenia 1: Budowa quizu z terminala][next-lesson].

[copilot-plans]: https://github.com/features/copilot/plans
[git]: https://git-scm.com/downloads
[gh-cli]: https://cli.github.com/
[install-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[active-models]: https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing
[next-lesson]: ../1-build/
