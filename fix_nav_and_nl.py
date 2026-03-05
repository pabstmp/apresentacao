import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove verbatim "\n" characters from previous script injections
    content = content.replace('\\n</head>', '\n</head>')
    content = content.replace('\\n</main>', '\n</main>')
    content = content.replace('\\n</body>', '\n</body>')
    # Also clean up any loose "\n" that got placed verbatim
    content = content.replace('    \\n\n', '')
    content = content.replace('  \\n\n', '')
    content = content.replace('\\n\n', '')

    # 2. Add "Evento" to the navigation links and update "Contato" -> LinkedIn URL
    # Look for the nav links div.
    # Typical: <a href="#ventures">Ventures</a><a href="#produtos">Produtos</a><a href="#consultoria">Consultoria</a><a href="#contato">Contato</a>
    
    if '<div class="nav-links">' in content:
        # We want to insert Evento before Contato, or after Produtos.
        # And replace Contato href with LinkedIn URL
        
        # PT
        if '>Produtos</a>' in content and '>Contato</a>' in content:
            content = content.replace('>Produtos</a>', '>Produtos</a><a href="#ai-innovation-challenge">Evento</a>')
            content = content.replace('<a href="#contato">Contato</a>', '<a href="https://www.linkedin.com/in/michelpabst/" target="_blank">Contato</a>')
        
        # EN (assuming Products / Contact are used or similar)
        elif '>Products</a>' in content and '>Contact</a>' in content:
            content = content.replace('>Products</a>', '>Products</a><a href="#ai-innovation-challenge">Event</a>')
            content = content.replace('<a href="#contact">Contact</a>', '<a href="https://www.linkedin.com/in/michelpabst/" target="_blank">Contact</a>')
            
        # ES (assuming Productos / Contacto are used or similar)
        elif '>Productos</a>' in content and '>Contacto</a>' in content:
            content = content.replace('>Productos</a>', '>Productos</a><a href="#ai-innovation-challenge">Evento</a>')
            content = content.replace('<a href="#contacto">Contacto</a>', '<a href="https://www.linkedin.com/in/michelpabst/" target="_blank">Contacto</a>')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Processed {f}")
