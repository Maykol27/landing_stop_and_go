with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I know it says: 
# .hero-brands-track img {
#   height: 120px; /* Even BIGGER as requested, since it now occupies the KPI slot */
#   object-fit: contain;
#   flex-shrink: 0;
# }

css = css.replace("height: 120px; /* Even BIGGER as requested", "height: 180px; /* Even BIGGER as requested")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Logo size increased.")
