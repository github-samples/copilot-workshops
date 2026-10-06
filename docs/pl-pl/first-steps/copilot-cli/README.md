---
title: "Pierwsze kroki z GitHub Copilot CLI"
description: "Przejdź prowadzone, terminalowe wprowadzenie do GitHub Copilot CLI, budując i dostarczając Space Quiz."
slug: pl-pl/first-steps/copilot-cli
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Przejdź przyjazne dla początkujących, praktyczne wprowadzenie do GitHub Copilot CLI. Zbudujesz kolorowy Space Quiz z pustego folderu i poznasz pętlę terminalową: buduj i przeglądaj diffy, zanim Git cokolwiek zapisze, uruchamiaj sesje równolegle, planuj przed edycją, a następnie twórz i scalaj pull request bez opuszczania powłoki.

Warsztat zajmuje około 60–90 minut. Projekt używa jednego pliku HTML bez zależności runtime, więc możesz skupić się na nauce CLI i jego agentycznych przepływów pracy.

> [!NOTE]
> Ten warsztat stworzył [James Montemagno][james], a został zaadaptowany z [First Steps with GitHub Copilot][source-lab]. Oryginalna treść jest dostępna na licencji [MIT][source-license].

## Ćwiczenia

| Ćwiczenie | Temat | Co zrobisz |
| ------ | ----- | ---------------- |
| [0. Wymagania wstępne i konfiguracja][lesson-0] | Konfiguracja | Sprawdź wymagania wstępne, zainstaluj Copilot CLI, zaloguj się i wybierz model |
| [1. Budowa quizu][lesson-1] | Budowa | Zbuduj quiz z terminala i wprowadź jedną skupioną zmianę |
| [2. Zapisanie instrukcji projektu][lesson-2] | Instrukcje | Wygeneruj i dostosuj instrukcje agenta poleceniem `/init` |
| [3. Publikacja projektu][lesson-3] | Publikacja | Zainicjalizuj, utwórz commit i opublikuj przez prompt albo ręcznie |
| [4. Praca nad zgłoszeniami równolegle][lesson-4] | Implementacja | Utwórz backlog, dodaj zgłoszenie do czatu, przejrzyj z `/diff` i uruchom drugą sesję w worktree |
| [5. Planowanie przed edycją][lesson-5] | Plan | Użyj `/plan`, aby uzgodnić podejście do drugiego zgłoszenia |
| [6. Co agent widzi][lesson-6] | Kontekst | Sprawdź i zresetuj kontekst poleceniami `/context` i `/clear` |
| [7. Wznawianie i praca zdalna][lesson-7] | Wznawianie | Opuszczaj i wracaj do sesji z `/resume`, a opcjonalnie kontynuuj z `/remote` |
| [8. Tworzenie, przegląd i scalanie][lesson-8] | Przegląd | Utwórz i scal pull request poleceniami `/pr create` i `/pr agentmerge` |
| [9. Delegowanie pracy][lesson-9] | Delegowanie | Przekaż nową funkcję do `/delegate` i śledź sesję w chmurze |
| [10. Podsumowanie i kolejne kroki][lesson-10] | Podsumowanie | Podsumuj przepływ pracy i kontynuuj naukę |

## Rozpocznij

[Zacznij od ćwiczenia 0: Wymagania wstępne i konfiguracja][lesson-0].

[james]: https://github.com/jamesmontemagno
[source-lab]: https://github.com/jamesmontemagno/first-steps-with-github-copilot
[source-license]: https://github.com/jamesmontemagno/first-steps-with-github-copilot/blob/main/LICENSE
[lesson-0]: 0-prerequisites/
[lesson-1]: 1-build/
[lesson-2]: 2-project-instructions/
[lesson-3]: 3-publish/
[lesson-4]: 4-issues-and-sessions/
[lesson-5]: 5-plan-mode/
[lesson-6]: 6-context/
[lesson-7]: 7-resume-and-remote/
[lesson-8]: 8-pull-request/
[lesson-9]: 9-delegate/
[lesson-10]: 10-review/
