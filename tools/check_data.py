"""Check CV bibliography invariants using only the Python standard library."""
from pathlib import Path
import re
import sys

STATUSES = {"published", "accepted", "preprint", "underreview"}


def records(text):
    # Braced BibTeX records with braced or quoted keyword fields.
    starts = list(re.finditer(r"(?m)^\s*@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", text))
    for start in starts:
        if start.group(1).lower() in {"comment", "preamble", "string"}:
            continue
        depth, quoted, escaped = 1, False, False
        pos = start.end()
        while pos < len(text) and depth:
            char = text[pos]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = not quoted
            elif not quoted and char == "{":
                depth += 1
            elif not quoted and char == "}":
                depth -= 1
            pos += 1
        if depth:
            raise ValueError(f"Unclosed record: {start.group(2)}")
        body = text[start.end():pos - 1]
        field = re.search(r'\bkeywords\s*=\s*(?:\{([^}]*)\}|"([^"]*)")', body, re.I)
        if not field:
            raise ValueError(f"Missing keywords: {start.group(2)}")
        tags = {s.strip() for s in (field.group(1) or field.group(2)).split(",") if s.strip()}
        status = tags & STATUSES
        if len(status) != 1:
            raise ValueError(f"{start.group(2)}: expected exactly ONE status, got {sorted(status)}")
        yield {"key": start.group(2), "status": next(iter(status)), "selected": "selected" in tags}


def check(text):
    entries = list(records(text))
    if not entries:
        raise ValueError("No bibliography records found")
    keys = [entry["key"] for entry in entries]
    if len(set(keys)) != len(keys):
        raise ValueError("Duplicate bibliography keys")
    return entries


def self_test():
    valid = '@article{one, keywords={published,selected}}'
    assert len(check(valid)) == 1
    bad_cases = [
        '@article{one, keywords={selected}}',
        '@article{one, keywords={published,accepted}}',
        '@article{one, title={No status}}',
        valid + "\n" + valid,
    ]
    for text in bad_cases:
        try:
            check(text)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid data was accepted")
    print("PASS: missing status, conflicting status and duplicate-key guards")


if __name__ == "__main__":
    try:
        if "--self-test" in sys.argv:
            self_test()
        source = Path(__file__).resolve().parents[1] / "publications.bib"
        entries = check(source.read_text(encoding="utf-8-sig"))
        selected = sum(e["selected"] and e["status"] != "underreview" for e in entries)
        print(f"PASS: {len(entries)} records; {selected} selected with under-review hidden")
        for status in sorted(STATUSES):
            print(f"  {status}: {sum(e['status'] == status for e in entries)}")
    except (ValueError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)