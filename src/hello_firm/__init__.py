def greet(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError(f"greet() expected str, got {type(name).__name__}")
    return f"Hello, {name}"
