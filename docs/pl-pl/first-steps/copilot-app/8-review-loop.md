---
title: "Lekcja 8 - Dokończ pętlę przeglądu Copilot"
description: "Utwórz pull request, poproś o przegląd Copilot, zajmij się wykonalnymi uwagami i pozwól Agent Merge utrzymać pull request w dobrej kondycji."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Zamień zaimplementowane zgłoszenie w pull request, poproś Copilota o przegląd i zajmij się uwagami przed scaleniem.

W tej lekcji:

- jeszcze raz przejrzysz zmiany z sesji.
- utworzysz pull request z sesji agenta.
- poprosisz o przegląd kodu przez Copilot.
- przejrzysz i zastosujesz wykonalne uwagi.
- włączysz Agent Merge, aby utrzymywał pull request w dobrej kondycji aż do scalenia.

## Utwórz i przejrzyj pull request

1. Otwórz wysuwany panel po prawej i wybierz zakładkę **Changes**, aby przejrzeć pliki zmienione w sesji.
2. Wybierz **Create PR** na pasku narzędzi sesji.
3. Przejrzyj wygenerowany tytuł i opis, a następnie utwórz pull request.
4. Otwórz pull request na GitHubie.
5. Z menu **Reviewers** poproś o przegląd od **Copilot**.
6. Otwórz zakładkę **Files changed** i przeczytaj każdy komentarz z przeglądu.
7. Przy każdym wykonalnym komentarzu użyj akcji Copilot **Fix** w aplikacji albo wprowadź zmianę samodzielnie.
8. Przejrzyj każdą zmianę i ponownie przetestuj funkcję.
9. Odpowiedz zwięzłym opisem tego, co się zmieniło, a następnie rozwiąż rozmowę.

> [!NOTE]
> Jeśli sugestia nie ma zastosowania albo wykracza poza zakres pull requesta, odpowiedz z uzasadnieniem zamiast wprowadzać niepotrzebną zmianę. Rozwiąż każdą rozmowę z przeglądu przed scaleniem.

## Scal z Agent Merge

Włącz **Agent Merge** dla pull requesta, aby agent utrzymywał go w dobrej kondycji. Agent zajmuje się komentarzami z przeglądu, poprawia nieudane sprawdzenia i rozwiązuje konflikty, gdy się pojawią, a następnie scala, gdy wszystko jest zielone.

Jeśli wolisz scalić samodzielnie, przejrzyj końcowy diff, zweryfikuj funkcję i scal pull request po przejściu wszystkich sprawdzeń.

## Podsumowanie i kolejne kroki

Ukończyłeś pętlę rozwoju od zgłoszenia do przejrzanego i scalonego pull requesta. Przejdź do [Lekcji 9: Zautomatyzuj triage zgłoszeń][next-lesson].

[next-lesson]: ../9-automations/
