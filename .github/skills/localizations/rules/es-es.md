# es-es

These rules apply to **both roles**: the `translator` agent uses them as generation directives (how to write the Spanish text), and the `evaluator` agent uses them as review criteria (what to check and flag). Wherever a rule says "flag" or "look for", the translator should read it as "produce text that satisfies this".

In general, producing and evaluating translation quality requires both accuracy of meaning and natural flow. Verify that the text passes core tests for accuracy, fluency, consistency, and cultural appropriateness.

The four core pillars are:

- **Accuracy:** Preserve the source meaning exactly, without additions, distortions, or omissions.
- **Fluency:** Follow Spanish grammar, spelling, punctuation, and idiom so the text reads as native European Spanish.
- **Terminology & Consistency:** Use specialized terms, names, and recurring phrases uniformly.
- **Cultural Appropriateness:** Adapt idioms, examples, register, and regional vocabulary for readers in Spain.

## English to Spanish (Spain) Localization Scenario

English-to-Spanish translation quality is best evaluated by checking grammatical agreement, idiomatic sentence structure, consistent treatment of the reader, and terminology appropriate to Spain. Avoid both English calques and unintended Latin American or European Portuguese usage.

### Key Evaluation Pillars for Spanish (Spain)

- **Regional Standard:** Use `es-ES` vocabulary and conventions. Prefer forms understood naturally in Spain, such as **archivo**, **ordenador/equipo**, **hacer clic**, **iniciar sesión**, and **correo electrónico**, according to context.
- **Reader Address and Register:** For technical documentation, use a professional, direct style. Prefer impersonal constructions or a consistent second-person singular treatment. Do not alternate between **tú**, **usted**, and plural forms within a document.
- **Grammatical Agreement:** Verify gender, number, articles, contractions (`al`, `del`), clitic pronouns, and adjective agreement, especially around untranslated product names and code terms.
- **Natural Syntax:** Restructure dense English noun stacks and repeated possessives. Spanish generally needs prepositions or subordinate clauses rather than long sequences of nominal modifiers.
- **Punctuation:** Use opening and closing question/exclamation marks (`¿?`, `¡!`) and Spanish punctuation rules. Do not insert English-style capitalization after a colon unless the following text independently requires it.

### Common Translation Mistakes to Flag

- **English Calques:** Flag literal renderings such as *aplicar para* for "apply for", *correr un programa* for "run a program", or unnecessary passive constructions. Prefer **solicitar**, **ejecutar un programa**, and natural active or `se` constructions.
- **False Friends:** Check terms such as *actual*, *eventually*, *library*, and *support*. Depending on context, use **real/actual**, **finalmente**, **biblioteca**, and **compatibilidad/asistencia**, not misleading cognates.
- **Gerund Misuse:** Do not use the gerund to express a later result or as an English-style adjective. Use a finite verb or relative clause.
- **Possessive Overuse:** English repeats "your" and "its" more often than Spanish. Omit possessives when the referent is clear, but preserve ownership where it affects meaning.
- **Regional Mixing:** Flag unexplained switching between Spain-specific and other regional forms, such as **ordenador/computadora** or **vosotros/ustedes**, when it makes the voice inconsistent.

### Practical Evaluation Framework

| Evaluation Metric | What to Look For (English to Spanish Context) |
| :--- | :--- |
| **Accuracy (exactitud)** | Are every fact, condition, number, name, and logical relationship preserved? |
| **Fluency (fluidez)** | Would a reader in Spain understand each sentence immediately without detecting English syntax? |
| **Style Guide (estilo)** | Are agreement, accents, punctuation, capitalization, and regional conventions correct? |

## Markdown Syntaxes

Keep Markdown delimiters attached to the text they format, while placing Spanish punctuation outside or inside the formatted span according to what is semantically emphasized. Do not allow translated punctuation or articles to enter URLs, code spans, or link targets.

- Correct: `Consulta la [**documentación de Node.js**](https://nodejs.org/).`
- Incorrect: `Consulta la **[documentación de Node.js](https://nodejs.org/).**` when the final period is not part of the link text.

When a translated heading changes its generated slug, update every same-document link to the localized anchor. Preserve external URLs exactly.

## Localization for Technical Documents for Developers

Spanish developer documentation should be precise and concise. Translate established concepts when the Spanish term is conventional, but retain product names, API names, identifiers, commands, and widely recognized technology terms when translating them would reduce clarity.

### Developer-Specific Evaluation Rules

#### Terminology and English Terms

