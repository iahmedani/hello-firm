# hello-firm

Minimal greeter — Ahmedani Studios warm-up project.

## Install

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

Returns `"Hello, {name}"`. Raises `TypeError` if `name` is not a `str`.

## Development

```bash
pytest
ruff check .
ruff format --check .
```

## CI

See [`.github/workflows/ci.yml`](.github/workflows/ci.yml).
Three required PR checks: `lint`, `test`, `security-scan` — all must be green to merge.

## License

MIT
