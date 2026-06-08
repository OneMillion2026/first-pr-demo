import re


def slugify(text):
    """Convert a string to a URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-")


def truncate(text, max_len):
    """Truncate text to max_len characters, appending '...' if cut."""
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."
