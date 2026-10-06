---
title: "Ćwiczenie 2 - Zapisanie instrukcji projektu"
description: "Uruchom /init, aby wygenerować instrukcje agenta opisujące gotowy Space Quiz, a następnie dostosuj je do swojego sposobu pracy."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Mając działający quiz na dysku, wygeneruj instrukcje agenta, które opisują rzeczywisty projekt. Każda przyszła sesja czyta te instrukcje przed rozpoczęciem pracy, więc nie musisz powtarzać tych samych wskazówek w każdym prompcie.

W tym ćwiczeniu:

- wygenerujesz instrukcje agenta poleceniem `/init`.
- przejrzysz wygenerowany plik przed akceptacją.
- skrócisz i spersonalizujesz instrukcje.

## Zapisz reguły poleceniem `/init`

1. Uruchom `/init` w sesji.
2. Przejrzyj wygenerowany plik instrukcji przed akceptacją.
3. Zostaw tylko wskazówki pasujące do tego projektu: jeden plik, bez zależności, dostępny i przetestowany w przeglądarce.

> [!IMPORTANT]
> **Kolejność ma znaczenie**
>
> `/init` czyta projekt w jego obecnym stanie. Uruchomienie po zbudowaniu i dopracowaniu quizu daje instrukcje oparte na rzeczywistym kodzie.

## Dostosuj je do siebie

Plik instrukcji nie służy wyłącznie do faktów o projekcie. Dodaj szczegóły, które inaczej powtarzałbyś w każdym prompcie: jak lubisz pisać kod, konwencje nazewnictwa, jakich bibliotek unikać i ile komentarzy chcesz. Każda przyszła sesja czyta ten plik przed Twoim promptem.

## Podsumowanie i kolejne kroki

Projekt ma teraz instrukcje agenta oparte na rzeczywistym kodzie. Przejdź do [ćwiczenia 3: Publikacja projektu][next-lesson].

[next-lesson]: ../3-publish/
