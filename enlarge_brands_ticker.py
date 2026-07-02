import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the current track with one that has more duplicates for a seamless infinite loop on ultra-wide screens
brand_images = """
          <img src="https://cabsas.co/wp-content/uploads/2025/11/terpel.png" alt="Terpel">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/zeuss.png" alt="Zeuss">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/puma.png" alt="Puma Energy">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/primax.png" alt="Primax">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/petromil.png" alt="Petromil">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/petrobras.png" alt="Petrobras">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/ecos.png" alt="Ecos">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/chevron.png" alt="Chevron">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/biomax.png" alt="Biomax">
"""

# We need two halves. Each half should be big enough to cover a 4k screen. 
# 1 set = 9 logos (approx 1500px). 3 sets = 27 logos (approx 4500px). 
half = brand_images * 3
full_track = f"""
        <div class="hero-brands-track">
{half}
{half}
        </div>
"""

# Find the track container and replace everything inside it
track_container_start = '<div class="hero-brands-track-container">'
track_container_end = '</div>\n    </div>\n  </section>'

start_idx = html.find(track_container_start)
end_idx = html.find('</div>\n    </div>\n  </section>', start_idx)

if start_idx != -1 and end_idx != -1:
    before = html[:start_idx + len(track_container_start)]
    after = html[end_idx:]
    html = before + full_track + "      " + after
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated with more logos for seamless loop.")
else:
    print("Could not find track container in HTML.")


with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update CSS
old_ticker_css = """
/* ========== HERO BRANDS TICKER ========== */
.hero-brands-ticker {
  position: absolute;
  bottom: 15px; /* Float nicely above the bottom edge */
  left: 0;
  width: 100%;
  z-index: 10;
}
.hero-brands-track-container {
  overflow: hidden;
  width: 100%;
  display: flex;
}
.hero-brands-track {
  display: flex;
  align-items: center;
  gap: 70px;
  padding-left: 70px;
  animation: hero-brands-scroll 40s linear infinite;
  min-width: max-content;
}
@keyframes hero-brands-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.hero-brands-track img {
  height: 32px;
  object-fit: contain;
  /* Full color by default */
}
"""

new_ticker_css = """
/* ========== HERO BRANDS TICKER ========== */
.hero-brands-ticker {
  position: absolute;
  bottom: 15px;
  left: 0;
  width: 100%;
  z-index: 10;
}
.hero-brands-track-container {
  overflow: hidden;
  width: 100%;
  display: flex;
}
.hero-brands-track {
  display: flex;
  align-items: center;
  gap: 80px;
  padding-left: 80px;
  animation: hero-brands-scroll 60s linear infinite;
  min-width: max-content;
}
@keyframes hero-brands-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.hero-brands-track img {
  height: 60px; /* Made logos much bigger */
  object-fit: contain;
  flex-shrink: 0;
}
"""

if old_ticker_css.strip() in css:
    css = css.replace(old_ticker_css.strip(), new_ticker_css.strip())
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css updated for bigger logos and seamless loop.")
else:
    print("Could not find the exact ticker CSS to replace.")

