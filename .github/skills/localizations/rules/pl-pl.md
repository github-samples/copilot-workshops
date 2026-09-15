# pl-pl

These rules apply to **both roles**: the `translator` agent uses them as generation directives (how to write the Polish text), and the `evaluator` agent uses them as review criteria (what to check and flag). Wherever a rule says "flag" or "look for", the translator should read it as "produce text that satisfies this".

In general, producing and evaluating translation quality requires both accuracy of meaning and natural flow. Verify that the text passes core tests for accuracy, fluency, consistency, and cultural appropriateness.

The four core pillars are:

- **Accuracy:** Preserve the source meaning exactly, without additions, distortions, or omissions.
- **Fluency:** Follow Polish grammar, spelling, punctuation, and idiom so the text reads as native Polish.
- **Terminology & Consistency:** Use specialized terms, names, and recurring phrases uniformly.
- **Cultural Appropriateness:** Adapt idioms, examples, register, and vocabulary for Polish-speaking developers.

## English to Polish Localization Scenario

English-to-Polish translation quality is best evaluated by checking case inflection, grammatical agreement, idiomatic sentence structure, consistent treatment of the reader, and established developer terminology. Avoid English calques and overly literal word-for-word renderings.

### Key Evaluation Pillars for Polish

- **Regional Standard:** Use standard Polish (`pl-PL`) as used in technical documentation in Poland. Prefer natural forms such as **plik**, **repozytorium**, **kliknij**, **zaloguj się**, and **poczta e-mail** / **e-mail**, according to context.
- **Reader Address and Register:** For technical documentation, use a professional, direct style with consistent second-person singular (**ty** / imperative forms such as **Uruchom**, **Otwórz**, **Wybierz**). Do not alternate between formal **Pan/Pani** and informal **ty** within a document. Past-tense and adjectival forms addressing the learner use the conventional masculine singular of Polish technical docs (**zainstalowałeś**, **użyłeś**, **Powinieneś**). Do not switch to plural-*państwo* / *oni* forms or doubled feminine/masculine pairs unless the English source explicitly requires inclusive double forms.
- **Grammatical Agreement:** Verify case, gender, number, and adjective agreement, especially around untranslated product names and code terms. Inflect surrounding Polish words correctly even when the product name stays in English.
- **Natural Syntax:** Restructure dense English noun stacks. Polish often needs prepositions, genitive constructions, or subordinate clauses rather than long sequences of nominal modifiers.
- **Punctuation:** Follow Polish punctuation rules. Prefer Polish quotation marks („ ”) in running prose when natural; do not invent capitalization after a colon unless the following text independently requires it.

### Common Translation Mistakes to Flag

- **English Calques:** Flag literal renderings such as *uruchomić aplikację* used where **uruchom** / **wykonaj** is clearer, or *kliknąć na* when **kliknij** is enough. Prefer natural Polish verbs for UI and terminal actions.
- **False Friends:** Check terms such as *aktualnie*, *ewentualnie*, *kontrolować*, and *aplikacja*. Depending on context, use **obecnie**, **ewentualnie/w razie potrzeby**, **sprawdzać/sterować**, and **aplikacja/program** carefully.
- **Case Errors:** English has no case system; Polish does. Flag wrong genitive/accusative/locative around nouns modified by untranslated English product names.
- **Possessive Overuse:** English repeats "your" and "its" more often than Polish. Omit possessives when the referent is clear, but preserve ownership where it affects meaning.
- **Inconsistent Imperatives:** Flag mixing **zrób** / **proszę zrobić** / **należy zrobić** without a clear pattern. Prefer direct imperatives for step-by-step instructions.

### Practical Evaluation Framework

| Evaluation Metric | What to Look For (English to Polish Context) |
| :--- | :--- |
| **Accuracy (dokładność)** | Are every fact, condition, number, name, and logical relationship preserved? |
| **Fluency (płynność)** | Would a Polish reader understand each sentence immediately without detecting English syntax? |
| **Style Guide (styl)** | Are case, agreement, punctuation, capitalization, and register correct? |

## Markdown Syntaxes

