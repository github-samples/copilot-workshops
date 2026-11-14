---
title: "Ćwiczenie 8 - Tworzenie, przegląd i scalanie z CLI"
description: "Sprawdź końcowy diff, utwórz pull request poleceniem /pr create, uwzględnij uwagi z przeglądu i scal z /pr agentmerge."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Dokończ pętlę rozwoju bez przełączania się na desktopowy interfejs.

W tym ćwiczeniu:

- sprawdzisz zmienione pliki po raz ostatni.
- utworzysz pull request z bieżącej gałęzi.
- przejrzysz pull request i uwzględnisz uwagi z przeglądu.
- zweryfikujesz i scalisz pull request poleceniem `/pr agentmerge`.

## Utwórz, przejrzyj i scal

1. Uruchom `/diff`, aby sprawdzić zmienione pliki po raz ostatni.
2. Poproś Copilota o utworzenie pull requesta z bieżącej gałęzi albo uruchom `/pr create`.
3. Otwórz kartę **Pull requests** w panelu bocznym, aby sprawdzić tytuł, opis, pliki i sprawdzenia statusu.
4. Popraw uwagi możliwe do wdrożenia, sprawdź wynik w przeglądarce i odpowiedz, co się zmieniło.
5. Gdy pull request będzie gotowy, uruchom `/pr agentmerge`, aby go zweryfikować i scalić po wymaganych potwierdzeniach i przejściu sprawdzeń.

## Podsumowanie i kolejne kroki

Utworzyłeś, przejrzałeś i scaliłeś pull request bez opuszczania terminala. Przejdź do [ćwiczenia 9: Delegowanie pracy, gdy ufasz pętli][next-lesson].

[next-lesson]: ../9-delegate/
