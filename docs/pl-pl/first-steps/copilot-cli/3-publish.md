---
title: "Ćwiczenie 3 - Publikacja projektu"
description: "Zainicjalizuj, utwórz commit i opublikuj Space Quiz na GitHubie — przez prompt albo uruchamiając polecenia samodzielnie."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-10-04
---

Zamień eksperyment w publiczne repozytorium GitHub. Możesz o to poprosić jednym promptem albo uruchomić polecenia samodzielnie. Wypróbuj obie metody raz, a dokładnie poznasz, co agent robi w Twoim imieniu.

W tym ćwiczeniu:

- zainicjalizujesz repozytorium Git i utworzysz pierwszy commit.
- utworzysz i wypchniesz publiczne repozytorium GitHub.
- potwierdzisz, że commit i plik trafiły na miejsce.

## Opcja A: Poproś o to

Wyślij poniższe polecenie:

```plaintext
Initialize this folder as a Git repository, create an initial commit, and create a new public GitHub repository named space-quiz in my account. Push the current branch and set it as the default branch.
```

Zatwierdzaj każdą akcję Gita i GitHuba, gdy agent o to poprosi.

## Opcja B: Uruchom samodzielnie

Dodaj prefiks `!` przed każdym poleceniem, aby uruchomić je z sesji, albo uruchom polecenia bez prefiksu we własnym terminalu:

```plaintext
!git init -b main
!git add .
!git commit -m "Add space quiz"
!gh repo create space-quiz --public --source=. --push
```

Ostatnie polecenie używa [GitHub CLI][gh-cli]. Jeśli go nie masz, utwórz repozytorium na GitHubie, a następnie uruchom `!git remote add origin <url>` i `!git push -u origin main`.

## Potwierdź wynik

1. Uruchom `!git log --oneline`, aby potwierdzić, że commit trafił na miejsce.
2. Otwórz repozytorium na GitHubie i upewnij się, że `index.html` jest obecny.

## Podsumowanie i kolejne kroki

Projekt jest teraz repozytorium GitHub ze znaną dobrą wersją do porównań. Przejdź do [ćwiczenia 4: Praca nad zgłoszeniami równolegle][next-lesson].

[gh-cli]: https://cli.github.com/
[next-lesson]: ../4-issues-and-sessions/
