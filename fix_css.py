import glob

old_css = """.carousel-slide img {
    width: 100%;
    height: auto;
    display: block;
    aspect-ratio: 16/9;
    object-fit: cover;
}"""

# New CSS: 
# Let's make the container have a fixed max height and use contain so nothing cuts.
new_css = """.carousel-slide {
    min-width: 100%;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #0f172a; /* Nice dark background for the letterboxing */
}
.carousel-slide img {
    width: 100%;
    height: 700px;
    max-height: 75vh;
    display: block;
    object-fit: contain;
}"""

old_slide_css = """.carousel-slide {
    min-width: 100%;
    box-sizing: border-box;
}"""

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if old_css in content:
        # First remove the old .carousel-slide block so we don't have duplicates
        content = content.replace(old_slide_css, '')
        
        # Then replace the img block with our combined block
        content = content.replace(old_css, new_css)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated CSS in {f}")
    else:
        print(f"CSS block not found in {f}")
