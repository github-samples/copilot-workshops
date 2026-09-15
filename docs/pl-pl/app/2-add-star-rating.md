---
title: "Lekcja 2 - Uruchomienie pierwszej sesji agenta"
description: "Rozpocznij pierwszą sesję agenta w aplikacji GitHub Copilot, wprowadź małą zmianę na kartach gier i scal ją przy użyciu pierwszego pull requesta."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-09
---

W poprzedniej lekcji zapoznałeś się z interfejsem aplikacji i użyłeś szybkiego czatu. Teraz czas rozpocząć **sesję agenta** i wprowadzić pierwszą zmianę w projekcie. Niech będzie niewielka: gry mają już ocenę w formie gwiazdek w danych, ale karty gier na stronie głównej jej jeszcze nie pokazują. Poprosisz agenta o jej wyświetlenie, przejrzysz zmianę i scalisz ją jako pierwszy pull request.

Podczas tej lekcji:

- rozpoczniesz sesję agenta i poznasz strukturę sesji.
- poprosisz agenta o małą, skoncentrowaną zmianę w projekcie.
- przejrzysz zmianę w widoku diff obszaru roboczego.
- uruchomisz aplikację lokalnie, aby potwierdzić zmianę w przeglądarce.
- otworzysz i scalisz pierwszy pull request.

## Scenariusz

Każda gra w Tailspin Toys może mieć ocenę gwiazdkową i aktualnie pojawia się ona na stronie szczegółów gry. Karty gier na stronie głównej pokazują jednak tylko tytuł, kategorię, wydawcę i opis. Na rozgrzewkę agent powinien umożliwić wyświetlanie istniejącej oceny na każdej karcie — drobna, samodzielna zmiana, idealna na pierwszą sesję.

## Anatomia sesji

**Sesja** to rozmowa z agentem działająca we własnym izolowanym obszarze roboczym. Każda sesja dostaje **dedykowany git worktree i gałąź**, dzięki czemu możesz uruchomić kilka sesji naraz — jedna dodaje funkcję, inna naprawia błąd — bez kolizji zmian. Sesje pojawiają się na pasku bocznym pogrupowane według repozytorium; wybierz dowolną, aby do niej przełączyć.

Wewnątrz sesji zobaczysz trzy elementy: **rozmowę** z agentem, **aktywność narzędzi** agenta podczas eksploracji i edycji plików oraz listę **zmienionych plików** z ich diffami.

## Rozpocznij sesję i poproś o zmianę

Rozpocznijmy nową sesję, aby zbadać projekt i zaimplementować funkcję. W [poprzedniej lekcji][prior-lesson] dodałeś projekt z repozytorium na GitHubie. Utworzymy nową sesję dla tego repozytorium i poprosimy o zmianę.

1. Wróć do (lub otwórz) aplikacji GitHub Copilot.
2. Wybierz **Home screen**.
3. Upewnij się, że dla repozytorium wybrane jest `tailspin-toys`.

   ![Interfejs aplikacji GitHub Copilot z selektorem repozytorium ustawionym na tailspin-toys i selektorem modelu poniżej monitu](../../_images/app-2-start-session.png)

4. Użyj poniższego polecenia, aby poprosić o zmianę:

   ```plaintext
   On the game cards, show each game's star rating. The Game type already includes a starRating field — it's a number out of 5, or null when a game hasn't been rated yet. Display it on each card in src/components/GameCard.astro, and when starRating is null show "No rating yet" instead. Keep the change small and don't restructure the card layout.
   ```

> [!NOTE]
> Zwróć uwagę, że monit zawierał nazwę pliku, który Copilot ma zaktualizować. Wskazanie plików nie jest wcale wymagane, ale skierowanie Copilota we właściwą stronę pomaga szybko generować kod i zmniejsza zużycie tokenów.

5. Wciśnij <kbd>Enter</kbd>, aby wysłać polecenie do Copilota.

Aplikacja Copilot zaczyna pracę od utworzenia nowego worktree — izolowanej kopii projektu. Następnie zbada projekt, lokalizując pliki potrzebne do dodania nowej funkcji, i stworzy niezbędny kod. Właśnie dodałeś nową funkcję wykorzystując aplikację Copilot!

## Przejrzyj diff

Wszystkie zmiany wygenerowane przez AI zasługują na przegląd przed scaleniem, nawet te małe. Zbadajmy zmiany za pomocą Copilota.

