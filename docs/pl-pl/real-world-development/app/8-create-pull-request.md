---
title: "Lekcja 8 - Tworzenie i scalanie PR funkcji"
description: "Przejrzyj razem filtrowanie, instrukcje, aktualizację skillu, profil QA i testy, potem utwórz PR i użyj Agent Merge."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-17
---

Implementacja filtrowania, aktualizacje instrukcji, aktualizacja skillu, profil zapewnienia jakości (QA) i testy są zapisane na jednej gałęzi. Czas przejrzeć je razem i otworzyć pull request. Pull request (PR) z ocenami w gwiazdkach scalałeś samodzielnie; tym razem pozwolisz **Agent Merge** zarządzać procesem.

> [!NOTE]
> Zwykle rozdzielilibyśmy funkcję, aktualizacje instrukcji, aktualizację skillu i agenta QA na kilka osobnych PR. Aby usprawnić warsztat, utrzymałeś pełny przepływ filtrowania i jakości w jednej sesji i na jednej gałęzi — cała ta praca trafia do tego PR.

W tej lekcji:

- poznasz, czym jest Agent Merge i jak automatyzuje cykl życia scalania.
- przejrzysz pełny PR funkcji oraz dowody weryfikacji.
- autoryzujesz Agent Merge dopiero po przeglądzie i potwierdzisz, że PR został scalony.

## Scenariusz

W całym przepływie filtrowania używałeś Copilota do planowania, implementacji i weryfikacji funkcji. Tailspin Toys chce teraz zautomatyzować pozostałą pracę nad PR, zachowując autoryzację scalenia pod kontrolą dewelopera.

## Przedstawiamy Agent Merge

**Agent Merge** automatyzuje pozostałą pracę potrzebną do wprowadzenia pull requesta w aplikacji GitHub Copilot. Gdy go włączysz, sesja aplikacji czyta Twój pull request, zajmuje się tym, co go blokuje — naprawia nieprzechodzące sprawdzenia ciągłej integracji (CI), odpowiada na uwagi z przeglądu, w razie potrzeby wykonuje rebase — i scala go, gdy tylko GitHub na to pozwoli. Działa w tle, przetrwa restarty aplikacji i wyłącza się sam, gdy pull request zostanie scalony.

Do tej pory samodzielnie wybierałeś **Merge pull request**. Agent Merge może przejąć tę odpowiedzialność, ale jego możliwość edycji kodu i scalania nadal wymaga Twojej wyraźnej autoryzacji. Przed przyznaniem uprawnienia do scalania przejrzyj dozwolone działania i samą pracę.

## Użyj Agent Merge do zarządzania PR

Gdy cały kod jest utworzony i przejrzany, pozwólmy Agent Merge zarządzać procesem PR.

1. Użyj selektora agenta, by wybrać **Default agent**.
2. Wybierz listę rozwijaną obok **Create PR**.
3. Wybierz **Agent merge**. Przycisk zmienia się na **Agent merge**.
4. Wybierz **Agent merge**, by uruchomić proces Agent Merge.

Proces Agent Merge się rozpoczyna. W jego ramach:

- Utworzy pull request z tytułem i opisem.
- Jeśli zacząłeś sesję od zgłoszenia, odwoła się do powiązanego zgłoszenia w treści opisu.
- Wykona rebase lub obsłuży ewentualne konflikty scalania z gałęzią docelową.
- Będzie monitorować proces CI, by upewnić się, że wszystkie sprawdzenia przechodzą.
- Będzie monitorować PR pod kątem opinii innych deweloperów lub przeglądu kodu Copilot. Wprowadzi aktualizacje, by rozwiązać te uwagi.
- Opcjonalnie może automatycznie scalić PR, gdy wszystko się powiedzie.

Pozwólmy Agent Merge także scalić PR, gdy wszystko przejdzie!

5. Wybierz listę rozwijaną obok **Agent merge**.
6. Upewnij się, że obok **Merge pull request** jest zaznaczenie.


> [!IMPORTANT]
> Agent Merge nie omija ochrony repozytorium ani brakujących uprawnień. Rozwiąż te blokery, zanim przejdziesz dalej.

## Podsumowanie i kolejne kroki

Zautomatyzowałeś kilka części procesu rozwoju, w tym generowanie kodu, testowanie i walidację, a teraz także proces pull requesta. W tej lekcji:

- poznałeś, czym jest Agent Merge i jak automatyzuje cykl życia scalania.
- przejrzałeś pełny PR funkcji oraz dowody weryfikacji.
- autoryzowałeś Agent Merge dopiero po przeglądzie i potwierdziłeś, że PR został scalony.

Następnie [użyjesz istniejącej kanwy i utworzysz kanwę triage][next-lesson], by poznać bogatszy sposób przeglądania, planowania i wizualizacji pracy z agentem.

## Zasoby

- [Managing issues and pull requests with the GitHub Copilot app][managing-issues-prs]
- [About the GitHub Copilot app][about-copilot-app]

[next-lesson]: ../9-canvases/
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
