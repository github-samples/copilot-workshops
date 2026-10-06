---
title: "Lekcja 9 - Eksploracja i tworzenie kanw"
description: "Użyj istniejącej kanwy Database Explorer, potem utwórz i przejrzyj kanwę triage opartą o repozytorium."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-17
---

Do tej pory kierowałeś agentami przez czat. Ale wiele pracy nie żyje w rozmowie — żyje na tablicy, w dokumencie lub na liście kontrolnej. **Kanwy** dają Tobie i agentowi współdzieloną powierzchnię właśnie do takiej pracy, bezpośrednio w aplikacji. W tej lekcji najpierw użyjesz kanwy dołączonej do Tailspin Toys, a potem utworzysz jedną dla backlogu, nad którym pracowałeś.

W tej lekcji:

- zrozumiesz, czym jest kanwa i kiedy jej używać.
- użyjesz istniejącej kanwy Database Explorer do przeglądu danych projektu.
- utworzysz współdzieloną kanwę tablicy Kanban do triage backlogu.
- przejrzysz i przećwiczysz nową kanwę bez implementowania kolejnej funkcji.

## Scenariusz

Tailspin Toys ma już kanwę do eksploracji bazy danych. Po użyciu jej, by zrozumieć, jak kanwa zamienia dane projektu w interaktywną powierzchnię, utworzysz wielokrotnego użytku tablicę do wyboru kolejnej pracy — bez rozpoczynania kolejnej funkcji.

## Czym jest kanwa?

[Kanwa][canvas-docs] to współdzielona, interaktywna powierzchnia dla artefaktu pracy — planu, tablicy triage, listy kontrolnej wydania, pulpitu lub dokumentu. Choć czat jest przydatny do opisywania intencji i rozstrzygania niejasności, większość pracy dzieje się na *powierzchni*. Kanwy pozwalają współpracować z agentem bezpośrednio na tej powierzchni.

Kanwy są **dwukierunkowe**: agent może aktualizować kanwę podczas pracy, a Ty możesz edytować tę samą powierzchnię samodzielnie. Gdy tworzysz kanwę, agent buduje ją na podstawie Twojego polecenia i przepływu pracy, a Ty możesz prosić o dodawanie, usuwanie lub poprawianie możliwości w trakcie. Po utworzeniu kanwa otwiera się w prawym panelu bocznym aplikacji.

Typowe przykłady obejmują:

- **Kanwy Markdown** do planowania dnia i priorytetyzacji zgłoszeń oraz pull requestów.
- **Agentowe tablice Kanban**, na których ludzie i agenci dodają karty i przesuwają pracę między kolumnami.
- **Tablice triage zgłoszeń**, które podsumowują najważniejsze zgłoszenia i powtarzające się motywy w repozytorium.

## Po co używać kanwy?

Sięgnij po kanwę, gdy zadanie wymaga struktury, iteracji i weryfikacji, a sam czat nie wystarczy. Kanwa pozwala:

- oprzeć pracę agenta na rzeczywistym artefakcie dopasowanym do Twojego przepływu pracy.
- sterować lub korygować pracę bezpośrednio na współdzielonej powierzchni, a potem pozwolić agentowi kontynuować od Twoich zmian.
- śledzić postęp jako widoczne zmiany artefaktu, a nie tylko odpowiedzi w czacie.

## Użyj kanwy Database Explorer

Zacznij od istniejącej kanwy Database Explorer w projekcie. Praca z działającym przykładem pozwala zobaczyć, jak zachowuje się kanwa o zakresie repozytorium, zanim utworzysz własną.

1. Upewnij się, że pull request (PR) filtrowania jest scalony, i zaktualizuj lokalny `main`.
2. Wróć do aplikacji GitHub Copilot i wybierz **Home screen**.
3. Upewnij się, że wybranym repozytorium jest `tailspin-toys`.
4. Utwórz sesję w **new working tree** na podstawie zaktualizowanego `main`, a następnie wybierz tryb **Interactive**.
5. Poproś Copilota o przygotowanie lokalnej bazy danych w razie potrzeby i otwarcie istniejącej kanwy bez jej zmiany:

    ```plaintext
    Set up the local database if needed, then open the repository's Database Explorer canvas. Do not change any files.
    ```

6. W Database Explorer przeglądaj dostępne tabele i wybierz `games`.
7. Uruchom zapytanie tylko do odczytu, które pokazuje pięć najwyżej ocenianych gier:

    ```sql
    SELECT title, star_rating
    FROM games
    ORDER BY star_rating DESC
    LIMIT 5;
    ```

