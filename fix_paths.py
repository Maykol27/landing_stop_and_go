import os
for file in ['index.html', 'carousel.js']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('"/assets/', '"./assets/').replace("'/assets/", "'./assets/")
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
