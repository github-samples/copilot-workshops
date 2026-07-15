# zh-cn

These rules apply to **both roles**: the `translator` agent uses them as generation directives (how to write Simplified Chinese), and the `evaluator` agent uses them as review criteria (what to check and flag). Wherever a rule says "flag" or "look for", the translator should read it as "produce text that satisfies this".

Translation quality requires exact meaning and natural Mainland Chinese usage. Verify accuracy, fluency, consistency, and cultural appropriateness without preserving English syntax mechanically.

The four core pillars are:

- **Accuracy:** Preserve every source fact, condition, number, name, and degree of obligation.
- **Fluency:** Use concise, grammatical Simplified Chinese with natural information order and punctuation.
- **Terminology & Consistency:** Follow established Mainland Chinese technical terminology and the product glossary.
- **Cultural Appropriateness:** Adapt idiom, tone, examples, and regional language for readers in Mainland China.

## English to Simplified Chinese Localization Scenario

English-to-Chinese quality is best evaluated by checking concise clause structure, omitted pronouns, modifier order, logical connectors, script consistency, and accepted Mainland terminology. Avoid word-for-word translation, unnecessary function words, and a mixture of Simplified and Traditional Chinese.

### Key Evaluation Pillars for Simplified Chinese

- **Script and Region:** Use Simplified Chinese characters and `zh-CN` terminology throughout. Flag Traditional forms or vocabulary associated with another Chinese locale when a Mainland equivalent is expected.
- **Conciseness:** Remove source-language padding and repeated subjects when context is clear, but do not omit conditions or weaken meaning.
- **Information Order:** Put time, scope, prerequisites, and conditions before the main action or result when natural in Chinese.
- **Modifier Clarity:** Break up long English noun stacks and relative clauses. Ensure each modifier clearly attaches to the intended noun.
- **Punctuation:** Use Chinese punctuation in prose (`，。；：“”《》`) and preserve ASCII punctuation inside code, URLs, commands, paths, and exact syntax.

### Common Translation Mistakes to Flag

- **Pronoun Overuse:** Avoid mechanical repetition of **您**, **你**, **它**, and **他们** where Chinese naturally omits the subject.
- **Passive Marker Overuse:** Do not map every English passive to **被**. Use an active, subjectless, or result construction unless the affected party is important.
- **Redundant Phrases:** Flag padding such as **进行配置操作**, **可以能够**, and repeated **的** chains when **配置**, **可以**, or a restructured sentence is clearer.
- **Literal Connectors:** Do not overuse **关于**, **在……方面**, or **当……的时候** as direct English calques when a shorter topic or conditional construction works.
- **Locale Mixing:** Flag Traditional characters and inconsistent pairs such as **文件/檔案**, **软件/軟體**, **登录/登入**, or **默认/預設**.

### Practical Evaluation Framework

| Evaluation Metric | What to Look For (English to Simplified Chinese Context) |
| :--- | :--- |
| **Accuracy (准确性)** | Are facts, conditions, names, numbers, and modality preserved exactly? |
| **Fluency (流畅性)** | Can a Mainland Chinese reader understand each sentence immediately without reconstructing English syntax? |
| **Style Guide (风格)** | Are Simplified characters, punctuation, terminology, and spacing conventions correct and consistent? |

## Markdown Syntaxes

Keep Markdown delimiters, URLs, and code spans intact. Chinese punctuation and grammatical particles must not be absorbed into a link target or code span.

- Correct: `安装 [**Node.js**](https://nodejs.org/) 和 npm 包。`
- Incorrect: `安装 [**Node.js 和**](https://nodejs.org/) npm 包。`

Use one consistent spacing convention around embedded Latin terms according to the product style guide; never insert spaces inside identifiers or commands. Update same-document links to localized heading anchors and preserve external URLs exactly.

## Localization for Technical Documents for Developers

Simplified Chinese developer documentation normally translates established concepts while retaining acronyms, product names, identifiers, and commands. Prefer the form that Mainland developers can recognize quickly.

### Developer-Specific Evaluation Rules

#### Terminology and English Terms

- Use established terms such as **字符串**, **数组**, **依赖项/依赖关系** according to context, **实例**, **线程**, **存储库**, **回调函数**, and **运行时**.
- Keep established forms such as **API**, **SDK**, protocol names, product names, and language keywords in Latin script.
- For a critical unfamiliar term, the first occurrence in a file may include the English term in parentheses, for example **运行时 (runtime)**. Apply this selectively and consistently.
- Keep variables, function names, APIs, CLI commands (`npm install`), paths, file names, and code exactly as in the source. Translate human-language comments when they are explanatory and not machine-significant.

