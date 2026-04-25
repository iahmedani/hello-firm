# hello-firm

Minimal greeting library — Ahmedani Studios' warm-up project for the CI/CD pipeline.

## Install

Clone the repo and install in development mode:

```bash
pip install -e ".[dev]"
```

## Quickstart

```python
from hello_firm import greet
greet("World")  # "Hello, World"
```

## API reference

### `greet(name: str) -> str`

Returns the string `"Hello, {name}"`. 

**Type contract:** Raises `TypeError` if `name` is not a `str` (see spec FR-3).

## Development

Install dev dependencies (pytest, ruff) via the `[dev]` extra in `pyproject.toml`:

```bash
pip install -e ".[dev]"
pytest                # run tests
ruff check .          # lint check
ruff format --check . # format verification
```

## CI

All PRs run three checks in parallel ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)):
- `lint` — style and correctness (ruff check + format)
- `test` — functional verification (pytest)
- `security-scan` — security checks (ruff S/B rules)

All three must pass to merge.

## License

MIT
