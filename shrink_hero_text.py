import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_h1 = '''.hero h1 {
  font-size: clamp(1.8rem, 4vw, 3.2rem); font-weight: 900;
  text-transform: uppercase; margin-bottom: 16px; color: #fff;
}'''

new_h1 = '''.hero h1 {
  font-size: clamp(1.5rem, 3.2vw, 2.5rem); font-weight: 900; line-height: 1.1;
  text-transform: uppercase; margin-bottom: 12px; color: #fff;
}'''

if old_h1 in css:
    css = css.replace(old_h1, new_h1)
    print("Hero h1 desktop CSS updated.")
else:
    print("Could not find the exact old hero h1 text in CSS.")

old_h1_mobile = '.hero h1 { font-size: clamp(2rem, 8vw, 3rem); }'
new_h1_mobile = '.hero h1 { font-size: clamp(1.6rem, 7vw, 2.2rem); }'

if old_h1_mobile in css:
    css = css.replace(old_h1_mobile, new_h1_mobile)
    print("Hero h1 mobile CSS updated.")
else:
    print("Could not find mobile CSS.")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
