---
title: "Lekcja 3 - Instrukcje niestandardowe w Copilocie"
description: "Dodamy do repozytorium zestaw instrukcji niestandardowych za pomocą aplikacji GitHub Copilot: zacznij od zgłoszenia w backlogu i scal zmianę jako pull request."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-09
---

Kontekst jest kluczowy przy pracy z generatywną AI. Jeśli zadanie ma być wykonane w określony sposób — albo istnieje informacja kontekstowa, którą Copilot powinien znać — trzeba się upewnić, by ten kontekst był dostępny. Jednym z najpotężniejszych narzędzi są [pliki instrukcji][instruction-files], które opisują nie tylko *co* ma powstać, ale *jak* powinno być ustrukturyzowane. Podczas tej lekcji dodasz do repozytorium standard dokumentacji — i zrobisz to tak, jak będziesz wykonywać większość pracy od tej chwili: zaczynając od zgłoszenia (issue) w backlogu i pozwalając agentowi wprowadzić zmianę.

Podczas tej lekcji:

- zapoznasz się z tym, jak instrukcje repozytorium i pliki instrukcji ograniczone do ścieżek docierają do agenta.
- rozpoczniesz sesję ze zgłoszenia o instrukcjach w backlogu.
- poprosisz agenta o dodanie standardu dokumentacji do `.github/copilot-instructions.md`.
- przejrzysz zmianę i scalisz ją jako pull request.

## Scenariusz

Jak każdy dobry zespół deweloperski, Tailspin Toys ma zestaw wytycznych i wymagań dotyczących praktyk tworzenia oprogramowania. Są one następujące:

- Dokumentacja powinna być dodawana do kodu w formie komentarzy TSDoc.
- Formatowanie powinno być udokumentowane i egzekwowane przez linting.

Dzięki plikom instrukcji mamy gwarancję, że Copilot ma właściwe informacje, by wykonywać zadania zgodnie z tymi praktykami.

## Pliki instrukcji

Instrukcje niestandardowe pozwalają przekazać Copilotowi kontekst i preferencje, aby lepiej rozumiał styl pisania kodu i wymagania. To potężna funkcja, która pomaga kierować Copilota ku bardziej trafnym sugestiom i fragmentom kodu. Możesz określić preferowane konwencje kodowania, biblioteki, a nawet typy komentarzy, które lubisz w kodzie. Możesz tworzyć instrukcje dla całego repozytorium albo dla określonych typów plików — jako kontekst na poziomie zadania.

Są dwa typy plików instrukcji:

- `.github/copilot-instructions.md` — pojedynczy plik instrukcji wysyłany do Copilota przy **każdym** żądaniu dla repozytorium. Powinien zawierać informacje na poziomie projektu — kontekst istotny dla większości żądań czatu lub CLI wysyłanych do Copilota. Może obejmować używany stos technologiczny, przegląd tego, co budujesz, dobre praktyki i inne globalne wskazówki.
- Pliki `.github/instructions/*.instructions.md` można tworzyć dla konkretnych zadań lub typów plików. Użyj ich, by podać wytyczne dla określonych języków (np. TypeScript lub Astro) albo zadań takich jak tworzenie komponentu UI czy nowego zestawu testów jednostkowych.

> [!NOTE]
> Copilot obsługuje też inne standardy wnoszenia wskazówek instrukcji przez AGENTS.md, CLAUDE.md i GEMINI.md, dzięki czemu Copilot zawsze ma właściwy kontekst.

### Dobre praktyki zarządzania plikami instrukcji

Zaawansowane metodologie tworzenia plików instrukcji wykraczają poza zakres warsztatu. Przykłady w tym projekcie pokazują jednak reprezentatywne podejście. Na wysokim poziomie:

- W `copilot-instructions.md` trzymaj instrukcje skupione na wskazówkach projektowych, takich jak opis tego, co jest budowane, struktura projektu i globalne standardy pisania kodu.
- Używaj plików `*.instructions.md`, by podawać konkretne instrukcje dla typów plików (testy jednostkowe, komponenty Astro, warstwa danych) lub konkretnych zadań.
- Używaj języka naturalnego. Niech wskazówki będą jasne. Podawaj przykłady, jak kod powinien (i nie powinien) wyglądać.

Nie ma jednego sposobu tworzenia plików instrukcji, tak jak nie ma jednego sposobu używania AI. Poprzez eksperymenty musisz znaleźć sposób, który najlepiej zadziała w Twoim projekcie.

