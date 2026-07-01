import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Modify mobile nav-logo size and add CABSAS responsive tweaks
css = css.replace(
    '.nav-logo img { height: 60px; max-width: 70vw; }',
    '.nav-logo img { height: 48px; max-width: 40vw; }\n  .nav-cabsas span { display: none; }\n  .cabsas-nav-img { height: 20px !important; }\n  .nav-cabsas { padding-right: 8px !important; border-right: none !important; }'
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Navbar responsive CSS updated.")
