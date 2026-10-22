---
title: "Opcjonalnie: Uwzględnienie Foundry"
slug: pl-pl/real-world-development/app/8-foundry-canvas
description: "Zbuduj Backer Concierge oparty o katalog za pomocą Microsoft Foundry Canvas, z bezpiecznymi punktami zatrzymania po drodze."
authors:
  - juliamuiruri4
lastUpdated: 2026-09-16
prev: { link: /copilot-workshops/pl-pl/real-world-development/app/10-review/, label: Podsumowanie i kolejne kroki }
next:
  link: /copilot-workshops/pl-pl/real-world-development/app/8-foundry-canvas/1-project-and-model/
  label: Przygotuj projekt i model
---

Ta opcjonalna ścieżka dodaje **Backer Concierge** do Tailspin Toys za pomocą Microsoft Foundry Canvas w aplikacji GitHub Copilot. Przechodzi od eksperymentu z modelem opartym o katalog, przez hostowanego agenta, aż do lokalnej integracji ze stroną.

## Ścieżka

Każdy moduł kończy się punktem kontrolnym i bezpiecznym miejscem na zatrzymanie. To samo repozytorium Tailspin Toys, gałąź worktree, sesja powiązana ze zgłoszeniem, projekt Foundry i wdrożenie modelu towarzyszą Ci przez całą ścieżkę.

- [Przygotuj projekt i model][module-1] ustala granicę katalogu, tworzy projekt i wdrożenie modelu oraz sprawdza je w Canvas.
- [Zbuduj i wdróż agenta][module-2] tworzy scaffold Backer Concierge, testuje go lokalnie oraz wdraża i ponownie testuje hostowanego agenta.
- [Podłącz agenta do strony][module-3] dodaje lokalny proxy chroniący poświadczenia, dostępny widget czatu oraz testy kompleksowe.

> [!IMPORTANT]
> Microsoft Foundry Canvas i hostowani agenci są w publicznej wersji zapoznawczej (public preview).
>
> Ta ścieżka tworzy płatne zasoby Azure, w tym wdrożenie modelu oraz — od modułu 2 — hostowanego agenta. Subskrypcja, region, limit (quota) i szacowany koszt wymagają zatwierdzenia przed utworzeniem zasobów. Czyszczenie obowiązuje nawet wtedy, gdy zatrzymasz się tylko po projekcie i modelu.

1. Zacznij od [Przygotuj projekt i model][module-1], trzymając pracę w repozytorium Tailspin Toys, a nie w tym repozytorium treści warsztatu.
2. Jeśli wolisz zakończyć podstawowy warsztat, przejdź do [Podsumowanie i kolejne kroki][core-review].

## Wyczyść swoje zasoby

Gdy skończysz eksperymentować w dowolnym punkcie kontrolnym, usuń zasoby Azure, by uniknąć niechcianych kosztów. Czyszczenie usuwa zasoby potrzebne w późniejszych modułach, więc kontynuacja potem wymaga ich ponownego utworzenia.

> [!WARNING]
> Usuwaj `rg-tailspin-toys` tylko wtedy, gdy grupa jest dedykowana temu ćwiczeniu i nie zawiera zasobów, które chcesz zachować. Usunięcie współdzielonej grupy zasobów usunęłoby także niezwiązane zasoby.
>
> Jeśli w module 1 zatwierdziłeś inną nazwę grupy zasobów, w każdym poleceniu poniżej podstaw ją zamiast `rg-tailspin-toys`.

1. Zatrzymaj w terminalu każdy lokalny Agent Inspector, Azure Function lub serwer deweloperski Astro, który uruchomiłeś.
2. Jeśli wdrożyłeś hostowanego agenta w module 2 lub 3, otwórz terminal w tym samym worktree Tailspin Toys, użyj tego samego środowiska `azd`, a następnie uruchom:

   ```bash
   azd down --purge
   ```

3. Sprawdź wybraną subskrypcję oraz to, czy grupa zasobów warsztatu nadal istnieje:

   ```bash
   az account show --output table
   az group exists --name rg-tailspin-toys
   ```

   Jeśli polecenie zwróci `false`, czyszczenie jest zakończone. Jeśli zwróci `true`, przejrzyj zasoby w grupie:

   ```bash
   az resource list --resource-group rg-tailspin-toys --output table
   ```

   Upewnij się, że wszystkie pozostałe zasoby należą do tego ćwiczenia. Jeśli zatrzymałeś się po module 1, projekt Foundry i model nadal wymagają czyszczenia, nawet jeśli nie wdrożyłeś usługi `azd`.
4. Jeśli dedykowana grupa zasobów warsztatu nadal istnieje i zawiera tylko zasoby, które zamierzasz usunąć, uruchom:

   ```bash
   az group delete --name rg-tailspin-toys --yes --no-wait
   ```

5. Ponieważ `--no-wait` wraca przed zakończeniem usuwania, ponawiaj poniższe polecenie, aż zwróci `false`:

   ```bash
   az group exists --name rg-tailspin-toys
   ```

## Zasoby

Dokumentacja Microsoft opisuje Canvas, wdrożenia hostowane i ich uprawnienia.

- [What is Microsoft Foundry Canvas?][foundry-canvas]
- [Deploy your first hosted agent with Foundry Canvas][hosted-agent-quickstart]
- [Hosted agent permissions][hosted-agent-permissions]

[module-1]: ./1-project-and-model/
[module-2]: ./2-build-and-deploy/
[module-3]: ./3-connect-to-site/
[core-review]: ../10-review/
[foundry-canvas]: https://learn.microsoft.com/azure/foundry/agents/concepts/foundry-canvas
[hosted-agent-quickstart]: https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=canvas
[hosted-agent-permissions]: https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions
