---
title: "Ćwiczenie 3 - Tryby agenta: Plan i Autopilot"
description: "Użyj trybu Plan, aby uzgodnić podejście, Autopilot do zbudowania filtrowania na podstawie zgłoszenia oraz trybu Interactive do przeglądu wyniku."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-18
---

Zaczęliśmy od dodania małej funkcji do projektu. Większe zmiany wymagają jednak bardziej solidnego procesu. Na szczęście GitHub Copilot CLI jest zbudowany tak, by współdziałać z istniejącym flow organizacji i pomagać budować właściwe rzeczy we właściwy sposób. To pierwsze z kilku ćwiczeń, w których przejdziesz typowy proces rozwoju napędzany agentami: zaczniesz od zgłoszenia, wygenerujesz nową funkcję, upewnisz się, że kod jest poprawny, funkcja działa zgodnie z oczekiwaniami, a na końcu zostanie pomyślnie scalona z projektem.

> [!NOTE]
> Będziesz korzystać z tej samej rozmowy i gałęzi w dalszej części workflow funkcji. Zazwyczaj miałbyś różne gałęzie lub PR-y dla różnych typów plików, ale tutaj skracamy ścieżkę, żeby skupić się na kluczowych koncepcjach.

Na początek w tym ćwiczeniu:

- rozpoczniesz nową rozmowę z Copilotem na podstawie zgłoszenia GitHub.
- zdefiniujesz wymagania w trybie Plan.
- zaimplementujesz nową funkcję w trybie Autopilot.
- przejrzysz kod.
- zweryfikujesz funkcję ręcznie w przeglądarce z przekierowanym portem.

W trakcie pracy nad tą funkcją zaktualizujesz instrukcje repozytorium, dostosujesz istniejący skill `quality-checks`, dodasz walidację MCP, utworzysz agenta QA i otworzysz PR funkcji.

## Scenariusz

Katalog Tailspin Toys rośnie, a odwiedzający potrzebują zawężać gry według kategorii i wydawcy. Zgłoszenie w backlogu opisuje funkcję, ale szczegóły — na przykład łączenie kategorii — wymagają uzgodnienia przed kodowaniem. Użyjesz trybu Plan, aby rozstrzygnąć te decyzje, a następnie zezwolisz na ograniczoną implementację w Autopilot.

## Tło

Wprowadzenie agentów AI do procesu deweloperskiego nie zmienia fundamentów. Jeśli już, stają się one jeszcze ważniejsze! Większość deweloperów podąża za flow, który wygląda mniej więcej tak:

1. Zacznij od zgłoszenia, które opisuje, co trzeba zrobić.
2. Utwórz plan tego, co ma zostać zbudowane.
3. Zbuduj i przejrzyj kod.
4. Uruchom testy, aby zweryfikować kod.
5. Ręcznie zweryfikuj nową funkcjonalność.
6. Utwórz pull request (PR).
7. Gdy kod zostanie przejrzany i proces ciągłej integracji zakończy się powodzeniem, scal kod.

> [!NOTE]
> W zależności od zespołu i organizacji szczegóły będą się różnić. Większość wariantów to jednak odmiana schematu opisanego powyżej.

Trzymając się tego standardowego podejścia, zapewniasz, że kod wygenerowany przez AI spełnia określone wymagania i przechodzi ten sam proces weryfikacji co kod napisany ręcznie.

## Tryby rozmowy

**Tryb rozmowy** steruje stopniem autonomii agenta. Przełączaj tryby kombinacją <kbd>Shift</kbd>+<kbd>Tab</kbd>:

- **Interactive**: Ty i agent pracujecie razem. Agent sugeruje zmiany i czeka na Twoje dane wejściowe przed kontynuacją.
- **Plan**: Agent najpierw tworzy plan i jest zablokowany przed edycją plików projektu.
- **Autopilot**: Agent pracuje autonomicznie — pisze kod, uruchamia testy i iteruje, aż zadanie zostanie ukończone.

Zacznij w trybie Plan, przejrzyj plan, a następnie użyj Autopilot do jego realizacji.

## Zacznij od zgłoszenia

Zanim zaczniesz pracę nad filtrowaniem, wróć do Codespace i upewnij się, że repozytorium oraz terminal są gotowe.

1. Wróć do Codespace. Jeśli jest zatrzymany, uruchom go ponownie przed kontynuacją.
2. Upewnij się, że PR z oceną gwiazdkową jest scalony.
3. Jeśli terminal nie jest otwarty, wciśnij <kbd>Control</kbd>+<kbd>\`</kbd> (Mac) lub <kbd>Ctrl</kbd>+<kbd>\`</kbd> (Windows/Linux).
4. Zaktualizuj `main`, a następnie utwórz gałąź do pracy nad filtrowaniem:

   ```bash
   git checkout main
   git pull --ff-only
   git checkout -b game-filters-cli
   ```

5. Uruchom Copilot CLI:

   ```bash
   copilot --yolo
   ```

6. Wciśnij <kbd>Tab</kbd> dwukrotnie, aby otworzyć kartę **Issues**.
7. Wciśnij <kbd>A</kbd>, aby wyświetlić wszystkie zgłoszenia.
8. Klawiszami strzałek podświetl zgłoszenie zatytułowane **Allow users to filter games by category and publisher**.
9. Wciśnij <kbd>C</kbd>, aby dodać zgłoszenie do promptu i wrócić do karty **Session**.

Zwróć uwagę, że prompt zaczyna się teraz od `#7` (lub podobnego numeru). `#` pozwala wprowadzić do kontekstu zgłoszenie lub pull request (PR) z GitHuba.

