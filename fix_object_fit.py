import re

with open('carousel.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace object-fit: cover with object-fit: contain
css = css.replace('object-fit: cover;', 'object-fit: contain; background-color: #070709;')

with open('carousel.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Changed object-fit to contain in carousel.css")
