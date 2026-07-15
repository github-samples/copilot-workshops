# ja-jp

These rules apply to **both roles**: the `translator` agent uses them as generation directives (how to write the Japanese text), and the `evaluator` agent uses them as review criteria (what to check and flag). Wherever a rule says "flag" or "look for", the translator should read it as "produce text that satisfies this".

Translation quality requires both exact meaning and natural Japanese. Verify accuracy, fluency, consistency, and cultural appropriateness rather than preserving English word order.

The four core pillars are:

- **Accuracy:** Preserve every source fact, condition, number, name, and degree of obligation.
- **Fluency:** Use natural Japanese grammar, particles, punctuation, and sentence structure.
- **Terminology & Consistency:** Apply approved Japanese terminology and loanword forms uniformly.
- **Cultural Appropriateness:** Use a register and level of directness suitable for Japanese readers.

## English to Japanese Localization Scenario

English-to-Japanese quality is best evaluated by checking subject omission, topic flow, modifier length, particles, register, and the handling of technical loanwords. Japanese should communicate the same logic without imitating English sentence structure.

### Key Evaluation Pillars for Japanese

- **Register:** Technical documentation uses consistent polite **です・ます調**. Headings and short UI labels may use noun phrases, but body prose must not drift unpredictably into **だ・である調**.
- **Subject Omission:** Omit repeated subjects and reader pronouns when context is clear. Avoid mechanical repetition of **あなた**, **それ**, or **彼ら**.
- **Information Order:** Place context, prerequisites, and conditions before the action or result when natural. Split long English sentences and unwind nested pre-nominal modifiers.
- **Particles and Counters:** Check `は`, `が`, `を`, `に`, `で`, `の`, counters, and classifier choice around code spans and Latin-script terms.
- **Script Choice:** Use kanji, hiragana, katakana, and Latin script according to established Japanese usage and the product glossary. Do not transliterate identifiers or product names.

### Common Translation Mistakes to Flag

- **Literal Pronouns:** Flag unnecessary **あなたの**, **それは**, and gendered pronouns introduced from English.
- **Nominalization and Padding:** Avoid repeated **～することができます**, **～を行います**, and **～となります** when shorter **～できます**, **～します**, or **～です** preserves the meaning.
- **Passive Overuse:** English passive voice often becomes a natural active, intransitive, or subjectless Japanese sentence. Retain passive meaning only when the affected party or responsibility matters.
- **Long Modifiers:** Do not stack clauses before a noun until the referent is difficult to identify. Split or reorder the sentence.
- **Inconsistent Loanwords:** Flag inconsistent spelling or long-vowel treatment for the same term, such as mixing **ユーザー** and **ユーザ** without a glossary reason.

### Practical Evaluation Framework

| Evaluation Metric | What to Look For (English to Japanese Context) |
| :--- | :--- |
| **Accuracy (正確性)** | Are facts, logical relationships, names, numbers, and modality unchanged? |
| **Fluency (流暢さ)** | Can a native reader understand the sentence immediately without reconstructing English syntax? |
| **Style Guide (スタイル)** | Are register, particles, script choice, punctuation, and loanword spelling correct and consistent? |

## Markdown Syntaxes

Keep Markdown delimiters and code spans intact. Japanese particles and punctuation normally belong outside a link or code span unless they are part of the linked phrase.

- Correct: `[**Node.js**](https://nodejs.org/)と npm パッケージをインストールします。`
- Incorrect: `[**Node.js と**](https://nodejs.org/) npm パッケージをインストールします。`

Do not insert spaces merely because Markdown emphasis or a link touches Japanese text. Update same-document anchor links when headings are localized, and preserve external URL targets exactly.

## Localization for Technical Documents for Developers

Japanese developer documentation commonly combines translated concepts, katakana loanwords, acronyms, and unchanged English identifiers. The goal is recognizability and precision, not maximum translation.

### Developer-Specific Evaluation Rules

#### Terminology and Loanwords

- Use established forms such as **文字列**, **配列**, **依存関係**, **インスタンス**, **スレッド**, **リポジトリ**, and **コールバック** when they match the product glossary.
- Keep **API**, **SDK**, protocol names, product names, and identifiers in their established Latin-script form.
- For an unfamiliar critical term, the first occurrence in a file may include the English form in parentheses, for example **依存関係 (dependency)**. Apply this only when it improves lookup or disambiguation.
- Keep variables, functions, APIs, CLI commands (`npm install`), file names, and code exactly as written. Translate human-language code comments and explanatory strings only when they are not programmatically significant.

#### Tone and Instructions

- Use concise **です・ます調**. Render instructions as polite guidance, commonly **～します** or **～してください**, and keep the selected pattern coherent.
- Avoid blunt imperatives such as **～しろ** and excessive honorific or humble language. Technical documentation should be polite, not ceremonial.
- Preserve distinctions among mandatory (**～する必要があります**), recommended (**～することをお勧めします**), and optional (**～できます**) behavior.

#### Syntactic Readability for Code Logic

