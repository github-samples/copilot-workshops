---
slug: pl-pl
title: "Praktyczne warsztaty z agentami GitHub Copilot"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-09
---

Niedawne rozszerzenia możliwości GitHub Copilot dają programistom potężne narzędzia podczas pracy na każdym etapie cyklu życia oprogramowania (SDLC). Obejmują pracę ze zgłoszeniami, pull requestami na GitHubie, interakcję z usługami zewnętrznymi oraz oczywiście tworzenie kodu. Te warsztaty opierają się na tych funkcjach, pokazując praktyczne przypadki użycia i wskazówki, jak w pełni wykorzystać te narzędzia.

> [!CAUTION]
> Ponieważ GitHub Copilot jest probabilistyczny, a nie deterministyczny, dokładny kod, zmienione pliki itd. mogą się różnić. W efekcie możesz zauważyć drobne różnice między zrzutami ekranu i fragmentami kodu w tych warsztatach a tym, co widzisz. To oczekiwane i wynika z natury tej klasy narzędzi.
>
> Jeśli coś wygląda na uszkodzone lub nie działa poprawnie, poproś mentora o pomoc!

## Wybierz środowisko

GitHub Copilot czeka na Ciebie tam, gdzie pracujesz. Wybierz środowisko dopasowane do sposobu, w jaki chcesz budować, i przejdź przez ćwiczenia implementujące zadania z backlogu Tailspin Toys. Każde środowisko zaczyna się od konfiguracji Twojej maszyny - wybierz tę, którą preferujesz.

### 🖥️ [VS Code](../vscode/)

GitHub Copilot w **Visual Studio Code** i GitHub Codespaces. Pracuj w trybie agenta Copilot Chat, z serwerami MCP i agentami niestandardowymi bez opuszczania edytora, którego już używasz — idealne, gdy chcesz wpleść pomoc AI bezpośrednio w IDE.

### 💻 [Copilot CLI](cli/)

**GitHub Copilot CLI** — asystent oparty na agentach działający w terminalu. Zainstaluj go, podłącz serwery MCP, generuj kod w trybie planowania i twórz własne skille, agentów niestandardowych oraz polecenia — wszystko z wiersza poleceń, bez przełączania się do edytora graficznego.

### 🤖 [Copilot App](app/)

**Aplikacja GitHub Copilot** — aplikacja desktopowa oparta na Copilot CLI. Uruchamiaj równoległe sesje agentów, przełączaj tryby sesji, współpracuj na kanwach i zarządzaj zgłoszeniami oraz pull requestami w GitHubie natywnie — wykorzystując między innymi **Agent Merge**, który tworzy pull requesty z opcją rebase, implementuje uwagi z przeglądu, poprawki CI i scala zmiany pomiędzy gałęziami.

### ☁️ [Copilot Cloud Agent](../cloud/)

**Agent chmurowy Copilot** — asynchroniczny partner programistyczny, który pracuje nad zgłoszeniami GitHub w tle. Przypisuj pracę, prowadź go agentami niestandardowymi, monitoruj postęp w panelu agentów i przeglądaj otwierane przez niego pull requesty.

## Scenariusz

Jesteś nowym programistą w Tailspin Toys, fikcyjnej firmie oferującej crowdfunding gier planszowych o tematyce deweloperskiej — ogromny rynek! Backlog zespołu jest już stworzony jako zgłoszenia w GitHubie, gotowe do podjęcia — zarówno prace funkcjonalne (np. filtrowanie i paginacja), jak i poprawa jakości (np. dostępność i standardy kodowania). Będziesz pracować iteracyjnie, eksplorując zarówno witrynę, jak i możliwości Copilota, aby dokończyć zadania.

## Rozpocznij

Wybierz środowisko powyżej, aby zacząć — każde rozpoczyna się od instrukcji jak skonfigurować środowisko potrzebne do rozpoczęcia pracy.
