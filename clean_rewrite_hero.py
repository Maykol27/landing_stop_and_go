import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="hero-overlay"></div>'
end_marker = '    <div class="hero-scroll">'

# Everything between start_marker and end_marker needs to be replaced.
# But wait, there is also the ticker currently below hero-scroll!
# Oh right, I checked out commit 218401b.
# Let's verify the ticker position in 218401b:
# It's after hero-scroll.
end_marker_actual = '  <!-- ===== ALIADOS ESTRATÉGICOS ===== -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker_actual)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    exit(1)

new_hero_content = """<div class="hero-overlay"></div>
    <div class="hero-overlay-green"></div>

    <!-- TOP ROW: TITLE (LEFT) AND KPIS (RIGHT) -->
    <div class="hero-top-row" style="width: 92%; max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 20px; z-index: 2; width: 100%;">
      
      <div class="hero-title-wrap" style="text-align: left; flex: 1; min-width: 300px;">
        <h1 data-aos="fade-up" data-aos-delay="100" data-aos-duration="1000" style="margin: 0;">
          Expande tu<br><em>Marca y Franquicia</em> en<br><strong>Puntos Premium</strong>
        </h1>
      </div>

      <div class="hero-stats hero-stats-top" data-aos="fade-up" data-aos-delay="400" style="flex-shrink: 0;">
        <div class="hero-stat"><h3 id="stat-proyectos">0+</h3><p>Puntos Disponibles</p></div>
        <div class="hero-stat"><h3 id="stat-roi">0%</h3><p>Ventas Cruzadas</p></div>
        <div class="hero-stat"><h3 id="stat-dias">0</h3><p>Días de Montaje</p></div>
      </div>

    </div>

    <!-- BOTTOM ROW: TEXT/BUTTONS (LEFT) AND TICKER (RIGHT) -->
    <div class="hero-bottom-row" style="width: 92%; max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 40px; z-index: 3; width: 100%;">
      
      <div class="hero-content" style="align-items: flex-start; text-align: left; flex: 1; min-width: 300px;">
        <div class="hero-badge" data-aos="fade-up">
          <span></span> Participantes FANYF 2026 - Corferias
        </div>
        <p class="hero-sub" data-aos="fade-up" data-aos-delay="250" data-aos-duration="900" style="margin-left: 0; margin-right: auto;">
          Conectamos marcas, franquicias y emprendimientos con espacios de alta afluencia en estaciones de servicio de todo el país. Infraestructura liviana modular y gestión integral de contratos llave en mano con el respaldo estratégico de CABSAS.
        </p>
        <div class="hero-ctas" data-aos="fade-up" data-aos-delay="400" style="justify-content: flex-start;">
          <a href="#modulos" class="btn btn-green">
            Ver Portafolio
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
          <a href="#contacto" class="btn btn-ghost">Hablar con un Asesor</a>
        </div>
      </div>

      <div class="hero-brands-ticker-container" style="flex-shrink: 0;">
        <div class="hero-brands-ticker">
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
              <!-- Set 2 -->
              <img src="https://cabsas.co/wp-content/uploads/2025/11/terpel.png" alt="Terpel">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/zeuss.png" alt="Zeuss">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/puma.png" alt="Puma Energy">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/primax.png" alt="Primax">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/petromil.png" alt="Petromil">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/petrobras.png" alt="Petrobras">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/ecos.png" alt="Ecos">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/chevron.png" alt="Chevron">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/biomax.png" alt="Biomax">
              <!-- Set 3 -->
              <img src="https://cabsas.co/wp-content/uploads/2025/11/terpel.png" alt="Terpel">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/zeuss.png" alt="Zeuss">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/puma.png" alt="Puma Energy">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/primax.png" alt="Primax">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/petromil.png" alt="Petromil">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/petrobras.png" alt="Petrobras">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/ecos.png" alt="Ecos">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/chevron.png" alt="Chevron">
              <img src="https://cabsas.co/wp-content/uploads/2025/11/biomax.png" alt="Biomax">
              <!-- Set 4 -->
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
      </div>

    </div>

    <div class="hero-scroll">
      <div class="scroll-line"></div>
      Scroll
    </div>
  </section>
  
  """

