---
title: "Lekcja 10 - Podsumowanie i kolejne kroki"
description: "Podsumuj przepływ pracy aplikacji, dwa kamienie milowe PR, ćwiczenia z kanwami i powtarzalne praktyki jakości, potem poznaj dalsze zasoby."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-29
---

Używałeś aplikacji GitHub Copilot w ciągłym przepływie pracy Tailspin Toys. W tym warsztacie:

- podłączyłeś repozytorium, poznałeś obszar roboczy aplikacji i przygotowany backlog oraz spróbowałeś szybkiego czatu.
- rozpocząłeś skupioną sesję ocen w gwiazdkach, przejrzałeś wynik w kanwie przeglądarki i ręcznie scaliłeś pierwszy pull request (PR).
- zacząłeś od zgłoszenia o filtrowaniu, zdefiniowałeś podejście w trybie **Plan**, zbudowałeś je w trybie **Autopilot** i przejrzałeś w trybie **Interactive**.
- prowadziłeś agenta instrukcjami niestandardowymi, potem dostosowałeś istniejący skill `quality-checks` i użyłeś go do uruchomienia testów jednostkowych, lintu i sprawdzeń typów.
- dodałeś serwer Model Context Protocol (MCP) Playwright i użyłeś go do zbadania filtrowania w prawdziwej przeglądarce.
- utworzyłeś i wybrałeś niestandardowego agenta zapewnienia jakości (QA), by ocenić wymagania, pokrycie, wyniki skillu i dowody z przeglądarki.
- przejrzałeś kompletną zmianę filtrowania i autoryzowałeś **Agent Merge** dla drugiego PR.
- użyłeś istniejącej kanwy Database Explorer, a następnie utworzyłeś i przetestowałeś kanwę triage opartą o repozytorium.

## Co dostarczyłeś

Warsztat ma dwa kamienie milowe PR, każdy na własnej gałęzi od zaktualizowanego `main`:

1. **Oceny w gwiazdkach:** wyświetlenie istniejącego `starRating` oraz jawnego stanu bez oceny na kartach gier.
2. **Filtrowanie i przepływ jakości:** implementacja filtrowania, aktualizacja instrukcji i zastosowanie ich do funkcji, dostosowanie raportu `quality-checks`, utworzenie profilu QA oraz dołączenie powiązanych testów.

Od planowania filtrowania po otwarcie jego PR używałeś tej samej sesji, worktree i gałęzi. Połączyliśmy tę pracę w jednym PR, by usprawnić warsztat. Następnie użyłeś istniejącego Database Explorer i utworzyłeś kanwę triage opartą o repozytorium bez powtarzania przepływu PR.

## Różne rodzaje weryfikacji

Sprawdzałeś kod na kilka sposobów: automatyczne testy, własna kontrola w przeglądarce oraz eksploracja przeglądarki przez Copilota z MCP. Skill `quality-checks` uruchamiał testy jednostkowe, lint i sprawdzenia typów oraz raportował je w nowym formacie. QA zebrał te wyniki z przeglądem wymagań i pokrycia testami przed PR.

Dodane testy powinny zamykać rzeczywiste luki; przebieg QA, który nie wymaga nowych testów, może być poprawny. Brakujące narzędzia, pominięte sprawdzenia i niepowodzenia to widoczne blokery, a nie sukcesy. Przejrzyj kod i dowody przed autoryzacją scalenia i odśwież dotknięte dowody po zmianach.

## Dobre praktyki

Kontekst i narzędzia, które dajesz Copilotowi, kształtują jego pracę. W tym warsztacie zaktualizowałeś instrukcje, dostosowałeś skill, utworzyłeś profil QA, skonfigurowałeś serwer MCP i utworzyłeś kanwę. Ponownie wykorzystuj te personalizacje między sesjami i dostosowuj je, gdy zmieniają się potrzeby zespołu. Instrukcje ustalają standardy, skille opisują powtarzalne zadania, agenci niestandardowi definiują role specjalistów, serwery MCP łączą zewnętrzne narzędzia, a kanwy zapewniają współdzielone interaktywne powierzchnie. Przeglądaj rzeczywiste zmiany i wyniki narzędzi, a nie tylko podsumowanie agenta.

Dopasuj **tryb i model** do zadania. Używaj **Plan**, by przemyśleć podejście przed budową, **Interactive**, by pozostać w pętli przy skupionych zmianach, a **Autopilot** tylko przy dobrze ograniczonych, izolowanych zadaniach. Wybierz szybszy model do rutynowych edycji i bardziej zdolny model z wyższym wysiłkiem rozumowania do złożonej pracy.

Kontekst nadal ma taką samą wagę jak infrastruktura. Jasne opisanie *czego* chcesz zbudować, *dlaczego* i *jak* znacząco zmienia wynik. Szybkie czaty to dobre miejsce, by określić zakres pomysłu, zanim zobowiążesz się do pełnej sesji.

## Więcej do odkrycia

Poznałeś podstawowy przepływ pracy. Kilka kolejnych funkcji wartych uwagi:

- [**Automatyzacje**][using-automations] do zadań cyklicznych lub na żądanie, na przykład podsumowywania niedawnej pracy. Przed przyjęciem przejrzyj harmonogram, uprawnienia i zakres; utworzenie automatyzacji to kolejny krok, a nie część tego warsztatu.
- **Rubber duck**, by przegadać problem i uzyskać wysokiej jakości informację zwrotną przed budową.
- [`/chronicle`][chronicle], by wygenerować narrację tego, co wydarzyło się w sesji.
- [Bring your own key (BYOK)][byok], by używać modeli z własnego dostawcy, w tym modeli lokalnych przez Ollama, Foundry Local lub LM Studio.
- [Deep links][deep-links], by otworzyć aplikację od razu w repozytorium, sesji lub prompcie.

## Kolejne kroki

Najlepszym sposobem, by poprawić się w dowolnym narzędziu, jest dalsze z niego korzystanie! Używaj go do kodu produkcyjnego, hobbystycznego, do małej aplikacji, którą masz w głowie od lat, ale nigdy nie zacząłeś budować. Dziel się spostrzeżeniami z zespołem i ucz się od niego. I jak zawsze — przeglądaj dokumentację.

Jeśli chcesz poznać więcej ekosystemu GitHub Copilot, sprawdź [środowisko VS Code][vscode-harness], [środowisko Copilot CLI][cli-harness] lub [środowisko agenta w chmurze][cloud-harness].

## Zasoby

- [About the GitHub Copilot app][about-copilot-app]
- [Getting started with the GitHub Copilot app][getting-started]
- [Customize the GitHub Copilot app][customize]
- [Using automations][using-automations]
- [Working with canvas extensions][canvas-docs]

[vscode-harness]: ../../vscode/
[cli-harness]: ../../cli/
[cloud-harness]: ../../cloud/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[customize]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[using-automations]: https://docs.github.com/copilot/how-tos/github-copilot-app/using-automations
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[chronicle]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle
[byok]: https://docs.github.com/copilot/how-tos/github-copilot-app/use-byok-models
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links
