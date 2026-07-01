import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace hardcoded color #fff with var(--text-color) for FANYF in the ticker
html = html.replace(
    'style="color: #fff; font-family: var(--heading); font-size: clamp(1.1rem, 4vw, 1.8rem); font-weight: 900; letter-spacing: 1px; display: flex; align-items: center; justify-content: center;"',
    'style="color: var(--text-color); font-family: var(--heading); font-size: clamp(1.1rem, 4vw, 1.8rem); font-weight: 900; letter-spacing: 1px; display: flex; align-items: center; justify-content: center;"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("FANYF text color updated to be responsive to light/dark mode.")
