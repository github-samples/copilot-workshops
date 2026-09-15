---
title: "Lekcja 8 - Podsumowanie i kolejne kroki"
description: "Podsumuj warsztaty z aplikacją GitHub Copilot, zautomatyzuj powtarzalną pracę i odkryj, jakie powinny być następne kroki."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-09
---

W ostatnich lekcjach przeprowadziłeś funkcjonalność aplikacji od pomysłu do scalenia za pomocą aplikacji GitHub Copilot, w tym:

- podłączenie repozytorium i zapoznanie się z interfejsem aplikacji oraz przygotowanym backlogiem.
- rozpoczynanie sesji od bezpośredniego polecenia i na podstawie zgłoszeń (issues) oraz używanie trybów Plan i Autopilot do sterowania pracą agenta.
- prowadzenie agenta instrukcjami niestandardowymi i wielokrotnego użytku skillem.
- testowanie pracy serwerem Playwright MCP w prawdziwej przeglądarce.
- współpracę z agentem na współdzielonej kanwie.
- wypychanie zmian za pomocą automatyzacji scalania — od samodzielnego scalania na github.com po scalenie pull requesta przez **Agent Merge**.

Zautomatyzujmy powtarzalną pracę, omówmy dobre praktyki i zobaczmy, dokąd iść dalej.

## Zautomatyzuj powtarzalną pracę

Aplikacja może uruchamiać agentów według harmonogramu lub na żądanie przez **automatyzacje** — świetne do rutynowych zadań, takich jak walidacja nowych zgłoszeń lub podsumowanie niedawnej aktywności. Utwórzmy prostą, która nie będzie wprowadzała trwałych zmian.

1. Wybierz **Automations** na pasku bocznym, a następnie **New automation**.
2. Nadaj nazwę, np. `Recap my recent work`.
3. Wybierz wyzwalacz. **Manual** pozwala uruchamiać na żądanie; **On a schedule** uruchamia automatycznie; **When an issue is created** reaguje na nowe zgłoszenia. W tej lekcji wybierz **Manual**.
4. Wprowadź polecenie tylko do odczytu, by automatyzacja nic nie zmieniała, na przykład:

   ```plaintext
   Summarize the pull requests merged in this repository over the last week, and list any issues still open in the backlog.
   ```

5. Wybierz projekt (repozytorium Tailspin Toys) i utwórz automatyzację.
6. Uruchom ją na żądanie, by zobaczyć wynik.

> [!TIP]
> Automatyzacje mogą działać lokalnie lub w chmurze. Włącz **Run in the cloud** i wybierz **Tools**, których automatyzacja może używać, gdy chcesz, by działała bez nadzoru według harmonogramu. Trzymaj zaplanowane automatyzacje w ograniczonym zakresie i nieniszczące, dopóki nie zaufasz ich wynikom.

## Dobre praktyki

Przy każdym narzędziu AI infrastruktura wokół niego determinuje jakość tego, co otrzymujesz. Pliki instrukcji, skille i agenci niestandardowi odegrały rolę w tym warsztacie — inwestuj w nie i wykorzystuj ponownie między sesjami.

Dopasuj **tryb i model** do zadania. Używaj **Plan**, by przemyśleć podejście przed budowaniem, **Interactive**, by na bieżąco rozmawiać z agentem przy złożonych zmianach, a **Autopilot** tylko przy dobrze opisanych, wyizolowanych zadaniach. Wybierz szybszy model do rutynowych edycji albo bardziej zdolny model z większymi możliwościami rozumowania do złożonej pracy — dopasuj wybór do konkretnego zadania.

Kontekst nadal ma znaczenie tak samo jak infrastruktura. Jasne opisanie *co* ma powstać, *dlaczego* i *jak* istotnie zmienia wynik. Szybkie czaty to świetne miejsce, by określić zakres pomysłu, zanim przeniesiesz się do pełnej sesji.

## Więcej do odkrycia

Poznałeś podstawowy tryb pracy z agentami. Kilka kolejnych funkcjonalności wartych uwagi:

- **Quick chats** do szybkich, jednorazowych pytań, które nie potrzebują pełnej sesji.
- **Rubber duck**, by przedyskutować problem i uzyskać wartościową informację zwrotną przed budowaniem.
- [**Agenci niestandardowi**][custom-agents], by zdefiniować rolę, jej narzędzia i instrukcje do powtarzalnej, specjalistycznej pracy.
- [`/chronicle`][chronicle], by wygenerować narrację tego, co wydarzyło się w sesji.
- [Własny klucz (BYOK)][byok], by używać modeli od własnego dostawcy, w tym lokalnych modeli przez Ollama, Foundry Local lub LM Studio.
- [Sandboxy chmurowe][sandboxes], by uruchamiać sesje w izolowanym środowisku hostowanym przez GitHuba.
- [Deep linki][deep-links], by otworzyć aplikację bezpośrednio w repozytorium, sesji lub poleceniu.

## Kolejne kroki

Najlepszy sposób, by poprawić swoje umiejętności pracy z każdym narzędziem, to nadal go używać! Używaj go do kodu produkcyjnego, hobbystycznego, do małej aplikacji, o której myślisz od lat, ale nigdy nie doszedłeś do zbudowania. Dziel się wnioskami z zespołem i ucz się od nich. I jak zawsze — czytaj dokumentację.

Jeśli chcesz poznać więcej ekosystemu GitHub Copilot, zajrzyj do [środowiska VS Code](../../vscode/), [środowiska Copilot CLI](../../cli/) lub [środowiska agenta chmurowego](../../cloud/).

## Zasoby

- [O aplikacji GitHub Copilot][about-copilot-app]
- [Pierwsze kroki z aplikacją GitHub Copilot][getting-started]
- [Dostosuj aplikację GitHub Copilot][customize]
- [Używanie automatyzacji][using-automations]
- [Praca z rozszerzeniami kanwy][canvas-docs]
- [O chmurowych i lokalnych sandboxach][sandboxes]

[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[customize]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[using-automations]: https://docs.github.com/copilot/how-tos/github-copilot-app/using-automations
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
[chronicle]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle
[custom-agents]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[byok]: https://docs.github.com/copilot/how-tos/github-copilot-app/use-byok-models
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links
