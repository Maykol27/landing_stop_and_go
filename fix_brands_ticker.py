import re

# Fix index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the title
html = html.replace('<p class="hero-brands-title">Distribuidores líderes del sector confían en nuestras soluciones</p>\n      ', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html updated.")

# Fix style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Revert hero padding
css = css.replace(
    'padding: 125px 0 calc(8vh + 110px);',
    'padding: 125px 0 8vh;'
)

# Update ticker styles
old_ticker_css = """
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

new_ticker_css = """
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

css = css.replace(old_ticker_css.strip(), new_ticker_css.strip())

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("style.css updated.")
