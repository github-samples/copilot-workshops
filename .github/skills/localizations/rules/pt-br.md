# pt-br

These rules apply to **both roles**: the `translator` agent uses them as generation directives (how to write Brazilian Portuguese), and the `evaluator` agent uses them as review criteria (what to check and flag). Wherever a rule says "flag" or "look for", the translator should read it as "produce text that satisfies this".

Translation quality requires exact meaning and natural Brazilian Portuguese. Verify accuracy, fluency, consistency, and cultural appropriateness rather than preserving English syntax.

The four core pillars are:

- **Accuracy:** Preserve the source meaning exactly, with no additions, distortions, or omissions.
- **Fluency:** Follow Brazilian Portuguese grammar, spelling, punctuation, and idiom.
- **Terminology & Consistency:** Apply specialized terms, names, and recurring phrases uniformly.
- **Cultural Appropriateness:** Use register, idioms, examples, and regional vocabulary suitable for Brazil.

## English to Brazilian Portuguese Localization Scenario

English-to-Portuguese quality is best evaluated by checking agreement, pronoun placement, prepositions, article use, natural clause order, and Brazilian terminology. Avoid English calques and accidental European Portuguese forms.

### Key Evaluation Pillars for Brazilian Portuguese

- **Regional Standard:** Use post-1990 orthography and established `pt-BR` vocabulary. Prefer **arquivo**, **tela**, **usuário**, **senha**, **fazer login/entrar**, and **salvar** where appropriate to the product glossary.
- **Reader Address:** Technical documentation normally uses a professional, direct voice with **você** understood or explicit. Keep treatment consistent; do not mix **você**, **tu**, **o senhor/a senhora**, and impersonal forms unintentionally.
- **Agreement and Government:** Verify gender/number agreement, contractions, verb and noun government, and prepositions, especially around untranslated product names.
- **Natural Syntax:** Break up English noun stacks, reduce repeated possessives, and place clitic pronouns according to natural contemporary Brazilian usage.
- **Orthography and Punctuation:** Check accents, hyphenation, capitalization, and punctuation. Preserve locale-neutral numbers when they are factual source values; localize display formats only when the content explicitly permits it.

### Common Translation Mistakes to Flag

- **False Cognates and Calques:** Flag misleading forms such as **aplicar para** (when **candidatar-se/solicitar** is meant), **eventualmente** for "eventually", and **biblioteca** versus **livraria** in software contexts.
- **Gerundism:** Avoid bureaucratic strings such as **vai estar executando** when **executará** or **vai executar** is clearer. A normal progressive gerund is acceptable when the action is genuinely ongoing.
- **Possessive and Pronoun Overuse:** Omit repeated **seu/sua** and **você** when context is clear, but rewrite ambiguous possessives instead of guessing their referent.
- **European Portuguese Leakage:** Flag forms such as **ficheiro**, **ecrã**, **palavra-passe**, **utilizador**, or **guardar** when the intended `pt-BR` term differs.
- **Unnatural Passive Voice:** Prefer active or reflexive constructions when they are clearer, without changing responsibility or emphasis.

### Practical Evaluation Framework

| Evaluation Metric | What to Look For (English to Brazilian Portuguese Context) |
| :--- | :--- |
| **Accuracy (precisão)** | Are facts, logical relationships, numbers, names, and modality preserved exactly? |
| **Fluency (fluência)** | Would a Brazilian reader understand each sentence immediately without detecting English syntax? |
| **Style Guide (estilo)** | Are spelling, accents, agreement, punctuation, pronouns, and regional conventions correct? |

## Markdown Syntaxes

Keep Markdown delimiters attached to the intended text. Articles, prepositions, and punctuation must not enter URLs or code spans accidentally.

- Correct: `Instale o [**Node.js**](https://nodejs.org/) e o pacote npm.`
- Incorrect: `Instale **[o Node.js e](https://nodejs.org/)** o pacote npm.`

When a translated heading changes its generated slug, update same-document links to the localized anchor. Preserve external URLs exactly.

## Localization for Technical Documents for Developers

Brazilian developer documentation combines translated concepts with English loanwords and unchanged identifiers. Prefer the terminology Brazilian developers actually use and follow the product glossary over dictionary literalism.

### Developer-Specific Evaluation Rules

#### Terminology and English Terms

