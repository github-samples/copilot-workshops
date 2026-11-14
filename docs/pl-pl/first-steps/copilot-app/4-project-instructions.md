---
title: "Lekcja 4 - Zapisz instrukcje projektu"
description: "Uruchom /init, aby wygenerować instrukcje agenta opisujące gotowy Space Quiz, a następnie dostosuj je do swojego sposobu pracy."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Skoro quiz jest zbudowany, dopracowany i przetestowany, zapisz, jak przyszłe sesje powinny traktować ten projekt. Instrukcje agenta czyta każda sesja przed rozpoczęciem pracy, więc nie musisz powtarzać tych samych wskazówek w każdym promptcie.

W tej lekcji:

- wygenerujesz instrukcje agenta za pomocą `/init`.
- przejrzysz wygenerowany plik przed zaakceptowaniem.
- skrócisz i spersonalizujesz instrukcje.

## Zapisz reguły za pomocą `/init`

1. Uruchom `/init` w sesji aplikacji.
2. Przejrzyj wygenerowany plik instrukcji agenta przed zaakceptowaniem.
3. Skróć go do wskazówek, które oddają ten projekt: jeden plik, bez zależności, dostępny i przetestowany w przeglądarce.

> [!IMPORTANT]
> **Dlaczego po dopracowaniu?**
>
> `/init` czyta projekt w stanie, w jakim jest teraz. Uruchomienie go po zbudowaniu i przetestowaniu quizu daje instrukcje opisujące realny kod, a nie pusty folder.

## Uczyń je swoimi

Plik instrukcji nie służy tylko do faktów o projekcie. Dodaj szczegóły, które inaczej powtarzałbyś w każdym promptcie: jak lubisz pisać kod, konwencje nazewnictwa, jakich bibliotek unikać i ile komentarzy chcesz. Każda przyszła sesja czyta ten plik, zanim przeczyta Twoje polecenie.

## Podsumowanie i kolejne kroki

Projekt ma teraz instrukcje agenta oparte na realnym kodzie. Przejdź do [Lekcji 5: Opublikuj projekt][next-lesson].

[next-lesson]: ../5-publish/
