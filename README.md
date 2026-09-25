# Recipes

A collection of recipes as plain HTML pages, published with GitHub Pages.

## Adding a recipe

1. Copy `recipes/_template.html` to `recipes/your-recipe-name.html` and fill it in.
   The `<title>` is what shows up on the index page.
2. Commit and push to `main`:
   ```sh
   git add recipes/your-recipe-name.html
   git commit -m "Add your recipe"
   git push
   ```
3. A GitHub Action rebuilds the index and redeploys the site within a minute or two.

Any self-contained HTML file dropped into `recipes/` works — the shared
`style.css` is optional. Files starting with `_` are left off the index.

To preview locally: `python3 scripts/build_index.py && python3 -m http.server`
