---
title: "Lekcja 5 - Testowanie z serwerem Playwright MCP"
description: "Dodaj serwer Playwright MCP do aplikacji GitHub Copilot i poproś agenta o ręczne przetestowanie funkcji filtrowania w prawdziwej przeglądarce."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-09
---

W poprzedniej lekcji utworzyłeś i zweryfikowałeś funkcję filtrowania zautomatyzowanym zestawem testów projektu. Testy automatyzują walidację kodu, ale pozwolenie agentowi na potwierdzenie zachowania pozwala na znacznie lepszą walidację. Umożliwia agentowi reagowanie na problemy, które widzi w faktycznym UI, które stworzył. Zbadajmy, jak MCP daje agentom AI dostęp do zewnętrznych możliwości i dodajmy serwer Playwright MCP, aby Copilot mógł bezpośrednio wchodzić w interakcję z budowaną witryną.

Podczas tej lekcji:

- zrozumiesz, czym jest Model Context Protocol (MCP) i jak aplikacja GitHub Copilot go używa.
- dodasz serwer Playwright MCP z ustawień aplikacji.
- poprosisz agenta o sterowanie przeglądarką i zbadanie funkcji filtrowania.

## Scenariusz

Choć testy jednostkowe i end-to-end są ważne, walidacja zmian w interfejsie użytkownika wymaga faktycznej interakcji z UI. Chcesz, by Copilot korzystał z witryny, nad którą pracujesz, jak użytkownik — by dalej automatyzować wprowadzanie zmian i mieć większą pewność, że aktualizacje działają zgodnie z oczekiwaniami.

## Czym jest Model Context Protocol (MCP)?

[Model Context Protocol (MCP)][mcp-blog-post] określa sposób komunikacji agentów AI z zewnętrznymi narzędziami i usługami. Dzięki MCP agenci AI mogą komunikować się z zewnętrznymi narzędziami i usługami w czasie rzeczywistym. Pozwala im to uzyskiwać aktualne informacje (za pomocą zasobów) i wykonywać działania w Twoim imieniu (za pomocą narzędzi).

Te narzędzia i zasoby są dostępne przez serwer MCP, który działa jako most między agentem AI a zewnętrznymi narzędziami i usługami. Serwer MCP zarządza komunikacją między agentem AI a zewnętrznymi narzędziami (np. istniejącymi API lub lokalnymi narzędziami jak pakiety NPM). Każdy serwer MCP reprezentuje inny zestaw narzędzi i zasobów dostępnych dla agenta AI.

Kilka popularnych istniejących serwerów MCP:

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**: Ten serwer zapewnia dostęp do zestawu API do zarządzania repozytoriami GitHub. Pozwala agentowi AI wykonywać działania takie jak tworzenie nowych repozytoriów, aktualizowanie istniejących oraz zarządzanie zgłoszeniami (issues) i pull requestami.
- **[Playwright MCP Server][playwright-mcp-server]**: Ten serwer zapewnia automatyzację przeglądarki za pomocą Playwright. Pozwala agentowi AI wykonywać działania takie jak nawigacja pomiędzy stronami, wypełnianie formularzy i klikanie przycisków.

Dostępnych jest wiele innych serwerów MCP zapewniających dostęp do różnych narzędzi i zasobów. GitHub hostuje [rejestr MCP](https://github.com/mcp), aby ułatwić dostęp do tych, których możesz potrzebować, jednocześnie wspierając cały ekosystem.

> [!CAUTION]
> Traktuj serwery MCP jak każdą inną zależność w projekcie. Przed użyciem serwera MCP dokładnie przejrzyj jego kod źródłowy, zweryfikuj wydawcę i rozważ potencjalne konsekwencje dla bezpieczeństwa rzeczy, z którymi pracujesz. Używaj tylko serwerów MCP, którym ufasz, i ostrożnie przyznawaj dostęp do wrażliwych zasobów lub operacji.

## Dodaj serwer Playwright MCP

Serwery MCP dodajesz i zarządzasz nimi w ustawieniach aplikacji. Aplikacja zawiera katalog popularnych serwerów, więc [serwer Playwright MCP][playwright-mcp-server] jest stosunkowo łatwy do znalezienia.

1. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>,</kbd>, aby otworzyć stronę ustawień aplikacji Copilot.
2. Wybierz **MCP servers**.
3. W oknie wyszukiwania wpisz `Playwright`.
4. Wybierz **Playwright** z listy **Popular MCP servers**.
5. Wybierz **Add server**, aby dodać go do listy dostępnych serwerów MCP.
6. Wciśnij <kbd>Esc</kbd>, aby zamknąć okno ustawień.

Dodałeś serwer Playwright MCP!

## Poproś Copilota o zbadanie funkcji przez Playwright

Poprośmy Copilota o ręczne przetestowanie funkcji za pomocą serwera Playwright MCP.

1. Użyj poniższego polecenia, aby poprosić Copilota o walidację nowej funkcjonalności:

   ```plaintext
   Start the dev server then use the Playwright MCP server to validate the functionality you just added exists. Use the details in the issue to ensure the newly added behavior matches the specs.
   ```

Copilot uruchomi przeglądarkę przez serwer Playwright MCP, przejdzie przez każdy krok i zgłosi, co znalazł. Zobaczysz, jak otworzy przeglądarkę na Twoim komputerze, by wykonać zadania!

2. Przeczytaj jego podsumowanie względem kryteriów akceptacji w zgłoszeniu. Jeśli coś wygląda nie tak, zadaj pytania uzupełniające albo wyślij go z powrotem, by naprawił kod, zanim otworzysz pull request.
3. Pozostaw tę sesję otwartą — zamkniemy ją w następnej lekcji!

Copilot zweryfikował też funkcjonalność w przeglądarce, testując funkcję jak użytkownik.

## Podsumowanie i kolejne kroki

Gratulacje — użyłeś serwera Playwright MCP, by przetestować funkcję w prawdziwej przeglądarce z aplikacji GitHub Copilot! Podsumowując:

- poznałeś, czym jest Model Context Protocol (MCP) i jak aplikacja udostępnia narzędzia MCP.
- dodałeś serwer Playwright MCP poprzez interfejs aplikacji.
- poprosiłeś agenta o sterowanie przeglądarką i zbadanie funkcji filtrowania.

Funkcja jest zbudowana, zweryfikowana i przetestowana w działaniu. Czas ją wypchnąć — używając **Agent Merge** do otwarcia i scalenia pull requesta. Przejdź do [Lekcji 6 - Scalanie z Agent Merge][next-lesson].

## Zasoby

- [What the heck is MCP and why is everyone talking about it?][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [Konfiguracja serwerów MCP w aplikacji GitHub Copilot][customize-app]

[next-lesson]: ../6-agent-merge/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
