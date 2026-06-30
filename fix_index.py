with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<script src="./carousel.js"></script>', '<script type="module" src="./carousel.js"></script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script tag in index.html")
