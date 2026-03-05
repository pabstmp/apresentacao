import glob
import re

html_files = glob.glob('*.html')

# Regex to extract the ai-innovation-challenge section
# We use re.DOTALL to let '.' match newlines
carousel_pattern = re.compile(r'(\n?\s*<section id="ai-innovation-challenge".*?</section>)', re.DOTALL)
produtos_pattern = re.compile(r'(<section id="produtos">.*?</section>)', re.DOTALL)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Extract the carousel section
    carousel_match = carousel_pattern.search(content)
    if not carousel_match:
        print(f"Skipping {f}, carousel not found.")
        continue
    
    carousel_html = carousel_match.group(1)
    
    # Remove it from its current position
    content = content.replace(carousel_html, '')
    
    # Trim leading/trailing newlines for clean insertion
    carousel_html = carousel_html.strip()
    
    # 2. Text Replacements inside the carousel HTML
    # Portuguese text
    carousel_html = carousel_html.replace(
        'dos produtos do Google (Gemini, Google Stitch, AI Studio) e Antigravity para',
        'dos produtos do Google para'
    )
    carousel_html = carousel_html.replace('>Evento Destacado<', '>Evento<')
    
    # English text
    carousel_html = carousel_html.replace(
        'of Google products (Gemini, Google Stitch, AI Studio) and Antigravity to',
        'of Google products to'
    )
    carousel_html = carousel_html.replace('>Featured Event<', '>Event<')
    
    # Spanish text
    carousel_html = carousel_html.replace(
        'de los productos de Google (Gemini, Google Stitch, AI Studio) y Antigravity para',
        'de los productos de Google para'
    )
    carousel_html = carousel_html.replace('>Evento Destacado<', '>Evento<')

    # Formatting wrapper for insertion
    carousel_html_to_insert = '\n\n' + carousel_html + '\n'

    # 3. Find produtos section and append the carousel right after it
    if produtos_pattern.search(content):
        content = produtos_pattern.sub(r'\1' + carousel_html_to_insert, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated and moved in {f}")
    else:
        print(f"produtos section not found in {f}, appending to bottom instead.")
        # If no #produtos section, put it before </main> or </body>
        if '</main>' in content:
            content = content.replace('</main>', carousel_html_to_insert + '\n</main>')
        elif '</body>' in content:
            content = content.replace('</body>', carousel_html_to_insert + '\n</body>')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
