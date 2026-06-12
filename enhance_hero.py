import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Enhance the Hero Section
# Let's make the background grid more visible and add a nice gradient to the text
c = c.replace(
    'linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%)',
    'radial-gradient(circle at 50% -20%, #ffffff 0%, #f1f5f9 60%, #e2e8f0 100%)'
)

# Make the hero name a beautiful gradient instead of plain dark text
c = c.replace(
    'color: var(--white);',
    'color: var(--white);\n      text-shadow: 0 10px 30px rgba(37, 99, 235, 0.1);'
)

# Make the "Creative Developer" text pop more
hero_name_css = '''    .hero-name {
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(4rem, 12vw, 10rem);
      font-weight: 600;
      background: linear-gradient(135deg, #0f172a 0%, #3b82f6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1.1;
      letter-spacing: 0.02em;
      animation: fadeInScale 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.4s both;
      position: relative;
    }'''

# Replace the old hero-name CSS
c = re.sub(r'\.hero-name\s*\{[^}]*\}', hero_name_css, c, count=1)

# Remove the span gradient since the whole name is now a gradient
c = re.sub(r'\.hero-name span\s*\{[^}]*\}', '.hero-name span { color: inherit; }', c, count=1)

# Enhance the grid to be slightly more visible in light mode
c = c.replace(
    'rgba(59, 130, 246, 0.04)',
    'rgba(37, 99, 235, 0.08)'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
