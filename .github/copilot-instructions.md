# GitHub Copilot Instructions for the `Pessoal` repository

This repository is a personal collection of small Python exercises and a single HTML file. There
is no application framework, build pipeline, or tests.  The goal of a Copilot/AI agent in this
repo is to help the user quickly understand and modify simple scripts.

## Repo layout

- `index.html` – a trivial HTML page at the root.
- `Atividades Python/` and `lista 1 python/` – two folders containing Python scripts named
  `AtividadeX.py` or `atividadeX.py`.  Each file is a standalone exercise that reads from
  `input()` and prints results.  There are no shared modules.

## Big picture

There is no service boundary or data flow beyond the standard input/output of each script.  These
are classroom/homework assignments written in Portuguese.  The `Atividades Python` directory uses
mixed case filenames; `lista 1 python` uses all lowercase.  Treat each script independently when
adding new features or refactoring.

## Running and debugging

- Use `python3 <path/to/script>.py` from the workspace root to execute any script.
- There are no tests or build commands; simply run the file interactively.
- Editors/IDEs may lock on the Portuguese strings – preserve them exactly unless the user
  requests translation.

## Coding conventions and patterns

- Code is rudimentary, often missing PEP 8 formatting.  Do not enforce style unless explicitly
  asked; the primary goal is correct logic and retaining the original I/O prompts.
- Many scripts prompt the user in Portuguese (`Digite um numero`, `Ola mundo` etc.).  Keep the
  messages intact when modifying or adding new prompts.
- There are no external dependencies; do not introduce new packages without checking with the
  user.
- When creating new scripts, place them in the appropriate folder and follow the existing
  naming pattern (e.g. `atividadeN.py` for the "lista 1 python" folder).

## Editing guidance

- If the user asks for enhancements (e.g. "make activity 3 calculate the average"), update only
  the specified file.  Do not refactor across multiple activities.
- Avoid changing folder names or refactoring the directory structure – it reflects the
  user's organization of exercises.

## Committing and collaboration

- There is no CI, so commit messages should be simple and descriptive (e.g. "fix typo in
  atividade2.py" or "add new exercise for loops").  The main branch is `main`.

> ⚠️ Note: This is a very small, ad‑hoc repository.  The most valuable assistance you can provide
> is concise, self‑contained Python snippets and explanations that respect the original Portuguese
> text.

Please let me know if there are any unclear sections or if you need additional instructions
specific to a particular script or workflow.