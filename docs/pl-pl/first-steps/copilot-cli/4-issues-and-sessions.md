---
title: "Ćwiczenie 4 - Praca nad zgłoszeniami równolegle"
description: "Utwórz backlog, dodaj zgłoszenie do czatu z panelu bocznego, przejrzyj zmiany z /diff i uruchom drugą sesję w osobnym worktree."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Trzymaj backlog i pętlę implementacji w terminalu oraz otwieraj osobne sesje dla niezależnej pracy.

W tym ćwiczeniu:

- utworzysz trzy skupione zgłoszenia GitHub.
- dodasz zgłoszenie do czatu z panelu bocznego i zaimplementujesz je.
- przejrzysz zmianę poleceniem `/diff`.
- uruchomisz drugą sesję w izolowanym worktree.

## Utwórz backlog

Wyślij poniższe polecenie:

```plaintext
Review the space quiz and create three focused GitHub issues with clear titles, user-focused descriptions, and acceptance criteria. Do not implement them yet.
```

## Zrealizuj pierwsze zgłoszenie w tej sesji

1. Wciśnij klawisz <kbd>Left arrow</kbd>, aby otworzyć panel boczny, a następnie <kbd>Tab</kbd>, aby przejść na kartę **Issues**.
2. Podświetl pierwsze zgłoszenie i wciśnij <kbd>c</kbd>, aby dodać je do czatu jako kontekst. Aby najpierw przeczytać pełne zgłoszenie, wciśnij zamiast tego <kbd>Enter</kbd>.
3. Poproś agenta o zaimplementowanie zgłoszenia.

![Ilustracja panelu bocznego Copilot CLI w terminalu. Karta Issues jest wybrana spośród kart Current, Sessions, Issues, Pull requests i Gists. Filtr wyszukiwania otwartych zgłoszeń w repozytorium space-quiz pokazuje jedno zgłoszenie: Add a score screen at the end of the quiz. Podpowiedzi wyjaśniają, że Left arrow otwiera panel, a Tab przełącza karty, a dolny wiersz wymienia klawisze: slash do wyszukiwania, Enter po szczegóły, o do otwarcia, w dla worktree, c do czatu i a dla wszystkich.](../../../_images/first-steps-cli-side-panel.svg)

Panel boczny wymienia karty u góry, a podpowiedzi na dole to klawisze działające na aktualnie podświetlony element.

## Przejrzyj zmianę poleceniem `/diff`

Projekt jest opublikowany, więc masz znaną dobrą wersję do porównania. `/diff` pokazuje dokładnie, co to zgłoszenie zmieniło względem niej — właśnie to, o czym zaraz poprosisz kogoś o przegląd.

1. Uruchom `/diff` i przeczytaj każdy zmieniony plik.
2. Poproś o poprawkę wszystkiego, co wygląda źle, a następnie uruchom `/diff` ponownie.
3. Uruchom `!git status` lub `!git diff`, kiedy chcesz sprawdzić Gita bezpośrednio.

## Zrealizuj drugie zgłoszenie równolegle

1. Otwórz ponownie panel boczny i przełącz się na kartę **Sessions**.
2. Uruchom kolejną sesję dla drugiego zgłoszenia bez utraty pierwszej.
3. W nowej sesji uruchom `/worktree`, żeby dostała izolowany worktree zamiast gałęzi w miejscu. Obie sesje mogą teraz działać jednocześnie bez wzajemnych zakłóceń.
4. Dodaj drugie zgłoszenie do tej sesji klawiszem <kbd>c</kbd>.
5. Na razie zostaw tę sesję. Następne ćwiczenie zaplanuje to zgłoszenie, zanim zostanie napisany jakikolwiek kod.

![Ilustracja wyjścia Copilot CLI po uruchomieniu /worktree. Raportuje utworzenie worktree ../space-quiz-13 na gałęzi issue-13-review-screen oraz to, że ta sesja pracuje teraz tam, podczas gdy main pozostaje nietknięty.](../../../_images/first-steps-cli-worktree.svg)

`/worktree` przenosi sesję do własnego checkoutu na własnej gałęzi, więc pierwsza sesja pracuje dalej bez zakłóceń.

## Podsumowanie i kolejne kroki

Zaimplementowałeś pierwsze zgłoszenie, przejrzałeś je z `/diff` i uruchomiłeś drugą sesję we własnym worktree. Przejdź do [ćwiczenia 5: Planowanie przed edycją][next-lesson].

[next-lesson]: ../5-plan-mode/