> [!TIP]
> Każdy projekt używający GitHub Copilot powinien mieć solidny zestaw plików instrukcji. Badając te w tym projekcie, możesz zauważyć pliki instrukcji dla wielu typów plików kodu.
>
> Szukasz szablonów lub punktu wyjścia? Zajrzyj do [awesome-copilot][awesome-copilot] — to repozytorium jest pełne plików instrukcji, agentów niestandardowych i innych zasobów.

## Zbadaj pliki instrukcji niestandardowych w tym projekcie

Poświęć chwilę na przeczytanie plików instrukcji dostarczanych z tym repozytorium — jest jeden główny `copilot-instructions.md` oraz zestaw plików `*.instructions.md` dla różnych zadań. Otwórz je w edytorze lub w interfejsie webowym GitHuba.

1. Jeśli panel przeglądu nie jest jeszcze widoczny, otwórz go, wybierając **Toggle review panel** w prawym górnym rogu.

   ![Górny pasek narzędzi aplikacji GitHub Copilot ze strzałką wskazującą przycisk Toggle review panel na prawo od Create PR](../../_images/app-2-review-panel.png)

2. Wybierz **+**, aby dodać nowy element do panelu przeglądu.
3. Wybierz **File**.
4. Wyszukaj `copilot-instructions.md`.
5. Wybierz `copilot-instructions.md` z listy plików, aby go otworzyć.
6. Zbadaj plik, zwracając uwagę na krótki opis projektu oraz sekcje takie jak **Agent notes**, **Code standards**, **Scripts** i **Repository Structure**. W **Code standards** zauważ zagnieżdżone wskazówki **GitHub Actions Workflows**. Dotyczą one wszelkich interakcji z Copilotem.
7. Wybierz **Show folder view**, aby otworzyć nawigator folderów.

   ![Przycisk Show folder view w panelu przeglądu z otwartym plikiem w aplikacji GitHub Copilot](../../_images/app-show-folder-view.png)

8. Przejdź do folderu `.github/instructions` i zbadaj pliki. Zauważ, że są instrukcje dla plików Astro, warstwy danych Drizzle, testów i innych.
9. Otwórz `.github/instructions/unit-tests.instructions.md`. Zwróć uwagę na pole `applyTo` na górze — ustawia glob (względem katalogu głównego repozytorium), który określa, do których plików instrukcje się stosują. W tym wypadku pasuje każdy plik testów TypeScript (np. pasujący do `**/*.test.ts`).
10. Zwróć uwagę na instrukcje dotyczące tworzenia testów jednostkowych dla tego projektu.
11. Na koniec otwórz `.github/instructions/drizzle.instructions.md` i przewiń na dół. Przejrzyj linki do innych plików instrukcji (np. `unit-tests.instructions.md`) oraz istniejących plików w projekcie. Dzięki temu możesz dzielić większe zestawy instrukcji na mniejsze, wielokrotnego użytku pliki i wskazywać Copilotowi przykłady do naśladowania przy generowaniu kodu. (Ścieżki tam są względne wobec pliku instrukcji, a nie katalogu głównego repozytorium.)

> [!NOTE]
> Sekcja **Code formatting requirements** w `copilot-instructions.md` dokumentuje standardy kodu w projekcie, ale nie wymaga jeszcze dokumentacji w kodzie. W kolejnych krokach dodasz reguły dotyczące komentarzy TSDoc i nagłówków komentarzy w plikach.

## Zacznij od zgłoszenia o instrukcjach

W poprzedniej lekcji rozpocząłeś sesję od bezpośredniego polecenia do Agenta. Większość pracy zaczyna się jednak od zgłoszenia. Utwórzmy nową sesję na podstawie zgłoszenia o aktualizacji plików instrukcji, a potem poprośmy o aktualizację.

> [!NOTE]
> Ponieważ pliki instrukcji mają duży wpływ na kod generowany przez Copilota, należy dbać o to, by jasno go prowadziły. Pozwolenie Copilotowi na utworzenie pierwszej wersji — jak zrobisz w tej lekcji — to dobre podejście, lecz potem powinieneś samodzielnie go przejrzeć, by upewnić się, że aktualizacje spełniają wymagania.

1. Wybierz **My work** na pasku bocznym
2. Wybierz zgłoszenie o tytule **Update our repository coding standards**, aby je otworzyć.
3. Wybierz **New session** w prawym górnym rogu, aby rozpocząć nową sesję na podstawie zgłoszenia.

   ![Widok zgłoszenia w aplikacji GitHub Copilot ze strzałką wskazującą przycisk New session w prawym górnym rogu](../../_images/app-new-session-from-issue.png)

