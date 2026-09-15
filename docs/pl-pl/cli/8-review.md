---
title: "Ćwiczenie 8 - Podsumowanie i kolejne kroki"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-10
---

W ostatnich ćwiczeniach poznałeś niektóre z najczęstszych przypadków użycia GitHub Copilot CLI, w tym:

- interakcję z GitHubem i innymi serwerami MCP.
- używanie plików instrukcji do kierowania generowaniem kodu.
- implementację skilli dodających narzędzia do funkcjonalności Copilot CLI.
- wywoływanie agentów niestandardowych do zaawansowanych i bardziej złożonych zadań.
- używanie poleceń slash do zarządzania sesją oraz opcjonalne łączenie z agentami w chmurze przez `/delegate`.

Omówmy kilka poleceń slash, dobre praktyki i kolejne kroki.

## Polecenia slash

Copilot CLI ma szereg poleceń slash do interakcji z nim, w tym takie, które pozwalają go dokładniej skonfigurować lub zobaczyć, co dzieje się za kulisami. Już użyłeś `/clear`, aby rozpocząć nową rozmowę czyszczącą bieżący kontekst, oraz `/mcp` do przeglądania i zarządzania serwerami MCP. Kilka dodatkowych, które mogą być pomocne:

| Polecenie          | Opis                                                          |
| ------------------ | ------------------------------------------------------------- |
| `/add-dir`         | Dodaj katalog do listy zaufanych dla Copilota                  |
| `/clear`, `/new`   | Wyczyść historię rozmowy i zacznij od nowa                    |
| `/compact`         | Podsumuj historię rozmowy, aby zmniejszyć użycie okna kontekstu |
| `/context`         | Pokaż użycie tokenów okna kontekstu i wizualizację            |
| `/diff`            | Przejrzyj zmiany wprowadzone w bieżącym katalogu              |
| `/model`           | Wybierz model AI do użycia (Claude Sonnet, GPT-5 itd.)        |
| `/plan <prompt>`   | Utwórz plan implementacji przed kodowaniem                    |
| `/review <prompt>` | Uruchom agenta przeglądu kodu do analizy zmian                |
| `/delegate`        | Deleguj zadanie do agenta Copilot w chmurze do przetwarzania asynchronicznego |
| `/session`         | Pokaż informacje o sesji i podsumowanie obszaru roboczego |
| `/share`           | Udostępnij sesję do pliku markdown lub gista GitHub           |
| `/skills`          | Zarządzaj skillami w celu rozszerzenia możliwości             |
| `/usage`           | Wyświetl metryki i statystyki użycia sesji                    |

> [!TIP]
> Użyj `/help`, aby zobaczyć pełną listę dostępnych poleceń i skrótów klawiszowych.

## Dobre praktyki

Przy korzystaniu z dowolnego narzędzia AI jakość wyniku w dużej mierze zależy od przygotowanej infrastruktury. Solidne pliki instrukcji, agenci niestandardowi i skille agenta odgrywają rolę — każde z nich poznałeś w tych warsztatach. [awesome-copilot][awesome-copilot] to dobre źródło szablonów, a sam Copilot może wygenerować ich szkielet jako punkt startowy.

Kontekst nadal ma znaczenie tak samo jak infrastruktura. Jasne opisanie *czego* chcesz, *dlaczego* i *jak* znacząco zmienia wynik. Jeśli jakaś informacja pomoże Copilotowi — przekaż ją.

## Kolejne kroki

Najlepszym sposobem na poprawę umiejętności z dowolnym narzędziem jest wykorzystanie go do dalszych eksperymentów i pracy! Używaj go do kodu produkcyjnego, hobbystycznego, do tej małej aplikacji, którą masz w głowie od lat, ale nigdy nie zabrałeś się do budowy. Dziel się wnioskami z zespołem i ucz się od zespołu. I jak zawsze — przeglądaj dokumentację.

Jeśli chcesz poznać więcej ekosystemu GitHub Copilot, zobacz [środowisko VS Code](../../vscode/) lub [środowisko Cloud agent](../../cloud/).

## Zasoby

- [O Copilot CLI][about-copilot-cli]
- [Korzystanie z Copilot CLI][using-copilot-cli]
- [Repozytorium Awesome Copilot][awesome-copilot]
- [Przewodnik po instrukcjach niestandardowych][repo-instructions]
- [Dokumentacja Agent Skills][agent-skills]
- [Dokumentacja agentów niestandardowych][custom-agents]
- [Specyfikacja MCP][mcp-spec]

[previous-lesson]: ../7-slash-commands/
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[awesome-copilot]: https://github.com/github/awesome-copilot
[repo-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[mcp-spec]: https://modelcontextprotocol.io/
