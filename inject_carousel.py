import os
import glob
import re

html_files = glob.glob('*.html')

carousel_css = """
<style>
/* Carrossel de Imagens - Evento AI */
.carousel-section {
    padding: 100px 0;
    background: var(--surface, #fff);
    position: relative;
    z-index: 1;
}
.carousel-container {
    max-width: 900px;
    margin: 0 auto;
    position: relative;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 12px 40px rgba(0,0,0,0.15);
}
.carousel-track {
    display: flex;
    transition: transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
}
.carousel-slide {
    min-width: 100%;
    box-sizing: border-box;
}
.carousel-slide img {
    width: 100%;
    height: auto;
    display: block;
    aspect-ratio: 16/9;
    object-fit: cover;
}
.carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(4px);
    border: none;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #333;
    z-index: 10;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.carousel-btn:hover {
    background: #fff;
    transform: translateY(-50%) scale(1.1);
}
.carousel-prev { left: 20px; }
.carousel-next { right: 20px; }
.carousel-indicators {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 10px;
    z-index: 10;
}
.carousel-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.4);
    cursor: pointer;
    transition: all 0.3s ease;
}
.carousel-dot.active {
    background: #fff;
    transform: scale(1.3);
}
.event-info {
    text-align: center;
    max-width: 800px;
    margin: 0 auto 48px auto;
    padding: 0 24px;
}
.event-info h2 {
    font-size: clamp(32px, 4vw, 48px);
    margin-bottom: 20px;
    font-weight: 800;
}
.event-info p {
    font-size: 18px;
    color: var(--muted, #555);
    line-height: 1.6;
}
.event-tags {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 28px;
    flex-wrap: wrap;
}
.event-tag {
    background: var(--surface, #fff);
    color: var(--text, #1e3a2f);
    padding: 8px 18px;
    border-radius: 100px;
    font-size: 14px;
    font-weight: 700;
    border: 1px solid var(--border, #d8e2dc);
    transition: all 0.3s;
}
.event-tag:hover {
    border-color: var(--green, #2d6a4f);
    color: var(--green, #2d6a4f);
}
</style>
"""

texts = {
    'pt': {
        'tag': 'Evento Destacado',
        'title': 'AI Innovation Challenge',
        'desc': 'Um evento focado na abordagem <strong>AI First</strong>, explorando o potencial dos produtos do Google (Gemini, Google Stitch, AI Studio) e Antigravity para resolver problemas reais e acelerar a inovação.'
    },
    'en': {
        'tag': 'Featured Event',
        'title': 'AI Innovation Challenge',
        'desc': 'An event focused on the <strong>AI First</strong> approach, exploring the potential of Google products (Gemini, Google Stitch, AI Studio) and Antigravity to solve real problems and accelerate innovation.'
    },
    'es': {
        'tag': 'Evento Destacado',
        'title': 'AI Innovation Challenge',
        'desc': 'Un evento enfocado en el enfoque <strong>AI First</strong>, explorando el potencial de los productos de Google (Gemini, Google Stitch, AI Studio) y Antigravity para resolver problemas reales y acelerar la innovación.'
    }
}

html_template = """
<section id="ai-innovation-challenge" class="carousel-section">
    <div class="container">
        <div class="event-info">
            <div class="section-tag" style="text-align:center; color: var(--teal, #40916c); font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; font-size: 13px;">{tag}</div>
            <h2>{title}</h2>
            <p>{desc}</p>
            <div class="event-tags">
                <span class="event-tag">AI First</span>
                <span class="event-tag">Gemini</span>
                <span class="event-tag">Google Stitch</span>
                <span class="event-tag">AI Studio</span>
                <span class="event-tag">Antigravity</span>
            </div>
        </div>
        <div class="carousel-container" id="event-carousel">
            <button class="carousel-btn carousel-prev" aria-label="Previous">&#10094;</button>
            <button class="carousel-btn carousel-next" aria-label="Next">&#10095;</button>
            <div class="carousel-track">
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
            </div>
        </div>
    </div>
</section>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // We scope this to the specific carousel
    const carouselEl = document.getElementById('event-carousel');
    if (!carouselEl) return;
    
    // Check if the script has already been initialized to avoid multiple bindings
    if (carouselEl.dataset.initialized) return;
    carouselEl.dataset.initialized = 'true';

    const track = carouselEl.querySelector('.carousel-track');
    const slides = Array.from(track.children);
    const nextButton = carouselEl.querySelector('.carousel-next');
    const prevButton = carouselEl.querySelector('.carousel-prev');
    const dotsNav = carouselEl.querySelector('.carousel-indicators');
    const dots = Array.from(dotsNav.children);

    let currentIndex = 0;

    const updateCarousel = (index) => {
        track.style.transform = 'translateX(-' + index * 100 + '%)';
        dots.forEach(dot => dot.classList.remove('active'));
        if(dots[index]) dots[index].classList.add('active');
    };

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex === slides.length - 1) ? 0 : currentIndex + 1;
        updateCarousel(currentIndex);
    });

    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex === 0) ? slides.length - 1 : currentIndex - 1;
        updateCarousel(currentIndex);
    });

    dotsNav.addEventListener('click', e => {
        const targetDot = e.target.closest('.carousel-dot');
        if (!targetDot) return;
        const targetIndex = dots.findIndex(dot => dot === targetDot);
        if(targetIndex !== -1) {
            currentIndex = targetIndex;
            updateCarousel(currentIndex);
        }
    });
    
    // Auto-advance
    setInterval(() => {
        currentIndex = (currentIndex === slides.length - 1) ? 0 : currentIndex + 1;
        updateCarousel(currentIndex);
    }, 5000);
});
</script>
"""

for f in html_files:
    if f.endswith('_en.html'):
        lang = 'en'
    elif f.endswith('_es.html'):
        lang = 'es'
    else:
        lang = 'pt'
        
    content = texts[lang]
    html_block = html_template.replace('{tag}', content['tag']).replace('{title}', content['title']).replace('{desc}', content['desc'])
    
    with open(f, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    if 'id="ai-innovation-challenge"' in file_content:
        print(f"Skipping {f}, already injected.")
        continue
    
    if '</head>' in file_content:
        file_content = file_content.replace('</head>', carousel_css + '\\n</head>')
    
    if '</main>' in file_content:
        injection = '\\n' + html_block + '\\n</main>'
        file_content = file_content.replace('</main>', injection)
    elif '</body>' in file_content:
        file_content = file_content.replace('</body>', html_block + '\\n</body>')
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(file_content)
        
    print(f"Injected into {f}")