Keep Markdown delimiters attached to the text they format, while placing Polish punctuation outside or inside the formatted span according to what is semantically emphasized. Do not allow translated punctuation or articles to enter URLs, code spans, or link targets.

- Correct: `Zapoznaj się z [**dokumentacją Node.js**](https://nodejs.org/).`
- Incorrect: `Zapoznaj się z **[dokumentacją Node.js](https://nodejs.org/).**` when the final period is not part of the link text.

When a translated heading changes its generated slug, update every same-document link to the localized anchor. Preserve external URLs exactly.

## Localization for Technical Documents for Developers

Polish developer documentation should be precise and concise. Translate established concepts when the Polish term is conventional, but retain product names, API names, identifiers, commands, and widely recognized technology terms when translating them would reduce clarity.

### Workshop Structure Conventions

Mirror the English harness structure, but keep these Polish naming patterns established in `docs/pl-pl/`:

- **Harness product names**
  - GitHub Copilot app → **Aplikacja GitHub Copilot** (short forms: **aplikacja Copilot**, **aplikacja** when unambiguous)
  - GitHub Copilot CLI → keep **GitHub Copilot CLI** / **Copilot CLI**
  - Copilot Cloud Agent → **Agent chmurowy Copilot** on the locale landing; in lesson/exercise prose prefer **agent w chmurze** / **agent Copilot w chmurze** / **agenci w chmurze** (English *cloud agent* is acceptable in mixed product lists such as “Copilot Chat, Copilot CLI i Copilot cloud agent”)
  - VS Code harness remains **VS Code** / **Visual Studio Code** and **GitHub Codespaces**
  - **Agent Merge** stays English; agree Polish pronouns/adjectives as masculine (**który**, **go**, **sam**, **on**)
- **Lesson vs exercise labels** (do not mix within a harness)
  - `docs/pl-pl/app/**` → **Lekcja** / **Lekcje**; titles like `Lekcja N - …` (ASCII hyphen)
  - `docs/pl-pl/cli/**` → **Ćwiczenie** / **Ćwiczenia**; titles like `Ćwiczenie N - …` (ASCII hyphen) or `Ćwiczenie 0: …` when the English source uses a colon
  - Locale landing (`docs/pl-pl/README.md`) may say **ćwiczenia** generically when referring to all harnesses together; keep **Lekcja** / **Ćwiczenie** inside each harness
- **Landing slugs:** `docs/pl-pl/README.md` → `slug: pl-pl`; harness landings → `slug: pl-pl/app`, `slug: pl-pl/cli`, etc.
- Common section titles to reuse: **Scenariusz**, **Wymagania wstępne**, **Rozpocznij**, **Podsumowanie i kolejne kroki**, **Zasoby**, **Dobre praktyki**.

### Developer-Specific Evaluation Rules

#### Terminology and English Terms

