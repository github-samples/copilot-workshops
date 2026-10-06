---
title: "Ćwiczenie 10 - Podsumowanie i kolejne kroki"
description: "Podsumuj przepływ Copilot CLI, dwa pull requesty, dostosowania wielokrotnego użytku i dalsze zasoby."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-29
---

Używałeś GitHub Copilot CLI w ciągłym przepływie pracy Tailspin Toys. W trakcie warsztatu:

- przygotowałeś Codespace, zainstalowałeś Copilot CLI, poznałeś projekt i znalazłeś wcześniej przygotowane zgłoszenie o filtrowaniu.
- dodałeś oceny w gwiazdkach, przejrzałeś wynik w przeglądarce z przekierowaniem portu i ręcznie scaliłeś pierwszy pull request (PR).
- zacząłeś od zgłoszenia o filtrowaniu, zdefiniowałeś podejście w trybie Plan, zbudowałeś je w trybie Autopilot i przejrzałeś w trybie Interactive.
- pokierowałeś agentem instrukcjami niestandardowymi, potem dostosowałeś istniejący skill `quality-checks` i użyłeś go do uruchomienia testów jednostkowych, lintu oraz sprawdzeń typów.
- dodałeś serwer Model Context Protocol (MCP) Playwright i użyłeś go do zbadania filtrowania w prawdziwej przeglądarce.
- utworzyłeś i wybrałeś agenta niestandardowego zapewnienia jakości (QA), by ocenić wymagania, pokrycie, wyniki skillu i dowody z przeglądarki.
- przejrzałeś kompletną zmianę filtrowania i autoryzowałeś Agent Merge dla PR z filtrowaniem.
- poznałeś polecenia slash do kontekstu, modeli, udostępniania i opcjonalnego delegowania do chmury.

## Co dostarczyłeś

Warsztat ma dwa kamienie milowe PR, każdy na własnej gałęzi od zaktualizowanego `main`:

1. **Oceny w gwiazdkach:** wyświetlenie istniejącego `starRating` oraz jawnego stanu bez oceny na kartach gier.
2. **Filtrowanie i przepływ jakości:** implementacja filtrowania, aktualizacja instrukcji i zastosowanie ich do funkcji, dostosowanie raportu `quality-checks`, utworzenie profilu QA oraz dołączenie powiązanych testów.

Od planowania filtrowania po otwarcie jego PR używałeś tej samej rozmowy i gałęzi. Połączyliśmy tę pracę w jednym PR, by usprawnić warsztat.

## Różne rodzaje weryfikacji

Sprawdzałeś kod na kilka sposobów: automatycznymi testami, własną kontrolą w przeglądarce oraz eksploracją przeglądarki przez Copilota z MCP. Skill `quality-checks` uruchamiał testy jednostkowe, lint i sprawdzenia typów oraz raportował je w nowym formacie. QA zebrał te wyniki z przeglądem wymagań i pokrycia testami przed PR.

Dodawane testy powinny zamykać rzeczywiste luki; przebieg QA, który nie wymaga nowych testów, też może być poprawny. Przejrzyj kod i dowody przed autoryzacją scalania i odśwież powiązane dowody po zmianach.

## Dobre praktyki

Kontekst i narzędzia, które dajesz Copilotowi, kształtują jego pracę. W tych warsztatach zaktualizowałeś instrukcje, dostosowałeś skill, utworzyłeś profil QA i skonfigurowałeś serwer MCP. Wykorzystuj te dostosowania w kolejnych rozmowach i zmieniaj je wraz z potrzebami zespołu. Instrukcje ustalają standardy, skille opisują powtarzalne zadania, agenci niestandardowi definiują role specjalistów, a serwery MCP łączą zewnętrzne narzędzia. Przeglądaj rzeczywiste zmiany i wyniki narzędzi, a nie tylko podsumowanie agenta.

Dopasuj **tryb i model** do zadania. Użyj **Plan**, by przemyśleć podejście przed budową, **Interactive**, by pozostać w pętli przy skupionych zmianach, oraz **Autopilot** dla dobrze określonych zadań. Wybierz szybszy model do rutynowych edycji i bardziej zdolny do złożonej pracy.

Kontekst nadal ma znaczenie tak samo jak infrastruktura. Jasne opisanie *czego* chcesz, *dlaczego* i *jak* znacząco zmienia wynik.

## Więcej do odkrycia

Poznałeś podstawowy przepływ. Kilka kolejnych funkcji CLI wartych uwagi:

- `/review`, by poprosić agenta przeglądu kodu o analizę zmian.
- `/rubber-duck`, by przegadać problem i uzyskać inną perspektywę.
- `/fleet`, by orkiestrować niezależne podzadania równolegle.
- `/worktree`, by izolować osobne zadanie.
- `/delegate`, by wysłać zadanie do Copilot cloud agent.

## Kolejne kroki

Najlepszym sposobem na poprawę umiejętności z dowolnym narzędziem jest dalsze korzystanie z niego! Używaj go do kodu produkcyjnego, hobbystycznego, do tej małej aplikacji, którą masz w głowie od lat, ale nigdy nie zabrałeś się do budowy. Dziel się wnioskami z zespołem i ucz się od zespołu. I jak zawsze — przeglądaj dokumentację.

Jeśli chcesz rozszerzyć Tailspin Toys z terminala, kontynuuj opcjonalną [serię Foundry Backer Concierge][foundry]. Aby porównać inne środowiska, zobacz [warsztat VS Code][vscode], [warsztat aplikacji GitHub Copilot][app] lub [warsztat Copilot cloud agent][cloud].

## Zasoby

- [About GitHub Copilot CLI][about-cli]
- [Copilot CLI command reference][cli-reference]
- [Customize Copilot CLI][customize-cli]
- [Manage pull requests with Copilot CLI][manage-prs]

[previous-lesson]: ../9-cli-power-tools/
[foundry]: ../8-foundry-agent/
[vscode]: ../../vscode/
[app]: ../../app/
[cloud]: ../../cloud/
[about-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[customize-cli]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot
[manage-prs]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/manage-pull-requests
