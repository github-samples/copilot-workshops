---
title: "Lekcja 2 - Zapisz instrukcje projektu"
description: "Uruchom /init w Copilot Chat, aby wygenerować .github/copilot-instructions.md dla Space Quiz, a następnie dostosuj plik."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Mając działający quiz w obszarze roboczym, wygeneruj instrukcje niestandardowe repozytorium, które opisują rzeczywisty projekt. Copilot czyta te instrukcje przy każdym żądaniu w czacie.

W tej lekcji:

- wygenerujesz instrukcje niestandardowe repozytorium za pomocą `/init`.
- przejrzysz `.github/copilot-instructions.md` przed zapisaniem.
- skrócisz i spersonalizujesz instrukcje.

## Zapisz reguły za pomocą `/init`

1. Uruchom `/init` w Copilot Chat.
2. Przejrzyj wygenerowany plik `.github/copilot-instructions.md` przed zapisaniem.
3. Zostaw tylko wskazówki pasujące do tego projektu: jeden plik, brak zależności, dostępność i testowanie w przeglądarce.

![Ilustracja VS Code z otwartym plikiem .github/copilot-instructions.md w edytorze i zaznaczonym w Explorerze, obok index.html. Plik ma tytuł Space Quiz i wymienia reguły: pojedynczy index.html bez zależności i bez kroku budowania, każda odpowiedź osiągalna z klawiatury oraz respektowanie prefers-color-scheme w obu motywach. Sekcja How I like code written prosi o małe funkcje, wczesne returny, brak sprytnych one-linerów i komentarze tylko przy tym, co naprawdę zaskakuje.](../../../_images/first-steps-vscode-instructions.svg)

Instrukcje niestandardowe repozytorium znajdują się w `.github/copilot-instructions.md` i obowiązują przy każdym żądaniu w czacie.

> [!IMPORTANT]
> **Kolejność ma znaczenie**
>
> `/init` czyta obszar roboczy w jego obecnym stanie. Uruchomienie go po zbudowaniu quizu daje instrukcje oparte na rzeczywistym kodzie.

## Dostosuj je do siebie

Plik instrukcji nie służy wyłącznie do faktów o projekcie. Dodaj szczegóły, które inaczej powtarzałbyś w każdym promptcie: jak lubisz pisać kod, konwencje nazewnictwa, jakich bibliotek unikać i ile komentarzy chcesz. Każda przyszła sesja czyta ten plik zanim przeczyta Twój prompt.

## Podsumowanie i kolejne kroki

Obszar roboczy ma teraz instrukcje niestandardowe oparte na rzeczywistym kodzie. Przejdź do [Lekcji 3: Sprawdź kontekst i przetestuj][next-lesson].

[next-lesson]: ../3-inspect-and-test/
