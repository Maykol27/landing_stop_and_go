import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_css = '''.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; flex-direction: column; align-items: center; justify-content: space-between;
  text-align: center; overflow: hidden;
  padding: 140px 0 8vh;
}'''

new_css = '''.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; flex-direction: column; align-items: center; justify-content: space-between;
  text-align: center; overflow: hidden;
  padding: 125px 0 8vh;
}'''

if old_css in css:
    css = css.replace(old_css, new_css)
    print("Hero CSS padding updated for desktop.")
else:
    print("Could not find the exact old hero text in CSS.")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Also let's check if h1 has margin-top
# In style.css, h1 by default might have a margin-top. Let's explicitly set margin-top: 0;
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<h1 data-aos="fade-up" data-aos-delay="100" data-aos-duration="1000" style="margin-bottom: 0;">',
    '<h1 data-aos="fade-up" data-aos-delay="100" data-aos-duration="1000" style="margin: 0;">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Hero h1 margin updated.")
