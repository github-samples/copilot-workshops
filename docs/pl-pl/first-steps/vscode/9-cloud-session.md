---
title: "Lekcja 9 - Przekaż kolejny pomysł do sesji w chmurze"
description: "Przełącz środowisko Copilot Chat z Local na Cloud i deleguj samodzielną funkcję, która wróci jako pull request."
authors:
  - jamesmontemagno
  - azkel
lastUpdated: 2026-09-28
---

Przeszedłeś całą pętlę lokalnie, więc wiesz już, jak wygląda dobry wynik. To właściwy moment, by coś mogło działać bez Ciebie. Copilot Chat może przełączyć środowisko, na którym działa, z Twojej maszyny na GitHub.

W tej lekcji:

- przełączysz środowisko Copilot Chat z **Local** na **Cloud**.
- delegujesz samodzielną funkcję z jasnymi kryteriami akceptacji.
- przejrzysz powstały pull request.

## Deleguj do chmury

![Ilustracja Copilot Chat w VS Code z otwartym selektorem Harness. Pod Copilot wybrane jest Cloud zamiast Local, a na liście są też inne środowiska, takie jak Claude i Codex. Powyżej widać żądanie dodania trzech nowych motywów kolorystycznych z komunikatem Working in the cloud oraz linkiem do śledzenia sesji na GitHub.](../../../_images/first-steps-vscode-cloud-harness.svg)

Selektor **Harness** wymienia Copilota działającego w trybie **Local** lub **Cloud**, obok innych środowisk. Przełącz na **Cloud**, a kolejne żądanie uruchomi się na GitHub zamiast na Twojej maszynie.

1. W Copilot Chat otwórz selektor **Harness** i przełącz Copilota z **Local** na **Cloud**.
2. Rozpocznij nową sesję i zleć samodzielną funkcję z jasnymi kryteriami akceptacji:

   ```plaintext
   Add a theme picker to the space quiz with three named themes: Deep Space, Launch Pad, and Lunar. Persist the choice in localStorage, keep everything in the single index.html with no dependencies, keep contrast accessible in every theme, and open a pull request when the tests pass.
   ```

3. Zamknij laptopa. Praca trwa na GitHub i wraca jako pull request.
4. Przejrzyj ten pull request równie dokładnie jak ten, który napisałeś sam.

> [!TIP]
> **Deleguj to, co potrafisz opisać**
>
> Sesje w chmurze nagradzają precyzyjny brief. Jeśli nie potrafisz napisać kryteriów akceptacji, zadanie nie jest jeszcze gotowe do opuszczenia Twojej maszyny.

## Podsumowanie i kolejne kroki

Delegowałeś funkcję do sesji w chmurze i przejrzałeś wynik. Przejdź do [Lekcji 10: Podsumowanie i kolejne kroki][next-lesson].

[next-lesson]: ../10-review/
