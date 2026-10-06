---
title: "Lekcja 0 - Wymagania wstępne i konfiguracja"
description: "Sprawdź wymagania wstępne warsztatu, zainstaluj aplikację GitHub Copilot i poznaj jej obszar roboczy."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Zanim zbudujesz Space Quiz, upewnij się, że masz wszystko, czego potrzebujesz, zainstaluj aplikację GitHub Copilot i poznaj jej obszar roboczy.

W tej lekcji:

- sprawdzisz wymagania wstępne warsztatu.
- zainstalujesz aplikację GitHub Copilot i zalogujesz się.
- wybierzesz model do sesji.
- poznasz główne obszary pracy aplikacji.
- wypróbujesz szybki czat.

## Wymagania wstępne

Potrzebujesz:

- konta GitHub z [planem Copilot][copilot-plans].
- komputera z systemem macOS, Windows lub Linux.

Aplikacja zawiera Git, więc nie musisz instalować nic więcej.

> [!NOTE]
> Jeśli korzystasz z Copilot Business lub Copilot Enterprise, administrator musi włączyć zasadę **Copilot CLI**, zanim sesje agenta zaczną działać.

## Zainstaluj i skonfiguruj aplikację

1. Pobierz i zainstaluj [aplikację GitHub Copilot][download-app] dla swojego systemu operacyjnego.
2. Otwórz aplikację.
3. Wybierz **Sign in to GitHub** i uwierzytelnij się.
4. Wybierz motyw, a następnie **Finish**.

## Wybierz model

Przy wyborze modelu stosuj poniższą kolejność preferencji i wybierz pierwszą dostępną opcję:

1. **GPT-6-Luna** (zalecany).
2. **Auto**, jako zrównoważona opcja zapasowa.
3. Dowolny model z [listy aktywnych modeli][active-models].

Dostępność modeli zależy od planu, zasad organizacji i wersji produktu.

## Poznaj obszar roboczy

Aplikacja łączy przepływ pracy rozwojowej w jednym miejscu:

- **New**: Uruchom sesję w projekcie albo wybierz **Chat**, aby zadać szybkie pytanie.
- **My work**: Przeglądaj zgłoszenia i pull requesty na GitHubie.
- **Automations**: Planuj powtarzalną pracę agenta w repozytorium.
- **Customize**: Zmieniaj motywy i modele oraz zarządzaj rozszerzeniami kanw.

## Wypróbuj szybki czat

Nie każde pytanie wymaga obszaru roboczego. W **New** wybierz **Chat** zamiast projektu. Czat nie ma podłączonego repozytorium i nie może edytować plików, więc to najszybszy sposób, by zadać pytanie, uzyskać wyjaśnienie albo przemyśleć podejście przed prawdziwą sesją.

Wyślij poniższe polecenie w czacie:

```plaintext
How does the GitHub Copilot app use worktrees?
```

## Podsumowanie i kolejne kroki

Sprawdziłeś wymagania wstępne, zainstalowałeś aplikację, wybrałeś model i poznałeś jej główne obszary pracy. Przejdź do [Lekcji 1: Utwórz obszar roboczy Space Quiz][next-lesson].

[copilot-plans]: https://github.com/features/copilot/plans
[download-app]: https://gh.io/app
[active-models]: https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing
[next-lesson]: ../1-create-workspace/
