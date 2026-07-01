import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove list items
html = re.sub(r'\s*<li><span class="icon">✗</span> Espacios vacíos y dependientes del combustible en las estaciones\.?</li>', '', html)
html = re.sub(r'\s*<li><span class="icon">✗</span> Falta de infraestructura liviana reubicable para probar ubicaciones\.?</li>', '', html)

# 2. Remove specific text
html = html.replace('(Autopista Norte, Carrera 30, Calle 26, Av. Boyacá).', '')

# 3. Increase CABSAS logo in index.html (the inline one)
html = html.replace('height: 18px;', 'height: 34px;')

# 4. Extract and move Aliados Estratégicos section
# Find the start of Aliados
start_aliados = html.find('<!-- ===== ALIADOS ESTRATÉGICOS ===== -->')
if start_aliados != -1:
    # Find the end of Aliados (start of CONTACTO)
    end_aliados = html.find('<!-- ===== CONTACTO ===== -->', start_aliados)
    if end_aliados != -1:
        aliados_section = html[start_aliados:end_aliados]
        # Remove from current position
        html = html[:start_aliados] + html[end_aliados:]
        
        # Insert after Hero
        insert_pos = html.find('<!-- ===== EL PROBLEMA & SOLUCIÓN ===== -->')
        if insert_pos != -1:
            html = html[:insert_pos] + aliados_section + html[insert_pos:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Now for style.css to emphasize CABSAS in the ticker
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.ticker-logo[alt="CABSAS"]' not in css:
    css += '\n/* Emphasize CABSAS logo in ticker */\n.ticker-logo[alt="CABSAS"] { transform: scale(1.4); opacity: 1; filter: brightness(1.2); }\n'

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Content changes applied successfully.")
