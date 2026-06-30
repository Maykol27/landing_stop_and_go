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
    r'<div class="sg-carousel-track" id="galleryTrack">.*?</div>\s*<!-- END TRACK -->',
    f'<div class="sg-carousel-track" id="galleryTrack">\n{slides_html}      </div> <!-- END TRACK -->',
    html, flags=re.DOTALL
)
# Wait, index.html might not have <!-- END TRACK -->. Let's do a smarter replace.
# Looking at index.html, it's just <div class="sg-carousel-track" id="galleryTrack"> ... </div>
html = re.sub(
    r'(<div class="sg-carousel-track" id="galleryTrack">)(.*?)(      </div>\s*<div class="sg-carousel-nav">)',
    r'\1\n' + slides_html + r'\3',
    html, flags=re.DOTALL
)

# Move hero-badge
# 1. Remove it from its current position
badge_match = re.search(r'\s*<div class="hero-badge"[^>]*>.*?</div>\s*', html, flags=re.DOTALL)
if badge_match:
    badge_html = badge_match.group(0).strip()
    html = html.replace(badge_match.group(0), '\n        ')
    
    # 2. Insert it after </h1>
    html = re.sub(
        r'(</h1>)',
        r'\1\n        ' + badge_html.replace('data-aos-delay="100"', 'data-aos-delay="200" style="margin-bottom: 24px;"'),
        html
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Read carousel.js
with open('carousel.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Generate JS array
js_array = "const images = [\n"
for img in gallery_images:
    js_array += f"    {{ src: './assets/{img}', cap: 'Proyecto' }},\n"
js_array += "  ];"

# Replace images array
js = re.sub(r'const images = \[.*?\];', js_array, js, flags=re.DOTALL)

with open('carousel.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    'font-size: clamp(2.4rem, 5vw, 4.5rem);',
    'font-size: clamp(1.8rem, 4vw, 3.2rem);'
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
