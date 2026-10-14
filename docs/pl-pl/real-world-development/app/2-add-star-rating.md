---
title: "Lekcja 2 - Dodawanie ocen w gwiazdkach: szybki sukces"
description: "Rozpocznij pierwszą sesję agenta w aplikacji GitHub Copilot, wprowadź małą zmianę na kartach gier i scal ją jako pierwszy pull request."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-07-09
---

Skoro zapoznałeś się z obszarem roboczym i użyłeś szybkiego czatu, czas rozpocząć **sesję agenta** i wprowadzić pierwszą zmianę w projekcie. Niech będzie niewielka: gry mają już ocenę w formie gwiazdek w danych, ale karty gier na stronie głównej jej jeszcze nie pokazują. Poprosisz agenta o jej wyświetlenie, przejrzysz zmianę i scalisz ją jako pierwszy pull request.

Podczas tej lekcji:

- rozpoczniesz sesję agenta i poznasz strukturę sesji.
- poprosisz agenta o małą, skoncentrowaną zmianę w projekcie.
- przejrzysz zmianę w widoku diff obszaru roboczego.
- uruchomisz aplikację lokalnie, aby potwierdzić zmianę w przeglądarce.
- otworzysz i scalisz pierwszy pull request.

## Scenariusz

Każda gra w Tailspin Toys może mieć ocenę w gwiazdkach i już pojawia się ona na stronie szczegółów gry. Karty gier na stronie głównej pokazują jednak tylko tytuł, kategorię, wydawcę i opis. Na rozgrzewkę agent powinien wyświetlić istniejącą ocenę na każdej karcie — drobna, samodzielna zmiana, idealna na pierwszą sesję.

## Anatomia sesji

**Sesja** to rozmowa z agentem działająca we własnym izolowanym obszarze roboczym. Każda sesja dostaje **dedykowany git worktree i gałąź**, dzięki czemu możesz uruchomić kilka sesji naraz — jedna dodaje funkcję, inna naprawia błąd — bez kolizji zmian. Sesje pojawiają się na pasku bocznym pogrupowane według repozytorium; wybierz dowolną, aby do niej przełączyć.

Wewnątrz sesji zobaczysz trzy elementy: **rozmowę** z agentem, **aktywność narzędzi** agenta podczas eksploracji i edycji plików oraz listę **zmienionych plików** z ich diffami.

## Rozpocznij sesję i poproś o zmianę

Rozpocznijmy nową sesję, aby zbadać projekt i zaimplementować funkcję. Podczas [konfiguracji aplikacji][prior-lesson] dodałeś projekt z jego repozytorium na GitHubie. Utworzymy nową sesję dla tego repozytorium i poprosimy o zmianę.

1. Wróć do (lub otwórz) aplikacji GitHub Copilot.
2. Wybierz **+** obok **Projects**.
3. Wybierz `tailspin-toys` jako repozytorium.
4. Wybierz **new working tree** i tryb **Interactive** pod polem promptu. Użyj poniższego polecenia, aby poprosić o zmianę:

    ```plaintext
    Show each game's starRating out of 5 in the game cards on the list page. If the rating is null, show "No rating yet". Keep the card layout as it is, add tests, and run the relevant checks.
    ```

5. Wciśnij <kbd>Enter</kbd>, aby wysłać polecenie do Copilota.

Aplikacja Copilot zaczyna pracę od utworzenia nowego worktree — izolowanej kopii projektu. Następnie zbada projekt, lokalizując pliki potrzebne do dodania nowej funkcji, i stworzy niezbędny kod. Właśnie dodałeś nową funkcję z aplikacją Copilot!

## Przejrzyj diff

Wszystkie zmiany wygenerowane przez AI zasługują na przegląd przed scaleniem, nawet te małe. Zbadajmy zmiany tu, w aplikacji Copilot.

1. W prawym górnym rogu aplikacji wybierz **Toggle review panel**. Otworzy się ekran diff ze wszystkimi oczekującymi zmianami wprowadzonymi przez Copilota.

    ![Górny pasek narzędzi aplikacji GitHub Copilot ze strzałką wskazującą przycisk Toggle review panel na prawo od Create PR](../../../_images/app-2-review-panel.png)

