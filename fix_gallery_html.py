import os
import re

assets_dir = 'public/assets'
all_files = os.listdir(assets_dir)
exclude = ['cab-logo.png', 'cgbi-logo.png', 'hero.png', 'logostop&go.jpeg', 'logostop_go.png', 'sikai-logo.png', 'stop_go_hero.png', 'fondohero.jpeg']

gallery_images = [f for f in all_files if f not in exclude and f.endswith(('.png', '.jpeg', '.jpg', '.webp'))]

# Generate index.html slides
slides_html = ""
for i, img in enumerate(gallery_images):
    active = ' active' if i == 0 else ''
    slides_html += f'''        <div class="sg-slide{active}" onclick="openLightbox({i})">
          <img src="./assets/{img}" alt="Proyecto {i+1}"/>
          <div class="sg-slide-info"><span>{i+1:02d} / {len(gallery_images):02d}</span><p>Proyecto {i+1}</p></div>
        </div>
'''

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace gallery
html = re.sub(
    r'(<div class="sg-carousel-track" id="galleryTrack">)(.*?)(      </div>\s*<button class="sg-arrow sg-arrow-prev")',
    r'\1\n' + slides_html + r'\3',
    html, flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done index.html gallery fix")
