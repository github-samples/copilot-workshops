---
title: "Ćwiczenie 6 - Co agent widzi"
description: "Użyj /context, aby sprawdzić, co wypełnia okno kontekstu, oraz /clear, aby zacząć od nowa, gdy rozmowa dryfuje."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Polecenia terminalowe czynią kontekst widocznym i świadomym. Wiedza o tym, co agent widzi, pomaga zrozumieć jego wyniki i zdecydować, kiedy zacząć od nowa.

W tym ćwiczeniu:

- sprawdzisz okno kontekstu poleceniem `/context`.
- zobaczysz, ile okna zużywa każda część.
- zresetujesz dryfującą rozmowę poleceniem `/clear`.

## Sprawdź kontekst

1. Uruchom `/context`, aby sprawdzić pliki, instrukcje i historię rozmowy.
2. Sprawdź, ile okna zużywa każda część.
3. Uruchom `/clear`, aby zacząć od nowa, gdy rozmowa zaczęła dryfować.
4. Dodaj z powrotem właściwy plik, zanim poprosisz o kolejną zmianę.

![Ilustracja wyjścia Copilot CLI po uruchomieniu /context. Miernik okna kontekstu pokazuje 61 procent użycia, podzielone między rozmowę, przeczytane pliki i instrukcje. Notatka sugeruje użycie /compact do podsumowania albo rozpoczęcie świeżej sesji, gdy kończy się miejsce.](../../../_images/first-steps-cli-context.svg)

`/context` pokazuje dokładnie, co wypełnia okno kontekstu i ile miejsca zostało. Gdy kończy się miejsce, użyj `/compact`, aby podsumować rozmowę, albo rozpocznij świeżą sesję.

## Podsumowanie i kolejne kroki

Potrafisz już zobaczyć i zarządzać tym, co agent wie. Przejdź do [ćwiczenia 7: Wznawianie i praca zdalna][next-lesson].

[next-lesson]: ../7-resume-and-remote/
