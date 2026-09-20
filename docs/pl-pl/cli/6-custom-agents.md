---
title: "Ćwiczenie 6 - Agenci niestandardowi z GitHub Copilot CLI"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-10
---

## Czym są agenci niestandardowi?

[Agenci niestandardowi][custom-agents-concept] w GitHub Copilot pozwalają tworzyć wyspecjalizowanych asystentów AI dostosowanych do konkretnych zadań lub domen w trakcie pracy programistycznej. Definiując agentów przez pliki markdown w folderze `.github/agents` repozytorium, możesz dać Copilotowi skupione instrukcje, dobre praktyki, wzorce kodowania i wiedzę domenową, które pomagają mu skuteczniej wykonywać określone typy pracy. Zespoły mogą konsolidować swoją wiedzę w agentach wielokrotnego użytku — agent dostępności egzekwujący zgodność z [WCAG][wcag], agent bezpieczeństwa stosujący praktyki bezpiecznego programowania albo agent testujący utrzymujący spójne wzorce testów.

Agenci niestandardowi są definiowani plikami markdown w folderze `.github/agents` projektu albo globalnie w `~/.copilot/agents`. Każdy plik ma nagłówek YAML z co najmniej polami `name` i `description`, a następnie treść markdown definiującą zachowanie, ekspertyzę i instrukcje agenta.

### Agenci niestandardowi a skille agenta

Między agentami niestandardowymi a [skillami agenta][agent-skills-concept] jest pewne logiczne zachodzenie. Oba są głównie definiowane plikami markdown i mówią naszemu AI, jak wykonywać operacje. Najczystszy sposób rozróżnienia: **agent niestandardowy** to pracownik, a **skille** to narzędzia.

Agenci niestandardowi mają własne okno kontekstu i są zbudowani do orkiestracji skilli (a nawet innych agentów) w ramach swojej pracy. W tych warsztatach agent niestandardowy dostępności przegląda i aktualizuje witrynę pod kątem wytycznych dostępności; w ramach tej pracy może wywoływać skille, takie jak skill przepływu pull requestów lub skill uruchamiający i zarządzający testami.

> [!NOTE]
> Nie ma jednej „właściwej” metody tworzenia agenta niestandardowego. Jak w każdym przypadku pracy z AI, testuj i iteruj, aby znaleźć to, co działa w Twoich środowiskach i scenariuszach.

## Scenariusz

Wiele aplikacji webowych nie jest w pełni dostępnych dla wszystkich użytkowników, a witryna, nad którą pracujesz, nie jest wyjątkiem. Użyjesz agenta niestandardowego do zidentyfikowania i usunięcia braków dostępności.

Tailspin Toys zobowiązuje się, by ich platforma crowdfundingowa była dostępna dla wszystkich użytkowników, niezależnie od możliwości wzrokowych czy preferencji. Niedawna opinia użytkowników wskazała, że niektórzy uznają obecny ciemny motyw za trudny do odczytania z powodu niewystarczającego kontrastu między tekstem a kolorami tła. Aby rozwiązać ten problem dostępności, zespół projektowy poprosił o implementację trybu wysokiego kontrastu, który użytkownicy mogą włączać i wyłączać.

Ponieważ dostępność jest krytyczna, chcesz wdrożyć to jak najszybciej. Użyjesz agenta niestandardowego do wygenerowania funkcjonalności.

Podczas tego ćwiczenia:

- poznasz agentów niestandardowych.
- włączysz agenta niestandardowego i przypiszesz mu zadanie w Copilot CLI.

## Przegląd agenta niestandardowego dostępności

Agent niestandardowy dostępności został już dla Ciebie utworzony. Przejrzyjmy jego treść, aby zrozumieć, jak pokieruje Copilotem.

1. Otwórz `.github/agents/accessibility.md`.
2. Zwróć uwagę na nagłówek YAML z polami `name` i `description`.

