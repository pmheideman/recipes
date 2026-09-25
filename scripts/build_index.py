"""Generate index.html listing every recipe in recipes/ (by its <title>)."""
import html, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
items = []
for f in sorted((root / "recipes").glob("*.html")):
    if f.name.startswith("_"):
        continue
    m = re.search(r"<title>(.*?)</title>", f.read_text(encoding="utf-8"), re.S | re.I)
    title = html.unescape(m.group(1).strip()) if m else f.stem.replace("-", " ").title()
    items.append((title.lower(), title, f.name))

links = "\n".join(
    f'    <li><a href="recipes/{html.escape(name)}">{html.escape(title)}</a></li>'
    for _, title, name in sorted(items)
) or "    <li>No recipes yet.</li>"

(root / "index.html").write_text(f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Recipes</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<main>
  <h1>Recipes</h1>
  <ul class="index">
{links}
  </ul>
</main>
</body>
</html>
""", encoding="utf-8")
print(f"index.html: {len(items)} recipe(s)")
