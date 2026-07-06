with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The media query block at the end looks like:
# .hero-title-wrap { text-align: center !important; }

css = css.replace(
    ".hero-title-wrap { text-align: center !important; }",
    ".hero-title-wrap { text-align: center !important; margin-top: 25px !important; }"
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Title margin added.")