1. W prawym górnym rogu aplikacji wybierz **Toggle review panel**. Otworzy się ekran diff ze wszystkimi oczekującymi zmianami wprowadzonymi przez Copilota.

   ![Górny pasek narzędzi aplikacji GitHub Copilot ze strzałką wskazującą przycisk Toggle review panel na prawo od Create PR](../../_images/app-2-review-panel.png)

2. Powinieneś zauważyć kod dodany do `GameCard.astro`, głównego pliku używanego do wyświetlania szczegółów gry. Powinien być podobny do poniższego — małe pole, które wyświetla ocenę, gdy jest obecna, a gdy `starRating` ma wartość `null`, pokazuje „No rating yet”:

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

Oczywiście nie powinniśmy tylko czytać kodu i zakładać, że działa. Powinniśmy też przetestować wszystko wizualnie! W tym celu uruchomimy aplikację za pomocą terminala, a potem potwierdzimy, że wszystko działa. Na szczęście w aplikacji Copilot jest wbudowany terminal!

1. W panelu przeglądu po prawej stronie aplikacji Copilot wybierz **Terminal**. Jeśli nie ma przycisku **Terminal**, wybierz **+** (etykieta **Open in panel**), a następnie **Terminal**.

   ![Przycisk Terminal w panelu kontekstowym aplikacji GitHub Copilot](../../_images/app-terminal-screenshot.png)

2. W oknie terminala wprowadź poniższe polecenie, aby uruchomić serwer deweloperski aplikacji webowej:

   ```shell
   npm run dev
   ```

3. Gdy serwer się uruchomi (zajmie to chwilę), otwórz okno przeglądarki.
4. Przejdź do http://localhost:4321.
5. Powinieneś teraz zobaczyć oceny gwiazdkowe przy wszystkich grach na stronie startowej!
6. Wróć do okna terminala.
7. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>C</kbd>, aby zatrzymać serwer deweloperski.

## Otwórz i scal pierwszy pull request

Zmiana wygląda dobrze — czas ją wypchnąć! Poprosisz agenta o otwarcie pull requesta, a następnie sam go przejrzysz i scalisz na github.com. Na razie tą drugą część zrobimy ręcznie. W nadchodzącej lekcji zobaczymy, jak Copilot może automatycznie wykonać część tej pracy.

1. W prawym górnym rogu wybierz **Create PR**.
2. Jeśli zostaniesz o to poproszony, wybierz **Sign in with your browser** i postępuj zgodnie z instrukcjami, aby się uwierzytelnić.
3. Copilot zabierze się za tworzenie PR.

Gdy PR zostanie utworzony, Copilot będzie śledzić workflow CI w repozytorium, które musi się uruchomić. Po chwili przycisk w prawym górnym rogu zmieni się na **Ready to merge**. To znak, że Twój PR jest gotowy do scalenia!

4. Wybierz dymek **PR** tuż nad czatem, aby otworzyć PR w panelu przeglądu i zobaczyć pull request. Możesz tu przejrzeć PR w razie potrzeby.
5. Gdy będziesz gotowy, wybierz **Ready to merge**.
6. Wybierz **Merge pull request** w nowym oknie dialogowym, aby scalić pull request!

Właśnie wypchnąłeś nową funkcję na witrynę!

## Podsumowanie i kolejne kroki

Rozpocząłeś pierwszą sesję agenta i wypchnąłeś pierwszą zmianę! Konkretnie:

- rozpocząłeś sesję agenta i poznałeś strukturę sesji.
- skierowałeś agenta na małą, skoncentrowaną zmianę kart gier.
- przejrzałeś zmianę w widoku diff obszaru roboczego.
- uruchomiłeś aplikację lokalnie, aby potwierdzić ocenę gwiazdkową w przeglądarce.
- otworzyłeś pull request i sam go scaliłeś na github.com.

W następnym kroku użyjesz aplikacji, aby dodać do repozytorium zestaw instrukcji niestandardowych — zaczynając od jednego ze zgłoszeń w backlogu. Przejdź do [Lekcji 3 - Instrukcje niestandardowe w Copilocie][next-lesson].

## Zasoby

- [Praca z sesjami agenta w aplikacji GitHub Copilot][agent-sessions]
- [O aplikacji GitHub Copilot][about-copilot-app]
- [Zarządzanie zgłoszeniami i pull requestami w aplikacji GitHub Copilot][managing-issues-prs]

[prior-lesson]: ../1-install-copilot-app/#zainstaluj-i-skonfiguruj-aplikację-github-copilot
[next-lesson]: ../3-custom-instructions/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
