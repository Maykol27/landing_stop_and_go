import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_hero = '''.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; align-items: flex-end; justify-content: center;
  text-align: center; overflow: hidden;
  padding: 100px 0  8vh;
}'''

new_hero = '''.hero {
  position: relative; height: 100vh; min-height: 640px;
  display: flex; align-items: flex-start; justify-content: center;
  text-align: center; overflow: hidden;
  padding: 200px 0 8vh;
}'''

if old_hero in css:
    css = css.replace(old_hero, new_hero)
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Hero CSS updated for desktop.")
else:
    print("Could not find the exact old hero text in CSS.")
