import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract H1 and put it before hero-wrapper
old_hero_content = '''    <div class="hero-wrapper">
      <div class="hero-content" style="align-items: flex-start; text-align: left;">
        <h1 data-aos="fade-up" data-aos-delay="100" data-aos-duration="1000">
          Expande tu<br><em>Marca y Franquicia</em> en<br><strong>Puntos Premium</strong>
        </h1>
        <div class="hero-badge" data-aos="fade-up">'''

new_hero_content = '''    <div class="hero-title-wrap" style="width: 92%; max-width: 1200px; margin: 0 auto; text-align: left; z-index: 2; width: 100%;">
      <h1 data-aos="fade-up" data-aos-delay="100" data-aos-duration="1000" style="margin-bottom: 0;">
        Expande tu<br><em>Marca y Franquicia</em> en<br><strong>Puntos Premium</strong>
      </h1>
    </div>
    <div class="hero-wrapper">
      <div class="hero-content" style="align-items: flex-start; text-align: left;">
        <div class="hero-badge" data-aos="fade-up">'''

html = html.replace(old_hero_content, new_hero_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 2. Update .hero CSS to be flex-column space-between
old_css = '''.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; align-items: flex-end; justify-content: center;
  text-align: center; overflow: hidden;
  padding: 100px 0  8vh;
}'''

new_css = '''.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; flex-direction: column; align-items: center; justify-content: space-between;
  text-align: center; overflow: hidden;
  padding: 140px 0 8vh;
}'''

css = css.replace(old_css, new_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Hero split successfully applied.")
