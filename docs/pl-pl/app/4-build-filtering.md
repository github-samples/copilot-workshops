---
title: "Lekcja 4 - Budowanie funkcji z Autopilot"
description: "Zbuduj statyczną, kliencką funkcję filtrowania wykorzystując tryby Plan i Autopilot w aplikacji GitHub Copilot, zobacz, jak dziedziczy standard dokumentacji, i zweryfikuj ją skillem agenta."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-09
---

Dotąd wprowadziliśmy kilka małych zmian w projekcie. Większe zmiany wymagają jednak bardziej rozbudowanego procesu. Na szczęście aplikacja GitHub Copilot jest zbudowana tak, by współpracować z istniejącymi przepływami i zapewniać, że budujemy właściwe rzeczy we właściwy sposób. To pierwsza z trzech lekcji, w których przejdziesz typowy proces tworzenia oprogramowania: zaczynając od zgłoszenia (issue), wygenerujesz nową funkcję, a skill agenta uruchomi testy walidacyjne i lintery.

Podczas tej lekcji:

- rozpoczniesz świeżą sesję na podstawie zgłoszenia o filtrowaniu.
- użyjesz trybu **Plan**, aby zaplanować implementację funkcji, a potem wykorzystasz **Autopilot**, aby ją zbudować.
- potwierdzisz, że wygenerowany kod stosuje standard dokumentacji wdrożony wcześniej.
- zweryfikujesz pracę skillem `quality-checks` projektu.

## Scenariusz

Strona główna wypisuje wszystkie gry, ale odwiedzający nie mogą zawęzić listy. Zgłoszenie o filtrowaniu wnioskuje, by umożliwić filtrowanie gier według **kategorii** i **wydawcy**. Użyjmy Copilota do zaimplementowania tej funkcjonalności.

## Kontekst

Wprowadzenie agentów kodujących AI do przepływu deweloperskiego nie zmienia podstaw. Jeśli już, stają się one jeszcze ważniejsze! Większość programistów stosuje przepływ zbliżony do:

1. Otwarcie złożonego zgłoszenia ze szczegółami tego, co trzeba zrobić.
2. Utworzenie planu tego, co trzeba zbudować.
3. Zbudowanie i przegląd kodu.
4. Uruchomienie testów w celu walidacji kodu.
5. Ręczna walidacja nowej funkcjonalności.
6. Utworzenie pull requesta (PR).
7. Gdy kod zostanie przejrzany i proces ciągłej integracji zakończy się sukcesem — scalenie kodu.

> [!NOTE]
> W zależności od zespołu i organizacji dokładne szczegóły będą się różnić. Większość będzie jednak wariacją powyższego motywu.

Trzymając się tego standardowego podejścia, zapewniasz, że kod wygenerowany przez AI spełnia wymagania i przechodzi ten sam proces weryfikacji co kod napisany ręcznie.

## Tryby sesji

**Tryb sesji** kontroluje, ile autonomii ma agent. Ustawisz go z listy rozwijanej pod polem monitu i możesz zmienić w dowolnym momencie:

- **Interactive**: Ty i agent pracujecie razem. Agent sugeruje zmiany i czeka na Twoje dane przed kontynuacją.
- **Plan**: Agent najpierw tworzy plan. Przeglądasz i zatwierdzasz plan, zanim agent go wykona.
- **Autopilot**: Agent pracuje w pełni autonomicznie — pisze kod, uruchamia testy i iteruje bez czekania na dane wejściowe.

## Zaplanuj funkcję filtrowania

Najlepszy moment, by wychwycić potencjalny problem, to zanim powstanie jakikolwiek kod, a najlepszy sposób to odrobina planowania z wyprzedzeniem. Planując z Copilotem, poprosisz go o wygenerowanie zestawu kroków i udokumentowanie podejścia. Następnie przejrzysz plan, wprowadzisz ewentualne sugestie usprawnień, a potem pozwolisz Copilotowi wygenerować kod na podstawie planu.

Otwórzmy zgłoszenie, rozpocznijmy nową sesję i utwórzmy plan, przełączając się w tryb planowania i wysyłając prośbę.

1. Wybierz **My work** z karty nawigacji.
2. Wybierz zgłoszenie o tytule **Allow users to filter games by category and publisher**.
3. Wybierz **New session** w prawym górnym rogu.

   ![Widok zgłoszenia w aplikacji GitHub Copilot ze strzałką wskazującą przycisk New session w prawym górnym rogu](../../_images/app-new-session-from-issue.png)