## Zaplanuj funkcję filtrowania

Planowanie daje szansę zdefiniować podejście do implementacji funkcji lub wykonania zadań, zanim przekażesz je Copilotowi. Przy czymś złożonym zawsze warto poświęcić chwilę na planowanie. Przełączmy się na tryb planowania i poprośmy Copilota o utworzenie planu.

1. Wciśnij <kbd>Shift</kbd>+<kbd>Tab</kbd>, aby przełączyć się na tryb Plan. Upewnij się, że wskaźnik trybu pod promptem wyświetla **Plan**.
2. Po odwołaniu do zgłoszenia dodanym w poprzednim kroku wpisz następujące polecenie:

   ```plaintext
   Create a plan for implementing this feature.
   ```

Copilot zabiera się do budowania planu! Najpierw zbada projekt, a następnie wybierze najlepsze podejście.

3. Po drodze Copilot może zadawać pytania o to, jak mają działać możliwości filtrowania. Odpowiadaj zgodnie ze swoimi preferencjami. Nie ma tu złych odpowiedzi!
4. Gdy plan będzie gotowy, wciśnij <kbd>Control</kbd>+<kbd>E</kbd> (Mac) lub <kbd>Ctrl</kbd>+<kbd>E</kbd> (Windows/Linux), aby go rozwinąć.
5. Przewijaj w górę i w dół, aby przejrzeć plan.
6. Poproś Copilota o poprawienie dowolnej części planu, która nie odpowiada Twoim decyzjom.

## Zatwierdź Autopilot

Plan jest napisany i przejrzany — czas go zaimplementować! Pozwólmy Copilotowi działać w trybie autopilot.

Autopilot pozwoli Copilotowi iterować nad problemem, aż uzna go za ukończony.

1. Wybierz **Accept plan and build on autopilot (recommended)** lub podobnie oznaczoną opcję w zainstalowanej wersji.
2. Upewnij się, że wskaźnik trybu pod promptem wyświetla **Autopilot**.
3. Obserwuj, jak Copilot iteruje przez ustalony plan, generuje kod i uruchamia testy.

> [!NOTE]
> Zatwierdzenie może natychmiast rozpocząć implementację, więc najpierw przejrzyj plan. Jeśli Copilot zgłosi brakujące zależności lub konflikt portu, rozwiąż problem konfiguracji, zanim uznasz sprawdzenia za zakończone.

## Przejrzyj i zweryfikuj implementację

Gdy kod zostanie wygenerowany, trzeba go przejrzeć przed scaleniem — tak jak każdy inny kod. Przejrzyjmy kod i uruchommy witrynę, żeby upewnić się, że wszystko wygląda dobrze.

1. Wciśnij <kbd>Shift</kbd>+<kbd>Tab</kbd>, aby wejść w tryb Interactive. Upewnij się, że wskaźnik trybu nie wyświetla już **Plan** ani **Autopilot**.
2. Wpisz `/diff` i sprawdź implementację filtrowania oraz testy.
3. Porównaj wynik ze zgłoszeniem i decyzjami podjętymi podczas planowania.
4. Po przejrzeniu kodu wciśnij <kbd>Esc</kbd>, aby wyjść z widoku diff.
5. Przejrzyj wynik sprawdzeń projektu i poproś Copilota o rozwiązanie ewentualnych błędów.

## Poznaj nową funkcjonalność

OK, kod wygląda dobrze — ale czy działa? Uruchommy aplikację jak wcześniej i otwórzmy witrynę przez przekierowanie portu Codespaces.

1. Poproś Copilota o uruchomienie aplikacji:

   ```plaintext
   Start the app so I can try the filtering feature in my browser. Tell me the URL and leave the server running.
   ```

2. Gdy Codespaces zgłosi, że port `4321` jest dostępny, wybierz **Open in Browser**.
3. Wypróbuj filtrowanie po kategorii, po wydawcy oraz kombinacje uzgodnione w planie.
4. Upewnij się, że reset i zachowanie przy pustym wyniku odpowiadają zgłoszeniu i Twoim decyzjom.
5. Wróć do Codespace i poproś Copilota o zatrzymanie uruchomionego serwera deweloperskiego.

## Podsumowanie i kolejne kroki

Użyłeś różnych trybów rozmowy do zbudowania i przeglądu funkcji. W tym ćwiczeniu:

- rozpocząłeś nową rozmowę z Copilotem na podstawie zgłoszenia GitHub.
- zdefiniowałeś wymagania w trybie Plan.
- zaimplementowałeś nową funkcję w trybie Autopilot.
- przejrzałeś kod.
- zweryfikowałeś funkcję ręcznie w przeglądarce z przekierowanym portem.

Następnie przyjrzyjmy się bliżej temu, jak generowany jest kod i jak zapewnić zgodność z udokumentowanymi praktykami, [korzystając z instrukcji niestandardowych][next-lesson].

## Zasoby

- [Autopilot in GitHub Copilot CLI][autopilot]
- [Copilot CLI command reference][cli-reference]

[autopilot]: https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot
[cli-reference]: https://docs.github.com/copilot/reference/copilot-cli-reference/cli-command-reference
[previous-lesson]: ../2-add-star-rating/
[next-lesson]: ../4-custom-instructions/
