import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<div class="hero-title-wrap" style="width: 92%; max-width: 1200px; margin: 0 auto; text-align: left; z-index: 2; width: 100%;">',
    '<div class="hero-title-wrap" style="width: 92%; max-width: 1280px; margin: 0 auto; text-align: left; z-index: 2;">'
)

# Also let's double check .hero-wrapper max-width. In style.css it is 1280px for .wrap and .nav-wrap.
# I set max-width: 1280px to align perfectly.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero title wrap width fixed.")
