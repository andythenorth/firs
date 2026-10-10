"""Render the latest NewGRF changelog entry as a forum release announcement.

Input is rendered changelog Markdown, after any project template substitutions.
Supported conventions: release titles between dashed rules, *section labels*,
four-space nested '- ' bullets, plain paragraphs and 'Not savegame compatible'
warnings. This is deliberately not a general Markdown renderer.

Chameleon is needed only when rendering. The adjacent template owns all BBCode.
"""

import argparse
from pathlib import Path


def get_release_data(changelog):
    """Extract title, version and template events from rendered changelog text."""
    lines = changelog.splitlines()

    # Release titles are surrounded by dashed rules. Stop at the next title.
    headings = [
        index
        for index in range(1, len(lines) - 1)
        if lines[index].strip().endswith(" Release")
        and len(lines[index - 1].strip()) >= 3
        and set(lines[index - 1].strip()) == {"-"}
        and len(lines[index + 1].strip()) >= 3
        and set(lines[index + 1].strip()) == {"-"}
    ]
    if not headings:
        raise ValueError("No release heading found in changelog.txt")
    version = lines[headings[0]].strip().removesuffix(" Release")
    end = headings[1] - 1 if len(headings) > 1 else len(lines)
    entry = lines[headings[0] + 2 : end]

    titles = [
        line.strip().partition(":")[2].strip()
        for line in lines[:headings[0] - 1]
        if line.strip().startswith("Changelog:")
    ]
    if len(titles) != 1 or not titles[0]:
        raise ValueError("Expected one non-empty 'Changelog: GRF Title' header")
    project_name = titles[0]
    if not version or any(char in version for char in '/\\'):
        raise ValueError("Release version must be non-empty and contain no path separators")

    # Collect paragraphs, section labels and bullet trees before formatting.
    blocks = []
    parents = []
    for line in entry:
        text = line.strip()
        if not text:
            continue
        if text.startswith("- "):
            indent = len(line) - len(line.lstrip(" "))
            depth = indent // 4
            if indent % 4 or depth > len(parents):
                raise ValueError(f"Unexpected changelog bullet indentation: {line!r}")
            item = {"text": text[2:].lstrip(), "children": []}
            if depth == 0:
                if not parents:
                    blocks.append({"kind": "list", "items": []})
                blocks[-1]["items"].append(item)
            else:
                parents[depth - 1]["children"].append(item)
            parents = parents[:depth] + [item]
            continue
        if parents and line.startswith(" " * (4 * len(parents))):
            parents[-1]["text"] += " " + text
            continue
        parents = []
        if text.startswith("Not savegame compatible"):
            kind = "warning"
        elif len(text) > 2 and text.startswith("*") and text.endswith("*"):
            kind = "section"
            text = text[1:-1]
        else:
            kind = "paragraph"
        blocks.append({"kind": kind, "text": text})

    # Flatten nested lists into template events; all BBCode lives in the .pt file.
    def list_events(items):
        yield {"kind": "list_open"}
        for item in items:
            yield {"kind": "item", "text": item["text"]}
            if item["children"]:
                yield from list_events(item["children"])
        yield {"kind": "list_close"}

    events = []
    for block in blocks:
        if block["kind"] == "list":
            events.extend(list_events(block["items"]))
        else:
            events.append(block)
        events.append({"kind": "blank"})

    return {"project_name": project_name, "version": version, "events": events}


def render_release_announcement(release_data):
    """Render extracted release data using the adjacent BBCode template."""
    from chameleon import PageTemplateLoader

    templates = PageTemplateLoader(str(Path(__file__).resolve().parent), format="text")
    announcement = templates["release_announcement.pt"](**release_data)
    return announcement.rstrip() + "\n"


def write_release_announcement(changelog_path, grf_name, output_dir="."):
    """Write <grf-name>-<changelog-version>-announcement.bbcode.txt."""
    if not grf_name or grf_name in (".", "..") or any(c in grf_name for c in '/\\'):
        raise ValueError("GRF name must be a filename identifier, not a path")
    changelog = Path(changelog_path).read_text(encoding="utf-8")
    data = get_release_data(changelog)
    announcement = render_release_announcement(data)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{grf_name}-{data['version']}-announcement.bbcode.txt"
    with output_path.open("w", encoding="utf-8", newline="\n") as destination:
        destination.write(announcement)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate a BBCode release announcement.")
    parser.add_argument("grf_name", help="Filename identifier, e.g. iron-horse")
    parser.add_argument(
        "--nested-docs-by-grf", action="store_true",
        help="Read docs/<grf_name>/changelog.txt instead of docs/changelog.txt",
    )
    parser.add_argument("--changelog", type=Path, help="Override the input changelog path")
    parser.add_argument("--output-dir", type=Path, default=Path("."))
    args = parser.parse_args()
    changelog_path = args.changelog
    if changelog_path is None:
        docs_dir = Path("docs") / args.grf_name if args.nested_docs_by_grf else Path("docs")
        changelog_path = docs_dir / "changelog.txt"
    try:
        output_path = write_release_announcement(changelog_path, args.grf_name, args.output_dir)
    except (OSError, ValueError) as error:
        parser.exit(1, f"BBCode announcement: {error}\n")
    print(f"[BBCODE ANNOUNCEMENT] {output_path}")


if __name__ == "__main__":
    main()
