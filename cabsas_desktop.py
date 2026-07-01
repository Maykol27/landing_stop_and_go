import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Increase CABSAS logo size on desktop
html = html.replace(
    '<img src="./assets/cab-logo.png" alt="CABSAS" class="cabsas-nav-img" style="height: 44px; filter: brightness(1.2);">',
    '<img src="./assets/cab-logo.png" alt="CABSAS" class="cabsas-nav-img" style="height: 72px; filter: brightness(1.2);">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Desktop CABSAS logo size increased.")
