import re
import os

def replace_sikai(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = re.sub(r'\bSIKAI CX\b', 'SIKAI Consulting', content, flags=re.IGNORECASE)
    content = re.sub(r'\bDatos \(SIKAI\)', 'Datos (SIKAI Consulting)', content, flags=re.IGNORECASE)
    content = re.sub(r'<h3>SIKAI</h3>', '<h3>SIKAI Consulting</h3>', content, flags=re.IGNORECASE)
    content = re.sub(r'<h4>SIKAI CX</h4>', '<h4>SIKAI Consulting</h4>', content, flags=re.IGNORECASE)
    content = re.sub(r'alt="SIKAI Logo', 'alt="SIKAI Consulting Logo', content, flags=re.IGNORECASE)
    content = re.sub(r'alt="SIKAI"', 'alt="SIKAI Consulting"', content, flags=re.IGNORECASE)
    content = re.sub(r'>SIKAI<', '>SIKAI Consulting<', content, flags=re.IGNORECASE)
    content = re.sub(r'\bSIKAI GEOMARKETING SYSTEM\b', 'SIKAI Consulting GEOMARKETING SYSTEM', content, flags=re.IGNORECASE)
    
    # Generic SIKAI not followed by Consulting, and not part of a word/class
    content = re.sub(r'(?<![-_a-zA-Z0-9])SIKAI(?![-_a-zA-Z0-9]|\s*Consulting)', 'SIKAI Consulting', content)
    content = re.sub(r'(?<![-_a-zA-Z0-9])Sikai(?![-_a-zA-Z0-9]|\s*Consulting)', 'Sikai Consulting', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_sikai('index.html')
replace_sikai('presentacion.html')
print("Done")