4. Użyj klawiszy <kbd>Shift</kbd>+<kbd>Tab</kbd>, aż tryb wyświetli **Plan**.

   ![Pole wpisywania poleceń aplikacji GitHub Copilot ze strzałką wskazującą selektor trybu ustawiony na Plan](../../_images/app-4-plan-mode.png)

5. Wyślij poniższe polecenie. Zgłoszenie o filtrowaniu jest już w kontekście tej sesji, bo zacząłeś od niego:

   ```plaintext
   Plan the work based on the requirements documented in the issue. Please ask any clarifying questions you might have as you build the plan.
   ```

6. Agent może zadawać dodatkowe pytania podczas budowania planu. Odpowiadaj na nie zgodnie z tym, jak zbudowałbyś funkcję.

> [!NOTE]
> Ponieważ Copilot jest probabilistyczny, dodatkowe pytania będą się różnić. W rzeczywistości może w ogóle nie zadać pytań! To całkowicie normalne.

7. Po zakończeniu Copilot zaproponuje podsumowanie planu. Przejrzyj plan. Powinieneś zobaczyć propozycję zbudowania zapytań, dodawania kontrolek filtrów i oczywiście testów. W razie potrzeby przekaż informację zwrotną — agent uwzględni Twoje sugestie w nowej wersji.

## Zbuduj to z Autopilot

Gdy plan jest gotowy, pozwólmy Copilotowi zbudować implementację!

1. Na liście opcji w oknie dialogowym **Plan summary** wybierz opcję najbliższą **Approve and implement with autopilot**.

Copilot zacznie pracę nad implementacją!

> [!NOTE]
> Jeśli Copilot nie zacznie automatycznie tworzyć niezbędnego kodu, możesz go do tego skłonić poleceniami w stylu „Go ahead and start building out the plan!”.
>
> Tworzenie niezbędnych aktualizacji zajmie kilka minut. Agent edytuje i tworzy pliki, pisze i uruchamia testy oraz iteruje. To dobry moment, by zastanowić się nad tym, co już zrobiłeś w ramach warsztatów, albo napić się czegoś.

## Przejrzyj zmiany

Cały kod wygenerowany przez AI wymaga przeglądu przed scaleniem. Przejrzyjmy kod i uruchommy witrynę, by upewnić się, że wszystko wygląda dobrze.

1. Wybierz **Changes** w prawym górnym rogu, aby otworzyć zmiany w kodzie.

   ![Karty panelu sesji w aplikacji GitHub Copilot ze strzałką wskazującą kartę Changes](../../_images/app-select-changes.png)

2. Przejrzyj zmiany. Powinieneś zobaczyć nowe pliki TypeScript i Astro oraz pliki testów. Zwróć uwagę, że nowe funkcje pomocnicze zawierają komentarze TSDoc i nagłówek komentarza pliku — standard dokumentacji scalony w Lekcji 3, zastosowany automatycznie bez potrzeby dodatkowych instrukcji z naszej strony.
3. W panelu przeglądu po prawej stronie aplikacji Copilot wybierz **Terminal**. Jeśli nie ma przycisku **Terminal**, wybierz **+** (etykieta **Open in panel**), a następnie **Terminal**.

   ![Przycisk Terminal w panelu kontekstowym aplikacji GitHub Copilot](../../_images/app-terminal-screenshot.png)

4. W oknie terminala wprowadź poniższe polecenie, aby uruchomić serwer deweloperski aplikacji webowej:

   ```shell
   npm run dev
   ```

5. Gdy serwer się uruchomi (zajmie to chwilę), otwórz okno przeglądarki.
6. Przejdź do http://localhost:4321.
7. Powinieneś teraz zobaczyć dostępne filtry na stronie startowej!
8. Jeśli coś nie wygląda dobrze, możesz poprosić Copilota o aktualizacje!
9. Gdy będziesz zadowolony, wróć do okna terminala.
10. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>C</kbd>, aby zatrzymać serwer deweloperski.

## Zweryfikuj pracę skillem quality-checks

Mógłbyś rzucić okiem na diff i uznać sprawę za załatwioną, ale zespół ma zdefiniowany próg jakości — i powtarzalny sposób jego sprawdzenia.

**Skille agenta** pozwalają dać Copilotowi wskazówki, jak wykonywać powtarzalne zadania, takie jak uruchamianie testów, generowanie buildów czy tworzenie pull requestów. Skille przechowywane są w folderze z instrukcjami, skryptami i zasobami, które agent może załadować na żądanie. [Agent Skills to otwarty standard][agent-skills-repo] używany przez szereg agentów, więc ten sam skill działa w Copilot Chat w trybie agenta, Copilot cloud agent, Copilot CLI i aplikacji GitHub Copilot.

