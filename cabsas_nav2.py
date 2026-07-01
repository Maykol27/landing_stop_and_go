with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_nav = """    <div class="nav-wrap">
      <a href="#hero" class="nav-logo" aria-label="STOP &amp; GO Station Inicio">
        <img src="./assets/logostop_go.png" alt="STOP &amp; GO Station Logo"/>
      </a>
      <button class="hamburger" id="hamburger" aria-label="Abrir menú" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav-links" id="nav-links" aria-label="Navegación principal">
        <a href="#solucion">Solución</a>
        <a href="#modulos">Portafolio</a>
        <a href="#galeria">Galería</a>
        <a href="#quienes-somos">Compañía</a>
        <a href="#aliados">Aliados</a>
        <a href="#contacto" class="nav-cta">Contacto</a>
        <button id="theme-toggle" aria-label="Cambiar modo claro/oscuro">🌙</button>
      </nav>
    </div>"""

new_nav = """    <div class="nav-wrap">
      <a href="#hero" class="nav-logo" aria-label="STOP &amp; GO Station Inicio">
        <img src="./assets/logostop_go.png" alt="STOP &amp; GO Station Logo"/>
      </a>
      <nav class="nav-links" id="nav-links" aria-label="Navegación principal">
        <a href="#solucion">Solución</a>
        <a href="#modulos">Portafolio</a>
        <a href="#galeria">Galería</a>
        <a href="#quienes-somos">Compañía</a>
        <a href="#aliados">Aliados</a>
        <a href="#contacto" class="nav-cta">Contacto</a>
        <button id="theme-toggle" aria-label="Cambiar modo claro/oscuro">🌙</button>
      </nav>
      <div style="display: flex; align-items: center; gap: 16px;">
        <a href="#aliados" class="nav-cabsas" style="display: flex; align-items: center; gap: 6px; text-decoration: none; padding-right: 12px; border-right: 1px solid rgba(255,255,255,0.1);">
          <span style="font-size: 0.65rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">By</span>
          <img src="./assets/cab-logo.png" alt="CABSAS" class="cabsas-nav-img" style="height: 28px; filter: brightness(1.2);">
        </a>
        <button class="hamburger" id="hamburger" aria-label="Abrir menú" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>"""

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced nav successfully.")
else:
    print("Nav not found.")
