import os

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ("Expande tu<br><em>Franquicia</em> en", "Expande tu<br><em>Marca y Franquicia</em> en"),
    ("Conectamos marcas y franquicias con espacios", "Conectamos marcas, franquicias y emprendimientos con espacios"),
    ("Facilitamos la entrada de tu franquicia en", "Facilitamos la entrada de tu marca o franquicia en"),
    ("para ayudar a franquicias a expandirse", "para ayudar a marcas, franquicias y emprendimientos a expandirse"),
    ("la expansión de tu franquicia sea", "la expansión de tu marca o franquicia sea"),
    ("Posiciona tu franquicia en los corredores", "Posiciona tu marca o franquicia en los corredores"),
    ("requerimientos específicos de tu franquicia.", "requerimientos específicos de tu marca o franquicia."),
    ("manual de marca de la franquicia',", "manual de marca o franquicia',")
]

for old, new in replacements:
    html = html.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_replacements = [
    ("right: -100%;", "right: 0;\n    transform: translateX(100%);"),
    (".nav-links.open {\n    right: 0;\n  }", ".nav-links.open {\n    transform: translateX(0);\n  }"),
    (".nav-logo img { height: 72px; object-fit: contain; }", ".nav-logo img { height: 96px; object-fit: contain; }"),
    (".nav-logo img { height: 52px; }", ".nav-logo img { height: 64px; }"),
    (".nav-logo img { height: 44px; }", ".nav-logo img { height: 52px; }"),
    (".footer-brand img { height: 50px; margin-bottom: 24px; }", ".footer-brand img { height: 96px; margin-bottom: 24px; }")
]

for old, new in css_replacements:
    css = css.replace(old, new)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixes applied.")
