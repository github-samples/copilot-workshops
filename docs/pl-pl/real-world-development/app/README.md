---
slug: pl-pl/real-world-development/app
title: "Aplikacja GitHub Copilot"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-10-04
---

**[Aplikacja GitHub Copilot](https://docs.github.com/copilot/concepts/agents/github-copilot-app)** to aplikacja desktopowa oparta na Copilot CLI, która łączy rozwój sterowany agentami w jednym, skoncentrowanym obszarze roboczym. Dodaje równoległe sesje agentów, przełączalne tryby sesji, współdzielone kanwy oraz natywne zarządzanie zgłoszeniami i pull requestami GitHub — w tym **Agent Merge**, który przeprowadza pull request przez rebase, uwagi z przeglądu, poprawki ciągłej integracji (CI) i scalenie.

Warsztat prowadzi jednym ciągłym przepływem pracy Tailspin Toys:

1. Przygotuj projekt, zainstaluj aplikację, podłącz repozytorium i poznaj obszar roboczy oraz przygotowany backlog.
2. Wprowadź skupioną zmianę z oceną w gwiazdkach, przejrzyj ją w przeglądarce i ręcznie scal pierwszy pull request (PR).
3. Zacznij od zgłoszenia o filtrowaniu, zdefiniuj podejście w trybie **Plan**, zbuduj je w trybie **Autopilot**, a następnie przejrzyj w trybie **Interactive**.
4. Zaktualizuj instrukcje repozytorium i zastosuj je do pracy nad filtrowaniem.
5. Dostosuj istniejący skill `quality-checks` i użyj go do uruchomienia sprawdzeń projektu.
6. Dodaj serwer Model Context Protocol (MCP) Playwright i użyj go do zbadania filtrowania w przeglądarce.
7. Utwórz niestandardowego agenta zapewnienia jakości (QA) i użyj go do przeglądu wymagań, pokrycia oraz dowodów weryfikacji.
8. Przejrzyj kompletną zmianę filtrowania i użyj Agent Merge dla drugiego PR.
9. Skorzystaj z istniejącej kanwy Database Explorer, a następnie utwórz i przetestuj kanwę triage opartą o repozytorium.

Aby utrzymać skupienie warsztatu, utworzysz dwa PR: oceny w gwiazdkach, a potem filtrowanie wraz z aktualizacjami instrukcji, skillu, profilu QA i testów. Każdy zaczynaj od zaktualizowanego `main`. Przepływ filtrowania i jakości dzieli jedną sesję, worktree i gałąź, żebyś mógł budować na swojej pracy, poznając kolejne narzędzia. Końcowe ćwiczenie z kanwą pozostaje we własnej sesji, abyś mógł skupić się na tworzeniu i testowaniu współdzielonej powierzchni zamiast powtarzać przepływ PR.

## Lekcje

| Lekcja | Temat | Opis |
|--------|-------|------|
| [0. Wymagania wstępne][ex0] | Konfiguracja | Zainstaluj Node.js i utwórz swoją kopię projektu Tailspin Toys |
| [1. Instalacja aplikacji Copilot][ex1] | Konfiguracja | Zainstaluj aplikację, podłącz projekt i zapoznaj się z obszarem roboczym |
| [2. Dodawanie ocen w gwiazdkach: szybki sukces][ex2] | Pierwsza zmiana | Wyświetl istniejące oceny i fallback dla wartości null, potem scal PR 1 |
| [3. Tryby agenta: Plan i Autopilot][ex3] | Tryby agenta | Zaplanuj funkcję na podstawie zgłoszenia, zbuduj z Autopilot, potem przejrzyj w trybie Interactive |
| [4. Prowadzenie Copilota instrukcjami niestandardowymi][ex4] | Kontekst | Poznaj i zaktualizuj instrukcje, potem zastosuj je do filtrowania |
| [5. Dostosowanie i użycie skillu quality-checks][ex5] | Powtarzalne sprawdzenia | Poznaj istniejący skill, zmień format raportu i uruchom go |
| [6. Walidacja funkcjonalności z Playwright MCP][ex6] | Obserwacja w przeglądarce | Skonfiguruj MCP przez Customize i sprawdź zachowanie filtrowania |
| [7. Tworzenie i użycie agenta QA][ex7] | Wymagania i pokrycie | Utwórz i wybierz profil specjalisty, potem zbierz końcowe dowody weryfikacji |
| [8. Tworzenie i scalanie PR funkcji][ex8] | Przegląd i scalanie | Przejrzyj filtrowanie, instrukcje, skill, profil QA i testy, potem użyj Agent Merge dla drugiego PR |
| [9. Eksploracja i tworzenie kanw][ex9] | Współpraca | Użyj Database Explorer, potem utwórz i przetestuj kanwę triage opartą o repozytorium |
| [10. Podsumowanie i kolejne kroki][ex10] | Podsumowanie | Przejrzyj przepływ pracy, artefakty i dalsze zasoby |

## Wymagania wstępne

Przed udziałem w tych warsztatach upewnij się, że masz:

- [ ] Konto GitHub z aktywnym planem **Copilot Student, Pro, Pro+, Business lub Enterprise**
- [ ] Komputer z **macOS, Linux lub Windows**
- [ ] [Zainstalowany Git][install-git] na komputerze

> [!TIP]
> Brak płatnego planu? Zweryfikowani studenci mogą otrzymać GitHub Copilot za darmo przez [GitHub Education][callout-student-plan-education]. Plan **Copilot Student** obejmuje agenta, MCP, przegląd kodu i funkcje Copilot CLI używane w tych warsztatach — dzięki temu ukończysz każde środowisko.

> [!NOTE]
> Ponieważ aplikacja Copilot działa na Twoim komputerze, a nie w codespace, [ćwiczenie wymagań wstępnych][ex0] przeprowadza Cię przez instalację Node.js i utworzenie kopii projektu przed instalacją aplikacji.

> [!NOTE]
> Jeśli korzystasz z Copilot Business lub Copilot Enterprise, administrator musi włączyć zasadę **Copilot CLI**, zanim będziesz mógł używać aplikacji.

## Rozpocznij

**[Zacznij od wymagań wstępnych →][ex0]**

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-app/
[ex2]: 2-add-star-rating/
[ex3]: 3-agent-modes/
[ex4]: 4-custom-instructions/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-canvases/
[ex10]: 10-review/
[install-git]: https://github.com/git-guides/install-git
[callout-student-plan-education]: https://github.com/education/students
