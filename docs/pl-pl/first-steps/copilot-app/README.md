---
title: "Przewodnik po aplikacji GitHub Copilot"
description: "Poznaj aplikację GitHub Copilot w praktyce, budując i wdrażając Space Quiz."
slug: pl-pl/first-steps/copilot-app
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Poznaj aplikację GitHub Copilot w praktycznym, przyjaznym dla początkujących przewodniku. Zbudujesz kolorowy Space Quiz z pustego folderu i przejdziesz przez pełną pętlę rozwoju — od pierwszego promptu do przejrzanego pull requesta.

Warsztat zajmuje około 60–90 minut. Projekt to pojedynczy plik HTML bez zależności runtime, dzięki czemu możesz skupić się na aplikacji i jej przepływach pracy z agentami.

> [!NOTE]
> Ten warsztat stworzył [James Montemagno][james], a został zaadaptowany z [First Steps with GitHub Copilot][source-lab]. Oryginalna treść jest dostępna na licencji [MIT][source-license].

## Lekcje

| Lekcja | Temat | Co zrobisz |
| ------ | ----- | ---------- |
| [0. Wymagania wstępne i konfiguracja][lesson-0] | Konfiguracja | Sprawdzisz wymagania wstępne, zainstalujesz aplikację, wybierzesz model i poznasz obszar roboczy |
| [1. Utwórz obszar roboczy][lesson-1] | Tworzenie | Uruchomisz sesję Interactive w pustym folderze lokalnym |
| [2. Zbuduj i dopracuj][lesson-2] | Budowanie | Utworzysz quiz i dopracujesz go w zintegrowanej przeglądarce |
| [3. Przejrzyj i przetestuj][lesson-3] | Kontekst i test | Przeczytasz szczegóły sesji i uruchomisz smoke test na poziomie przeglądarki |
| [4. Zapisz instrukcje projektu][lesson-4] | Instrukcje | Wygenerujesz i dostosujesz instrukcje agenta za pomocą `/init` |
| [5. Opublikuj projekt][lesson-5] | Publikacja | Utworzysz publiczne repozytorium GitHub z lokalnego projektu |
| [6. Praca ze zgłoszeniami i sesjami][lesson-6] | Implementacja | Utworzysz backlog, zaimplementujesz jedno zgłoszenie w izolowanym worktree i przejrzysz diff |
| [7. Zaplanuj przed edycją][lesson-7] | Planowanie | Użyjesz trybu Plan, aby uzgodnić podejście do drugiego zgłoszenia |
| [8. Dokończ pętlę przeglądu][lesson-8] | Przegląd | Otworzysz pull request, odpowiesz na uwagi z przeglądu Copilot i użyjesz Agent Merge |
| [9. Zautomatyzuj triage zgłoszeń][lesson-9] | Automatyzacja | Zaplanujesz i uruchomisz cotygodniową automatyzację triage zgłoszeń |
| [10. Kontynuuj sesję zdalnie][lesson-10] | Zdalnie (opcjonalnie) | Kontynuujesz trwającą sesję na GitHubie za pomocą `/remote` |
| [11. Poznaj kanwę][lesson-11] | Kanwa | Zaczniesz pracę z kanwy Repository Issues Kanban |
| [12. Podsumowanie i kolejne kroki][lesson-12] | Podsumowanie | Podsumujesz przepływ pracy i przejdziesz do dalszej nauki |

## Rozpocznij

[Zacznij od Lekcji 0: Wymagania wstępne i konfiguracja][lesson-0].

[james]: https://github.com/jamesmontemagno
[source-lab]: https://github.com/jamesmontemagno/first-steps-with-github-copilot
[source-license]: https://github.com/jamesmontemagno/first-steps-with-github-copilot/blob/main/LICENSE
[lesson-0]: 0-prerequisites/
[lesson-1]: 1-create-workspace/
[lesson-2]: 2-build-and-polish/
[lesson-3]: 3-inspect-and-test/
[lesson-4]: 4-project-instructions/
[lesson-5]: 5-publish/
[lesson-6]: 6-issues-and-sessions/
[lesson-7]: 7-plan-mode/
[lesson-8]: 8-review-loop/
[lesson-9]: 9-automations/
[lesson-10]: 10-remote/
[lesson-11]: 11-canvas/
[lesson-12]: 12-review/
