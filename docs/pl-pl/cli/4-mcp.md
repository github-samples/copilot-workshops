---
title: "Ćwiczenie 4 - Testowanie funkcji serwerem Playwright MCP"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-10
---

Właśnie wygenerowałeś funkcję filtrowania wykorzystując Copilot CLI. Zanim otworzysz pull request, upewnij się, że działa w przeglądarce. Zamiast klikać po aplikacji samodzielnie, połączysz **serwer Playwright MCP** i pozwolisz Copilotowi sterować prawdziwą przeglądarką, aby przetestować funkcję za Ciebie.

Podczas tego ćwiczenia:

- zrozumiesz, czym jest Model Context Protocol (MCP) i jak serwery MCP rozszerzają Copilot CLI.
- dodasz serwer Playwright MCP do Copilot CLI.
- poprosisz Copilota, by użył go do ręcznego przetestowania funkcji filtrowania w przeglądarce.

## Czym jest Model Context Protocol (MCP)?

[Model Context Protocol (MCP)](https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/) daje agentom AI sposób komunikacji z zewnętrznymi narzędziami i usługami. Dzięki MCP agenci AI mogą komunikować się z nimi w czasie rzeczywistym. Pozwala to uzyskiwać aktualne informacje (za pomocą zasobów) i wykonywać działania w Twoim imieniu (za pomocą narzędzi).

Te narzędzia i zasoby są dostępne przez serwer MCP, który działa jako most między agentem AI a zewnętrznymi narzędziami i usługami. Serwer MCP zarządza komunikacją między agentem AI a narzędziami zewnętrznymi (np. istniejącymi API lub lokalnymi narzędziami, takimi jak pakiety NPM). Każdy serwer MCP reprezentuje inny zestaw narzędzi i zasobów dostępnych dla agenta AI.

Kilka popularnych istniejących serwerów MCP:

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**: Ten serwer zapewnia dostęp do zestawu API do zarządzania repozytoriami GitHub. Pozwala agentowi AI m.in. tworzyć nowe repozytoria, aktualizować istniejące oraz zarządzać zgłoszeniami i pull requestami.
- **[Playwright MCP Server](https://github.com/microsoft/playwright-mcp)**: Ten serwer zapewnia automatyzację przeglądarki za pomocą Playwright. Pozwala agentowi AI m.in. nawigować do stron, wypełniać formularze i klikać przyciski.

Dostępnych jest wiele innych serwerów MCP z dostępem do różnych narzędzi i zasobów. GitHub hostuje [rejestr MCP](https://github.com/mcp), aby ułatwić odkrywanie i wkład w ekosystem.

> [!CAUTION]
> Pod względem bezpieczeństwa traktuj serwery MCP jak każdą inną zależność w projekcie. Przed użyciem serwera MCP dokładnie przejrzyj jego kod źródłowy, zweryfikuj wydawcę i rozważ konsekwencje bezpieczeństwa. Używaj tylko zaufanych serwerów MCP i ostrożnie przyznawaj dostęp do wrażliwych zasobów lub operacji.

> [!NOTE]
> [Serwer GitHub MCP][github-mcp-server] jest **wbudowany** w Copilot CLI — jest już dostępny bez konfiguracji, dzięki czemu Copilot czytał i zapisywał w Twoim repozytorium przez cały warsztat. Podczas tego ćwiczenia dodasz *drugi* serwer, Playwright, aby dać Copilotowi przeglądarkę.

## Dodaj serwer Playwright MCP

Najszybszym sposobem dodania serwera jest interaktywne polecenie `/mcp add`. Zarejestrujesz [serwer Playwright MCP][playwright-mcp-server], który da Copilotowi przeglądarkę, którą może sterować.

1. Wróć do codespace. Jeśli go zamknąłeś, przejdź do repozytorium na GitHub.com, wybierz **Code** > **Codespaces**, a następnie ponownie otwórz istniejący codespace.
2. Wróć do otwartej sesji Copilot CLI. Jeśli terminal jest zamknięty lub wyszedłeś z Copilot CLI, otwórz terminal. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>\`</kbd>, a następnie uruchom go z katalogu głównego repozytorium poleceniem `copilot --yolo --enable-all-github-mcp-tools`. Zaufaj folderowi projektu, jeśli zostaniesz o to poproszony, potem uruchom `/models` i wybierz **Auto**.
3. W sesji Copilot CLI wpisz:

    ```text
    /mcp add
    ```

4. Pojawi się formularz konfiguracji. Użyj <kbd>Tab</kbd>, aby przechodzić między polami, i wypełnij je tak:

    - **Server Name**: `playwright`
    - **Server Type**: wybierz **Local** (oznaczony też jako **STDIO**)
    - **Command**: `npx @playwright/mcp@latest --headless`
    - **Tools**: zostaw `*`, aby zezwolić na wszystkie narzędzia serwera

5. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>S</kbd>, aby zapisać. Serwer jest dodany i od razu dostępny — restart nie jest wymagany.

Flaga `--headless` każe Playwrightowi uruchamiać przeglądarkę bez widocznego okna, co jest wymagane w codespace, gdzie nie ma pulpitu do wyświetlenia. W tle zapisuje to serwer w pliku `~/.copilot/mcp-config.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "type": "local",
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--headless"],
      "tools": ["*"]
    }
  }
}
```

6. Upewnij się, że serwer jest zarejestrowany i aktywny, listując serwery MCP:

    ```text
    /mcp show
    ```

7. Powinieneś zobaczyć `playwright` na liście obok wbudowanego serwera `github`.

> [!NOTE]
> Projekt Tailspin Toys już używa Playwrighta do testów end-to-end, więc przeglądarka potrzebna Playwrightowi jest zwykle już zainstalowana. Jeśli Copilot później zgłosi brak przeglądarki, każ mu uruchomić `npx playwright install chromium` i spróbuj ponownie.

## Uruchom witrynę

Serwer Playwright MCP potrzebuje działającej aplikacji do testów. Uruchom serwer deweloperski Astro w **osobnym** terminalu, żeby działał dalej, gdy pracujesz w Copilot CLI.

1. Otwórz nowy terminal w codespace. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
2. Uruchom witrynę:

    ```bash
    npm run dev
    ```

3. Zostaw ten terminal uruchomiony. Gdy zobaczysz baner `Astro server: http://localhost:4321`, aplikacja jest gotowa.