8. Upewnij się, że wyniki zawierają nie więcej niż pięć gier w kolejności malejącej oceny.
9. Otwórz **Files** i przejrzyj `.github/extensions/database-explorer/extension.mjs`. Zwróć uwagę, jak kanwa jest przechowywana z projektem i ogranicza zapytania do instrukcji `SELECT` i `WITH` tylko do odczytu.
10. Upewnij się, że sesja nie ma zmian w plikach.

## Utwórz kanwę do triage zgłoszeń

Teraz utwórz inny rodzaj współdzielonej powierzchni. Zapisanie kanwy triage w zakresie projektu czyni ją zasobem repozytorium, który zespół może przeglądać i ponownie wykorzystywać.

1. W tej samej sesji wpisz `/create-canvas`, a następnie opisz kanwę, którą chcesz utworzyć:

   ```plaintext
   Create a Kanban triage canvas for this repo's open issues and save it under .github/extensions/. Highlight the three issues you'd prioritize and explain why, with the rest below. Include summaries and links.

   Give each card an "Add to current context" action that adds the issue details without starting work or changing the issue. Make it keyboard-accessible and open it so I can try it.
   ```

Copilot tworzy rozszerzenie kanwy w `.github/extensions` i otwiera współdzieloną powierzchnię w prawym panelu bocznym aplikacji. Wygenerowane rozszerzenie to wykonywalna zawartość repozytorium, a nie tylko artefakt wizualny — dlatego w kolejnym kroku przejrzysz jego pliki i zachowanie.

## Przejrzyj i przećwicz kanwę

Zanim udostępnisz kanwę, porównaj ją z rzeczywistymi zgłoszeniami w repozytorium i przećwicz jej elementy sterujące. Dzięki temu potwierdzisz, że treść jest dokładna, interakcja dostępna, a akcja zgłoszenia dodaje kontekst bez rozpoczynania pracy.

1. Otwórz **Changes** i upewnij się, że definicja kanwy jest oparta o repozytorium w `.github/extensions/`, a nie zapisana tylko dla użytkownika lub sesji. Sprawdź, że istniejące rozszerzenia i pliki aplikacji nie zostały zmienione.
2. Porównaj tablicę z rzeczywistymi otwartymi zgłoszeniami i oceń wyjaśnienia rankingów.
3. Sprawdź, że karty i elementy sterujące są czytelne i użyteczne z klawiatury.
4. Wybierz **Add to current context** dla zgłoszenia i upewnij się, że do rozmowy trafiają tylko jego szczegóły. Nie powinna rozpocząć się implementacja ani zmiana stanu zgłoszenia.
5. Przejrzyj ewentualne poprawki i poproś Copilota o uruchomienie obowiązującej istniejącej walidacji dla zmienionych plików. Zanotuj wyniki i blokery zamiast zakładać, że interaktywna powierzchnia jest poprawna tylko dlatego, że się otworzyła.
6. Jeśli kanwa wymaga zmian, poproś o ukierunkowane ulepszenia w zakresie triage, a następnie powtórz dotknięte sprawdzenia. Nie implementuj jednego ze zgłoszeń z backlogu jako części pracy nad kanwą.

Warsztat kończy się przed utworzeniem kolejnego PR, bo przećwiczyłeś już zarówno ręczne scalanie, jak i Agent Merge. W produkcji przejrzyj i scal kanwę zwykłym procesem zespołu, zanim inni na niej polegają.

## Podsumowanie i kolejne kroki

Utworzyłeś i ponownie wykorzystałeś współdzieloną powierzchnię, na której Ty i agent możecie współpracować. W tej lekcji:

- zrozumiałeś, czym jest kanwa i kiedy jej używać.
- użyłeś istniejącej kanwy Database Explorer do przeglądu danych projektu.
- utworzyłeś współdzieloną kanwę tablicy Kanban do triage backlogu.
- przejrzałeś i przećwiczyłeś nową kanwę bez implementowania kolejnej funkcji.

Gdy backlog jest śledzony, [przejrzysz wszystko, co zbudowałeś, i poznasz kolejne kierunki][next-lesson].

## Zasoby

- [Working with canvas extensions in the GitHub Copilot app][canvas-docs]
- [Canvases on Awesome Copilot][awesome-copilot-canvases]
- [About the GitHub Copilot app][about-copilot-app]

[next-lesson]: ../10-review/
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[awesome-copilot-canvases]: https://awesome-copilot.github.com/extensions/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
