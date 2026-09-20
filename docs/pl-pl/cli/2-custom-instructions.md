---
title: "Ćwiczenie 2 - Instrukcje niestandardowe (Copilot CLI)"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-10
---

[← Poprzednie ćwiczenie: Instalacja Copilot CLI][previous-lesson] · [Następne ćwiczenie: Generowanie kodu z CLI →][next-lesson]

Kontekst jest kluczowy przy pracy z generatywną AI. Jeśli zadanie ma być wykonane w określony sposób — albo istnieje kontekst, który Copilot powinien znać — chcesz mieć pewność, że te informacje są dostępne dla agenta. Masz kilka narzędzi, które pomagają Copilotowi; poznamy je w trakcie tych warsztatów. Zaczynamy od [plików instrukcji][instruction-files], które zwykle skupiają się na tym, jak sam kod powinien być ustrukturyzowany. Dzięki temu Copilot rozumie nie tylko *jaki* kod chcesz, ale też *jak* powinien być zbudowany.

Podczas tego ćwiczenia:

- zobaczysz, jak kontekst projektu, wytyczne kodowania i standardy dokumentacji docierają do Copilota przez instrukcje niestandardowe repozytorium oraz pliki instrukcji ograniczone ścieżką,
- wygenerujesz pierwszy fragment kodu pod filtrowanie danych przy *obecnych* instrukcjach,
- dodasz nowy standard dla całego repozytorium do `.github/copilot-instructions.md`,
- uruchomisz polecenie uzupełniające i zobaczysz, jak zregenerowany kod przyjmie nowy standard,
- zatwierdzisz (commit) zmiany w instrukcjach i helperze, aby kolejne ćwiczenie mogło na nich budować.

> [!CAUTION]
> Wygenerowany kod może odbiegać od części ustalonych standardów. Copilot jest niedeterministyczny. Celem jest zobaczenie *tendencji* zmiany zachowania po aktualizacji instrukcji, a nie dopasowanie wyniku znak po znaku.

## Pliki instrukcji

### Scenariusz

Jak każdy dobry zespół deweloperski, Tailspin Toys ma zestaw wytycznych i wymagań dotyczących praktyk rozwoju. Obejmują one:

- Warstwa danych zawsze wymaga testów jednostkowych.
- UI powinien być w trybie ciemnym i mieć nowoczesny wygląd.
- Dokumentacja powinna być dodawana do kodu w formie komentarzy TSDoc.
- Na początku każdego pliku powinien znaleźć się blok komentarzy opisujący, co plik robi.

Dzięki plikom instrukcji zapewnisz Copilotowi właściwe informacje, aby wykonywał zadania zgodnie z tymi praktykami.

### Instrukcje niestandardowe

Instrukcje niestandardowe pozwalają przekazać Copilotowi kontekst i preferencje, żeby lepiej rozumiał styl programowania i oczekiwania. To potężna funkcja, która pomaga kierować Copilota ku bardziej trafnym sugestiom i fragmentom kodu. Możesz określić preferowane konwencje pisania kodu, wykorzystywanych bibliotek, a nawet typy komentarzy, które lubisz w kodzie. Instrukcje możesz tworzyć dla całego repozytorium albo dla konkretnych typów plików — z kontekstem na poziomie zadania.

Są dwa typy plików instrukcji:

- `.github/copilot-instructions.md` — jeden plik instrukcji wysyłany do Copilota przy **każdym** żądaniu dla repozytorium. Powinien zawierać informacje na poziomie projektu — kontekst istotny dla większości żądań czatu lub CLI do Copilota. Może to być używany stack technologiczny, przegląd tego, co budujesz, dobre praktyki i inne globalne wskazówki.
- Pliki `.github/instructions/*.instructions.md` można tworzyć dla konkretnych zadań lub typów plików. Użyjesz ich do wytycznych dla określonych języków (np. TypeScript lub Astro) albo zadań takich jak tworzenie komponentu UI czy nowego zestawu testów jednostkowych.

> [!NOTE]
> W IDE pliki instrukcji są używane tylko do generowania kodu w Copilot Chat — nie do uzupełnień kodu ani sugestii następnej edycji.
>
> Copilot Chat, Copilot CLI i Copilot cloud agent korzystają zarówno z plików na poziomie repozytorium, jak i z plików `*.instructions.md` (z front matter `applyTo`) przy generowaniu kodu.
>
> Ponadto Copilot [obsługuje pliki instrukcji według innych standardów][custom-instructions-support], w tym AGENTS.md i CLAUDE.md.

