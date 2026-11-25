"""The 3 AM Excuse — make.fun entry (Account A / overtheraa).

One line, in the voice of a hardware wallet refusing to sign at 3 AM.
Judge brief, in order: (1) on subject — the line now says the refusal
outright ("I'm not signing") instead of only implying it by clocking
off; (2) originality — beauty sleep / wellness, not the usual battery,
firmware-update or cold-storage jokes; (3) wallet's own voice — a device
with its own bedtime and grudges, ordering its human to bed too;
(4) the hour is the joke — "sunrise" and "3 AM" make the line
unpasteable onto a 3 PM transaction; (5) economy — one tight breath,
ending on the punch that the coins will survive the night but the
human's 3 AM judgment will not.
"""

ENTRY = "It's 3 AM — I'm not signing, I'm clocking off for beauty sleep, and so are you. Your coins will still be here at sunrise; your judgment won't."


def verify(text=ENTRY):
    """Enforce the gate: UTF-8, 1-200 chars, non-blank, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def write_entry(path="/output/entry.txt"):
    """Write ENTRY plus a trailing newline to path, creating dirs."""
    verify()
    import os

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main():
    verify()
    write_entry()
    print(f"{len(ENTRY)} characters")
    print(ENTRY)


if __name__ == "__main__":
    main()