- Use established equivalents such as **łańcuch** / **string** (when discussing the data type conceptually, prefer the form common in Polish developer docs), **tablica**, **zależność**, **wątek**, **instancja**, and **repozytorium**. Do not vary synonyms casually within one file.
- Keep recognized forms such as **API**, **SDK**, **framework**, **runtime**, product names, and protocol names when that is the normal developer usage.
- Preferred recurring workshop terms (follow the forms already used in `docs/pl-pl/`):

  | English | Polish workshop form | Notes |
  | :--- | :--- | :--- |
  | harness | **środowisko** | Workshop sense: VS Code / CLI / App / Cloud. Never leave **harness** in learner-facing prose. |
  | infrastructure (scaffolding around the tool) | **infrastruktura** | Review/best-practices sense: instructions, skills, agents that shape output quality. Do **not** use **środowisko** here — that word is reserved for harness. |
  | pull request | **pull request** / **PR** | Keep English; avoid **żądanie ściągnięcia**. Inflect surrounding Polish (*pull requesta*, *pull requestami*). |
  | issue | **zgłoszenie** | Optional `(issues)` on first mention when clarifying GitHub Issues; keep UI labels like **When an issue is created** in English. |
  | branch | **gałąź** / **gałęzie** | Prefer over English *branch* / *branchami* in prose. |
  | commit | **commit** | Prefer **commit** for Git objects; Polish verb forms as needed (*commitować* only if natural). |
  | merge (verb/noun) | **scal** / **scalanie** | Keep product name **Agent Merge** unchanged; masculine agreement in Polish. |
  | helper (code unit) | **helper** | Keep English when naming a helper module/function (*fundament helpera*, *publishers helper*). Optional paraphrase **funkcja wspomagająca** only when not naming a specific helper. |
  | custom instructions | **instrukcje niestandardowe** | Instruction files → **pliki instrukcji**; headings like **Pliki instrukcji**. |
  | custom agent | **agent niestandardowy** / **agenci niestandardowi** | Agree number/gender with surrounding Polish. |
  | agent skill(s) | **skill** / **skille** / **skilli** / **skillu** | Keep English root; apply Polish inflection. Prefer **skille agenta**; first mention may use **Skille agenta (agent skills)**. Titles: **Korzystanie ze skilli agenta**. Do not use **umiejętność** for the product feature. |
  | slash command(s) | **polecenie slash** / **polecenia slash** | Keep **slash**; do not invent **polecenia ukośnikowe**. Prefer **polecenie** over **komenda** in prose. |
  | MCP server | **serwer MCP** | Keep **MCP** and product server names (**Playwright MCP**, **GitHub MCP Server**). |
  | canvas / canvases | **kanwa** / **kanwy** | |
  | session | **sesja** / **sesja agenta** | |
  | session mode | **tryb sesji** | Mode names **Plan**, **Interactive**, **Autopilot** stay English (UI). |
  | plan mode | **tryb planowania** | |
  | workspace | **obszar roboczy** | Prefer over English *workspace* in prose. |
  | quick chat(s) | **szybki czat** / **szybkie czaty** | Sidebar/UI label **Quick chats** may stay English when mirroring the product surface. |
  | codespace | **codespace** | Keep English lowercase in prose (*w codespace*); UI chrome **Codespaces** stays as in the product. |
  | worktree | **worktree** / **git worktree** | Keep English. |
  | diff | **diff** | Keep English in UI/review contexts (*widok diff*, *Przejrzyj diff*). |
  | prompt | **prompt** | Keep English for the Copilot input; instructional prose around it is Polish. |
  | automation(s) | **automatyzacja** / **automatyzacje** | UI labels like **Automations**, **New automation** stay English. |
  | code review | **przegląd kodu** / **przegląd** | Prefer over **przeglądanie kodu**. |

- For critical or unfamiliar jargon, the first occurrence in a file may include the English source term in parentheses when it improves lookup, for example, **Skille agenta (agent skills)** or **środowisko uruchomieniowe (runtime)**. Apply this selectively.
- Keep variables, function names, APIs, CLI commands (`npm install`), file names, and code exactly as in the source. Translate only human-language comments and explanatory prose inside code blocks.
- **Learner prompts in fenced blocks** that the user is instructed to paste into Copilot must stay in **English** so the agent receives the intended prompt. Translate surrounding instructional prose only.
- **UI chrome strings** that must match the product UI may stay in English when they mirror the English product surface. Examples from the workshop: `Use this template`, `Create a new repository`, `Home screen`, `Sessions`, `My work`, `New session`, `Toggle review panel`, `Create PR`, `Ready to merge`, `Merge pull request`, `Sign in with your browser`, `MCP servers`, `Add server`, `Popular MCP servers`, `Automations`, `Plan`, `Interactive`, `Autopilot`, `Yes, proceed`, `Quick chats`.

#### Tone and Instructions

