---
title: "Lekcja 11 - Poznaj kanwę"
description: "Zainstaluj kanwę Repository Issues Kanban i uruchom sesję z karty zgłoszenia."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

**Kanwa (Canvas)** to współdzielona, dwukierunkowa powierzchnia, na której Ty i agent możecie aktualizować ten sam plan, tablicę, listę kontrolną albo pulpit. Poznaj kanwę Kanban, która zamienia zgłoszenia repozytorium w wizualny przepływ pracy.

W tej lekcji:

- zainstalujesz rozszerzenie kanwy.
- połączysz kanwę z repozytorium Space Quiz.
- przeniesiesz zgłoszenie do aktywnej pracy.
- przejrzysz sesję utworzoną na podstawie zgłoszenia.

## Zainstaluj kanwę Repository Issues Kanban

1. Przejrzyj [galerię rozszerzeń Canvas][canvas-gallery].
2. Otwórz [rozszerzenie Repository Issues Kanban][kanban-extension].
3. Wybierz **Install in GitHub Copilot app** i zatwierdź instalację.
4. W aplikacji otwórz **Customize**, a następnie **Canvas**.
5. Upewnij się, że rozszerzenie jest zainstalowane.

## Zacznij pracę z kanwy

1. Wybierz **New session** dla kanwy.
2. Wybierz projekt `space-quiz`.
3. Poznaj tablicę zgłoszeń.
4. Przenieś kartę zgłoszenia do kolumny aktywnej pracy.
5. Otwórz automatycznie wygenerowaną sesję.
6. Upewnij się, że wybrane zgłoszenie jest dostępne jako kontekst sesji.

![Ilustracja kanwy Repository Issues Kanban z pasami Backlog, Plan, Ready i Implement. Zgłoszenie 13, Review screen, jest przeciągane z Backlog do pasa Plan, a zgłoszenie 12, Per-question timer, pozostaje w Backlog.](../../../_images/first-steps-app-canvas-kanban.svg)

Gdy upuścisz kartę na pas, kanwa przekazuje to zgłoszenie do nowej sesji z już załadowanym zgłoszeniem.

> [!NOTE]
> Bieżące rozszerzenie Repository Issues Kanban przenosi karty przez przeciąganie i upuszczanie wskaźnikiem. Jeśli nie możesz użyć tej interakcji, zanotuj numer zgłoszenia na tablicy, otwórz zgłoszenie w **My work**, a następnie wybierz **New session**. To tworzy tę samą sesję opartą na zgłoszeniu bez przenoszenia karty.

Kanwa daje wizualny sposób wyboru i rozpoczęcia pracy, jednocześnie utrzymując agenta w kontekście zgłoszenia.

## Podsumowanie i kolejne kroki

Użyłeś współdzielonej powierzchni wizualnej, aby uruchomić sesję agenta. Przejdź do [Lekcji 12: Podsumowanie i kolejne kroki][next-lesson].

[canvas-gallery]: https://awesome-copilot.github.com/extensions/
[kanban-extension]: https://awesome-copilot.github.com/extension/accessibility-kanban/
[next-lesson]: ../12-review/
