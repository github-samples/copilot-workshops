---
title: "Ćwiczenie 5 - Korzystanie ze skilli agenta"
authors:
  - geektrainer
  - azkel
lastUpdated: 2026-09-10
---

Tworzenie aplikacji często obejmuje powtarzalne zadania, takie jak generowanie buildów, uruchamianie testów czy tworzenie pull requestów (PR). **Skille agenta (agent skills)** pozwalają przekazać Copilotowi — i innym agentom AI — wskazówki, jak wykonywać te zadania. Skill to folder z instrukcjami, skryptami i zasobami, które agent może wczytać na żądanie. [Agent Skills to otwarty standard][agent-skills-repo] używany przez różne agenty, więc ten sam skill może działać w Copilot Chat w trybie agenta, agentach Copilot w chmurze, Copilot CLI oraz aplikacji GitHub Copilot.

Zobaczmy, jak skill może zapewnić, że pull requesty spełniają wymagania zespołu.

## Scenariusz

Zespół ma zestaw wymagań dla pull requestów:

- jasne komunikaty commitów, z plikami pogrupowanymi logicznie.
- wszystkie testy muszą przejść przed utworzeniem PR.
- każdy PR musi zawierać następujące sekcje:
    - opis, dlaczego wprowadzono zmiany.
    - przegląd zmienionych plików.
    - fragmenty ważnych bloków kodu.
    - szczegóły zmian pogrupowane razem.

Ponieważ zespół używa Copilota do generowania kodu i PR-ów, chce mieć pewność, że narzędzia AI przestrzegają tych wymagań.

Podczas tego ćwiczenia:

- przejrzysz istniejący skill do tworzenia pull requestów.
- nauczysz się, jak skille są wykorzystywane przez agenta AI.
- utworzysz PR zgodny z wytycznymi za pomocą skillu.

## Tworzenie skilli agenta

Skille znajdują się w folderze `.github/skills` projektu albo globalnie w `~/.copilot/skills`. Każdy skill to folder zawierający plik `SKILL.md` z nagłówkiem YAML (pola `name` i `description`), a następnie instrukcje w markdown:

```yaml
---
name: make-contribution
description: All changes to code must follow the guidance documented in the repository. Before any issue is filed, branch is made, commits generated, or pull request (or PR) created, a search must be done to ensure the right steps are followed. Whenever asked to create an issue, commit messages, to push code, or create a PR, use this skill so everything is done correctly.
---
```

Skille mogą też zawierać podfoldery ze skryptami, zasobami i materiałami referencyjnymi. Pełna struktura jest opisana w [specyfikacji agent skills][agent-skills-spec].

> [!TIP]
> Skille są wczytywane dynamicznie. Agent decyduje, który skill ma zastosowanie, na podstawie pola `description` — jasny, związany ze scenariuszem opis to różnica między skillem, który zostanie użyty, a takim, który zostanie zignorowany.

## Wykonywanie skilli

Skille są wczytywane dynamicznie, gdy agent uzna, że są potrzebne. Decyzja, których skilli użyć, wynika z opisu w pliku `SKILL.md`. Dlatego ważne są jasne opisy definiujące przypadek użycia, który ma zostać zastosowany.

## Przegląd skillu PR

Ponieważ Tailspin Toys ma zestaw wymagań dotyczących tworzenia PR-ów, utworzyli skill, który pomaga narzędziom AI generować PR-y zgodne z tymi wytycznymi. Przejrzyjmy skill, aby zrozumieć, co zrobi.

1. Otwórz `.github/skills/make-contribution/SKILL.md`.
2. Zwróć uwagę na nazwę i opis. Zauważ, jak opis podkreśla scenariusz użycia — zawsze gdy prosisz o utworzenie pull requestu lub commitowanie kodu.
3. Przeczytaj skill. Zwróć uwagę na reguły dotyczące tworzenia gałęzi, generowania commitów oraz zawartości pull requestu.

## Użycie skillu

Jak wspomniano wcześniej, skille są automatycznie wywoływane przez Copilot CLI. Wystarczy więc poprosić Copilota o utworzenie PR!

1. Wróć do codespace. Jeśli go zamknąłeś, przejdź do repozytorium na GitHub.com, wybierz **Code** > **Codespaces**, a następnie ponownie otwórz istniejący codespace.
2. Wróć do otwartej sesji Copilot CLI. Jeśli terminal jest zamknięty lub wyszedłeś z Copilot CLI, otwórz terminal. Użyj kombinacji <kbd>Ctrl</kbd>+<kbd>\`</kbd>, a następnie uruchom go z katalogu głównego repozytorium poleceniem `copilot --yolo --enable-all-github-mcp-tools`. Zaufaj folderowi projektu, jeśli zostaniesz o to poproszony, potem wywołaj polecenie `/models` i wybierz **Auto**.
3. Poproś Copilota o utworzenie PR, używając poniższego polecenia:

    ```
    Can you please create a pull request for me!
    ```

4. Copilot potwierdzi żądanie. Po chwili zauważysz, że Copilot wskaże, iż korzysta ze skillu **make-contribution**.
5. Następnie Copilot będzie postępował zgodnie z instrukcjami w skillu. Zacznie od uruchomienia testów, potem utworzy gałąź, committy i w końcu PR.
6. Gdy PR zostanie utworzony, wróć do repozytorium i otwórz PR. Zwróć uwagę, że sekcje odpowiadają wytycznym ze skillu i wymaganiom zespołu.
7. Przed przejściem do następnego ćwiczenia zresetuj lokalny obszar roboczy do świeżej gałęzi z `main`, aby praca nad usprawnieniami dostępności pozostała oddzielona od poprzedniego PR dotyczącego filtrowania:

    ```bash
    git checkout main
    git pull
    git checkout -b accessibility-cli
    ```

## Podsumowanie i kolejne kroki

Za pomocą skillu agenta utworzyłeś nowy PR zgodny z udokumentowanymi wymaganiami! Podczas tego ćwiczenia:

- przejrzałeś istniejący skill do tworzenia pull requestów.
- nauczyłeś się, jak skille są wykorzystywane przez agenta AI.
- utworzyłeś PR zgodny z wytycznymi za pomocą skillu.

W następnym kroku poznasz [agentów niestandardowych][next-lesson] — skille są idealne do zadań, ale do bardziej rozbudowanych operacji warto z nich skorzystać!

## Zasoby

- [O Agent Skills][about-agent-skills]
- [Specyfikacja Agent Skills][agent-skills-spec]
- [Repozytorium Agent Skills][agent-skills-repo]
- [Agent Skills w awesome-copilot][awesome-copilot-skills]

[previous-lesson]: ../4-mcp/
[next-lesson]: ../6-custom-agents/
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[awesome-copilot-skills]: https://github.com/github/awesome-copilot/tree/main/skills
[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification
