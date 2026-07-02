import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

brands_html = """
    <!-- Ticker Marcas -->
    <div class="hero-brands-ticker">
      <p class="hero-brands-title">Distribuidores líderes del sector confían en nuestras soluciones</p>
      <div class="hero-brands-track-container">
        <div class="hero-brands-track">
          <!-- Set 1 -->
          <img src="https://cabsas.co/wp-content/uploads/2025/11/terpel.png" alt="Terpel">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/zeuss.png" alt="Zeuss">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/puma.png" alt="Puma Energy">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/primax.png" alt="Primax">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/petromil.png" alt="Petromil">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/petrobras.png" alt="Petrobras">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/ecos.png" alt="Ecos">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/chevron.png" alt="Chevron">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/biomax.png" alt="Biomax">
          <!-- Set 2 (for infinite loop) -->
          <img src="https://cabsas.co/wp-content/uploads/2025/11/terpel.png" alt="Terpel">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/zeuss.png" alt="Zeuss">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/puma.png" alt="Puma Energy">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/primax.png" alt="Primax">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/petromil.png" alt="Petromil">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/petrobras.png" alt="Petrobras">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/ecos.png" alt="Ecos">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/chevron.png" alt="Chevron">
          <img src="https://cabsas.co/wp-content/uploads/2025/11/biomax.png" alt="Biomax">
        </div>
      </div>
    </div>
  </section>
"""

html = html.replace('  </section>\n\n  <!-- ========== ALIADOS (TICKER) ========== -->', brands_html + '\n  <!-- ========== ALIADOS (TICKER) ========== -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Hero HTML updated with brands ticker.")

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

brands_css = """
/* ========== HERO BRANDS TICKER ========== */
.hero-brands-ticker {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background: rgba(0, 0, 0, 0.75);
  padding: 15px 0 20px;
  z-index: 10;
  backdrop-filter: blur(5px);
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}
.hero-brands-title {
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.85rem;
  font-weight: 400;
  letter-spacing: 1px;
  margin-bottom: 16px;
}
.hero-brands-track-container {
  overflow: hidden;
  width: 100%;
  display: flex;
}
.hero-brands-track {
  display: flex;
  align-items: center;
  gap: 60px;
  padding-left: 60px;
  animation: hero-brands-scroll 40s linear infinite;
  min-width: max-content;
}
@keyframes hero-brands-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.hero-brands-track img {
  height: 35px;
  object-fit: contain;
  filter: grayscale(100%) opacity(0.6) brightness(1.5);
  transition: all 0.3s ease;
}
.hero-brands-track img:hover {
  filter: grayscale(0%) opacity(1) brightness(1);
}
"""

css = css.replace('.hero-badge span { width: 6px; height: 6px; background: var(--primary); border-radius: 50%; display: block; animation: blink 1.5s infinite; }',
                  '.hero-badge span { width: 6px; height: 6px; background: var(--primary); border-radius: 50%; display: block; animation: blink 1.5s infinite; }\n' + brands_css)

# Update padding-bottom of .hero
old_hero_css = '''.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; flex-direction: column; align-items: center; justify-content: space-between;
  text-align: center; overflow: hidden;
  padding: 125px 0 8vh;
}'''

new_hero_css = '''.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; flex-direction: column; align-items: center; justify-content: space-between;
  text-align: center; overflow: hidden;
  padding: 125px 0 calc(8vh + 110px);
}'''

if old_hero_css in css:
    css = css.replace(old_hero_css, new_hero_css)
else:
    print("Could not find the exact old hero padding CSS.")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Hero CSS updated with brands ticker styles.")
