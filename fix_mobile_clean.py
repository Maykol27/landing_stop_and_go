import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add html { overflow-x: hidden; width: 100%; } globally
if 'html { scroll-behavior: smooth;' in css:
    css = css.replace('html { scroll-behavior: smooth; }', 'html { scroll-behavior: smooth; overflow-x: hidden; width: 100%; }')

# 2. Fix .hero padding in max-width: 768px
css = re.sub(
    r'(\.hero\s*\{\s*min-height:\s*100vh;\s*min-height:\s*100dvh;\s*padding:\s*)80px\s*0\s*30px(;?\s*\})',
    r'\1 140px 0 30px\2',
    css
)

# 3. Shrink logo in max-width: 768px
if '.hamburger { display: flex; }' in css:
    css = css.replace('.hamburger { display: flex; }', '.hamburger { display: flex; }\n  .nav-logo img { height: 60px; max-width: 70vw; }')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated mobile styles securely.")