- Prefer condition-first logic: **キーがない場合、エラーが発生します。**
- Isolate variables grammatically: **ここで、`userId` はユーザー ID を表します。** Do not alter the variable to make it fit Japanese morphology.
- Use Japanese punctuation in prose (`。`, `、`, `「」`) while preserving punctuation that is part of code, commands, paths, or exact UI strings.

### Quick Quality Checklist for Developer Docs

| What to Flag (Bad) | What to Approve (Good) | Why it Matters |
| :--- | :--- | :--- |
| Repeating **あなたは** in every instruction | Omitting the understood subject | Produces natural Japanese documentation. |
| **インストールすることができます** | **インストールできます** | Removes unnecessary nominalization. |
| Translating `getUserById` | Keeping `getUserById` unchanged | Preserves the identifier. |
| Mixing **サーバー** and **サーバ** | One glossary-approved form | Keeps loanword spelling consistent. |

## Evaluator Scoring Rubric

This is the **definitive pass/fail gate** for the `evaluator` role:

- **Tier A — Hard-fail criteria** must score 5.
- **Tier B — Graded criteria** use a 1–5 scale and pass only at 4 or 5.

A document **PASSES only when every applicable Tier A criterion scores 5 and every applicable Tier B criterion scores 4 or 5.** Otherwise return it with source/target snippets and the failed criterion. Escalate to a human when the same subjective criterion still fails after **3 iterations**.

Tier B scale:

- **5 — Excellent:** Fully meets the criterion.
- **4 — Good (pass):** At most 1–2 trivial, non-blocking nits per ~1,000 words.
- **3 — Borderline (fail):** Several noticeable issues or one issue that changes how a sentence reads.
- **2 — Poor (fail):** Frequent or significant violations.
- **1 — Unacceptable (fail):** The criterion is largely unmet.

### Determining Content Type

- **Technical documentation** targets developers/operators or contains code, commands, or API identifiers. Criteria 7–8 apply.
- **Non-technical content** includes UI, marketing, narrative, and conversational copy without code. Criteria 7–8 do not apply, and Criterion 4 uses its audience-appropriate register.

Criterion 2 and Criterion 7 still apply to occasional code or links in otherwise non-technical content.

### Tier A — Hard-Fail Criteria (Must Score 5)

| # | Criterion | Passes (5) when… | Fails (<5) when… |
| :-- | :--- | :--- | :--- |
| 1 | **Accuracy (正確性)** | Meaning, facts, numbers, names, conditions, and modality exactly match the source. | Any mistranslation, omission, addition, negation flip, altered name/number, or changed requirement level occurs. |
| 2 | **Markdown & Structural Integrity** | Frontmatter keys, Markdown, tables, URLs, and heading order are preserved; localized anchors and asset paths resolve. | Any broken link/path, translated frontmatter key, stale English anchor, or corrupted Markdown/table occurs. |

### Tier B — Graded Criteria (Must Score at Least 4)

| # | Criterion | Scores 5 when… | Pass floor — Score 4 | Fail ceiling — Score 3 | Scores 1 when… |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 3 | **Fluency (流暢さ)** | Particles, information order, punctuation, script choice, and sentence length are natural; no translationese or padding. | At most 2 minor slips that do not impede reading. | One sentence requires rereading, or 3+ language errors occur. | English-shaped or ungrammatical Japanese is pervasive. |
| 4 | **Register & Tone** | Body prose consistently uses audience-appropriate **です・ます調**; headings and labels follow coherent conventions. | One isolated ending slip without a perceived register shift. | Two or more style shifts, blunt imperatives, or unsuitable honorific language. | Register is mixed or inappropriate throughout. |
| 5 | **Terminology & Consistency** | Japanese equivalents, katakana forms, acronyms, and first-mention English references follow the glossary consistently. | One minor recognizable inconsistency. | Two or more inconsistent forms or one misleading term. | Terminology and script forms are unreliable throughout. |
| 6 | **Cultural & Linguistic Naturalness** | Subjects are omitted naturally; directness, passives, and modifier length suit Japanese documentation. | One or two harmless stylistic nits. | Several literal pronouns, padded constructions, or overlong modifiers occur. | Literal English discourse patterns dominate. |
| 7 | **Code & Command Integrity** *(technical only — Tier A severity: any violation caps this at ≤2)* | Identifiers, APIs, commands, paths, and file names are unchanged; only human-language comments are translated. | — (no trivial tolerance) | A single code element or command is altered. | Code and commands are repeatedly translated or corrupted. |
| 8 | **Developer Terminology Convention** *(technical only)* | Terms match Japanese developer usage and the product glossary without forced translation. | One borderline but recognizable choice. | A nonstandard translation or transliteration would confuse a developer. | Technical concepts are consistently unnatural or unrecognizable. |

> Criterion 7 has Tier A severity in practice: any altered command or identifier fails the document.

**Overall result:** PASS only if Criteria 1–2 equal 5 and every applicable Criterion 3–8 is at least 4, with no Criterion 7 violation. Otherwise FAIL and iterate, up to the 3-iteration escalation cap. Record a defect under its most specific criterion only.