---
slug: pl-pl/real-world-development/cli/8-foundry-agent
title: "Opcjonalnie: Włącz Foundry"
description: "Trzymodułowa seria: przygotuj model, zbuduj i wdróż agenta opartego o katalog, a potem podłącz go do Tailspin Toys."
authors:
  - juliamuiruri4
  - azkel
lastUpdated: 2026-09-16
---

Ta opcjonalna seria wykorzystuje GitHub Copilot CLI i Microsoft Foundry Skill, by zamienić katalog Tailspin Toys w asystenta konwersacyjnego. Trzy moduły prowadzą Cię od przygotowania projektu i modelu do hostowanego agenta oraz działającej integracji z witryną.

W tej serii:

- przygotujesz środowisko Azure i przetestujesz model względem katalogu.
- zbudujesz szkielet, przetestujesz i wdrożysz hostowanego agenta Backer Concierge.
- podłączysz agenta do witryny przez lokalne proxy po stronie serwera oraz widżet czatu.

## Scenariusz

Backerzy Tailspin Toys mogą przeglądać gry według kategorii i wydawcy, ale te filtry nie każdemu pomagają znaleźć następną grę. Niektórzy backerzy mają pytania w stylu *Które gry pasowałyby do kogoś, kto kocha żarty o Gicie?* Na takie pytania nie ma odpowiedzi w postaci listy rozwijanej.

Tailspin Toys chce **Backer Concierge**, który pomoże backerom odkrywać gry w rozmowie. Powinien rekomendować gry z katalogu Tailspin, zadawać krótkie pytanie doprecyzowujące, gdy preferencje są niejasne, oraz pamiętać wcześniejsze rekomendacje przy pytaniach uzupełniających.

Backerzy potrzebują odpowiedzi, którym mogą zaufać. Concierge powinien korzystać wyłącznie z informacji w katalogu i jasno mówić, gdy szczegół nie jest dostępny — zamiast wymyślać gry, wydawców, oceny, sumy finansowania, liczby backerów, ceny, liczby graczy, czasy gry czy daty premiery.

## Wybierz kolejny krok

Moduły budują na sobie nawzajem w tym samym repozytorium Tailspin Toys, gałęzi i projekcie Foundry. Każdy kończy się działającym punktem kontrolnym.

| Moduł | Co zrobisz | Punkt ukończenia |
| --- | --- | --- |
| [1. Przygotuj projekt i model][project-model] | Skonfiguruj narzędzia, wyeksportuj katalog oraz wybierz i przetestuj model | Wdrożony model, który poprawnie odpowiada na pytania o katalog |
| [2. Zbuduj i wdróż agenta][build-deploy] | Zbuduj szkielet agenta, przetestuj zachowanie i wdróż go do Foundry | Działający hostowany Backer Concierge |
| [3. Podłącz agenta do witryny][connect-site] | Zbuduj lokalne proxy i widżet czatu, potem przetestuj cały przepływ | Concierge dostępny przez lokalną witrynę |

> [!IMPORTANT]
> Hostowani agenci Microsoft Foundry są w publicznej wersji zapoznawczej.
>
> Ta seria tworzy rozliczane zasoby Azure, w tym wdrożenie modelu i hostowanego agenta. Utworzenie zasobów wymaga przeglądu wybranej subskrypcji, regionu, limitu (quota) i szacowanego kosztu. [Instrukcje czyszczenia][cleanup] obowiązują nawet wtedy, gdy zatrzymasz się po pierwszym lub drugim module.

1. Aby rozpocząć opcjonalną serię, przejdź do [Przygotuj projekt i model][project-model]. Instrukcje konfiguracji są tam zawarte.
2. Jeśli wolisz zakończyć podstawowy warsztat, przejdź do [Podsumowanie i kolejne kroki][review].

## Wyczyść swoje zasoby

Gdy skończysz eksperymentować w dowolnym punkcie kontrolnym, usuń zasoby Azure, by uniknąć niechcianych kosztów. Czyszczenie usuwa zasoby potrzebne w późniejszych modułach, więc kontynuacja potem wymaga ich ponownego utworzenia.

> [!CAUTION]
> Usuwaj `rg-tailspin-toys` tylko wtedy, gdy grupa jest przeznaczona wyłącznie do tego ćwiczenia i nie zawiera zasobów, które musisz zachować. Usunięcie współdzielonej grupy zasobów usunęłoby też niezwiązane zasoby.

1. Zatrzymaj lokalnego agenta, Function lub serwer deweloperski Astro, które uruchomiłeś, używając kombinacji <kbd>Ctrl</kbd>+<kbd>C</kbd> w ich terminalu.
2. Wyjdź z Copilot CLI. Jeśli zbudowałeś szkielet agenta w module 2, uruchom z katalogu głównego repozytorium Tailspin Toys w tym samym środowisku `azd`:

    ```bash
    azd down --purge
    ```

3. Sprawdź wybraną subskrypcję poleceniem `az account show`. Przejrzyj `rg-tailspin-toys` w tej subskrypcji i upewnij się, że wszystkie pozostałe zasoby należą do tego ćwiczenia. Jeśli zatrzymałeś się po module 1, projekt Foundry i model nadal wymagają czyszczenia, nawet jeśli nie zbudowałeś szkieletu usługi `azd`.
4. Jeśli dedykowana grupa zasobów warsztatu nadal istnieje i zawiera tylko zasoby, które zamierzasz usunąć, uruchom:

    ```bash
    az group delete --name rg-tailspin-toys --yes --no-wait
    ```

5. W portalu Azure potwierdź, że usuwanie grupy zasobów się kończy. Polecenie z `--no-wait` wraca przed zakończeniem usuwania.

## Zasoby

- [Azure Skills Plugin][azure-skills]
- [Use the Microsoft Foundry Skill in coding agents][foundry-skill]
- [Deploy your first hosted agent with the Microsoft Foundry Skill][hosted-agent-quickstart]
- [Hosted agent permissions][hosted-agent-permissions]

[project-model]: 1-project-and-model/
[build-deploy]: 2-build-and-deploy/
[connect-site]: 3-connect-to-site/
[review]: ../10-review/
[cleanup]: #wyczyść-swoje-zasoby
[azure-skills]: https://github.com/microsoft/azure-skills#github-copilot-cli
[foundry-skill]: https://learn.microsoft.com/azure/foundry/how-to/develop/use-microsoft-foundry-skill?tabs=copilot-cli
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=foundry-skills
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
