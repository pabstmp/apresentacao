import glob
import os

old_block = """            <div class="carousel-track">
                <div class="carousel-slide"><img src="28.01-12.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
                <div class="carousel-slide"><img src="28.01-14.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
                <div class="carousel-slide"><img src="28.01-15.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
                <div class="carousel-slide"><img src="28.01-16.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
                <div class="carousel-slide"><img src="28.01-24.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
                <div class="carousel-slide"><img src="28.01-25.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
                <div class="carousel-slide"><img src="28.01-27.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
            </div>
            <div class="carousel-indicators">
                <div class="carousel-dot active" data-index="0"></div>
                <div class="carousel-dot" data-index="1"></div>
                <div class="carousel-dot" data-index="2"></div>
                <div class="carousel-dot" data-index="3"></div>
                <div class="carousel-dot" data-index="4"></div>
                <div class="carousel-dot" data-index="5"></div>
                <div class="carousel-dot" data-index="6"></div>
            </div>"""

new_block = """            <div class="carousel-track">
                <div class="carousel-slide"><img src="28.01-12-1.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
                <div class="carousel-slide"><img src="28.01-15-1.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
                <div class="carousel-slide"><img src="28.01-16-1.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
                <div class="carousel-slide"><img src="28.01-27-1.jpg" alt="AI Innovation Challenge" loading="lazy"></div>
            </div>
            <div class="carousel-indicators">
                <div class="carousel-dot active" data-index="0"></div>
                <div class="carousel-dot" data-index="1"></div>
                <div class="carousel-dot" data-index="2"></div>
                <div class="carousel-dot" data-index="3"></div>
            </div>"""

html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Try direct replacement first
    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        # If indentation varied, try regex
        import re
        pattern = re.compile(r'<div class="carousel-track">\s*<div class="carousel-slide"><img src="28\.01-12\.jpg".*?</div>\s*</div>', re.DOTALL)
        if pattern.search(content):
            print(f"Skipping {f}, found with regex but indentation mismatch")
        else:
            print(f"Skipping {f}, old block not found at all")