Skille znajdują się w folderze `.github/skills` projektu albo globalnie w `~/.copilot/skills`. Każdy skill to folder zawierający plik `SKILL.md` z nagłówkiem YAML (`name` i `description`), a potem instrukcjami markdown:

```yaml
---
name: quality-checks
description: Run the project's test suites and linter to verify code changes are ready to commit, push, or merge.
---
```

Skille mogą też zawierać podfoldery ze skryptami, zasobami i materiałami referencyjnymi. Pełną strukturę opisuje [specyfikacja agent skills][agent-skills-spec].

> [!TIP]
> Skille są ładowane dynamicznie. Agent decyduje, który skill pasuje, na podstawie pola `description` — jasny, scenariuszowy opis to różnica między skillem używanym a ignorowanym.

## Zbadaj skill quality-checks

Zbadajmy skill, by zobaczyć, co robi.

1. Jeśli panel przeglądu nie jest jeszcze widoczny, otwórz go, wybierając **Toggle review panel** w prawym górnym rogu.

   ![Górny pasek narzędzi aplikacji GitHub Copilot ze strzałką wskazującą przycisk Toggle review panel na prawo od Create PR](../../_images/app-2-review-panel.png)

2. Wybierz **+**, aby dodać nowy element do panelu przeglądu.
3. Wybierz **File**.
4. Wyszukaj `SKILL.md`.
5. Wybierz `SKILL.md .github/skills/quality-checks` z listy plików, aby go otworzyć.
6. Zwróć uwagę na `name` i `description`. Opis mówi agentowi *kiedy* go użyć — gdy zmiany w kodzie wymagają testów, lintingu lub weryfikacji przed commitem, pushem lub mergem.
7. Przeczytaj skill. Zwróć uwagę, że dokumentuje, który skrypt uruchamia który zestaw (testy jednostkowe, testy end-to-end Playwright, ESLint), w jakiej kolejności i jak debugować typowe awarie — dzięki temu agent uruchamia sprawdzenia po drodze zespołu zamiast zgadywać.

## Uruchom sprawdzenia

W tej samej sesji filtrowania poproś agenta o weryfikację pracy. Nie musisz podawać nazwy skillu — agent dopasuje go na podstawie Twojej prośby.

1. Wróć do aplikacji Copilot.
2. Wywołaj skill bezpośrednio poleceniem `/quality-checks` i wciśnij <kbd>Enter</kbd>.
3. Zgodnie ze skillem agent uruchamia testy jednostkowe, linter i testy end-to-end oraz raportuje wyniki. Jeśli coś się nie powiedzie, poproś o naprawę i uruchom sprawdzenia ponownie, aż wszystko będzie zielone.
4. **Pozostaw tę sesję otwartą.** W następnej lekcji dodasz serwer Playwright MCP i użyjesz go, by zobaczyć funkcję filtrowania działającą w prawdziwej przeglądarce.

## Podsumowanie i kolejne kroki

Zbudowałeś prawdziwą funkcję od końca do końca i zweryfikowałeś ją względem wymagań zespołu! Konkretnie:

- rozpocząłeś świeżą sesję na podstawie zgłoszenia o filtrowaniu na aktualnym projekcie.
- użyłeś trybu Plan do zaplanowania funkcji i Autopilot do jej zbudowania.
- potwierdziłeś, że wygenerowana funkcja pomocnicza stosuje standard dokumentacji przygotowany w Lekcji 3.
- zweryfikowałeś pracę skillem `quality-checks`.

W następnym kroku podłączysz serwer Playwright MCP i poprosisz agenta o zbadanie funkcji filtrowania w prawdziwej przeglądarce. Przejdź do [Lekcji 5 - Testowanie z serwerem Playwright MCP][next-lesson].

## Zasoby

- [Praca z sesjami agenta w aplikacji GitHub Copilot][agent-sessions]
- [O Agent Skills][about-agent-skills]
- [Dostosowywanie aplikacji GitHub Copilot][customize-app]
- [O chmurowych i lokalnych sandboxach GitHub Copilot][sandboxes]

[ex0]: ../0-prerequisites/
[ex2]: ../2-add-star-rating/
[ex3]: ../3-custom-instructions/
[next-lesson]: ../5-mcp-playwright/
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification
