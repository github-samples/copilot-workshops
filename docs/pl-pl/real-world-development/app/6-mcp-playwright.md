---
title: "Lekcja 6 - Walidacja funkcjonalności z Playwright MCP"
description: "Skonfiguruj Playwright MCP przez Customize i obserwuj filtrowanie w przeglądarce w istniejącym worktree funkcji."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-07-09
---

Jak już podkreślaliśmy, pisanie kodu to coś więcej niż samo pisanie kodu. Trzeba pracować z danymi, usługami zewnętrznymi, a nawet udostępniać Copilotowi dodatkowe automatyzacje. Tu właśnie wchodzą w grę serwery MCP. Serwery MCP pozwalają Copilotowi wyjść poza to, co jest wbudowane w aplikację, i dają mu jeszcze więcej narzędzi oraz usług.

W tej lekcji:

- zrozumiesz, czym jest Model Context Protocol (MCP) i jak korzysta z niego aplikacja GitHub Copilot.
- dodasz serwer MCP Playwright.
- poprosisz agenta, by sterował przeglądarką i zbadał funkcję filtrowania.

## Scenariusz

Choć testy jednostkowe i kompleksowe (end-to-end) są ważne, walidacja aktualizacji interfejsu wymaga rzeczywistej interakcji z UI. Chcesz, żeby Copilot mógł korzystać ze strony, nad którą pracujesz, tak jak użytkownik — aby jeszcze bardziej zautomatyzować wprowadzanie zmian i zwiększyć pewność, że aktualizacje działają zgodnie z oczekiwaniami.

## Czym jest Model Context Protocol (MCP)?

[Model Context Protocol (MCP)][mcp-blog-post] daje agentom AI sposób komunikacji z zewnętrznymi narzędziami i usługami. Dzięki MCP agenci AI mogą komunikować się z nimi w czasie rzeczywistym. Pozwala im to uzyskiwać aktualne informacje (przez zasoby) oraz wykonywać działania w Twoim imieniu (przez narzędzia).

Do tych narzędzi i zasobów uzyskuje się dostęp przez serwer MCP, który działa jak most między agentem AI a zewnętrznymi narzędziami i usługami. Serwer MCP zarządza komunikacją między agentem AI a narzędziami zewnętrznymi (takimi jak istniejące API lub lokalne narzędzia, na przykład pakiety NPM). Każdy serwer MCP reprezentuje inny zestaw narzędzi i zasobów, do których agent AI może uzyskać dostęp.

Kilka popularnych serwerów MCP:

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**: ten serwer zapewnia dostęp do zestawu API do zarządzania repozytoriami GitHub. Pozwala agentowi AI wykonywać działania takie jak tworzenie nowych repozytoriów, aktualizowanie istniejących oraz zarządzanie zgłoszeniami i pull requestami.
- **[Playwright MCP Server][playwright-mcp-server]**: ten serwer zapewnia automatyzację przeglądarki za pomocą Playwright. Pozwala agentowi AI wykonywać działania takie jak nawigacja do stron, wypełnianie formularzy i klikanie przycisków.

Dostępnych jest wiele innych serwerów MCP, które udostępniają różne narzędzia i zasoby. GitHub hostuje [rejestr MCP](https://github.com/mcp), by ułatwić odkrywanie i wkład w ekosystem.

> [!CAUTION]
> Traktuj serwery MCP jak każdą inną zależność w projekcie. Przed użyciem serwera MCP uważnie przejrzyj jego kod źródłowy, zweryfikuj wydawcę i rozważ implikacje bezpieczeństwa. Używaj wyłącznie serwerów MCP, którym ufasz, i ostrożnie przyznawaj dostęp do wrażliwych zasobów lub operacji.

## Dodaj serwer MCP Playwright

Serwerami MCP zarządzasz przez **Customize** na pasku bocznym. Serwery skonfigurowane dla Twoich repozytoriów lub Copilot CLI mogą być już dostępne w aplikacji — sprawdź to, zanim dodasz duplikat. [Dokumentacja personalizacji aplikacji][customize-app] opisuje dostępne opcje.

1. Wybierz **Customize** na pasku bocznym.
2. Wybierz **MCP**, a następnie sprawdź **Installed** pod kątem istniejącego serwera Playwright.
3. W razie potrzeby znajdź **Playwright** wśród dostępnych serwerów albo skorzystaj z przepływu serwera niestandardowego opisanego przez wydawcę.
4. Przed zatwierdzeniem przejrzyj wydawcę, konfigurację i ewentualne monity instalacji. Postępuj zgodnie z monitami, by dodać serwer; polityka organizacji lub brakujące wymagania wstępne mogą zablokować konfigurację.
5. Wróć do sesji filtrowania w trybie **Interactive** i upewnij się, że narzędzia Playwright MCP są dostępne.

Jeśli konfiguracja się nie powiedzie, rozwiąż problem z konfiguracją lub uprawnieniami, zanim przejdziesz dalej.

## Poproś Copilota o zbadanie funkcji przez Playwright

Zgłoszenie i decyzje z planowania są już w kontekście. Zatrzymaj każdy serwer deweloperski uruchomiony wcześniej, zanim poprosisz Copilota o uruchomienie nowego.

1. Użyj poniższego polecenia, by poprosić Copilota o walidację nowej funkcjonalności:

    ```plaintext
    Start the app and use Playwright MCP to check filtering against the issue and our plan. Tell me what works and what doesn't, without making changes. Stop the server you started when you're done.
    ```

> [!NOTE]
> Nie musisz mówić Copilotowi, by użył konkretnego serwera MCP; zwykle sam znajdzie właściwy na podstawie bieżącego kontekstu. Mimo to nigdy nie zaszkodzi wskazać Copilotowi coś, co uważasz za ważne.

2. Usiądź wygodnie i obserwuj!

Copilot uruchomi serwer, otworzy przeglądarkę i będzie interagować ze stroną! Gdy skończy, zatrzyma serwer i przedstawi raport.

## Podsumowanie i kolejne kroki

Gratulacje — użyłeś serwera MCP Playwright, by zbadać funkcję w prawdziwej przeglądarce z poziomu aplikacji GitHub Copilot! Podsumowując:

- poznałeś Model Context Protocol (MCP) i sposób, w jaki aplikacja GitHub Copilot z niego korzysta.
- dodałeś serwer MCP Playwright.
- poprosiłeś agenta, by sterował przeglądarką i zbadał funkcję filtrowania.

Następnie [utworzysz niestandardowego agenta QA][next-lesson], który łączy skill i narzędzia przeglądarki w roli specjalisty.

## Zasoby

- [What the heck is MCP and why is everyone talking about it?][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [Configuring MCP servers in the GitHub Copilot app][customize-app]

[next-lesson]: ../7-qa-agent/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