- Use established terms such as **cadeia de caracteres/string** according to the product glossary, **matriz/array**, **dependência**, **instância**, **thread**, **repositório**, **retorno de chamada/callback**, and **tempo de execução/runtime**. Select one approved form per concept and use it consistently.
- Keep **API**, **SDK**, protocol names, product names, and identifiers in their established form.
- For an unfamiliar critical term, the first occurrence in a file may include the English source in parentheses, for example **tempo de execução (runtime)**. Apply this selectively.
- Keep variables, function names, APIs, CLI commands (`npm install`), paths, file names, and code exactly as in the source. Translate explanatory human-language comments when they are not machine-significant.

#### Tone and Instructions

- Use concise professional prose. Direct instructions commonly use the imperative associated with **você**, such as **Execute o comando** and **Selecione a opção**. Keep this style consistent.
- Avoid unnecessary **por favor**, bureaucratic language, and repeated **você deve** when a direct imperative preserves the requirement.
- Preserve requirement levels: **deve/é necessário** for requirements, **recomenda-se** for recommendations, and **pode** for capability or permission.

#### Syntactic Readability for Code Logic

- Prefer condition-first logic: **Se a chave estiver ausente, ocorrerá um erro.**
- Isolate variables grammatically: **Aqui, `userId` representa a ID do usuário.** Do not translate or inflect the identifier.
- Rewrite ambiguous **seu/sua** references with the exact noun when more than one antecedent is possible.

### Quick Quality Checklist for Developer Docs

| What to Flag (Bad) | What to Approve (Good) | Why it Matters |
| :--- | :--- | :--- |
| **“vai estar executando `npm install`”** | **“execute `npm install`”** | Avoids gerundism and preserves the command. |
| **“livraria de software”** | **“biblioteca de software”** | Uses the established technical meaning. |
| Mixing **você** and **tu** | One consistent treatment | Keeps the documentation voice stable. |
| Translating `StringBuilder` | Keeping `StringBuilder` unchanged | Preserves the identifier exactly. |

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
| 1 | **Accuracy (precisão)** | Meaning, facts, conditions, names, numbers, and modality exactly match the source. | Any mistranslation, omission, addition, negation flip, altered name/number, or changed requirement level occurs. |
| 2 | **Markdown & Structural Integrity** | Frontmatter keys, Markdown, tables, URLs, heading order, localized anchors, and asset paths are preserved and valid. | Any broken link/path, translated frontmatter key, stale English anchor, or corrupted Markdown/table occurs. |

### Tier B — Graded Criteria (Must Score at Least 4)

| # | Criterion | Scores 5 when… | Pass floor — Score 4 | Fail ceiling — Score 3 | Scores 1 when… |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 3 | **Fluency (fluência)** | Grammar, agreement, prepositions, pronouns, punctuation, and syntax are natural `pt-BR`; no calques or gerundism. | At most 2 minor slips that do not impede reading. | One sentence requires rereading, or 3+ language errors occur. | English-shaped or ungrammatical prose is pervasive. |
| 4 | **Register & Reader Address** | Professional tone and treatment (**você**, impersonal, or another audience-appropriate form) are consistent. | One isolated treatment slip without a perceived voice shift. | Two or more treatment shifts or an unsuitable tone. | Register and reader address are inconsistent throughout. |
| 5 | **Terminology & Consistency** | Terms follow `pt-BR` and product conventions; translated and retained English terms are consistent. | One minor recognizable inconsistency. | Two or more inconsistent forms, a false cognate, or one misleading term. | Terminology is unreliable throughout. |
| 6 | **Regional & Linguistic Naturalness** | Idiom, pronoun placement, possessives, passives, and vocabulary are natural in Brazil. | One or two harmless stylistic nits. | Several calques, ambiguous possessives, or European Portuguese forms occur. | The text consistently sounds translated or targets the wrong locale. |
| 7 | **Code & Command Integrity** *(technical only — Tier A severity: any violation caps this at ≤2)* | Identifiers, APIs, commands, paths, and file names are unchanged; only human-language comments are translated. | — (no trivial tolerance) | A single code element or command is altered. | Code and commands are repeatedly translated or corrupted. |
| 8 | **Developer Terminology Convention** *(technical only)* | Terms match Brazilian developer usage and the product glossary without forced translation. | One borderline but recognizable choice. | A nonstandard translation would confuse a developer. | Technical concepts are consistently unnatural or unrecognizable. |

> Criterion 7 has Tier A severity in practice: any altered command or identifier fails the document.

**Overall result:** PASS only if Criteria 1–2 equal 5 and every applicable Criterion 3–8 is at least 4, with no Criterion 7 violation. Otherwise FAIL and iterate, up to the 3-iteration escalation cap. Record a defect under its most specific criterion only.