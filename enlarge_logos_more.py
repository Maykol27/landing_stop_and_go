import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_css = """
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

new_css = """
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

if old_css.strip() in css:
    css = css.replace(old_css.strip(), new_css.strip())
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css updated for even bigger logos.")
else:
    print("Could not find CSS to replace.")
