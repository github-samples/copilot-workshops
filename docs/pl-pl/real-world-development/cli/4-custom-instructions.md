---
title: "Ćwiczenie 4 - Kierowanie Copilotem za pomocą instrukcji niestandardowych"
description: "Poznaj instrukcje repozytorium, dodaj standard dokumentacji i zastosuj go do kodu filtrowania."
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-18
---

Kontekst jest kluczowy przy pracy z generatywną AI. Jeśli zadanie ma być wykonane w określony sposób, chcesz, żeby te wskazówki były dostępne dla Copilota. [Pliki instrukcji][instruction-files] opisują nie tylko *jaki* kod chcesz, ale też *jak* powinien być ustrukturyzowany. Skoro zbudowałeś filtrowanie, przejrzysz instrukcje, z których korzystał Copilot, dodasz standard dokumentacji i zastosujesz go do kodu.

W tym ćwiczeniu:

- zobaczysz, jak instrukcje repozytorium oraz pliki instrukcji ograniczone ścieżką docierają do agenta.
- zaktualizujesz plik instrukcji, aby zapewnić przestrzeganie standardów kodowania.
- zobaczysz wpływ plików instrukcji na kod.

## Scenariusz

Jak każdy dobry zespół deweloperski, Tailspin Toys ma zestaw wytycznych i wymagań dotyczących praktyk rozwoju. Obejmują one:

- Komentarze powinny wyjaśniać intencję i nieoczywiste decyzje, a nie powtarzać kod.
- Wyeksportowane funkcje w `db/` i `src/lib/` powinny dokumentować cel, parametry i wartości zwracane za pomocą TSDoc/JSDoc, w tym wstrzykiwany argument `db`, gdy jest obecny.
- Wielokrotnego użytku komponenty Astro powinny dokumentować kontrakty `Props`, a komentarze powinny pozostawać aktualne przy zmianach powiązanego kodu.
- Istniejące wytyczne formatowania i lintowania powinny zostać zachowane.

Dzięki plikom instrukcji zapewnisz Copilotowi właściwe informacje, aby wykonywał zadania zgodnie z tymi praktykami.

## Pliki instrukcji

Instrukcje niestandardowe pozwalają przekazać Copilotowi kontekst i preferencje, żeby lepiej rozumiał styl programowania i wymagania. To potężna funkcja, która pomaga kierować Copilota ku bardziej trafnym sugestiom i fragmentom kodu. Możesz określać preferowane konwencje kodowania, biblioteki, a nawet rodzaje komentarzy, które lubisz umieszczać w kodzie. Możesz tworzyć instrukcje dla całego repozytorium albo dla określonych typów plików — jako kontekst na poziomie zadania.

Istnieją dwa typy plików instrukcji:

- `.github/copilot-instructions.md` — pojedynczy plik instrukcji wysyłany do Copilota przy **każdym** żądaniu dotyczącym repozytorium. Ten plik powinien zawierać informacje na poziomie projektu istotne dla większości żądań.
- pliki `.github/instructions/*.instructions.md`, które dostarczają wytycznych dla konkretnych języków, typów plików lub zadań.

> [!NOTE]
> Inne formaty instrukcji i zakres wsparcia różnią się w zależności od środowiska. Zapoznaj się z [dokumentacją obsługi instrukcji niestandardowych][custom-instructions-support], zanim oprzesz się na konkretnym formacie.

## Przejrzyj pliki instrukcji niestandardowych w tym projekcie

Aby ułatwić start, zestaw plików instrukcji jest już dołączony do projektu startowego. Przejrzyjmy, co już jest, zanim wprowadzimy zmianę i zobaczymy jej wpływ.

1. Wróć do Codespace.
2. W edytorze Codespaces (nie w terminalu) otwórz `.github/copilot-instructions.md`.
3. Przejrzyj plik, zwracając uwagę na krótki opis projektu i wytyczne kodowania. Te instrukcje obowiązują przy każdej interakcji z Copilotem w tym repozytorium.
4. Otwórz folder `.github/instructions` i przejrzyj pliki. Zwróć uwagę, że są instrukcje dla plików Astro, warstwy danych Drizzle, testów i innych.
5. Otwórz `.github/instructions/unit-tests.instructions.md`. Zwróć uwagę na pole `applyTo` na górze — ustawia glob określający, do których plików stosują się instrukcje.
6. Otwórz `.github/instructions/drizzle.instructions.md` i zwróć uwagę na odnośniki do innych plików instrukcji oraz istniejących plików projektu. Dzięki temu możesz dzielić większe zestawy instrukcji na mniejsze, wielokrotnego użytku pliki i wskazywać Copilotowi przykłady do naśladowania.

## Zaktualizuj pliki instrukcji zgodnie z wytycznymi zespołu

Istniejące pliki to dobry start, ale nadal jest luka. Zmodyfikujmy główny plik `copilot-instructions.md`, aby zapewnić dodawanie komentarzy TSDoc do nowo generowanego TypeScriptu.

1. W `.github/copilot-instructions.md` znajdź sekcję zatytułowaną **Code formatting guidance** — powinna być około linii 35.
2. Dodaj poniższy punkt jako ostatni element listy:

   ```markdown
   - All new TypeScript should contain TSDocs comments for documentation purposes.
   ```

Plik zostanie zapisany automatycznie!

## Użyj zaktualizowanych wytycznych

Copilot CLI wczytuje instrukcje repozytorium przy starcie rozmowy. Po edycji wznów rozmowę o filtrowaniu, żeby nowe wytyczne były dostępne bez utraty kontekstu funkcji.

1. Poproś Copilota o zastosowanie zaktualizowanych wytycznych:

   ```plaintext
   We just updated our instructions and code guidance. Can you please update the code you generated to match that guidance?
   ```

2. Wpisz `/diff` i przeczytaj zmienione pliki TypeScript. Zwróć uwagę na nowo wygenerowane komentarze TSDoc i upewnij się, że dokładnie wyjaśniają kod.

## Podsumowanie i kolejne kroki

Poznałeś, jak Copilot CLI pobiera kontekst z plików instrukcji, i zastosowałeś nowy standard do swojej funkcji. Konkretnie:

- zobaczyłeś, jak instrukcje repozytorium oraz pliki instrukcji ograniczone ścieżką docierają do agenta.
- zaktualizowałeś plik instrukcji, aby zapewnić przestrzeganie standardów kodowania.
- zobaczyłeś wpływ plików instrukcji na kod.

Następnie [dostosujesz i uruchomisz wielokrotnego użytku skill quality-checks][next-lesson], aby lintowanie i testy były uruchamiane spójnie.

## Zasoby

- [Add custom instructions for Copilot CLI][instruction-files]
- [Custom instructions support][custom-instructions-support]
- [Best practices for creating custom instructions][instructions-best-practices]
- [Awesome Copilot — a collection of instruction files and other resources][awesome-copilot]

[instruction-files]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
[instructions-best-practices]: https://docs.github.com/copilot/concepts/prompting/response-customization#writing-effective-custom-instructions
[awesome-copilot]: https://awesome-copilot.github.com/
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[previous-lesson]: ../3-agent-modes/
[next-lesson]: ../5-agent-skills/