### Dobre praktyki zarządzania plikami instrukcji

Zaawansowane metodologie tworzenia plików instrukcji wykraczają poza zakres warsztatu. Przykłady w tym projekcie pokazują jednak reprezentatywne podejście. Na wysokim poziomie:

- W `copilot-instructions.md` trzymaj wskazówki na poziomie projektu: opis tego, co budujesz, strukturę projektu i globalne standardy kodowania.
- Używaj plików `*.instructions.md` do konkretnych instrukcji dla typów plików (testy jednostkowe, komponenty Astro, warstwa danych) lub zadań.
- Pisz językiem naturalnym. Utrzymuj wskazówki jasne. Podawaj przykłady, jak kod powinien (i nie powinien) wyglądać.

Nie ma jednej właściwej metody tworzenia plików instrukcji — tak jak nie ma jednej właściwej metody używania AI. Eksperymentując, znajdziesz to, co najlepiej działa w Twoim projekcie.

> [!TIP]
> Każdy projekt korzystający z GitHub Copilot powinien mieć solidny zestaw plików instrukcji. Przeglądając te w tym projekcie, możesz zauważyć pliki dla wielu typów zadań, w tym [aktualizacji UI][ui-instructions] i [Astro][astro-instructions].
>
> Copilot może też pomóc wygenerować pliki instrukcji. Każde środowisko robi to inaczej (np. **Configure Chat → Generate Agent Instructions** w VS Code albo `/init` w Copilot CLI) — ćwiczenie dla środowiska, w którym jesteś, wskaże to, gdy będzie to istotne.
>
> Szukasz szablonów lub punktu startowego? Zobacz [awesome-copilot][awesome-copilot] — repozytorium pełne plików instrukcji, agentów niestandardowych i innych zasobów.

## Przegląd plików instrukcji niestandardowych w tym projekcie

Poświęć chwilę na przeczytanie plików instrukcji dostarczonych z tym repozytorium — jest jeden główny `copilot-instructions.md` oraz kolekcja plików `*.instructions.md` dla różnych zadań. Otwórz je w edytorze lub w interfejsie webowym GitHuba.

1. Otwórz `.github/copilot-instructions.md`.
2. Przejrzyj plik, zwracając uwagę na krótki opis projektu oraz sekcje takie jak **Agent notes**, **Code standards**, **Scripts** i **Repository Structure**. W **Code standards** zwróć uwagę na zagnieżdżone wskazówki **GitHub Actions Workflows**. Dotyczą one każdej interakcji z Copilotem.
3. Otwórz folder `.github/instructions` i przejrzyj dostępne pliki. Są instrukcje dla plików Astro, warstwy danych Drizzle, testów i innych.
4. Otwórz `.github/instructions/unit-tests.instructions.md`. Zwróć uwagę na pole `applyTo` na górze — ustawia glob (względem katalogu głównego repozytorium), który określa, do których plików instrukcje się stosują. Tutaj pasuje każdy plik testów TypeScript (np. zgodny ze ścieżką `**/*.test.ts`).
5. Zwróć uwagę na instrukcje dotyczące tworzenia testów jednostkowych w tym projekcie.
6. Na koniec otwórz `.github/instructions/drizzle.instructions.md` i przewiń na dół. Zwróć uwagę na odnośniki do innych plików instrukcji (np. `unit-tests.instructions.md`) oraz istniejących plików w projekcie. Dzięki temu możesz dzielić większe zestawy instrukcji na mniejsze pliki wielokrotnego użytku i wskazywać Copilotowi przykłady do naśladowania przy generowaniu kodu. (Ścieżki tam są względne w odniesieniu do pliku instrukcji, a nie katalogu głównego repozytorium.)

> [!NOTE]
> Sekcja **Code formatting requirements** w `copilot-instructions.md` dokumentuje standardy pisania kodu w projekcie, ale jeszcze nie wymaga dokumentacji w kodzie. W kolejnych krokach dodasz reguły dla komentarzy TSDoc i nagłówków komentarzy plików.

## Utwórz gałąź

Będziesz wprowadzać zmiany w kodzie, więc utwórz gałąź do pracy.