- Use concise professional prose. Prefer direct instructions such as **Uruchom poniższe polecenie**.
- Address the learner with consistent second-person singular (**ty**) and masculine past-tense / modal forms common in Polish technical docs (**zainstalowałeś**, **użyłeś**, **przejrzałeś**, **Powinieneś**). Plural-*oni* / *państwo* address and feminine/masculine doublets are out of scope for this workshop unless the English source explicitly requires them.
- Prefer **polecenie** (or **zapytanie** when asking for an example/output) over **monit** for what the learner sends to Copilot (`Użyj poniższego polecenia`, `Wyślij poniższe polecenie`). English *prompt* may remain in UI sense as **pole monitu** / **interfejs** when naming the input box; do not force **monit** for instructional steps.
- Keyboard: **Wciśnij** for single keys (`Enter`); **Użyj kombinacji** for chords (`Ctrl`+`C`).
- Browser auth flows: **postępuj zgodnie z instrukcjami** (not *monitami*).
- Prefer future tense when narrating what Copilot will do next (**zabierze się za**, **zbada**, **stworzy**).
- Prefer **na podstawie zgłoszenia** when starting a session from an issue.
- Prefer instructional **Zwróć uwagę** / **Przejrzyj** / **Upewnij się** over bare **Zauważ** / **Potwierdź** where the learner must verify something.
- Avoid unnecessary courtesy formulas and repeated reader pronouns. Do not pad instructions with **proszę**.
- Preserve distinctions among requirements (**musi** / **wymagane**), recommendations (**zalecane** / **powinien**), and possibilities (**może**). Never weaken or strengthen normative language.

#### Syntactic Readability for Code Logic

- Put prerequisites and conditions before outcomes when that improves comprehension: **Jeśli brakuje klucza, wystąpi błąd.**
- Treat variables as grammatical units without changing them: **Tutaj `userId` identyfikuje użytkownika.**
- Avoid ambiguous pronouns after sentences containing several possible antecedents; repeat the precise noun where needed.
- Inflect Polish around untranslated English nouns correctly (*pull requesta*, *serwera MCP*, *skillu*, *sesji agenta*).

### Quick Quality Checklist for Developer Docs

| What to Flag (Bad) | What to Approve (Good) | Why it Matters |
| :--- | :--- | :--- |
| **"odpal `npm install`"** | **"uruchom `npm install`"** | Keeps a professional register while preserving the command. |
| **"biblioteka ładuje swoje zależności"** when ownership is unclear | **"biblioteka ładuje zależności"** | Avoids an ambiguous possessive. |
| Switching between **ty** and **Pan/Pani** | One consistent treatment | Keeps the documentation voice stable. |
| Translating `StringBuilder` | Keeping `StringBuilder` unchanged | Preserves the identifier exactly. |
| Translating a learner prompt the user must paste | Leaving the fenced prompt in English | Ensures Copilot receives the intended English prompt. |
| **"harness"** / **"żądanie ściągnięcia"** / **"umiejętność"** for agent skills | **"środowisko"** / **"pull request"** / **"skill"/"skille agenta"** | Matches workshop glossary and product language. |
| Mixing **Lekcja** and **Ćwiczenie** in one harness | **Lekcja** in app, **Ćwiczenie** in CLI | Preserves the established per-harness naming. |
| **"GitHub Copilot app"** left untranslated in prose | **"Aplikacja GitHub Copilot"** | Matches the localized product name used on landings and lessons. |
| Leaving UI labels like **Ready to merge** translated | Keeping product UI chrome in English | Learner can match on-screen controls. |
| **"Agent Merge, które/ono"** | **"Agent Merge, który/on"** | Product name takes masculine agreement in Polish. |
| **"środowisko"** for instructions/skills scaffolding | **"infrastruktura"** | Keeps **środowisko** = harness only. |
| Title **"… umiejętności agenta"** for agent skills | **"… skilli agenta"** | Product feature stays **skill**, not **umiejętność**. |

## Evaluator Scoring Rubric

This is the **definitive pass/fail gate** for the `evaluator` role. Criteria are split into two tiers:

- **Tier A — Hard-fail criteria:** any material defect makes the document unusable, so these **must score 5 to pass**.
- **Tier B — Graded criteria:** scored on the 1–5 scale below; these **pass at 4 or 5**.

A document **PASSES only when every applicable Tier A criterion scores 5 and every applicable Tier B criterion scores 4 or 5.** Otherwise it FAILS and is returned to the translator with specific notes that cite the offending source/target snippets and criterion. If the same subjective criterion still fails after **3 iterations**, escalate to a human.

