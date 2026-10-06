---
slug: pl-pl/real-world-development/cli
title: "GitHub Copilot CLI"
description: "Zbuduj, zweryfikuj i dostarcz dwie zmiany Tailspin Toys, poznając tryby Copilot CLI, dostosowania, narzędzia MCP i automatyzację pull requestów."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-10-04
---

**[GitHub Copilot CLI][about-copilot-cli]** umieszcza GitHub Copilot w terminalu jako agentycznego asystenta programowania. Eksploruje bazy kodu, generuje kod, uruchamia polecenia i łączy się z zewnętrznymi narzędziami — wszystko z linii poleceń, dzięki czemu możesz pozostać w przepływie pracy bez przełączania się na edytor graficzny.

Warsztat prowadzi jednym ciągłym przepływem pracy Tailspin Toys:

1. Przygotuj projekt w GitHub Codespaces, zainstaluj Copilot CLI i zapoznaj się z narzędziem.
2. Wprowadź skupioną zmianę z oceną w gwiazdkach, przejrzyj ją w przeglądarce i ręcznie scal pierwszy pull request (PR).
3. Zacznij od zgłoszenia o filtrowaniu, zdefiniuj podejście w trybie Plan, zbuduj je w trybie Autopilot, a następnie przejrzyj w trybie Interactive.
4. Zaktualizuj instrukcje repozytorium i zastosuj je do pracy nad filtrowaniem.
5. Dostosuj istniejący skill `quality-checks` i użyj go do uruchomienia sprawdzeń projektu.
6. Dodaj serwer Model Context Protocol (MCP) Playwright i użyj go do zbadania filtrowania w przeglądarce.
7. Utwórz niestandardowego agenta zapewnienia jakości (QA) i użyj go do przeglądu wymagań, pokrycia oraz dowodów weryfikacji.
8. Przejrzyj kompletną zmianę filtrowania i użyj Agent Merge dla PR z filtrowaniem.
9. Poznaj przydatne polecenia slash do kontekstu, modeli, udostępniania oraz opcjonalnego delegowania do chmury.

Aby utrzymać skupienie warsztatu, utworzysz dwa PR: oceny w gwiazdkach, a potem filtrowanie wraz z aktualizacjami instrukcji, skillu, profilu QA i testów. Przepływ filtrowania i jakości dzieli jedną rozmowę i gałąź, żebyś mógł budować na swojej pracy, poznając kolejne narzędzia.

## Ćwiczenia

| Ćwiczenie | Temat | Opis |
| ------ | ----- | ----------- |
| [0. Wymagania wstępne][ex0] | Konfiguracja | Utwórz repozytorium i Codespace |
| [1. Instalacja Copilot CLI][ex1] | Instalacja | Zainstaluj i uwierzytelnij Copilot CLI, potem zapoznaj się z narzędziem |
| [2. Dodawanie ocen w gwiazdkach: szybki sukces][ex2] | Pierwsza zmiana | Wyświetl istniejące oceny i fallback dla wartości null, potem scal pierwszy PR |
| [3. Tryby agenta: Plan i Autopilot][ex3] | Tryby agenta | Zaplanuj funkcję na podstawie zgłoszenia, zbuduj z Autopilot, potem przejrzyj w trybie Interactive |
| [4. Prowadzenie Copilota instrukcjami niestandardowymi][ex4] | Kontekst | Poznaj i zaktualizuj instrukcje, potem zastosuj je do filtrowania |
| [5. Dostosowanie i użycie skillu quality-checks][ex5] | Powtarzalne sprawdzenia | Poznaj istniejący skill, zmień format raportu i uruchom go |
| [6. Walidacja funkcjonalności z Playwright MCP][ex6] | Obserwacja w przeglądarce | Skonfiguruj MCP w CLI i sprawdź zachowanie filtrowania |
| [7. Tworzenie i użycie agenta QA][ex7] | Wymagania i pokrycie | Utwórz i wybierz profil specjalisty, potem zbierz końcowe dowody weryfikacji |
| [8. Tworzenie i scalanie PR funkcji][ex8] | Przegląd i scalanie | Przejrzyj kompletną zmianę, utwórz PR i użyj Agent Merge |
| [9. Polecenia slash w GitHub Copilot CLI][ex9] | Funkcje CLI | Poznaj kontekst, modele, udostępnianie i opcjonalne delegowanie do cloud agent |
| [10. Podsumowanie i kolejne kroki][ex10] | Podsumowanie | Przejrzyj przepływ pracy, wielokrotnego użytku dostosowania i dalsze zasoby |
| [Opcjonalnie: Foundry][foundry] | Hostowani agenci | Przygotuj model, wdróż agenta opartego o katalog i podłącz go do witryny |

## Wymagania wstępne

Przed udziałem w tych warsztatach upewnij się, że masz:

- [ ] Konto GitHub z aktywnym planem **Copilot Student, Pro, Pro+, Business lub Enterprise**
- [ ] Uprawnienie do utworzenia repozytorium i Codespace
- [ ] Podstawową znajomość obsługi terminala lub linii poleceń

> [!TIP]
> Brak płatnego planu? Zweryfikowani studenci mogą otrzymać GitHub Copilot za darmo przez [GitHub Education][student-plan]. Plan **Copilot Student** obejmuje agenta, MCP, przegląd kodu i funkcje Copilot CLI używane w tych warsztatach.

> [!NOTE]
> Jeśli korzystasz z Copilot Business lub Copilot Enterprise, upewnij się, że administrator włączył Copilot CLI.

## Rozpocznij

**[Zacznij od wymagań wstępnych →][ex0]**

[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[student-plan]: https://github.com/education/students
[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-cli/
[ex2]: 2-add-star-rating/
[ex3]: 3-agent-modes/
[ex4]: 4-custom-instructions/
[ex5]: 5-agent-skills/
[ex6]: 6-mcp-playwright/
[ex7]: 7-qa-agent/
[ex8]: 8-create-pull-request/
[ex9]: 9-cli-power-tools/
[ex10]: 10-review/
[foundry]: 8-foundry-agent/
