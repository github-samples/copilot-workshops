---
title: "Ćwiczenie 5 - Planowanie przed edycją"
description: "Przełącz drugą sesję w tryb planowania poleceniem /plan, żeby agent zaproponował podejście, zanim edytuje jakiekolwiek pliki."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Masz już drugą sesję działającą we własnym worktree. Nie zaczynaj tam od kodu. Tryb planowania bada projekt i proponuje podejście, pozostawiając pliki nietknięte.

W tym ćwiczeniu:

- przełączysz drugą sesję w tryb planowania.
- przejrzysz i dopracujesz zaproponowany plan agenta.
- zatwierdzisz plan i pozwolisz sesji go zaimplementować.

## Uzgodnij podejście przed jakąkolwiek edycją

1. Przełącz się na **drugą sesję**, którą otworzyłeś w poprzednim ćwiczeniu.
2. Uruchom `/plan`, aby przełączyć tę sesję w tryb planowania.
3. Wyślij poniższe polecenie i pozwól agentowi zbadać projekt bez edycji czegokolwiek:

   ```plaintext
   Plan how to implement this issue. Investigate the existing quiz, list the files you would change, call out risks to accessibility and the single-file constraint, and stop before making any edits.
   ```

4. Przeczytaj plan, dopytaj o brakujące elementy, a następnie zatwierdź go.
5. Sesja przechodzi do implementacji z zatwierdzonym planem jako wytycznymi.

> [!TIP]
> **Kiedy tryb planowania się opłaca**
>
> Używaj trybu planowania przy wszystkim, co jest niejednoznaczne, przekrojowe lub kosztowne do cofnięcia. Najtańsze miejsce na poprawę złego podejścia jest przed pierwszą edycją.

## Podsumowanie i kolejne kroki

Uzgodniłeś podejście z agentem, zanim napisał jakikolwiek kod. Przejdź do [ćwiczenia 6: Co agent widzi][next-lesson].

[next-lesson]: ../6-context/