## Przetestuj funkcję filtrowania

Wróć do sesji Copilot CLI i poproś Copilota o przetestowanie funkcji.

[Serwer Playwright MCP][playwright-mcp-server] daje Copilotowi prawdziwą przeglądarkę do sterowania. Zamiast klikać po aplikacji, by sprawdzić pracę, agent może otworzyć stronę, nawigować, zastosować filtry i odczytać wynik — a potem podsumować, co zobaczył. To najszybszy sposób upewnienia się, że funkcja zachowuje się zgodnie z oczekiwaniami, bez opuszczania rozmowy.

Pod spodem serwer Playwright MCP działa na [drzewie dostępności][playwright-mcp-server] strony, a nie na zrzutach ekranu. Agent rozumuje więc nad ustrukturyzowanymi, oznaczonymi etykietami elementami (przyciski, linki, elementy list) tak samo jak technologie asystujące — szybki test funkcjonalny jest jednocześnie lekką kontrolą dostępności.

Przy podłączonym serwerze i działającej aplikacji poproś Copilota o przećwiczenie właśnie zbudowanej funkcji filtrowania:

```text
Using the Playwright MCP server, open a browser to the running app at http://localhost:4321 and verify the new game filtering feature:

1. Go to the games page and note how many games are listed.
2. Apply a category filter and confirm the list updates to only show games in that category.
3. Clear it, then apply a publisher filter and confirm the list updates to that publisher.
4. Combine a category and a publisher filter and confirm the results respect both.

Report what you observe at each step, and call out anything that does not behave as expected.
```

Copilot uruchomi przeglądarkę przez serwer Playwright MCP, przejdzie przez każdy krok i zgłosi, co znalazł. Porównaj jego podsumowanie z kryteriami akceptacji w zgłoszeniu — jeśli coś wygląda nie tak, zadaj pytania uzupełniające lub wyślij go z powrotem, by naprawił kod, zanim otworzysz pull request.

> [!NOTE]
> Aplikacja musi działać pod adresem `http://localhost:4321` na potrzeby tego testu. Jeśli zatrzymałeś serwer deweloperski, uruchom go ponownie przed wysłaniem polecenia. Przy pierwszym użyciu serwera Playwright MCP Copilot może potrzebować pobrać przeglądarkę — jeśli zgłosi brak przeglądarki, każ mu uruchomić `npx playwright install chromium` i spróbuj ponownie.

## Podsumowanie i kolejne kroki

Gratulacje — użyłeś serwera Playwright MCP do ręcznego przetestowania funkcji za pomocą Copilot CLI! Podsumowując:

- poznałeś Model Context Protocol (MCP) i to, jak serwery MCP rozszerzają Copilot CLI.
- dodałeś serwer Playwright MCP za pomocą `/mcp add`.
- poprosiłeś Copilota o sterowanie przeglądarką i weryfikację funkcji filtrowania przed wysyłką.

W następnym kroku [otworzysz pull request za pomocą skillu agenta][next-lesson].

## Zasoby

- [What the heck is MCP and why is everyone talking about it?][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [Dodawanie serwerów MCP do Copilot CLI][cli-add-mcp]
- [GitHub MCP Server][github-mcp-server]

[previous-lesson]: ../3-generating-code/
[next-lesson]: ../5-agent-skills/
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[github-mcp-server]: https://github.com/github/github-mcp-server
[cli-add-mcp]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