1. W terminalu codespace utwórz i przełącz się na nową gałąź:

   ```bash
   git checkout -b update-custom-instructions
   ```

2. Upewnij się, że Copilot CLI jest zainstalowany i uwierzytelniony:

   ```bash
   copilot --version
   ```

   Jeśli polecenie nie zostanie znalezione lub nie jesteś zalogowany, wróć do [Ćwiczenia 1 - Instalacja GitHub Copilot CLI](../1-install-copilot-cli/).

## Użyj Copilot CLI *przed* aktualizacją instrukcji

Aby zobaczyć wpływ instrukcji niestandardowych, zacznij od wygenerowania kodu przy obecnych instrukcjach. Później zaktualizujesz plik i uruchomisz polecenie uzupełniające.

> [!CAUTION]
> `--yolo` włącza pełne automatyczne uprawnienia (`--allow-all-tools`, `--allow-all-paths` i `--allow-all-urls`). Używaj go tylko w izolowanym środowisku, takim jak codespace lub maszyna wirtualna, i nigdy nie ustawiaj go jako domyślnego aliasu w codziennej pracy. Szczegóły: [Allowing and denying tool use][allow-all-warning].

Uruchomienie Copilot CLI z **katalogu głównego repozytorium** zapewnia automatyczne wczytanie `.github/copilot-instructions.md`. `--enable-all-github-mcp-tools` włącza narzędzia GitHub MCP do odczytu/zapisu, aby Copilot mógł czytać backlog i otwierać pull requesty w dalszej części tych warsztatów.

