---
name: deslop
description: Use when cleaning up AI-generated code slop, unnecessary comments, boilerplate, or over-engineering in current project code, or when reviewing SKILL.md files for quality before promoting them.
---

# Remove AI Code Slop

Review the code currently present in the project and remove unnecessary complexity, redundant comments, and boilerplate based on its actual behavior and local conventions.

## Trigger

Use when the user requests code cleanup or when code feels over-engineered.

## Scope

Use the files or directories the user specifies. Otherwise, review the current project's source code, excluding third-party dependencies and generated output. Include existing and newly written code regardless of commit status. The skill also works in directories without Git.

## Workflow

1. Locate source files within the scope and identify the project's conventions and available checks.
2. Read the current files and relevant callers to understand behavior, then identify slop patterns from the focus areas below.
3. Remove or simplify the identified slop while preserving intended functionality.
4. Re-read the edited code and affected callers to verify the cleanup remains consistent with the surrounding implementation.
5. Run the project's relevant tests, type checks, or lint checks for the affected code. Report any checks that could not be run.
6. Summarise what was cleaned.

## Focus Areas

- Extra comments that state the obvious or are inconsistent with local style
- Defensive try/catch blocks that are abnormal for trusted internal code paths
- Casts to `any` used only to bypass type issues
- Over-engineered abstractions for one-time operations (premature helpers, factories)
- Deeply nested code that should be simplified with early returns
- Backwards-compatibility hacks (renamed `_vars`, re-exports, `// removed` comments)
- Features, refactoring, or "improvements" beyond what was requested
- Docstrings, type annotations, or comments that add no useful information in context
- Error handling for scenarios that can't happen in trusted internal paths

## Guardrails

- Keep behavior unchanged unless fixing a clear bug.
- Prefer minimal, focused edits over broad rewrites.
- Three similar lines of code is better than a premature abstraction.
- If you remove something, verify it's truly unused first.
- Keep the final summary concise (1-3 sentences).

## Skill-file mode

When the target is a `SKILL.md`, lint it against the same
slop instinct applied to prose. Run this before promoting a skill. Flag:

- **Stale lines** - guidance written for an old version of the skill that no
  longer matches what it does. Cut it.
- **Bloat** - the skill runs past one screen with detail that belongs in a
  linked reference. Push it down: in-skill step, then in-skill reference, then
  an external file behind a pointer.
- **Dead sentences** - a line that changes nothing if deleted. Delete it.
- **Duplication** - the same instruction stated in two places, so edits drift.
  Keep one source of truth.
- **Premature stop** - the method ends before the work does (asks the question
  but never records the answer, cleans but never verifies).
- **Weak anchor** - no single concept the skill turns on. A skill the reader
  can name in one word triggers and executes in fewer tokens.
- **Missing invocation intent** - no declared human-run vs auto-triggered mode.
  See [`rules/skill-conventions.mdc`](../../rules/skill-conventions.mdc).
- **Wrong write op** - a state-changing skill that does not say whether it
  adds, updates, or appends, or that duplicates its output on a second run.

**Skill-file mode output:** the flagged issues by line, the edits applied,
the cleanup summary, and whether the skill is ready to promote.

## Output (code mode)

- List of slop patterns found with file locations
- Edits applied
- One-line summary of what was cleaned
