# Parallel manuscript revision workflow

This workflow is for agents working from `docs/manuscript_revision_task_board.md`.

The intended user prompt is simple.

`Let's tackle EDIT-001.`

The agent should read this workflow, read the task board, inspect the relevant source files, create a task branch, make the smallest useful change, commit it, and report what remains.

## Ground Rules

Use `uv` for any Python work.

Do not build or compile LaTeX unless Kyle explicitly asks.

Do not edit `Definitions/mdpi.cls`.

Do not use author-date citation commands. Use `\cite{}`.

Do not use em dash characters in manuscript text or docs.

Keep task edits narrow. Avoid broad cleanup outside the active task.

Respect existing untracked or modified files. Do not revert changes made by another session unless Kyle explicitly asks.

## Branch And Worktree Pattern

Each task should happen on its own branch.

Use the `codex/` prefix for branches. A good branch name is `codex/edit-001-front-matter` or `codex/edit-013-red-lines`.

If the session is already inside a prepared worktree, start with:

```bash
git status --short --branch
git switch -c codex/edit-001-front-matter
```

If creating a worktree manually from the repository root, use a sibling directory:

```bash
git fetch origin
git worktree add ../masters-thesis-edit-001 -b codex/edit-001-front-matter main
cd ../masters-thesis-edit-001
```

If `main` has local divergence, stop and report that before creating the worktree. Do not guess which side should be used.

## Task Start Checklist

Read `AGENTS.md` first.

Read `docs/manuscript_revision_task_board.md`.

Find the active task ID.

Inspect the source Word document only if the task needs Word context.

Inspect `manuscript.tex` and any figure, bibliography, or analysis files listed by the task.

Mark the task as `In progress` in the task board if the branch will modify the board. If that would create avoidable conflicts, leave the status unchanged and report the claim in the final message.

## How To Work A Task

Keep the task scoped to the listed task ID.

If the task exposes a new dependency, record it in the task note rather than expanding the task silently.

If the task needs a Kyle decision, ask Kyle. Mark the task `Blocked` only when the same blocking condition persists and no useful progress remains.

For manuscript prose, preserve the current scientific meaning unless the task asks for a wording change.

For statistics, do not invent values. Find the analysis source, rerun the analysis with `uv` or the existing project toolchain, or ask Kyle where the source values live.

For figures, find and update the source script when possible. Do not edit final PNGs by hand unless no source exists and Kyle approves.

For bibliography, add complete BibTeX entries to `bibliography/Thesis.bib` and cite with existing key style when possible.

## Completion Checklist

Before committing, check:

```bash
git diff --check
rg "$(printf '\\342\\200\\224')" docs manuscript.tex bibliography || true
```

Run a build only if Kyle explicitly asked for one.

Update the task board status to `Done` when the task is complete. Add a short completion note under the task if helpful.

Commit the task atomically:

```bash
git add docs/manuscript_revision_task_board.md manuscript.tex bibliography/Thesis.bib figures
git commit -m "Address EDIT-001 front matter sync"
```

Only stage files that the task actually changed.

## Merge Back Pattern

After a task branch is complete, merge it back with no fast forward:

```bash
git switch main
git merge --no-ff codex/edit-001-front-matter
```

If conflicts occur, resolve them with care. For `manuscript.tex`, preserve compatible changes from both branches. For task board conflicts, preserve the newest task status and completion notes from both branches.

Ask Kyle when a conflict represents a scientific choice, a statistical choice, or incompatible prose.

After the merge succeeds, commit the merge if Git has not already done so. Then continue to the next task or section gate.

## Section Gate Rule

The task board has ordered sections.

Do not start a task in Section 2 until all Section 1 tasks are merged to `main`.

Do not start a task in Section 3 until all Section 2 tasks are merged to `main`, unless Kyle explicitly overrides the gate for a purely mechanical caption or cross-reference task.

Do not start Section 4 until figures, tables, and analysis decisions are settled.

Do not start Section 5 until all earlier sections are merged.

## Final Message Pattern

When finishing a task, report:

The task ID.

The branch name.

The files changed.

Whether the task is done or blocked.

Any Kyle decision that remains.

Whether tests or builds were run.
