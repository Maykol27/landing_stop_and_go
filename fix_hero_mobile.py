import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace mobile hero styles
css = re.sub(
    r'(\.hero\s*\{\s*min-height:\s*100vh;\s*min-height:\s*100dvh;\s*padding:\s*)140px\s*0\s*30px(;?\s*\})',
    r'\1 160px 0 40px; height: auto \2',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated mobile hero height and padding.")
