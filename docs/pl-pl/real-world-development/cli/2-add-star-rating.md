---
title: "Ćwiczenie 2 - Dodawanie ocen w gwiazdkach: szybki sukces"
description: "Użyj Copilot CLI, aby wprowadzić małą zmianę na kartach gier, przejrzeć ją w przeglądarce z przekierowanym portem i scalić jako pierwszy pull request."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-18
---

Skoro zainstalowałeś Copilot CLI i przeprowadziłeś rozmowę, czas na pierwszą zmianę w projekcie. Zachowaj ją małą: gry mają już ocenę gwiazdkową w danych, ale karty gier na stronie głównej jeszcze jej nie pokazują. Poprosisz agenta o jej wyświetlenie, przejrzysz zmianę i scalisz ją jako pierwszy pull request.

W tym ćwiczeniu:

- rozpoczniesz skoncentrowaną rozmowę z Copilotem na gałęzi funkcji.
- poprosisz agenta o małą zmianę w projekcie.
- przejrzysz zmianę za pomocą `/diff`.
- uruchomisz aplikację, aby potwierdzić zmianę w przeglądarce z przekierowanym portem.
- otworzysz i scalisz pierwszy pull request.

## Scenariusz

Każda gra w Tailspin Toys może mieć ocenę gwiazdkową i już pojawia się ona na stronie szczegółów gry. Karty gier na stronie głównej pokazują jednak tylko tytuł, kategorię, wydawcę i opis. Na rozgrzewkę poprosisz agenta o wyświetlenie istniejącej oceny na każdej karcie — to drobna, samodzielna zmiana, idealna na pierwszą sesję.

## Anatomia rozmowy

**Rozmowa** to miejsce, w którym pracujesz z Copilot CLI nad zadaniem. W przeciwieństwie do aplikacji GitHub Copilot zwykła rozmowa w CLI używa repozytorium i gałęzi Git aktualnie aktywnej w terminalu, zamiast tworzyć dedykowany worktree. Zapisane rozmowy pozwalają wrócić do tej samej dyskusji później, a pliki i gałąź pozostają zwykłym stanem Gita na dysku.

W rozmowie zobaczysz trzy elementy: swoje polecenia i odpowiedzi agenta, aktywność narzędzi agenta podczas eksploracji i edycji plików oraz zmiany, które możesz sprawdzić za pomocą `/diff`.

## Rozpocznij rozmowę i poproś o zmianę

Zacznijmy nową rozmowę, aby rozpocząć implementację funkcji.

1. Wróć do Codespace.
2. Jeśli terminal nie jest otwarty z wcześniejszej pracy, użyj kombinacji <kbd>Ctl</kbd>+<kbd>\`</kbd>.
3. Jeśli Copilot nie jest jeszcze uruchomiony, wystartuj go poniższym poleceniem:

   ```bash
   copilot --yolo
   ```

4. Upewnij się, że rozpoczęła się nowa sesja, używając polecenia slash `/new` i wybierając <kbd>Enter</kbd>.
5. Użyj poniższego polecenia, aby poprosić o zmianę:

   ```plaintext
   Show each game's starRating out of 5 in the game cards on the list page. If the rating is null, show "No rating yet". Keep the card layout as it is, add tests, and run the relevant checks.
   ```

Copilot eksploruje projekt, lokalizuje pliki używane do wyświetlania szczegółów gier i tworzy potrzebny kod. Właśnie dodałeś nową funkcję za pomocą Copilot CLI!

## Przejrzyj diff

Wszystkie zmiany wygenerowane przez AI zasługują na przegląd przed scaleniem — nawet drobne. Przejrzyjmy zmiany bezpośrednio w Copilot CLI.

1. Wpisz `/diff` i sprawdź każdy zmieniony plik.
2. Upewnij się, że karta gry wyświetla ocenę liczbową, gdy jest obecna, oraz `No rating yet`, gdy `starRating` ma wartość `null`.
3. Upewnij się, że testy obejmują oba stany.
4. Przejrzyj wyniki sprawdzeń uruchomionych przez Copilota i poproś go o naprawienie ewentualnych błędów.
5. Po zakończeniu przeglądu wciśnij <kbd>Esc</kbd>, aby wyjść z ekranu diff.

> [!NOTE]
> Ponieważ Copilot, jak wszystkie narzędzia generatywnej AI, jest probabilistyczny, a nie deterministyczny, dokładny kod może się różnić. Przeglądaj zachowanie, zamiast oczekiwać jednej konkretnej implementacji.

## Sprawdź zmiany

Oczywiście nie powinniśmy tylko czytać kodu i zakładać, że działa. Poprośmy Copilota o uruchomienie witryny, żebyśmy mogli zbadać zaktualizowany interfejs użytkownika (UI) w przeglądarce otwartej przez przekierowanie portu Codespaces.

1. Poproś Copilota o uruchomienie aplikacji:

   ```plaintext
   Start the app so I can inspect the star-rating change in my browser. Tell me the URL and leave the server running.
   ```

2. Gdy Codespaces zgłosi, że port `4321` jest dostępny, wybierz **Open in Browser**.
3. Upewnij się, że karty gier wyświetlają oceny w skali do pięciu.
4. Wróć do Copilota i poproś go o zatrzymanie uruchomionego serwera:

   ```plaintext
   Stop the development server you started.
   ```

## Otwórz i scal pierwszy pull request

Funkcja jest gotowa! Czas utworzyć pull request (PR), aby scalić nowy kod z projektem.

1. Poproś domyślnego agenta o zatwierdzenie (commit) zmiany:

   ```plaintext
   Commit the reviewed star-rating changes with an appropriate commit message.
   ```

2. Wpisz `/pr create`. Copilot CLI wypycha istniejący commit przy tworzeniu PR i wyświetla URL pull requesta.
3. Otwórz PR, przytrzymując <kbd>Command</kbd> (Mac) lub <kbd>Ctrl</kbd> (Windows/Linux) i wybierając URL wyświetlony przez Copilot CLI.
4. Przejrzyj zmienione pliki i sprawdzenia.
5. Gdy będziesz gotowy, wybierz **Merge pull request**, a następnie potwierdź scalenie.
6. Wróć do Codespace i wyjdź z Copilot CLI poleceniem `/exit`.
7. Zaktualizuj lokalną gałąź `main`:

   ```bash
   git checkout main
   git pull
   ```

## Podsumowanie i kolejne kroki

Gratulacje! Wypchnąłeś pierwszą zmianę za pomocą GitHub Copilot CLI! Konkretnie:

- rozpocząłeś skoncentrowaną rozmowę z Copilotem na gałęzi funkcji.
- skierowałeś agenta do wprowadzenia małej zmiany na kartach gier.
- przejrzałeś zmianę za pomocą `/diff`.
- uruchomiłeś aplikację, aby potwierdzić ocenę gwiazdkową w przeglądarce z przekierowanym portem.
- otworzyłeś i scaliłeś pierwszy pull request.

Następnie [zaczniesz od zgłoszenia o filtrowaniu i użyjesz trybów Plan oraz Autopilot][next-lesson], aby zbudować większą funkcję.

## Zasoby

- [About GitHub Copilot CLI][about-copilot-cli]
- [Copilot CLI command reference][cli-reference]

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-agent-modes/
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
