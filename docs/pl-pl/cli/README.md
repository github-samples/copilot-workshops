---
slug: pl-pl/cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-10
---

**[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** umieszcza GitHub Copilot w terminalu jako agentycznego asystenta programowania. Eksploruje bazy kodu, generuje kod, uruchamia polecenia i łączy się z zewnętrznymi narzędziami — wszystko z linii poleceń, dzięki czemu możesz pozostać w przepływie pracy bez przełączania się na edytor graficzny.

Podczas tych ćwiczeń zainstalujesz i uwierzytelnisz Copilot CLI, a następnie dasz mu kontekst projektu za pomocą instrukcji niestandardowych, zanim użyjesz trybu planowania do świadomego wygenerowania funkcji. Połączysz serwer Playwright MCP, aby przetestować tę funkcję w prawdziwej przeglądarce, a potem rozszerzysz Copilota o skille agenta wielokrotnego użytku i agentów niestandardowych. Na koniec poznasz polecenia slash do zarządzania kontekstem, modelami i udostępnianiem, a zakończysz przeglądem tego, co zbudowałeś.

## Ćwiczenia

| Ćwiczenie | Temat | Opis |
|----------|-------|-------------|
| [0. Wymagania wstępne][ex0] | Konfiguracja | Utwórz własną kopię repozytorium i codespace |
| [1. Instalacja Copilot CLI][ex1] | Instalacja | Zainstaluj i uwierzytelnij Copilot CLI |
| [2. Instrukcje niestandardowe][ex2] | Kontekst | Dodaj instrukcję i zobacz, jak Copilot CLI jej przestrzega |
| [3. Generowanie kodu][ex3] | Generowanie kodu | Użyj trybu planowania i generuj funkcje |
| [4. Testowanie z Playwright MCP][ex4] | Narzędzia zewnętrzne | Dodaj serwer Playwright MCP i przetestuj funkcję w przeglądarce |
| [5. Skille agenta][ex5] | Skille | Rozszerz Copilota o wyspecjalizowane skille |
| [6. Agenci niestandardowi][ex6] | Agenci | Przejrzyj i użyj agentów niestandardowych |
| [7. Polecenia slash][ex7] | Funkcje CLI | Poznaj kontekst, modele, udostępnianie i opcjonalne delegowanie do cloud agent |
| [8. Podsumowanie][ex8] | Podsumowanie | Przypomnij kluczowe pojęcia i kolejne kroki |

## Wymagania wstępne

Przed udziałem w tych warsztatach upewnij się, że masz:

- [ ] Konto GitHub z aktywnym planem **Copilot Student, Pro, Pro+, Business lub Enterprise**
- [ ] Podstawową znajomość obsługi terminala/linii poleceń
- [ ] Zainstalowany i skonfigurowany Git

> [!TIP]
> Brak płatnego planu? Zweryfikowani studenci mogą uzyskać GitHub Copilot za darmo przez [GitHub Education][callout-student-plan-education]. Plan **Copilot Student** obejmuje agenta, MCP, przegląd kodu i funkcje Copilot CLI używane w tych warsztatach — dzięki temu ukończysz każdą ze ścieżek.

> [!NOTE]
> Jeśli korzystasz z Copilot Business lub Copilot Enterprise, upewnij się, że administrator włączył Copilot CLI.

## Rozpocznij

**[Zacznij od Ćwiczenia 0: Wymagania wstępne →][ex0]**

[ex0]: 0-prerequisites/
[ex1]: 1-install-copilot-cli/
[ex2]: 2-custom-instructions/
[ex3]: 3-generating-code/
[ex4]: 4-mcp/
[ex5]: 5-agent-skills/
[ex6]: 6-custom-agents/
[ex7]: 7-slash-commands/
[ex8]: 8-review/
[callout-student-plan-education]: https://github.com/education/students
