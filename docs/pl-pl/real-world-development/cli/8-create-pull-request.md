---
title: "Ćwiczenie 8 - Tworzenie i scalanie PR funkcji"
description: "Przejrzyj filtrowanie, instrukcje, aktualizację skillu, profil QA i testy razem, potem utwórz PR i użyj Agent Merge."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-18
---

Implementacja filtrowania, aktualizacje instrukcji, aktualizacja skillu, profil zapewnienia jakości (QA) i testy są zapisane na jednej gałęzi. Czas przejrzeć je razem i otworzyć pull request. Pull request (PR) z ocenami w gwiazdkach scaliłeś samodzielnie; tym razem pozwolisz **Agent Merge** zarządzać procesem.

> [!NOTE]
> Zwykle podzielilibyśmy funkcję, aktualizacje instrukcji, aktualizację skillu i agenta QA na kilka osobnych PR. Aby usprawnić warsztat, utrzymałeś pełny przepływ filtrowania i jakości w jednej rozmowie i gałęzi — cała ta praca trafia do tego PR.

W tym ćwiczeniu:

- poznasz, czym jest Agent Merge i jak automatyzuje cykl życia scalania.
- przejrzysz pełną zmianę funkcji oraz dowody weryfikacji.
- utworzysz PR z filtrowaniem.
- włączysz Agent Merge dopiero po przeglądzie i potwierdzisz, że PR został scalony.

## Scenariusz

W całym przepływie filtrowania używałeś Copilota do planowania, implementacji i weryfikacji funkcji. Tailspin Toys chce teraz zautomatyzować pozostałą pracę nad PR, zachowując jednocześnie autoryzację scalania pod kontrolą dewelopera.

## Przedstawiamy Agent Merge

**Agent Merge** automatyzuje pozostałą pracę potrzebną do doprowadzenia pull requesta do scalenia. Gdy go włączysz, Copilot zajmuje się tym, co blokuje PR — naprawiając nieudane sprawdzenia ciągłej integracji (CI), odpowiadając na komentarze z przeglądu i robiąc rebase w razie potrzeby — a następnie włącza GitHub auto-merge, gdy repozytorium na to pozwala.

Dotąd sam wybierałeś **Merge pull request**. Agent Merge może przejąć tę odpowiedzialność. Przejrzyj pracę i zdecyduj, że jest gotowa, zanim włączysz Agent Merge.

## Użyj Agent Merge do zarządzania PR

Mając cały kod utworzony, przejrzyjmy go razem, utwórzmy PR i pozwólmy Agent Merge zarządzać resztą procesu.

1. Wróć do Codespace.
2. Otwórz dialog agenta, wpisując `/agent`.
3. Wybierz **Default** z listy opcji i wciśnij <kbd>Enter</kbd>.
4. Utwórz nowy PR poleceniem `/pr create`.
5. Aktywuj Agent Merge poleceniem `/pr agentmerge`
6. Copilot będzie obserwować proces ciągłej integracji na PR. Gdy wszystko się powiedzie, wykona scalenie.
7. Upewnij się, że widzisz komunikat od Copilota podobny do „PR #14 was squash-merged successfully.”

> [!IMPORTANT]
> Agent Merge nie omija wymaganych zatwierdzeń, ochrony gałęzi, kolejek scalania, ustawień repozytorium ani brakujących uprawnień. Jeśli jest zablokowany, przeczytaj podany powód i wykonaj przejrzane scalenie ręcznie, gdy repozytorium na to pozwala.

## Podsumowanie i kolejne kroki

Zautomatyzowałeś kilka części procesu deweloperskiego, w tym generowanie kodu, testowanie i walidację, a teraz także proces pull request. W tym ćwiczeniu:

- poznałeś, czym jest Agent Merge i jak automatyzuje cykl życia scalania.
- przejrzałeś pełną zmianę funkcji oraz dowody weryfikacji.
- utworzyłeś PR z filtrowaniem.
- włączyłeś Agent Merge dopiero po przeglądzie i potwierdziłeś, że PR został scalony.

Następnie [poznasz bardziej przydatne polecenia slash Copilot CLI][next-lesson] do kontekstu, modeli, udostępniania i opcjonalnego delegowania do chmury.

## Zasoby

- [Manage pull requests with Copilot CLI][manage-prs]
- [Copilot CLI command reference][cli-reference]

[previous-lesson]: ../7-qa-agent/
[next-lesson]: ../9-cli-power-tools/
[manage-prs]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/manage-pull-requests
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
