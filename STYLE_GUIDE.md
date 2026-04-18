# STYLE_GUIDE — CV Michel Pabst (tema zeroaodeploy escuro)

Guia de design do currículo. O alvo é o tema escuro do **zeroaodeploy.com**: fundo grafite, texto branco, três accents neon (roxo, ciano, pink).

Os arquivos canônicos são `index.html` (PT), `index_en.html` (EN) e `index_es.html` (ES). Qualquer mudança visual **deve ser replicada nos três**.

---

## 1. Paleta de cores

Todas as cores são expostas como variáveis CSS em `:root` (topo de cada `index*.html`). **Nunca** hardcodar hex no corpo do CSS — use as variáveis.

### Superfícies

| Variável | Hex | Uso |
|---|---|---|
| `--bg` | `#0e0e0e` | Background principal da página |
| `--surface` | `#1a1a1a` | Cards, header pill, inputs |
| `--surface-2` | `#1e1e24` | Superfícies elevadas, hover de cards |
| `--border` | `#333333` | Bordas sutis, divisores |

### Texto

| Variável | Hex | Uso |
|---|---|---|
| `--text` | `#ffffff` | Texto principal, títulos |
| `--muted` | `#a1a1aa` | Labels, captions, texto secundário |

### Accents (somente 3 — manter disciplina)

| Variável | Hex | Semântica |
|---|---|---|
| `--accent-purple` | `#e08efe` | Cor primária — CTAs, stats, highlights |
| `--accent-cyan` | `#81ecff` | Secundária — tags de seção, links |
| `--accent-pink` | `#f472b6` | Seleção de texto, badges pontuais |

**Regra**: um bloco visual não deve usar os 3 accents ao mesmo tempo. Escolha 1 predominante por seção.

---

## 2. Tipografia

Carregadas via Google Fonts em `<head>`:

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### Fontes

| Variável | Família | Uso |
|---|---|---|
| `--font-display` | Space Grotesk | Títulos (h1, h2, h3), números de impacto |
| `--font-body` | Inter | Corpo de texto, parágrafos, labels, botões |

### Escala

| Elemento | Tamanho | Weight | Notas |
|---|---|---|---|
| h1 | `clamp(40px, 5vw, 64px)` | 700 | `letter-spacing: -0.02em`, `line-height: 1.1` |
| h2 | `clamp(32px, 4vw, 48px)` | 700 | `letter-spacing: -0.02em` |
| h3 | 22px (padrão) | 600 | `letter-spacing: -0.01em` |
| Body | 16px | 400 | `line-height: 1.7` |
| Section tag | 12-13px | 700 | `text-transform: uppercase`, `letter-spacing: 2px` |
| Stat value | 24-36px | 700 | display font |

**Regra**: nunca carregar uma terceira família de fonte. Se precisar de destaque, use peso + accent color, não outra fonte.

---

## 3. Ícones

O CV é HTML estático — **não** adotar Font Awesome, Lucide, Material Icons. Usar:

1. **Emojis Unicode** — permitidos apenas em:
   - Badges de status (`✓ EXIT`, `🚀 LANÇAMENTO`)
   - Início de bullets curtos em CTAs
   - Avatar/seção de contato pontual (`🌎`)
2. **Setas Unicode** — sempre `→` (U+2192). Nunca `>`, `»`, `&gt;`.
3. **SVG inline** — somente bandeiras do seletor de idioma e controles do carousel (`&#10094;` `&#10095;`).

**Regra**: um emoji por contexto. Evitar linhas como `🚀 ✨ 💰 AI Products` — poluição visual.

---

## 4. Componentes-chave

Referências por linha em `index.html` (pós-refator):

| Componente | CSS (linha aprox.) | HTML (linha aprox.) |
|---|---|---|
| `.portrait-organic` + `.portrait-blob` | 230-250 | 848 |
| `.stat-pill` | 260-280 | 844 |
| `.section-header` | 288 | várias |
| `.header-pill` (nav flutuante) | buscar `.header-pill` | topo da página |
| `.wave-divider` | buscar `wave-divider` | entre seções |
| `.cta-section` | buscar `.cta-section` | seção "Treinamento" |

### Foto de perfil

- Arquivo: `michel_circle_v2.png` (fundo transparente, formato circular).
- **Nunca** aplicar `mask-image` ou `clip-path` à `<img>` — o frame/borda é controlado pelo container `.portrait-organic`.
- Estilo atual: `border-radius: 50%`, `border: 6px solid var(--surface)`, `box-shadow` sutil.

### Blob animado atrás da foto

`.portrait-blob` usa gradiente entre os dois primeiros accents (roxo → ciano) e animação `morph` de 10s. Para trocar a paleta do blob, ajustar apenas a gradient; não mexer na animação.

---

## 5. Multi-idioma

- `index.html` = pt-BR | `index_en.html` = English | `index_es.html` = Español.
- Mesma estrutura HTML, mesmas classes, mesmas variáveis CSS.
- Seletor de bandeiras está em cada arquivo (SVGs inline).
- **Antes de commitar**, rodar:
  ```bash
  diff <(grep -c 'var(--' index.html) <(grep -c 'var(--' index_en.html)
  ```
  para sanity-check de paridade de variáveis.

---

## 6. Não-objetivos (o que evitar)

- Tailwind, Bootstrap ou qualquer framework CSS — CSS artesanal no `<style>` de cada HTML.
- React / Vue / build step — o CV é servido direto pelo GitHub Pages.
- Font Awesome / bibliotecas de ícone — custo de HTTP não justifica para um CV de 1 página.
- Dark/light toggle — tema é exclusivamente escuro.
- Mais de 3 accent colors.

Para a landing `zeroaodeploy.html` (curso) as regras são **outras** — ela é um app React/Vite separado com Space Grotesk + Inter e tem seu próprio build.

---

## 7. Workflow de mudanças

1. Editar `index.html`, depois replicar em `index_en.html` e `index_es.html`.
2. Testar em viewport desktop (1440px) e mobile (375px).
3. Rodar: `grep -rn "var(--green\|var(--teal\|var(--sage\|var(--cream\|Nunito\|mask-image" index*.html` — deve retornar vazio.
4. Commit com mensagem descritiva.
