import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_cabsas = '''        <a href="#aliados" class="nav-cabsas" style="display: flex; align-items: center; gap: 6px; text-decoration: none; padding-right: 12px; border-right: 1px solid rgba(255,255,255,0.1);">
          <span style="font-size: 0.65rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">By</span>
          <img src="./assets/cab-logo.png" alt="CABSAS" class="cabsas-nav-img" style="height: 28px; filter: brightness(1.2);">
        </a>'''

new_cabsas = '''        <a href="#aliados" class="nav-cabsas" style="display: flex; align-items: center; text-decoration: none; padding-right: 16px; border-right: 1px solid rgba(255,255,255,0.1);">
          <img src="./assets/cab-logo.png" alt="CABSAS" class="cabsas-nav-img" style="height: 44px; filter: brightness(1.2);">
        </a>'''

html = html.replace(old_cabsas, new_cabsas)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update mobile CSS for CABSAS logo
css = css.replace('.cabsas-nav-img { height: 20px !important; }', '.cabsas-nav-img { height: 32px !important; }')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CABSAS logo updated.")
