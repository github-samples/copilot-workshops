---
title: "Ćwiczenie 6 - Walidacja funkcjonalności z Playwright MCP"
description: "Sprawdź lub skonfiguruj Playwright MCP w Copilot CLI i użyj go do zbadania funkcji filtrowania w przeglądarce."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-18
---

Jak już podkreślaliśmy, pisanie kodu to nie wszystko. Trzeba też pracować z danymi, zewnętrznymi usługami i udostępniać Copilotowi dodatkowe automatyzacje. Tu wchodzą w grę serwery MCP. Pozwalają Copilotowi wyjść poza to, co jest wbudowane w CLI, i dają mu jeszcze więcej narzędzi oraz usług.

W tym ćwiczeniu:

- zrozumiesz, czym jest Model Context Protocol (MCP) i jak Copilot CLI z niego korzysta.
- dodasz serwer Playwright MCP, jeśli nie jest jeszcze dostępny.
- poprosisz agenta, by sterował przeglądarką i zbadał funkcję filtrowania.

## Scenariusz

Testy jednostkowe i end-to-end są ważne, ale walidacja zmian w UI wymaga rzeczywistej interakcji z interfejsem. Chcesz pozwolić Copilotowi korzystać z witryny, nad którą pracujesz, tak jak użytkownik — by jeszcze bardziej zautomatyzować wprowadzanie zmian i mieć większą pewność, że aktualizacje działają zgodnie z oczekiwaniami.

## Czym jest Model Context Protocol (MCP)?

[Model Context Protocol (MCP)][mcp-blog-post] daje agentom AI sposób komunikacji z zewnętrznymi narzędziami i usługami. Dzięki MCP agenci AI mogą komunikować się z nimi w czasie rzeczywistym. Pozwala to uzyskiwać aktualne informacje i wykonywać działania w Twoim imieniu.

Te narzędzia i zasoby są dostępne przez serwer MCP, który działa jako most między agentem AI a zewnętrznymi narzędziami i usługami. Każdy serwer MCP reprezentuje inny zestaw narzędzi i zasobów dostępnych dla agenta AI.

Kilka popularnych istniejących serwerów MCP:

- **[GitHub MCP Server][github-mcp]**: Zapewnia dostęp do API do zarządzania repozytoriami GitHub, zgłoszeniami i pull requestami.
- **[Playwright MCP Server][playwright-mcp-server]**: Zapewnia automatyzację przeglądarki za pomocą Playwright.

Dostępnych jest wiele innych serwerów MCP. GitHub hostuje [rejestr MCP][mcp-registry], aby ułatwić odkrywanie i wkład w ekosystem.

> [!CAUTION]
> Traktuj serwery MCP jak każdą inną zależność w projekcie. Przed użyciem przejrzyj kod źródłowy, zweryfikuj wydawcę i rozważ konsekwencje bezpieczeństwa.

## Dodaj serwer Playwright MCP

Dodajmy serwer Playwright MCP, żeby Copilot mógł wchodzić w interakcję z witryną tak, jak użytkownik.

1. Wróć do Codespace.
2. Otwórz dialog dodawania serwera MCP, wpisując w Copilot CLI poniższe polecenie:

   ```plaintext
   /mcp add
   ```

3. Jako nazwę wpisz `playwright`, a następnie wciśnij <kbd>Tab</kbd>.
4. Potwierdź typ serwera **STDIO**, wciskając <kbd>Enter</kbd>, a następnie wciśnij <kbd>Tab</kbd>.
5. Wklej poniższe do dialogu **Command**:

   ```plaintext
   npx -y @playwright/mcp@latest --headless --no-sandbox
   ```

6. Użyj kombinacji <kbd>Control</kbd>+<kbd>S</kbd> (Mac) lub <kbd>Ctrl</kbd>+<kbd>S</kbd> (Windows/Linux), aby zapisać nowy serwer MCP.
7. Wciśnij <kbd>Esc</kbd>, aby wyjść z dialogu MCP.

## Poproś Copilota o zbadanie funkcji przez Playwright

Wcześniej ręcznie potwierdziłeś, że funkcjonalność działa zgodnie z oczekiwaniami. Teraz użyjmy właśnie dodanego serwera Playwright, żeby Copilot zrobił to samo!

1. Użyj poniższego polecenia, żeby powiedzieć Copilotowi, by użył serwera Playwright MCP do walidacji funkcjonalności:

   ```plaintext
   Start the app and use Playwright MCP to check filtering against the issue and our plan. Tell me what works and what doesn't, without making changes. Stop the server you started when you're done.
   ```

> [!NOTE]
> Nie musisz wprost mówić Copilotowi, by użył serwera MCP — zwykle sam to rozpozna. Skoro jednak wiesz, czego powinien użyć, zawsze warto wskazać właściwy kierunek! Zapewnia to bardziej spójne wyniki i oszczędza trochę tokenów.

2. Obserwuj, jak Copilot wypisuje kolejne kroki wykonywane w przeglądarce, by potwierdzić działanie funkcjonalności.
3. Przeczytaj raport i upewnij się, że wszystko zachowuje się zgodnie z oczekiwaniami.

Copilot uruchomi serwer, użyje Playwright do interakcji z witryną, zatrzyma serwer i przedstawi raport.

## Podsumowanie i kolejne kroki

Gratulacje — użyłeś serwera Playwright MCP, by zbadać funkcję w prawdziwej przeglądarce z poziomu Copilot CLI! Podsumowując:

- poznałeś, czym jest Model Context Protocol (MCP) i jak Copilot CLI z niego korzysta.
- dodałeś serwer Playwright MCP, jeśli nie był jeszcze dostępny.
- poprosiłeś agenta, by sterował przeglądarką i zbadał funkcję filtrowania.

Następnie [utworzysz agenta niestandardowego QA][next-lesson], który łączy skill i narzędzia przeglądarki w roli specjalisty.

## Zasoby

- [What the heck is MCP and why is everyone talking about it?][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [Add MCP servers to Copilot CLI][add-mcp]

[previous-lesson]: ../5-agent-skills/
[next-lesson]: ../7-qa-agent/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[github-mcp]: https://github.com/github/github-mcp-server
[mcp-registry]: https://github.com/mcp
[add-mcp]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