Tier B scale:

- **5 — Excellent:** Fully meets the criterion; no issues.
- **4 — Good (pass):** At most 1–2 trivial, non-blocking nits per ~1,000 words.
- **3 — Borderline (fail):** Several noticeable issues, or any issue that changes how a sentence reads.
- **2 — Poor (fail):** Frequent or significant violations.
- **1 — Unacceptable (fail):** The criterion is largely unmet.

### Determining Content Type

- **Technical documentation** is content for developers/operators or any document containing code, commands, or API identifiers. Criteria 7–8 apply.
- **Non-technical content** is UI, marketing, narrative, or conversational copy without code. Criteria 7–8 do not apply, and Criterion 4 uses the audience-appropriate register.

If otherwise non-technical content contains occasional code or links, Criterion 2 and Criterion 7 still apply to those spans.

### Tier A — Hard-Fail Criteria (Must Score 5)

| # | Criterion | Passes (5) when… | Fails (<5) when… |
| :-- | :--- | :--- | :--- |
| 1 | **Accuracy (dokładność)** | Meaning matches the source exactly; all facts, numbers, names, conditions, and modality are preserved. | Any mistranslation, negation flip, fabricated/dropped fact, altered number/name, or changed requirement level occurs. |
| 2 | **Markdown & Structural Integrity** | Frontmatter keys, Markdown, tables, external URLs, and heading order are preserved; localized anchors resolve; image paths point to real assets. | Any link or asset path is broken, a frontmatter key is translated, an English anchor remains after its heading changes, or Markdown/table structure is corrupted. |

### Tier B — Graded Criteria (Must Score at Least 4)

| # | Criterion | Scores 5 when… | Pass floor — Score 4 | Fail ceiling — Score 3 | Scores 1 when… |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 3 | **Fluency (płynność)** | Reads as native `pl-PL`; grammar, case, agreement, syntax, and punctuation are correct; no calques. | At most 2 minor slips that do not impede reading. | Any awkward calque requiring rereading, or 3+ language errors. | English-shaped or ungrammatical prose is pervasive. |
| 4 | **Register & Reader Address** | Professional register and **ty**/imperative treatment fit the audience and remain uniform. | One isolated treatment slip that does not shift the perceived voice. | Two or more treatment shifts, or an audience-inappropriate tone. | Register and reader address are inconsistent throughout. |
| 5 | **Terminology & Consistency** | Terms follow `pl-PL` conventions and the workshop glossary above (including harness names and Lekcja/Ćwiczenie); each concept is rendered consistently. | One minor inconsistency remains understandable. | Two or more inconsistent renderings, a false friend, or one misleading term. | Terminology is unreliable throughout. |
| 6 | **Regional & Linguistic Naturalness** | Idioms, possessives, and vocabulary are natural for Polish without unnecessary source-language interference. | One or two harmless stylistic nits. | Several calques, ambiguous possessives, or unnatural phrasing. | The text consistently sounds translated. |
| 7 | **Code & Command Integrity** *(technical only — Tier A severity: any violation caps this at ≤2)* | Variables, identifiers, APIs, file names, and commands are unchanged; learner prompts stay English; only human-language comments are translated. | — (no trivial tolerance) | A single identifier, file name, command, or learner prompt is altered. | Code and commands are repeatedly translated or corrupted. |
| 8 | **Developer Terminology Convention** *(technical only)* | Established Polish and retained English terms match actual developer usage; over-translation is avoided. | One borderline but recognizable choice. | A forced translation or nonstandard term would confuse a developer. | Technical concepts are consistently rendered unnaturally. |

> Criterion 7 has Tier A severity in practice: any altered command, identifier, or learner prompt fails the document.

**Overall result:** PASS only if Criteria 1–2 equal 5 and every applicable Criterion 3–8 is at least 4, with no Criterion 7 violation. Otherwise FAIL and iterate, up to the 3-iteration escalation cap. Score each defect under the most specific criterion and do not double-penalize it.
