import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_additions = """
  .hero-top-row { flex-direction: column; align-items: center !important; text-align: center; gap: 40px !important; }
  .hero-title-wrap { text-align: center !important; }
  .hero-wrapper { flex-direction: column; align-items: center; justify-content: center; }
  .hero-brands-ticker { max-width: 100%; margin-top: 20px; }
"""

insert_target = '.hero-wrapper { padding: 0 16px; flex-direction: column; align-items: center; }'
if insert_target in css:
    css = css.replace(insert_target, insert_target + "\n" + mobile_additions)
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Mobile flex fixes added.")
else:
    print("Could not find mobile flex insert point.")