> [!CAUTION]
> Nagłówek z `name` i `description` jest wymagany dla agentów niestandardowych.

3. Następnie przejrzyj kolejne sekcje, które podkreślają:
   - Główne obowiązki przy generowaniu kodu dla dostępnej witryny.
   - Dobre praktyki dostępności.
   - Przykłady kodu dla HTML, CSS i JavaScript.
   - Listę typowych pułapek i błędów.

## Użycie agenta niestandardowego w Copilot CLI

Możesz uruchomić agenta niestandardowego w Copilot CLI poleceniem `/agent`. Wykonajmy przegląd dostępności naszej witryny.

1. Wróć do codespace. Jeśli go zamknąłeś, przejdź do repozytorium na GitHub.com, wybierz **Code** > **Codespaces**, a następnie ponownie otwórz istniejący codespace.
2. Wróć do otwartej sesji Copilot CLI. Jeśli terminal jest zamknięty lub wyszedłeś z Copilot CLI, otwórz terminal. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>\`</kbd>, a następnie uruchom go z katalogu głównego repozytorium poleceniem `copilot --yolo --enable-all-github-mcp-tools`. Zaufaj folderowi projektu, jeśli zostaniesz o to poproszony, potem uruchom `/models` i wybierz **Auto**.
3. Wyświetl listę agentów: wpisz `/agent` w interfejsie Copilot CLI i wciśnij <kbd>Enter</kbd>.
4. Wybierz **Accessibility agent** z listy dostępnych agentów.
5. Użyj poniższego polecenia, aby poprosić agenta dostępności o przegląd i wygenerowanie poprawek dla elementu backlogu dotyczącego dostępności:

    ```
    Perform an accessibility review of the site. Pull the related issue down from the repository for details. Implement a high-contrast mode toggle that persists the user's preference across page reloads. Ensure there are e2e tests for any updates made to the project. Then create a PR with the updates.
    ```

6. Copilot zabierze się do pracy! Zacznie od pobrania zgłoszenia, potem wykona przegląd, wprowadzi zmiany i na koniec utworzy PR. Powinieneś też zauważyć, że przy tworzeniu PR korzysta ze skillu skoncentrowanego na PR-ach w projekcie.

> [!NOTE]
> Ten proces prawdopodobnie zajmie kilka minut. To dobra chwila, by zastanowić się nad wszystkim, czego się nauczyłeś, napić się czegoś albo zajrzeć do następnego modułu o dodatkowych poleceniach dostępnych w Copilot CLI.

## Podsumowanie i kolejne kroki

To ćwiczenie omówiło [agentów niestandardowych][custom-agents] w GitHub Copilot — wyspecjalizowanych asystentów AI dostosowanych do konkretnych zadań i domen. Dzięki agentom niestandardowym możesz opisywać sposób pracy i standardy zespołu w agentach wielokrotnego użytku, które pomagają Copilotowi skuteczniej wykonywać określone typy pracy.

Poznałeś następujące pojęcia:

- jak definiuje się agentów niestandardowych.
- użycie agenta niestandardowego w Copilot CLI.

W następnym kroku poznasz [kilka poleceń slash][next-lesson], pozwalających odkryć dodatkowe triki z Copilot CLI.

## Zasoby

- [Agenci niestandardowi][custom-agents]
- [Tworzenie agentów niestandardowych dla repozytorium][creating-custom-agents]
- [Agenci niestandardowi w awesome-copilot][awesome-copilot-agents]
- [Przygotowanie do używania agentów niestandardowych w organizacji][org-custom-agents]
- [Przygotowanie do używania agentów niestandardowych w przedsiębiorstwie][enterprise-custom-agents]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-slash-commands/
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[creating-custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents
[awesome-copilot-agents]: https://github.com/github/awesome-copilot/tree/main/agents
[org-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
[enterprise-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
[custom-agents-concept]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[agent-skills-concept]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/