1. Wróć do codespace. Jeśli go zamknąłeś, przejdź do repozytorium na GitHub.com, wybierz **Code** > **Codespaces**, a następnie ponownie otwórz istniejący codespace.
2. Wróć do otwartej sesji Copilot CLI. Jeśli terminal jest zamknięty lub wyszedłeś z Copilot CLI, otwórz terminal. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>\`</kbd>, a następnie uruchom go z katalogu głównego repozytorium poleceniem `copilot --yolo --enable-all-github-mcp-tools`. Zaufaj folderowi projektu, jeśli zostaniesz o to poproszony, potem uruchom `/models` i wybierz **Auto**.
3. W interfejsie Copilot CLI poproś o wygenerowanie funkcji wspomagającej filtrowanie danych o dostępnych wydawcach:

   ```plaintext
   Create a new data-access helper at src/lib/publishers.ts to return a list of all publishers. It should return the name and id for all publishers. Do not run the tests yet.
   ```

4. Copilot CLI zbada projekt, zaproponuje plan i zapisze plik w tej sesji `--yolo`. Monitoruj zmiany w oknie terminala, a następnie przejrzyj je w edytorze.
5. Otwórz wygenerowany `src/lib/publishers.ts` w edytorze.
6. Zwróć uwagę, że funkcja wspomagająca to typowana metoda przyjmująca klienta `db` jako pierwszy argument i zwracająca typowaną tablicę wydawców — to wynika z konwencji warstwy danych w `.github/instructions/drizzle.instructions.md` (które dotyczą `src/lib/*.ts`).
7. Zwróć uwagę, że w wygenerowanym kodzie **brakuje** komentarzy TSDoc oraz nagłówka komentarza na poziomie pliku.

> [!CAUTION]
> Copilot jest probabilistyczny — istnieje szansa, że doda komentarze dokumentacyjne nawet bez polecenia. Jeśli tak się stanie, to w porządku; wnioskiem nadal jest *poprawa spójności* po aktualizacji instrukcji.

## Dodaj nowy standard repozytorium

Jak wspomniano wcześniej, `.github/copilot-instructions.md` służy do przekazywania Copilotowi informacji na poziomie projektu. Upewnijmy się, że standardy kodowania repozytorium są udokumentowane, aby poprawić sugestie kodu.

1. Ponownie otwórz `.github/copilot-instructions.md`.
2. Znajdź sekcję **Code formatting requirements**, która powinna być w okolicy linii 27. Zwróć uwagę, jak dokumentuje standardy samego pisania kodu w projekcie — ale nie ma jeszcze reguły odnośnie pisania dokumentacji w kodzie, dlatego wygenerowany helper nie miał adekwatnej dokumentacji w postaci komentarzy.
3. Dodaj poniższe linie markdown tuż pod istniejącymi standardami, aby poinstruować Copilota o nagłówkach z komentarzami w plikach i komentarzach TSDoc:

   ```markdown
   - Every exported function should have a TSDoc comment describing its purpose, parameters, and return value.
   - Before imports or any code, add a comment block to the file that explains its purpose.
   ```

4. Zapisz `copilot-instructions.md`.

> [!TIP]
> Jak widziałeś w poprzednim ćwiczeniu, pliki instrukcji można tworzyć na poziomie repozytorium (`.github/copilot-instructions.md`) dla wskazówek globalnych albo jako pliki `*.instructions.md` dla konkretnych języków, typów plików lub zadań. Plik na poziomie repozytorium to właściwe miejsce na standardy obejmujące cały projekt, takie jak reguła komentarzy dokumentacyjnych, którą właśnie dodałeś.

## Ponownie uruchom polecenie i zaobserwuj zmianę

Skoro instrukcje mają już wpis o generowaniu komentarzy, poproś Copilot CLI o aktualizację właśnie wygenerowanego pliku wydawców. Ta sama dyrektywa standardów pokieruje przepisaniem.

1. Wyślij `/clear` w sesji Copilot CLI, aby zacząć od czystej rozmowy.
2. Wyślij poniższe polecenie:

   ```plaintext
   Update src/lib/publishers.ts to follow the latest documentation conventions in .github/copilot-instructions.md.
   ```

3. Poczekaj na zakończenie edycji, a następnie ponownie otwórz `src/lib/publishers.ts`.
4. Zwróć uwagę, że plik otwiera się teraz blokiem komentarza podobnym do:

   ```typescript
   /**
    * Publisher data-access helpers for the Tailspin Toys Crowd Funding platform.
    * Provides functions to retrieve publisher information from the database.
    */
   ```

5. Zwróć uwagę, że wygenerowana funkcja zawiera teraz komentarz TSDoc podobny do:

   ```typescript
   /**
    * Returns a list of all publishers with their id and name.
    *
    * @param db - The Drizzle database client.
    * @returns A promise that resolves to an array of publisher objects.
    */
   ```

6. Zostaw ten zaktualizowany plik na miejscu. To pierwszy fragment danych, na którym zbudujesz kolejne funkcjonalności w następnym ćwiczeniu.

## Commit i push pierwszego fragmentu filtrowania

1. W terminalu sprawdź zmienione pliki:

   ```bash
   git status
   ```

2. Dodaj do listy zmian aktualizację instrukcji i zmodyfikowany kod:

   ```bash
   git add .github/copilot-instructions.md src/lib/publishers.ts
   ```

3. Zatwierdź zmiany:

   ```bash
   git commit -m "Add doc comment standards and publishers helper foundation"
   ```

4. Wypchnij gałąź:

   ```bash
   git push -u origin update-custom-instructions
   ```

## Podsumowanie i kolejne kroki

Zobaczyłeś, jak Copilot pobiera kontekst z plików instrukcji w tym projekcie, a następnie użyłeś Copilot CLI do:

- wygenerowania fundamentu funkcji wspomagającej filtrowanie danych wydawców za pomocą *istniejących* instrukcji,
- dodania nowego standardu dla całego repozytorium w `.github/copilot-instructions.md`,
- uruchomienia polecenia aktualizującego poprzednie instrukcje i obserwacji, jak zregenerowany kod przyjął nowy standard,
- zatwierdzenia i wypchnięcia zarówno zmian w instrukcjach, jak i pierwszych zmian w kodzie.

W następnym kroku zastosujesz te instrukcje, realizując pracę z backlogu w [ćwiczeniu generowania kodu][next-lesson].

## Zasoby

- [Pliki instrukcji do dostosowywania GitHub Copilot][instruction-files]
- [Dobre praktyki tworzenia instrukcji niestandardowych][instructions-best-practices]
- [5 wskazówek dotyczących lepszych instrukcji niestandardowych dla Copilot][copilot-instructions-five-tips]
- [Awesome Copilot — zbiór plików instrukcji i innych zasobów][awesome-copilot]

[previous-lesson]: ../1-install-copilot-cli/
[next-lesson]: ../3-generating-code/
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[copilot-instructions-five-tips]: https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/
[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools
[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[awesome-copilot]: https://github.com/github/awesome-copilot
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