#### Tone and Instructions

- Use a concise, professional, neutral voice. Prefer direct verbs such as **选择**, **运行**, and **输入**. Avoid repeated **请** unless politeness is needed for the context.
- Use **您** only when the product voice requires direct respectful address; otherwise omit the reader pronoun. Never mix **你** and **您** unintentionally.
- Preserve requirement levels: **必须/需要** for requirements, **建议** for recommendations, and **可以** for capability or permission.

#### Syntactic Readability for Code Logic

- Prefer condition-first logic: **如果缺少密钥，则会发生错误。** Omit **则** when the shorter sentence remains clear.
- Isolate variables grammatically: **其中，`userId` 表示用户 ID。** Do not translate or inflect the variable.
- Avoid long **的** chains; split the sentence or move conditions into a preceding clause.

### Quick Quality Checklist for Developer Docs

| What to Flag (Bad) | What to Approve (Good) | Why it Matters |
| :--- | :--- | :--- |
| **“进行包的安装操作”** | **“安装包”** | Removes source-language padding. |
| Repeating **“您需要”** in every step | Using the direct verb | Matches concise technical style. |
| Translating `getUserById` | Keeping `getUserById` unchanged | Preserves the identifier. |
| Mixing **文件** and **檔案** | Consistent **文件** | Keeps the document in `zh-CN`. |

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
| 1 | **Accuracy (准确性)** | Meaning, facts, conditions, names, numbers, and modality exactly match the source. | Any mistranslation, omission, addition, negation flip, altered name/number, or changed requirement level occurs. |
| 2 | **Markdown & Structural Integrity** | Frontmatter keys, Markdown, tables, URLs, heading order, localized anchors, and asset paths are preserved and valid. | Any broken link/path, translated frontmatter key, stale English anchor, or corrupted Markdown/table occurs. |

### Tier B — Graded Criteria (Must Score at Least 4)

| # | Criterion | Scores 5 when… | Pass floor — Score 4 | Fail ceiling — Score 3 | Scores 1 when… |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 3 | **Fluency (流畅性)** | Clause order, modifiers, grammar, punctuation, and concision are natural; no translationese or redundant padding. | At most 2 minor slips that do not impede reading. | One sentence requires rereading, or 3+ language errors occur. | English-shaped or ungrammatical Chinese is pervasive. |
| 4 | **Register & Tone** | Professional neutral tone and reader address (**你**, **您**, or impersonal) fit the audience and remain consistent. | One isolated pronoun or politeness slip without a voice shift. | Two or more **你/您** shifts or an unsuitable level of directness. | Tone and reader address are inconsistent throughout. |
| 5 | **Terminology & Consistency** | Terms use Simplified Chinese and accepted Mainland forms consistently; English references follow the glossary. | One minor recognizable inconsistency. | Two or more inconsistent forms, a Traditional form, or one misleading term. | Terminology and script are unreliable throughout. |
| 6 | **Regional & Linguistic Naturalness** | Pronoun omission, active/result constructions, connectors, and modifier order suit Mainland Chinese. | One or two harmless stylistic nits. | Several literal pronouns, **被** constructions, calques, or **的** chains occur. | Literal English patterns or wrong-locale forms dominate. |
| 7 | **Code & Command Integrity** *(technical only — Tier A severity: any violation caps this at ≤2)* | Identifiers, APIs, commands, paths, and file names are unchanged; only human-language comments are translated. | — (no trivial tolerance) | A single code element or command is altered. | Code and commands are repeatedly translated or corrupted. |
| 8 | **Developer Terminology Convention** *(technical only)* | Terms match Mainland developer usage and the product glossary without forced translation. | One borderline but recognizable choice. | A nonstandard translation would confuse a developer. | Technical concepts are consistently unnatural or unrecognizable. |

> Criterion 7 has Tier A severity in practice: any altered command or identifier fails the document.

**Overall result:** PASS only if Criteria 1–2 equal 5 and every applicable Criterion 3–8 is at least 4, with no Criterion 7 violation. Otherwise FAIL and iterate, up to the 3-iteration escalation cap. Record a defect under its most specific criterion only.