2. Powinieneś zauważyć kod dodany do `GameCard.astro`, głównego pliku używanego do wyświetlania szczegółów gry. Powinien być podobny do poniższego — mały blok, który renderuje ocenę, gdy jest obecna, a gdy `starRating` ma wartość `null`, pokazuje „No rating yet”:

   ```astro
   {game.starRating !== null ? (
       <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-amber-900/60 text-amber-300" data-testid="game-rating">
           ★ {game.starRating} / 5
       </span>
   ) : (
       <span class="text-xs font-medium text-slate-500" data-testid="game-rating-empty">
           No rating yet
       </span>
   )}
   ```

> [!NOTE]
> Ponieważ Copilot, jak wszystkie narzędzia generatywnej AI, jest probabilistyczny, a nie deterministyczny, dokładny kod może różnić się od powyższego. Powinien jednak być względnie podobny.

## Sprawdź zmiany

Przed otwarciem przeglądarki przejrzyj wyniki automatycznych sprawdzeń agenta. Upewnij się, że testy obejmują numeryczne `starRating` oraz fallback dla `null`. Brakujący warunek wstępny lub pominięte sprawdzenie to nie sukces; przed zatwierdzeniem przejrzyj każdą prośbę o instalację.

Oczywiście nie powinniśmy tylko czytać kodu i zakładać, że działa. Poprośmy Copilota, aby otworzył witrynę, żebyśmy mogli zbadać zaktualizowany UI. Zrobimy to, każąc mu uruchomić witrynę i otworzyć ją w kanwie przeglądarki.

> [!TIP]
> Kanwa to interaktywny widżet dostępny bezpośrednio w aplikacji Copilot. Później poznasz niestandardowe kanwy i nawet utworzysz własną, ale na razie użyjemy wbudowanej kanwy przeglądarki.

1. Użyj poniższego polecenia, aby poprosić Copilota o uruchomienie aplikacji i otwarcie strony w kanwie przeglądarki:

    ```plaintext
    Start the app and open it in the browser canvas.
    ```

2. Po chwili aplikacja się uruchomi i w aplikacji Copilot otworzy się okno przeglądarki.
3. Potwierdź, że karty gier z oceną wyświetlają wartość w skali do pięciu.
4. Gdy skończysz, poproś Copilota o zatrzymanie serwera deweloperskiego uruchomionego dla tej sesji, używając poniższego polecenia:

    ```plaintext
    Stop the dev server and close the browser canvas.
    ```

## Otwórz i scal swój pierwszy pull request

Funkcja jest gotowa! Czas utworzyć pull request (PR), aby scalić nowy kod z istniejącą bazą kodu.

1. Wybierz **Create PR** w prawym górnym rogu.
2. Gdy zostaniesz o to poproszony, wybierz **Sign in with your browser** i postępuj zgodnie z instrukcjami, aby się uwierzytelnić.
3. Copilot zabiera się za tworzenie PR.
4. Wybierz dymek **PR** tuż nad czatem, aby otworzyć PR w panelu przeglądu. W razie potrzeby możesz tu przejrzeć pull request.
5. Gdy będziesz gotowy, wybierz **Ready to merge**.
6. W nowym oknie dialogowym wybierz **Merge pull request**, aby scalić pull request!

## Podsumowanie i kolejne kroki

Gratulacje! Wypchnąłeś pierwszą zmianę za pomocą aplikacji GitHub Copilot! Konkretnie:

- rozpocząłeś sesję agenta i poznałeś strukturę sesji.
- skierowałeś agenta do wprowadzenia małej, skoncentrowanej zmiany na kartach gier.
- przejrzałeś zmianę w widoku diff obszaru roboczego.
- uruchomiłeś aplikację lokalnie, aby potwierdzić ocenę w gwiazdkach w przeglądarce.
- otworzyłeś PR 1, przejrzałeś jego sprawdzenia i jawnie go scaliłeś.

Następnie [zaczniesz od zgłoszenia o filtrowaniu i użyjesz trybów Plan oraz Autopilot][next-lesson], aby zbudować większą funkcję.

## Zasoby

- [Praca z sesjami agenta w aplikacji GitHub Copilot][agent-sessions]
- [O aplikacji GitHub Copilot][about-copilot-app]
- [Zarządzanie zgłoszeniami i pull requestami w aplikacji GitHub Copilot][managing-issues-prs]

[prior-lesson]: ../1-install-copilot-app/#zainstaluj-i-skonfiguruj-aplikację-github-copilot
[next-lesson]: ../3-agent-modes/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