4. Użyj poniższego polecenia, aby poprosić Copilota o aktualizację plików instrukcji zgodnie z wymaganiami udokumentowanymi w zgłoszeniu:

  ```plaintext
  Following this issue, make the updates to the instructions files in this project to meet the requirements documented. Don't create the PR quite yet!
  ```

Copilot wprowadzi zmiany!

## Przejrzyj zmianę

Przeczytajmy zmiany w kodzie wprowadzone przez Copilota, a także poprośmy go o przykład kodu, który teraz będzie generował na podstawie zaktualizowanych instrukcji.

1. Wybierz **Changes** w prawym górnym rogu, aby otworzyć zmiany w kodzie.

   ![Karty panelu sesji w aplikacji GitHub Copilot ze strzałką wskazującą kartę Changes](../../_images/app-select-changes.png)

2. Przejrzyj zaktualizowany plik instrukcji. Upewnij się, że zawiera wytyczne dotyczące dodawania dokumentacji i komentarzy do kodu.

> [!NOTE]
> Ponieważ AI jest probabilistyczna, a nie deterministyczna, dokładny tekst będzie się różnić.

3. Użyj poniższego zapytania, aby poprosić Copilota o utworzenie przykładu kodu, który teraz będzie generował:

  ```plaintext
  Do not make any updates, but show me what the code would look like. Based on the new instructions, if I asked Copilot to create a new library component to return all Publishers what would that code look like?
  ```

4. Przejrzyj kod zaproponowany przez Copilota. Zwróć uwagę na komentarze TSDoc i nagłówek komentarza pliku — to dokładnie to, o co proszą zaktualizowane instrukcje.

Zaktualizowałeś pliki instrukcji w projekcie i sprawdziłeś, jaki będzie ich wpływ!

## Otwórz i scal pull request

Pliki instrukcji stają się zasobami w repozytorium, czyli są współdzielone z resztą zespołu. Utwórzmy PR z naszą zmianą!

1. W prawym górnym rogu wybierz **Create PR**.
2. Jeśli zostaniesz o to poproszony, wybierz **Sign in with your browser** i postępuj zgodnie z instrukcjami, aby się uwierzytelnić.
3. Copilot zabiera się do tworzenia PR.

Gdy PR zostanie utworzony, Copilot będzie obserwować workflow w repozytorium, który musi się uruchomić. Po chwili przycisk w prawym górnym rogu zmieni się na **Ready to merge**. To znak, że Twój PR jest gotowy do scalenia!

4. Wybierz **Ready to merge**.
5. Wybierz **Merge pull request** w nowym oknie dialogowym, aby scalić pull request!

> [!NOTE]
> Gdy standard zostanie scalony z gałęzią domyślną, staje się częścią projektu dla wszystkich — i dla każdej nowej sesji. Gdy w następnej lekcji rozpoczniesz sesję filtrowania z aktualnej gałęzi domyślnej, agent będzie automatycznie stosować ten standard. Zobaczysz, że generowany TypeScript zawiera komentarze TSDoc bez pytania — mały, ale realny dowód, że instrukcje kształtują generowany kod.

## Podsumowanie i kolejne kroki

Zbadałeś, jak aplikacja pobiera kontekst z plików instrukcji, a następnie użyłeś sesji, by dodać i scalić standard obejmujący całe repozytorium. Konkretnie:

- poznałeś `copilot-instructions.md` repozytorium oraz pliki `*.instructions.md` ograniczone do ścieżek.
- rozpocząłeś sesję na podstawie zgłoszenia o instrukcjach w backlogu.
- poprosiłeś agenta o dodanie standardu dokumentacji do `.github/copilot-instructions.md`.
- przejrzałeś zmianę i scaliłeś ją jako pull request.

W następnym kroku zbudujesz funkcję filtrowania w świeżej sesji — i zobaczysz, jak Agent wdraża standard, który właśnie scaliłeś. Przejdź do [Lekcji 4 - Budowanie funkcji z Autopilot][next-lesson].

## Zasoby

- [Pliki instrukcji do dostosowania GitHub Copilot][instruction-files]
- [Dostosowywanie aplikacji GitHub Copilot][customize-app]
- [Dobre praktyki tworzenia instrukcji niestandardowych][instructions-best-practices]
- [Awesome Copilot — zbiór plików instrukcji i innych zasobów][awesome-copilot]

[next-lesson]: ../4-build-filtering/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[awesome-copilot]: https://awesome-copilot.github.com/
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
