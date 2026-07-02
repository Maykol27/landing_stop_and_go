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

old_target = "    </div>\n  </section>\n\n  <!-- ===== ALIADOS ESTRATÉGICOS ===== -->"
if old_target in html:
    html = html.replace(old_target, "    </div>\n" + brands_html + "\n  <!-- ===== ALIADOS ESTRATÉGICOS ===== -->")
    print("Hero HTML updated.")
else:
    print("HTML replace target not found.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
