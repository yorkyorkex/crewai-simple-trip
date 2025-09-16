# Repository Guidelines

## Project Structure & Module Organization
- Core code sits in `src/travel_planner/`; `main.py` manages interactive CLI, `crew.py` registers agents/tasks, and `tools/` hosts shared integrations like `search_tool.py` and `html_generator.py`.
- Configuration YAML lives in `src/travel_planner/config/` and is loaded by crew decorators. Update both `agents.yaml` and `tasks.yaml` when changing roles.
- Reference outputs and regression fixtures are in `tests/`, while reusable context (for prompts) lives in `knowledge/`. Keep generated plans (`travel_plan.md`, HTML) under source control only when used as baselines.

## Build, Test & Development Commands
- `pip install uv` then `uv sync` to install Python >=3.10,<3.14 dependencies declared in `pyproject.toml`.
- `crewai install` locks dependencies with the crewAI CLI (mirrors uv sync but generates a lockfile).
- `uv run python -m travel_planner.main` starts the interactive planner; append `--demo` to replay the Tokyo example and regenerate `travel_plan.md`.
- `crewai run` executes the configured crew pipeline using the YAML definitions.

## Coding Style & Naming Conventions
- Follow PEP 8: 4 spaces, snake_case for functions/modules, PascalCase for classes, lower_snake_case keys in YAML.
- Keep functions pure when possible; share expensive resources via `tools/tool_registry.py`.
- Document public entry points with docstrings and limit inline comments to non-obvious logic.

## Testing Guidelines
- Automated tests are pending; rely on the `--demo` run plus diffing outputs in `tests/` against new results.
- When introducing features, add or refresh representative Markdown/HTML fixtures and describe manual verification in the PR.
- Validate knowledge base updates (`knowledge/user_preference.txt`) so prompts stay consistent.

## Commit & Pull Request Guidelines
- Commits use concise sentence-style summaries (example: `Refactor Tokyo travel guide: Update itinerary and styling`). Scope each commit narrowly.
- PRs must include: overview of scenario, reproduction steps or commands, regenerated artifacts when applicable, and references to issues or discussions. Add screenshots of rendered plans when they aid review.
- Note any required `.env` variables (e.g., `OPENAI_API_KEY`, `SERPER_API_KEY`, `MODEL`) and configuration tweaks in the description.

## Configuration & Secrets
- Keep secrets in `.env` only; never commit API keys. Update `.env.example` if defaults change.
- Synchronize agent/task changes across YAML and Python (`crew.py`, tools) to avoid configuration drift; list any migrations or manual steps in releases.
