---
title: "Ćwiczenie 9 - Polecenia slash w GitHub Copilot CLI"
description: "Poznaj polecenia slash do zarządzania kontekstem, wyboru modeli, udostępniania sesji i opcjonalnego delegowania do chmury."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-18
---

Jak każde dobre narzędzie CLI, GitHub Copilot CLI zawiera wiele poleceń slash do interakcji z nim. Te polecenia udostępniają zaawansowane funkcje, informacje „za kulisami” i dodatkowe opcje konfiguracji. Już używałeś poleceń takich jak `/diff`, `/mcp`, `/skills`, `/agent` i `/pr`. Przyjrzyjmy się kilku kolejnym przydatnym.

W tym ćwiczeniu:

- użyjesz `/context` i `/compact`, by zbadać, jak Copilot zarządza kontekstem rozmowy.
- użyjesz `/model`, by przejrzeć dostępne modele.
- poznasz, jak `/share` może wyeksportować lub udostępnić sesję.
- poznasz opcjonalne polecenia do pracy równoległej, worktree i delegowania do cloud agent.

## Scenariusz

Zakończyłeś podstawowy przepływ CLI. Spójrzmy teraz na kilka dodatkowych możliwości — zarządzanie kontekstem, przełączanie modeli, udostępnianie sesji i opcjonalne delegowanie pracy do [Copilot cloud agent][about-cloud-agent].

## Poznaj kontekst Copilot CLI

Przy większych lub bardziej złożonych zadaniach możesz dojść do maksymalnego okna kontekstu modelu. Copilot CLI automatycznie kompaktuje rozmowę w razie potrzeby, a Ty możesz samodzielnie sprawdzić lub skompaktować kontekst poleceniami slash.

1. Wróć do Codespace i uruchom Copilot CLI z katalogu głównego repozytorium, jeśli nie jest jeszcze otwarty.
2. Wpisz:

   ```plaintext
   /context
   ```

3. Zwróć uwagę na model, bieżące użycie tokenów oraz podział kontekstu między instrukcje systemowe, narzędzia, wiadomości i wolne miejsce.
4. Skompaktuj rozmowę:

   ```plaintext
   /compact
   ```

5. Ponownie wpisz `/context` i porównaj wynik. Zmiana może nie być drastyczna, jeśli rozmowa jest już mała.

> [!NOTE]
> Copilot CLI automatycznie kompaktuje kontekst, gdy okno się zapełnia. Użyj `/compact`, gdy chcesz sam wybrać moment. Użyj `/clear` lub `/new`, gdy przechodzisz do niezwiązanego zadania i chcesz świeżej rozmowy.

## Wybierz model

Różne modele mają różne mocne strony, a różni deweloperzy mają różne preferencje. Copilot CLI pozwala wyświetlić listę i wybrać model, którego chcesz użyć.

1. Wpisz:

   ```plaintext
   /model
   ```

2. Przejrzyj dostępne modele i informacje o użyciu.
3. Zostaw bieżący model, wybierz inny albo wciśnij <kbd>Esc</kbd>, aby zamknąć listę.

## Udostępnij sesję

Wspólna praca w zespole i dzielenie się wnioskami pomaga wszystkim lepiej korzystać z narzędzi AI. Polecenie `/share` może wyeksportować sesję do pliku Markdown lub HTML, utworzyć udostępniany link albo opublikować gist GitHub.

1. Wpisz `/help` i przejrzyj opcje `/share` w zainstalowanej wersji.
2. Jeśli chcesz udostępnić tę sesję, wybierz miejsce docelowe odpowiadające potrzebom, na przykład `/share file` dla lokalnego eksportu Markdown.
3. Przejrzyj wyeksportowaną treść, zanim wyślesz ją komukolwiek lub opublikujesz. Eksporty sesji mogą zawierać polecenia, odpowiedzi i szczegóły projektu.

Publikacja linku lub gista jest opcjonalna. Nie publikuj treści repozytorium ani rozmowy, których zespół nie zamierza udostępniać.

## Opcjonalnie: skaluj lub deleguj

Podstawowy warsztat jest zakończony. Copilot CLI oferuje też polecenia do większych zadań:

- `/fleet` może podzielić niezależne podzadania między subagentów i uruchomić je równolegle.
- `/worktree` może utworzyć izolowany git worktree dla osobnego zadania.
- `/delegate` może wysłać zadanie do Copilot cloud agent, który pracuje asynchronicznie i może otworzyć pull request.

Te polecenia są opcjonalne, bo mogą tworzyć dodatkowe worktree lub pracę zdalną. Zanim ich spróbujesz, zacznij od świeżego, dobrze określonego zadania i przejrzyj wynik w zwykłym przepływie pracy. Jeśli chcesz głębiej poznać asynchroniczną pracę agentów, kontynuuj [warsztat cloud agent][cloud-workshop].

## Podsumowanie i kolejne kroki

Polecenia slash w Copilot CLI pozwalają go konfigurować, udostępniać sesje i zobaczyć, co dzieje się za kulisami. W tym ćwiczeniu:

- użyłeś `/context` i `/compact`, by zbadać, jak Copilot zarządza kontekstem rozmowy.
- użyłeś `/model`, by przejrzeć dostępne modele.
- poznałeś, jak `/share` może wyeksportować lub udostępnić sesję.
- poznałeś opcjonalne polecenia do pracy równoległej, worktree i delegowania do cloud agent.

Dostępnych jest więcej poleceń slash i więcej do odkrycia z Copilot CLI! Zamknijmy tę drogę [przeglądem tego, czego się nauczyliśmy][next-lesson] oraz kolejnymi krokami w nauce.

## Zasoby

- [Copilot CLI command reference][cli-reference]
- [Context management in Copilot CLI][context-management]
- [About Copilot cloud agent][about-cloud-agent]

[previous-lesson]: ../8-create-pull-request/
[next-lesson]: ../10-review/
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[context-management]: https://docs.github.com/copilot/concepts/agents/copilot-cli/context-management
[about-cloud-agent]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent
[cloud-workshop]: ../../cloud/
