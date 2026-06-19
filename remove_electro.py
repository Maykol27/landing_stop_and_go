import re
import os

def clean_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Meta description
    content = content.replace("para estaciones de servicio y electrolineras.", "para estaciones de servicio.")
    
    # Meta keywords
    content = content.replace("estaciones de servicio, electrolineras, inversión", "estaciones de servicio, inversión")

    # Hero and other mentions
    content = content.replace("estaciones de servicio y electrolineras de", "estaciones de servicio de")
    content = content.replace("estaciones de servicio y electrolineras aliadas", "estaciones de servicio aliadas")
    content = content.replace("estaciones de servicio, electrolineras y espacios", "estaciones de servicio y espacios")
    content = content.replace("Integración nativa con electrolineras y tecnología EV.", "Integración nativa con tecnología EV.")
    
    # Javascript array feature
    content = content.replace("'Electrolineras AC/DC de última generación', ", "")

    # Remove the whole card block
    card_regex = r"<!-- Electrolineras -->\s*<div class=\"canal-card card\" data-tilt>.*?</div>\s*</div>\s*"
    content = re.sub(card_regex, "", content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

clean_file('index.html')
clean_file('presentacion.html')
print("Done")
