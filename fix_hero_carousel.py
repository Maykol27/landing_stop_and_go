import re

# 1. Fix carousel.js
with open('carousel.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

js_content = js_content.replace(
    'track.style.transform = `translateX(-${index * 100}%)`;',
    'track.style.transform = `translateX(-${index * (100 / images.length)}%)`;'
)

with open('carousel.js', 'w', encoding='utf-8') as f:
    f.write(js_content)


# 2. Fix style.css hero positioning
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Change .hero from align-items: center to align-items: flex-end
css_content = re.sub(
    r'(\.hero\s*\{[^}]*display:\s*flex;\s*align-items:\s*)center(;[^}]*padding:\s*100px\s+0\s+)40px(;[^}]*\})',
    r'\1flex-end\2 8vh\3',
    css_content
)

# Wait, the regex might fail if spaces don't match. 
# Let's do simple string replace on .hero
css_old = """.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; align-items: center; justify-content: center;
  text-align: center; overflow: hidden;
  padding: 100px 0 40px;
}"""
css_new = """.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; align-items: flex-end; justify-content: center;
  text-align: center; overflow: hidden;
  padding: 100px 0 10vh;
}"""
if css_old in css_content:
    css_content = css_content.replace(css_old, css_new)
else:
    # Fallback if there are minor whitespace differences
    css_content = re.sub(
        r'(\.hero\s*\{.*?align-items:\s*)center(.*?padding:\s*100px\s+0\s+)40px(.*?})',
        r'\1flex-end\2 10vh\3',
        css_content,
        flags=re.DOTALL
    )

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Fixes applied successfully.")
