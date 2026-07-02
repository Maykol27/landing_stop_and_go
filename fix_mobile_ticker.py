import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix .hero mobile padding
old_hero_mobile = '.hero { min-height: 100vh; min-height: 100dvh; padding:   160px 0 40px; height: auto ; }'
new_hero_mobile = '.hero { min-height: 100vh; min-height: 100dvh; padding: 160px 0 90px; height: auto; }'

if old_hero_mobile in css:
    css = css.replace(old_hero_mobile, new_hero_mobile)
    print("Updated mobile hero padding.")
else:
    print("Could not find mobile hero padding rule.")

# Add mobile ticker scale down slightly and reduce gap
mobile_ticker_css = """
  .hero-brands-track { gap: 50px; padding-left: 50px; }
  .hero-brands-track img { height: 60px; }
"""

# Insert this into the @media (max-width: 768px) block right after the .hero adjustments
insert_target = '.hero-wrapper { padding: 0 16px; flex-direction: column; align-items: center; }'
if insert_target in css:
    css = css.replace(insert_target, insert_target + "\n" + mobile_ticker_css)
    print("Added mobile ticker adjustments.")
else:
    print("Could not find insert target for mobile ticker CSS.")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
