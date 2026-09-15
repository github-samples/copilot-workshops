---
title: "Lekcja 7 - Planowanie z kanwami"
description: "Utwórz współdzieloną, sterowaną agentem kanwę w aplikacji GitHub Copilot, aby planować i śledzić pracę razem z agentem."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-09
---

Dotąd kierowałeś agentami przez czat. Ale wiele pracy nie żyje w rozmowie — żyje na tablicy, w dokumencie albo na liście zadań. **Kanwy** dają Tobie i agentowi współdzieloną powierzchnię właśnie do takiej pracy, bezpośrednio w aplikacji. Podczas tej lekcji utworzysz prostą kanwę do planowania i śledzenia backlogu, nad którym pracowałeś.

Podczas tej lekcji:

- zrozumiesz, czym jest kanwa i kiedy jej używać.
- utworzysz współdzieloną kanwę tablicy Kanban do zarządzania backlogiem.
- zapiszesz kanwę w repozytorium i udostępnisz ją dla zespołu.
- otworzysz kanwę w nowej sesji i zaczniesz z niej pracę.

## Scenariusz

Patrzenie na listę zgłoszeń (issues) może być przytłaczające, nawet w spokojniejszym okresie życia projektu. Programiści Tailspin Toys szukali narzędzia, które pozwoliłoby szybko przeglądać zgłoszenia i zaczynać nad nimi pracę w aplikacji Copilot.

## Czym jest kanwa?

[Kanwa][canvas-docs] to współdzielona, interaktywna powierzchnia dla całej wykonanej pracy w projekcie — planu, tablicy zarządzania backlogiem, listy wydań, pulpitu lub dokumentów. Choć czat świetnie opisuje intencję i pomaga weryfikować niejasności, większość pracy dzieje się na *powierzchni*. Kanwy pozwalają współpracować z agentem bezpośrednio na tej powierzchni.

Kanwy są **dwukierunkowe**: agent może aktualizować kanwę podczas pracy, a Ty możesz edytować tę samą powierzchnię samodzielnie. Gdy tworzysz kanwę, agent buduje ją na podstawie Twojego polecenia i przepływu pracy, a Ty możesz prosić o dodanie, usunięcie lub zmianę możliwości w trakcie. Po utworzeniu kanwa otwiera się w prawym panelu bocznym aplikacji.

Typowe przykłady:

- **Kanwy Markdown** do planowania dnia i priorytetyzacji zgłoszeń oraz pull requestów.
- **Agentowe tablice kanban**, na których ludzie i agenci dodają karty i przesuwają pracę między kolumnami.
- **Tablice zarządzania zgłoszeniami**, które podsumowują najważniejsze zgłoszenia i powtarzające się tematy w repozytorium.

## Po co używać kanwy?

Sięgnij po kanwę, gdy zadanie wymaga struktury, iteracji i weryfikacji, a sam czat nie wystarcza. Kanwa pozwala:

- oprzeć pracę agenta na rzeczywistym artefakcie pasującym do Twojego przepływu.
- kierować lub korygować pracę bezpośrednio na współdzielonej powierzchni, a potem pozwolić agentowi kontynuować od Twoich zmian.
- śledzić postęp jako widoczne zmiany w całym produkcie, a nie tylko odpowiedzi w czacie.

## Utwórz kanwę do śledzenia pracy

Wdrożyłeś sporo rzeczy: ocena gwiazdkowa, standard dokumentacji i funkcję filtrowania - wszystkie są już scalone. Ale w backlogu nadal są elementy. Utwórzmy kanwę, by szybko zaplanować pracę.

1. Wróć do (lub otwórz) aplikacji GitHub Copilot.
2. Wybierz **Home screen**.
3. Upewnij się, że dla repozytorium wybrane jest `tailspin-toys`.
4. W polu polecenia użyj poniższego tekstu, aby utworzyć kanwę spełniającą potrzeby:

   ```plaintext
   Create a basic Kanban board canvas that allows me to quickly triage work. Highlight the three issues which are most likely to need attention right now, with the remainder in a second section down below. The top three cards should include a description of the issue's content and a justification of why they're at the top of the list. Each issue should have a button that allows me to add it to the current context for the current session so I can get to work on it straightaway.
   ```

Copilot zabierze się za tworzenie kanwy!

