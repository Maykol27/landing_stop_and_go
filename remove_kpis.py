import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find and remove hero-stats block
pattern = r'(<div class="hero-stats hero-stats-top".*?</div>\s*</div>\s*</div>)'
# Actually let's just use string finding to be extremely safe

start_tag = '<div class="hero-stats hero-stats-top"'
if start_tag in html:
    start_idx = html.find(start_tag)
    # The stats block has 3 hero-stat divs inside, so 4 </div> total from the start of hero-stats
    # Let's just find the end of the top row which is right after it.
    end_idx = html.find('</div>\n\n    </div>', start_idx) 
    
    if end_idx == -1:
        # let's try finding by matching </div> tags
        current = start_idx
        for _ in range(4):
            current = html.find('</div>', current) + 6
        html = html[:start_idx] + html[current:]
        print("KPIs removed from index.html (fallback matching).")
    else:
        # found the closing div of hero-stats
        # wait, the exact HTML we generated is:
        #       <div class="hero-stats hero-stats-top" ...>
        #         <div class="hero-stat"><h3 id="stat-proyectos">0+</h3><p>Puntos Disponibles</p></div>
        #         <div class="hero-stat"><h3 id="stat-roi">0%</h3><p>Ventas Cruzadas</p></div>
        #         <div class="hero-stat"><h3 id="stat-dias">0</h3><p>Días de Montaje</p></div>
        #       </div>
        #
        #     </div>
        
        # we can just regex the exact block
        html = re.sub(r'\s*<div class="hero-stats hero-stats-top".*?</div>\s*</div>', '', html, flags=re.DOTALL)
        print("KPIs removed from index.html.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
