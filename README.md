# first-pr-demo

A small Python utility for common string helpers.

## Instalation

No dependencies required — pure Python 3.

## Usage

```python
from utils import slugify, truncate

slugify("Hello World!")   # "hello-world"
truncate("Long text", 5)  # "Long..."
```

## Fuctions

- `slugify(text)` — converts a string to a URL-friendly slug
- `truncate(text, max_len)` — truncates a string and appends `...`