- Use established equivalents such as **cadena** (String, when discussing the data type conceptually), **matriz/arreglo** according to the product glossary, **dependencia**, **subproceso/hilo**, **instancia**, and **repositorio**. Do not vary synonyms casually within one file.
- Keep recognized forms such as **API**, **SDK**, **framework**, **runtime**, product names, and protocol names when that is the normal developer usage or the product glossary requires it.
- For critical or unfamiliar jargon, the first occurrence in a file may include the English source term in parentheses when it improves lookup, for example, **entorno de ejecución (runtime)**. Apply this selectively.
- Keep variables, function names, APIs, CLI commands (`npm install`), file names, and code exactly as in the source. Translate only human-language comments and explanatory prose inside code blocks.

#### Tone and Instructions

- Use concise professional prose. Prefer direct instructions such as **Ejecuta el comando siguiente** or an impersonal pattern such as **Ejecute el comando siguiente**, but select one treatment and keep it consistent.
- Avoid unnecessary courtesy formulas and repeated reader pronouns. Do not make instructions less direct by padding them with **por favor**.
- Preserve distinctions among requirements (**debe**), recommendations (**se recomienda/debería**), and possibilities (**puede**). Never weaken or strengthen normative language.

#### Syntactic Readability for Code Logic

- Put prerequisites and conditions before outcomes when that improves comprehension: **Si falta la clave, se produce un error.**
- Treat variables as grammatical units without changing them: **Aquí, `userId` identifica al usuario.**
- Avoid ambiguous pronouns after sentences containing several possible antecedents; repeat the precise noun where needed.

### Quick Quality Checklist for Developer Docs

| What to Flag (Bad) | What to Approve (Good) | Why it Matters |
| :--- | :--- | :--- |
| **"corre `npm install`"** | **"ejecuta `npm install`"** | Avoids an English calque while preserving the command. |
| **"la librería carga sus dependencias"** when ownership is unclear | **"la biblioteca carga las dependencias"** | Uses conventional terminology and avoids an ambiguous possessive. |
| Switching between **tú** and **usted** | One consistent treatment | Keeps the documentation voice stable. |
| Translating `StringBuilder` | Keeping `StringBuilder` unchanged | Preserves the identifier exactly. |

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
| 1 | **Accuracy (exactitud)** | Meaning matches the source exactly; all facts, numbers, names, conditions, and modality are preserved. | Any mistranslation, negation flip, fabricated/dropped fact, altered number/name, or changed requirement level occurs. |
| 2 | **Markdown & Structural Integrity** | Frontmatter keys, Markdown, tables, external URLs, and heading order are preserved; localized anchors resolve; image paths point to real assets. | Any link or asset path is broken, a frontmatter key is translated, an English anchor remains after its heading changes, or Markdown/table structure is corrupted. |

### Tier B — Graded Criteria (Must Score at Least 4)

| # | Criterion | Scores 5 when… | Pass floor — Score 4 | Fail ceiling — Score 3 | Scores 1 when… |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 3 | **Fluency (fluidez)** | Reads as native `es-ES`; grammar, accents, agreement, syntax, and punctuation are correct; no calques or gerund misuse. | At most 2 minor slips that do not impede reading. | Any awkward calque requiring rereading, or 3+ language errors. | English-shaped or ungrammatical prose is pervasive. |
| 4 | **Register & Reader Address** | Professional register and treatment (`tú`, `usted`, or impersonal) fit the audience and remain uniform. | One isolated treatment slip that does not shift the perceived voice. | Two or more treatment shifts, or an audience-inappropriate tone. | Register and reader address are inconsistent throughout. |
| 5 | **Terminology & Consistency** | Terms follow `es-ES` conventions and the product glossary; each concept is rendered consistently. | One minor inconsistency remains understandable. | Two or more inconsistent renderings, a false friend, or one misleading term. | Terminology is unreliable throughout. |
| 6 | **Regional & Linguistic Naturalness** | Idioms, possessives, passives, and regional vocabulary are natural for Spain without unnecessary source-language interference. | One or two harmless regional or stylistic nits. | Several calques, ambiguous possessives, or inconsistent regional forms. | The text consistently sounds translated or targets the wrong locale. |
| 7 | **Code & Command Integrity** *(technical only — Tier A severity: any violation caps this at ≤2)* | Variables, identifiers, APIs, file names, and commands are unchanged; only human-language comments are translated. | — (no trivial tolerance) | A single identifier, file name, or command is altered. | Code and commands are repeatedly translated or corrupted. |
| 8 | **Developer Terminology Convention** *(technical only)* | Established Spanish and retained English terms match actual developer usage; over-translation is avoided. | One borderline but recognizable choice. | A forced translation or nonstandard term would confuse a developer. | Technical concepts are consistently rendered unnaturally. |

> Criterion 7 has Tier A severity in practice: any altered command or identifier fails the document.

**Overall result:** PASS only if Criteria 1–2 equal 5 and every applicable Criterion 3–8 is at least 4, with no Criterion 7 violation. Otherwise FAIL and iterate, up to the 3-iteration escalation cap. Score each defect under the most specific criterion and do not double-penalize it.