import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract the title wrap
title_pattern = r'(<div class="hero-title-wrap".*?</div>)'
title_match = re.search(title_pattern, html, re.DOTALL)
title_html = title_match.group(1)

# 2. Extract the stats
stats_pattern = r'(<div class="hero-stats".*?</div>\s*</div>)'
stats_match = re.search(stats_pattern, html, re.DOTALL)
stats_html = stats_match.group(1)

# 3. Extract the ticker
ticker_pattern = r'(<!-- Ticker Marcas -->.*?</div>\s*</div>\s*</div>)'
ticker_match = re.search(ticker_pattern, html, re.DOTALL)
ticker_html = ticker_match.group(1)

# Now, we need to create the new layout:
# Top row
top_row_html = f"""
    <div class="hero-top-row" style="width: 92%; max-width: 1280px; margin: 0 auto; display: flex; justify-content: space-between; align-items: flex-end; z-index: 2; flex-wrap: wrap; gap: 20px;">
      {title_html.replace('style="width: 92%; max-width: 1280px; margin: 0 auto; text-align: left; z-index: 2;"', 'style="text-align: left;"')}
      {stats_html}
    </div>
"""

# New wrapper with ticker inside
wrapper_start_pattern = r'(<div class="hero-wrapper">.*?<div class="hero-ctas"[^>]*>.*?</div>\s*</div>)'
wrapper_start_match = re.search(wrapper_start_pattern, html, re.DOTALL)
wrapper_content = wrapper_start_match.group(1)

new_wrapper_html = f"""
    {wrapper_content}
      {ticker_html}
    </div>
"""

# Remove old pieces
new_html = html.replace(title_html, '')
new_html = new_html.replace(stats_html, '')
new_html = new_html.replace(ticker_html, '')

# We also need to replace the old wrapper start because it was captured.
# Actually, it's better to just replace the whole hero section body.
start_marker = '<div class="hero-overlay-green"></div>'
end_marker = '<div class="hero-scroll">'

start_idx = html.find(start_marker) + len(start_marker)
end_idx = html.find(end_marker)

new_hero_body = f"""
{top_row_html}
    <div class="hero-wrapper" style="width: 92%; max-width: 1280px; margin: 0 auto; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 40px; padding: 0;">
{wrapper_content.replace('<div class="hero-wrapper">', '')}
{ticker_html}
    </div>
"""

# wait, wrapper_content already has <div class="hero-wrapper"> in it. 
# let's just use string replacement on the full html
html = html.replace(title_html, top_row_html)
html = html.replace(stats_html, '')
html = html.replace(ticker_html, '')

# now html has top_row_html where title was, no stats, no ticker.
# we just need to insert ticker into hero-wrapper
wrapper_end_pattern = r'(<div class="hero-ctas".*?</div>\s*</div>)'
wrapper_end_match = re.search(wrapper_end_pattern, html, re.DOTALL)
if wrapper_end_match:
    insert_point = html.find(wrapper_end_match.group(1)) + len(wrapper_end_match.group(1))
    html = html[:insert_point] + "\n" + ticker_html + html[insert_point:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html rewritten successfully.")

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update CSS for hero-stats and hero-brands-ticker
old_stats = """
.hero-stats {
  position: relative; z-index: 3;
  display: flex; gap: 0; align-items: stretch;
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
  backdrop-filter: blur(12px);
  background: rgba(7,7,9,0.6);
  width: 100%; max-width: 620px;
}
.hero-stat {
  flex: 1; padding: 16px 20px; text-align: center;
  border-right: 1px solid var(--border);
}
.hero-stat:last-child { border-right: none; }
.hero-stat h3 { font-size: 1.8rem; font-weight: 900; color: var(--primary); text-shadow: 0 0 20px var(--primary-glow); line-height: 1; }
.hero-stat p { font-size: 0.68rem; text-transform: uppercase; letter-spacing: 1.5px; color: var(--text-muted); margin-top: 5px; }
"""

new_stats = """
.hero-stats {
  position: relative; z-index: 3;
  display: flex; gap: 0; align-items: stretch;
  border: 1px solid var(--border);
  border-radius: 16px; /* smaller */
  overflow: hidden;
  backdrop-filter: blur(12px);
  background: rgba(7,7,9,0.6);
  width: 100%; max-width: 480px; /* smaller */
}
.hero-stat {
  flex: 1; padding: 12px 14px; text-align: center; /* smaller */
  border-right: 1px solid var(--border);
}
.hero-stat:last-child { border-right: none; }
.hero-stat h3 { font-size: 1.4rem; font-weight: 900; color: var(--primary); text-shadow: 0 0 20px var(--primary-glow); line-height: 1; }
.hero-stat p { font-size: 0.58rem; text-transform: uppercase; letter-spacing: 1.5px; color: var(--text-muted); margin-top: 4px; }
"""

old_ticker = """
/* ========== HERO BRANDS TICKER ========== */
.hero-brands-ticker {
  position: absolute;
  bottom: 5px;
  left: 0;
  width: 100%;
  z-index: 10;
}
.hero-brands-track-container {
  overflow: hidden;
  width: 100%;
  display: flex;
}
.hero-brands-track {
  display: flex;
  align-items: center;
  gap: 90px;
  padding-left: 90px;
  animation: hero-brands-scroll 60s linear infinite;
  min-width: max-content;
}
@keyframes hero-brands-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.hero-brands-track img {
  height: 80px; /* Maximize logo size in the available space */
  object-fit: contain;
  flex-shrink: 0;
}
"""

new_ticker = """
/* ========== HERO BRANDS TICKER ========== */
.hero-brands-ticker {
  position: relative;
  width: 100%;
  max-width: 650px;
  z-index: 10;
  margin-bottom: -15px; /* Pull it slightly down if needed */
}
.hero-brands-track-container {
  overflow: hidden;
  width: 100%;
  display: flex;
  mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
}
.hero-brands-track {
  display: flex;
  align-items: center;
  gap: 80px;
  padding-left: 80px;
  animation: hero-brands-scroll 50s linear infinite;
  min-width: max-content;
}
@keyframes hero-brands-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.hero-brands-track img {
  height: 100px; /* Even bigger as requested */
  object-fit: contain;
  flex-shrink: 0;
}
"""

css = css.replace(old_stats.strip(), new_stats.strip())
css = css.replace(old_ticker.strip(), new_ticker.strip())

# Make .hero-wrapper flex space-between
old_hero_wrapper = """
.hero-wrapper {
  position: relative; z-index: 3; width: 100%; max-width: 1500px;
  display: flex; align-items: flex-end; justify-content: center; flex-wrap: wrap; gap: 40px;
  padding: 0 20px;
}
"""

new_hero_wrapper = """
.hero-wrapper {
  position: relative; z-index: 3; width: 92%; max-width: 1280px; margin: 0 auto;
  display: flex; align-items: flex-end; justify-content: space-between; flex-wrap: wrap; gap: 40px;
  padding: 0;
}
"""
if old_hero_wrapper.strip() in css:
    css = css.replace(old_hero_wrapper.strip(), new_hero_wrapper.strip())

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("style.css rewritten successfully.")
