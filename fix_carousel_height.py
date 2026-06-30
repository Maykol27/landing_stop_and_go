import re

with open('carousel.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace desktop height
css_content = re.sub(
    r'(\.sg-carousel-track\s*\{.*?height:\s*)520px(.*?})',
    r'\1 75vh; min-height: 520px; max-height: 850px\2',
    css_content,
    flags=re.DOTALL
)

# Replace mobile height
css_content = re.sub(
    r'(\.sg-carousel-track\s*\{\s*height:\s*)280px(;.*?})',
    r'\1 55vh; min-height: 350px\2',
    css_content
)

with open('carousel.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated carousel height.")