> [!NOTE]
> Zajmie to kilka minut. Ponieważ to skomplikowane zadanie, możesz nie być zadowolony z pierwszej wersji. Możesz wysyłać kolejne polecenia, by zbudować narzędzie swoich marzeń!

## Zapisz kanwę i scal ją z repozytorium

Kanwy mogą stać się zasobami w repozytorium, tak jak pliki instrukcji i skille. Poprośmy Copilota o dodanie jej do repozytorium i scalenie, by cały zespół mógł z niej korzystać.

1. W tej samej sesji poproś Copilota o zapisanie kanwy w repozytorium poniższym poleceniem:

   ```plaintext
   Let's save this canvas definition to the repository so I can share it with my development team
   ```

2. Gdy Copilot zapisze pliki kanwy, wybierz listę rozwijaną obok **Create PR** w prawym górnym rogu.
3. Wybierz **Agent merge**, aby włączyć agent merge.

   ![Lista rozwijana Create PR w aplikacji GitHub Copilot rozwinięta, ze strzałką wskazującą opcję Agent merge](../../_images/app-enable-agent-merge.png)

4. Tekst przycisku zmienia się teraz na **Agent merge**.
5. Wybierz przycisk **Agent merge**, aby uruchomić proces agent merge.

Aplikacja Copilot rozpocznie proces tworzenia i zarządzania PR. Zacznie od przejrzenia projektu, by ustalić, jak najlepiej utworzyć PR, a potem go stworzy.

Po chwili zauważysz, że Copilot znów zabierze się do pracy, patrząc na warunki PR — proces CI uruchamiający wszystkie testy w repozytorium. Zgłosi status wszelkich komentarzy pozostawionych przez innych członków zespołu, walidacji do uruchomienia (proces CI) oraz tego, czy PR jest możliwy do scalenia.

6. Pozwól agent merge scalić pull request, wybierając listę rozwijaną obok **Agent merge**, a następnie **Merge pull request**.

   ![Lista rozwijana Agent merge pokazująca dozwolone działania agenta — Address reviews, Fix CI failures, Resolve conflicts — ze strzałką wskazującą Merge pull request](../../_images/app-agent-merge-merge.png)

7. Poczekaj, aż wszystkie procesy CI przejdą (staną się zielone). Gdy to się stanie, Copilot automatycznie scali pull request!

Utworzyłeś nową współdzieloną kanwę dla zespołu!

## Pracuj na kanwie

Gdy kanwa jest utworzona, rozpocznijmy nową sesję i użyjmy jej!

1. W aplikacji Copilot rozpocznij nową sesję, wybierając **New session** obok **tailspin-toys**.
2. Poproś Copilota o otwarcie kanwy zadań poniższym poleceniem:

   ```plaintext
   Open the triage issues canvas
   ```

3. Powinieneś zauważyć, że kanwa, którą zbudowałeś, jest teraz otwarta w tej nowej sesji!
4. Wybierz **Add to current context** na jednym ze zgłoszeń, które najbardziej Cię interesuje.
5. Copilot zabierze się za pracę nad zgłoszeniem!

Użyłeś utworzonej kanwy, by usprawnić proces deweloperski.

## Podsumowanie i kolejne kroki

Utworzyłeś współdzieloną powierzchnię, na której Ty i agent możecie współpracować! W ramach tej lekcji:

- poznałeś, czym są kanwy i kiedy ich używać.
- utworzyłeś z agentem współdzieloną kanwę tablicy Kanban do zarządzania zadaniami.
- zapisałeś i scaliłeś kanwę z repozytorium za pomocą Agent Merge.
- otworzyłeś kanwę w nowej sesji i użyłeś jej do rozpoczęcia pracy.

Gdy backlog jest widoczny, zrób krok wstecz, by przejrzeć wszystko, co zbudowałeś, i dokąd iść dalej. Przejdź do [Lekcji 8 - Podsumowanie i kolejne kroki][next-lesson].

## Zasoby

- [Praca z rozszerzeniami kanwy w aplikacji GitHub Copilot][canvas-docs]
- [Kanwy na Awesome Copilot][awesome-copilot-canvases]
- [O aplikacji GitHub Copilot][about-copilot-app]

[next-lesson]: ../8-review/
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[awesome-copilot-canvases]: https://awesome-copilot.github.com/extensions/
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
