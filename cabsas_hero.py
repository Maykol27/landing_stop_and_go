import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_badge = '''        <div class="hero-badge" data-aos="fade-up">
          <span></span> Participantes FANYF 2026 - Corferias
        </div>'''

new_badges = '''        <div style="display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 28px;">
          <div class="hero-badge" data-aos="fade-up" style="margin-bottom: 0;">
            <span></span> Participantes FANYF 2026 - Corferias
          </div>
          <div class="hero-badge" data-aos="fade-up" data-aos-delay="100" style="margin-bottom: 0; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.2); color: #fff;">
            <span style="background: #fff; animation: none;"></span> Respaldo Integral <img src="./assets/cab-logo.png" alt="CABSAS" style="height: 24px; margin-left: 4px; filter: brightness(1.3);">
          </div>
        </div>'''

if old_badge in html:
    html = html.replace(old_badge, new_badges)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced badges successfully.")
else:
    print("Could not find the exact old badge text.")