html = html[:start_idx] + new_hero_content + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html rewritten successfully.")

# Now for CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .hero-stats and .hero-brands-ticker
old_stats = """
.hero-stats {
  position: relative; z-index: 3;
  display: flex; gap: 0; align-items: stretch;
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
  backdrop-filter: blur(12px);
  background: rgba(7,7,9,0.6);
  width: 100%; max-width: 620px;
}
.hero-stat {
  flex: 1; padding: 16px 20px; text-align: center;
  border-right: 1px solid var(--border);
}
.hero-stat:last-child { border-right: none; }
.hero-stat h3 { font-size: 1.8rem; font-weight: 900; color: var(--primary); text-shadow: 0 0 20px var(--primary-glow); line-height: 1; }
.hero-stat p { font-size: 0.68rem; text-transform: uppercase; letter-spacing: 1.5px; color: var(--text-muted); margin-top: 5px; }
"""

new_stats = """
.hero-stats {
  position: relative; z-index: 3;
  display: flex; gap: 0; align-items: stretch;
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  backdrop-filter: blur(12px);
  background: rgba(7,7,9,0.6);
  width: 100%; max-width: 480px;
}
.hero-stat {
  flex: 1; padding: 12px 14px; text-align: center;
  border-right: 1px solid var(--border);
}
.hero-stat:last-child { border-right: none; }
.hero-stat h3 { font-size: 1.3rem; font-weight: 900; color: var(--primary); text-shadow: 0 0 20px var(--primary-glow); line-height: 1; }
.hero-stat p { font-size: 0.55rem; text-transform: uppercase; letter-spacing: 1.5px; color: var(--text-muted); margin-top: 4px; }
"""

old_ticker = """
/* ========== HERO BRANDS TICKER ========== */
.hero-brands-ticker {
  position: absolute;
  bottom: 5px;
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
  gap: 90px;
  padding-left: 90px;
  animation: hero-brands-scroll 60s linear infinite;
  min-width: max-content;
}
@keyframes hero-brands-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.hero-brands-track img {
  height: 80px; /* Maximize logo size in the available space */
  object-fit: contain;
  flex-shrink: 0;
}
"""

new_ticker = """
/* ========== HERO BRANDS TICKER ========== */
.hero-brands-ticker-container {
  width: 100%; max-width: 650px;
  position: relative;
}
.hero-brands-ticker {
  position: relative;
  width: 100%;
  z-index: 10;
}
.hero-brands-track-container {
  overflow: hidden;
  width: 100%;
  display: flex;
  mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
}
.hero-brands-track {
  display: flex;
  align-items: center;
  gap: 60px;
  padding-left: 60px;
  animation: hero-brands-scroll 45s linear infinite;
  min-width: max-content;
}
@keyframes hero-brands-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.hero-brands-track img {
  height: 120px; /* Even BIGGER as requested, since it now occupies the KPI slot */
  object-fit: contain;
  flex-shrink: 0;
}
"""

if old_stats.strip() in css:
    css = css.replace(old_stats.strip(), new_stats.strip())
if old_ticker.strip() in css:
    css = css.replace(old_ticker.strip(), new_ticker.strip())

# Clean up unused .hero-wrapper class
old_wrapper_css = """
.hero-wrapper {
  position: relative; z-index: 3; width: 100%; max-width: 1500px;
  display: flex; align-items: flex-end; justify-content: center; flex-wrap: wrap; gap: 40px;
  padding: 0 20px;
}
"""
if old_wrapper_css.strip() in css:
    css = css.replace(old_wrapper_css.strip(), "/* Removed old hero-wrapper */")

# We need to add responsive CSS for the new layout
mobile_css = """
@media (max-width: 992px) {
  .hero-top-row { flex-direction: column; align-items: center !important; text-align: center; gap: 30px !important; }
  .hero-title-wrap { text-align: center !important; }
  .hero-bottom-row { flex-direction: column; align-items: center !important; text-align: center; gap: 40px !important; }
  .hero-content { text-align: center !important; align-items: center !important; }
  .hero-sub { margin: 0 auto 28px !important; }
  .hero-ctas { justify-content: center !important; }
  .hero-brands-track img { height: 80px !important; }
}
"""
css += mobile_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("style.css rewritten successfully.")
