# 12 posts prontos para publicar — Zero ao Deploy

Cada post está pronto para copiar e colar no LinkedIn. Os campos `[ajustar]` são pontos onde vale uma checagem rápida com a sua memória/realidade antes de publicar — números, nomes, datas. Mantenha a verdade da história, só troque o detalhe.

Cadência: **segunda, quarta, sexta** — preferência por 8h ou 12h (horário de almoço tem ótimo desempenho).

---

## SEMANA 1

### 🟦 Segunda — Bastidores
**Tema:** A pasta de projetos não terminados

> Tenho uma pasta no computador chamada `projetos`.
>
> Dentro dela, [ajustar: ~14] subpastas.
>
> Nenhuma delas está no ar.
>
> Cada uma representa um fim de semana animado, um curso que comprei, uma ideia que ia mudar tudo.
>
> Aplicativo de finanças. Clone do Instagram. Bot do Telegram. Site da empresa do meu primo.
>
> Todas paradas no mesmo lugar: localhost:3000.
>
> O que ninguém me contou quando eu comecei é que o problema nunca foi aprender a programar.
>
> O problema era terminar.
>
> Terminar significa: colocar no ar, mandar o link, ver alguém usar.
>
> E terminar dá um tipo específico de medo que nenhum tutorial resolve — porque o tutorial sempre acaba antes do deploy.
>
> Hoje eu olho pra essa pasta com carinho. Foi ela que me fez perceber o que eu precisava ensinar.
>
> Pergunta sincera: quantos projetos parados você tem aí?
>
> #desenvolvimento #carreiratech #devjr

---

### 🟩 Quarta — Insight da trincheira
**Tema:** Rodou no meu computador

> "Mas no meu computador funciona."
>
> Eu já falei essa frase. Você provavelmente já falou também.
>
> Da primeira vez que ouvi um sênior responder, ele só sorriu e disse:
>
> "Legal. E o usuário vai usar o seu computador?"
>
> Foi a melhor aula de deploy da minha vida e ela durou 12 segundos.
>
> A diferença entre rodar local e rodar em produção é uma fronteira invisível que separa quem aprende a programar de quem entrega software.
>
> Local você controla tudo: a versão do Node, as variáveis, o banco, a porta, o cache do navegador.
>
> Produção é o oposto: nada está como você deixou.
>
> Por isso o primeiro deploy é tão dolorido. Não é que o seu código está errado — é que o seu código nunca foi testado fora da sua bolha.
>
> A boa notícia: depois do primeiro, fica muito mais fácil. Você passa a programar pensando no ambiente onde aquilo vai rodar.
>
> Qual foi a primeira vez que o "rodou aqui" te traiu?
>
> #deploy #devops #programacao

---

### 🟥 Sexta — Manifesto
**Tema:** Deploy é coragem, não conhecimento

> Vou falar uma coisa que vai incomodar muita gente.
>
> A maioria dos devs juniores que eu conheço **sabe** fazer deploy.
>
> Eles assistiram aula. Leram artigo. Salvaram tutorial. Já fizeram passo a passo na máquina local.
>
> O que falta não é conhecimento. É coragem.
>
> Porque colocar um projeto no ar significa:
>
> — Alguém pode acessar e ver que tem bug.
> — Alguém pode comentar que tá feio.
> — Alguém pode dizer que já existe melhor.
>
> Deploy é a primeira vez que o seu código sai do quarto e entra no mundo.
>
> E o mundo, diferente do localhost, não devolve `200 OK` pra tudo.
>
> Por isso a maior parte das pessoas que aprendem a programar nunca termina nada. Não é técnica — é emocional.
>
> Termine alguma coisa essa semana. Mesmo feio. Mesmo simples. Mesmo só pra você.
>
> Você não precisa do próximo curso. Você precisa de um link funcionando.
>
> P.S. — é exatamente isso que eu trabalho com quem entra no Zero ao Deploy. Não é um curso de tecnologia. É um curso de terminar. (zeroaodeploy.com)
>
> #carreiratech #programacao #softwareengineer

---

## SEMANA 2

### 🟦 Segunda — Bastidores
**Tema:** A conta de AWS que esqueci ligada

> Acordei num sábado de manhã com um e-mail da AWS.
>
> "Your bill is now $[ajustar: 87.42]."
>
> Eu tinha [ajustar: 19] anos e nenhum dólar na conta.
>
> Na noite anterior eu tinha subido uma instância EC2 pra testar uma coisa qualquer. Funcionou. Fechei o navegador. Fui dormir.
>
> A instância não fechou junto.
>
> Passei o sábado inteiro tentando entender como desligar aquilo, em inglês, com a barriga embrulhada, lendo documentação que parecia escrita pra outro planeta.
>
> No fim do dia, consegui. Mas o estrago já estava feito.
>
> Pode rir, mas foi a melhor aula de cloud que eu tive.
>
> Aprendi naquele dia três coisas que nenhum curso tinha me ensinado:
>
> 1. Recurso na nuvem custa enquanto está ligado, não enquanto está sendo usado.
> 2. Sempre tenha alerta de billing antes de ter o serviço.
> 3. O medo de errar é menor depois que você erra a primeira vez.
>
> Hoje, quando alguém me pergunta se "pode quebrar alguma coisa testando", eu lembro daquele sábado e respondo: pode. E é melhor que aconteça com você sabendo, do que com o seu cliente.
>
> Qual foi a sua conta surpresa?
>
> #aws #cloud #devops

---

### 🟩 Quarta — Insight da trincheira
**Tema:** O .env que foi parar no GitHub

> Um colega meu já fez isso. Eu já fiz isso. Você, leitor que está negando agora, provavelmente também já fez.
>
> Subir o `.env` no GitHub.
>
> Com chave de API real. Em repositório público.
>
> O detalhe: bots varrem o GitHub em tempo real procurando exatamente isso.
>
> Da última vez que vi acontecer, em menos de [ajustar: 11] minutos a chave já tinha sido usada pra rodar mineração de cripto.
>
> Tem três coisas que eu peço pra qualquer pessoa que está começando a colocar projeto no ar fazer **antes** do primeiro deploy:
>
> 1. Criar o `.gitignore` na hora que cria o repositório, não depois. Adicionar `.env` antes de qualquer commit.
> 2. Usar `.env.example` com as **chaves** das variáveis, sem os valores, pra documentar.
> 3. Rotacionar qualquer chave que tenha sido commitada uma vez. Apagar do histórico do git não basta — ela já foi indexada.
>
> Parece básico. É básico. Mas é o tipo de básico que ninguém ensina porque o tutorial assume que você já sabe.
>
> A maior parte do que você precisa pra colocar um projeto em produção não é técnica avançada. É uma lista de "não pise aqui" que ninguém escreveu pra você ainda.
>
> Que erro de iniciante você ainda lembra com vergonha?
>
> #seguranca #git #devops

---

### 🟥 Sexta — Manifesto
**Tema:** Quem nunca colocou nada no ar ainda não aprendeu

> Vou ser direto.
>
> Você pode ter feito 12 cursos.
>
> Pode ter o certificado pendurado no LinkedIn.
>
> Pode ter terminado a trilha completa de full-stack.
>
> Se você nunca colocou um projeto no ar e mandou o link pra alguém usar, você ainda não aprendeu a programar.
>
> Aprendeu a copiar código. Aprendeu sintaxe. Aprendeu padrão. Coisas valiosas. Mas não a entregar.
>
> E entregar é a parte que separa quem é pago de quem é estudante.
>
> Mercado não compra conhecimento. Compra resultado.
>
> Resultado em código tem um nome: link funcionando, com domínio, que outra pessoa consegue abrir.
>
> Se a sua resposta pra "me mostra um projeto seu" é um GitHub com 30 repositórios e nenhum link, o problema não é o seu currículo.
>
> Boa notícia: dá pra resolver em um fim de semana.
>
> Pega o seu projeto menos vergonhoso, gasta sábado limpando o que dá vergonha, e domingo coloca no ar. Em qualquer lugar. Vercel, Render, Railway, Fly. Tanto faz.
>
> Segunda você vai ser outra pessoa.
>
> Quem aqui topa o desafio do fim de semana?
>
> #carreiratech #devjr #programacao

---

## SEMANA 3

### 🟦 Segunda — Bastidores
**Tema:** O aluno que ficou 6 meses no mesmo bug

> Recebi uma mensagem esses dias que me derrubou.
>
> Um aluno meu — vou chamar de [ajustar: J.] — me escreveu dizendo que tinha ficado [ajustar: seis] meses travado no mesmo erro.
>
> Não exagerando. Seis meses.
>
> Toda vez que tentava rodar o projeto dele em produção, dava um `502 Bad Gateway`. Local funcionava. Em produção, morria.
>
> Ele tentou de tudo. Trocou de provedor. Refez o Dockerfile. Apagou e refez o projeto. Quase desistiu de programar.
>
> Aí ele entrou no Zero ao Deploy. Na segunda semana, descobriu o que era.
>
> A porta. Era a porta.
>
> O servidor dele estava escutando na porta 3000. O serviço esperava na 8080.
>
> Uma linha. Seis meses.
>
> Eu fiquei pensando na quantidade de pessoas que estão exatamente nessa situação agora, lendo esse post, com um projeto pronto que não roda em produção por causa de uma linha.
>
> Programar não é difícil. Programar sozinho, sem ninguém pra olhar por cima do ombro e dizer "olha aqui, é só isso", é que é.
>
> Se você tá nessa há mais tempo do que devia: peça ajuda. Pra mim, pra outro dev, pra qualquer um. Seis meses de bug não é mérito. É só dor desnecessária.
>
> Qual foi o bug que te custou mais tempo até descobrir que era bobagem?
>
> #carreiratech #mentoria #programacao

---

### 🟩 Quarta — Insight da trincheira
**Tema:** Quando o problema não é o código

> [Ajustar: 80%] dos bugs de produção que eu já resolvi não eram bugs de código.
>
> Eram:
>
> — Variável de ambiente faltando
> — Permissão errada no servidor
> — Porta diferente entre serviços
> — DNS que ainda não propagou
> — Memória estourando porque o plano grátis tem 512MB
> — Build que rodou local mas falhou no CI porque o `package-lock.json` tava desatualizado
>
> Quando você vê isso pela primeira vez, parece misterioso. Parece que tem algo errado com você.
>
> Não tem.
>
> Tem algo errado com a forma como nós aprendemos a programar: focada 100% na lógica, 0% no ambiente.
>
> A lógica é a parte fácil. A IDE te ajuda. O TypeScript reclama. O linter aponta.
>
> O ambiente é silencioso. Ele só te devolve um log obscuro e te deixa lá.
>
> A regra que eu uso quando algo quebra em produção e não local:
>
> 1. **Logs antes de hipótese.** Antes de chutar o que é, lê o log inteiro.
> 2. **Diferenças antes de suposições.** Listar o que tem de diferente entre local e produção — versão, env, porta, secret, recurso.
> 3. **Mudar um por vez.** Se mudar três coisas juntas e funcionar, você ainda não sabe qual era.
>
> Não é truque. É método. E método se aprende fazendo, com alguém apontando o que olhar.
>
> Qual erro de produção te ensinou mais?
>
> #devops #debug #engenhariadesoftware

---

### 🟥 Sexta — Manifesto
**Tema:** O seu portfólio não é o GitHub, é o link

> Recrutador não abre o seu GitHub.
>
> Eu sei que dói ler isso. Eu também queria que abrisse. Mas ele tem [ajustar: 200] currículos pra olhar essa semana e tempo médio por candidato é de [ajustar: 7] segundos.
>
> O que ele faz?
>
> Procura um link. Clica. Se abrir alguma coisa decente, você passa. Se não abrir, ou cair em erro, ou ele tiver que rodar `npm install` mentalmente — você não passa.
>
> O seu portfólio profissional não é uma lista de tecnologias. É um link clicável.
>
> Um link clicável vale mais do que:
>
> — Certificado de bootcamp
> — Pós-graduação em desenvolvimento
> — 40 projetos no GitHub sem deploy
> — Stack list de 20 tecnologias no perfil
>
> Porque o link prova que você terminou. Que você passou pelo medo do deploy. Que entendeu o ciclo completo.
>
> E "terminou" é o adjetivo mais raro entre devs juniores.
>
> Não precisa ser projeto grande. Pode ser uma calculadora. Um joguinho. Uma página com seu currículo bonitinho. Um clone simples.
>
> Precisa, sim, ter:
>
> — Domínio próprio ou subdomínio de provedor
> — Funcionar no celular
> — Carregar em menos de [ajustar: 3] segundos
> — Não dar erro na primeira interação
>
> É isso. É essa a régua.
>
> Você passa nessa régua hoje?
>
> #carreiratech #devjr #portfolio

---

## SEMANA 4

### 🟦 Segunda — Bastidores
**Tema:** Por que comecei a ensinar deploy

> Faz [ajustar: três] anos que eu ensino deploy.
>
> Antes disso, eu ensinava programação tradicional. Front, back, banco. O caminho que todo curso ensina.
>
> Até que um dia uma aluna minha me mandou uma mensagem assim:
>
> "Michel, eu aprendi tudo que você ensinou. Sei React. Sei Node. Sei banco. Mas eu ainda não consegui colocar nada no ar. Como faz isso?"
>
> Eu respondi com um tutorial. Ela voltou três dias depois:
>
> "Não funcionou."
>
> Voltei. Mandei outro tutorial.
>
> "Esse também não."
>
> No quinto tutorial, eu parei. Sentei. E percebi uma coisa que tinha passado batido por mim por anos:
>
> Eu nunca tinha ensinado a parte mais importante.
>
> Programação a gente aprende com material de sobra. YouTube, curso, livro, ChatGPT, documentação. Não falta conteúdo.
>
> Deploy a gente aprende sozinho, no susto, perdendo um fim de semana inteiro, com o gato olhando.
>
> E ninguém escreve sobre essa parte porque ela é entediante de ensinar. Não tem feature nova. Não tem framework brilhante. É variável de ambiente, é DNS, é log, é porta, é certificado.
>
> Mas é exatamente essa parte que decide quem é dev de verdade.
>
> Foi por isso que eu criei o Zero ao Deploy. Não porque o mercado precisava de mais um curso. Porque a [ajustar: aluna] precisava.
>
> E depois dela, mais [ajustar: várias centenas de pessoas] precisaram da mesma coisa.
>
> Qual foi a pergunta de aluno que mudou o jeito que você ensina/trabalha?
>
> P.S. — para quem chegou aqui curioso: zeroaodeploy.com tem todos os detalhes.
>
> #educacao #carreiratech #programacao

---

### 🟩 Quarta — Insight da trincheira
**Tema:** DNS, domínio e a hora de espera

> Tem uma frase que todo dev ouve uma vez na vida, geralmente às 23h, geralmente antes de uma demo importante:
>
> "Deve ser o DNS."
>
> E é. Quase sempre é.
>
> Domínio é a parte do deploy que mais confunde quem está começando, porque ele tem uma característica única: você faz uma mudança e ela não acontece na hora.
>
> Você clica em "salvar". Não muda nada.
>
> Você recarrega. Não muda nada.
>
> Você acha que clicou errado. Refaz. Não muda nada.
>
> Você se desespera. Não muda nada.
>
> Aí 40 minutos depois, sem você fazer nada, funciona.
>
> Isso se chama propagação de DNS, e é a primeira lição de paciência que todo dev precisa aprender.
>
> O que eu queria ter ouvido antes:
>
> 1. **TTL importa.** Se você sabe que vai mudar DNS amanhã, abaixa o TTL hoje. Vai economizar horas.
> 2. **`dig` é seu amigo.** `dig seudominio.com` te mostra o que o mundo está vendo, não o que o seu navegador tá vendo (que pode estar em cache).
> 3. **Cache do navegador mente.** Sempre teste em aba anônima ou outro dispositivo.
> 4. **HTTPS depois do DNS.** Tentar emitir certificado antes do domínio resolver gera erro feio. Ordem importa.
>
> Pequenas coisas. Mas é a soma delas que faz o deploy ser tranquilo, ao invés de uma noite acordado.
>
> Qual etapa de deploy você acha mais chata de explicar pra quem está começando?
>
> #devops #dns #infra

---

### 🟥 Sexta — Manifesto
**Tema:** Termine uma coisa esse fim de semana

> A maior parte das pessoas que vão ler esse post tem pelo menos um projeto parado.
>
> Não falta código. Falta um empurrão.
>
> Vou propor um desafio simples pra esse fim de semana:
>
> **Sábado.** Pega o projeto menos vergonhoso da sua pasta. Não o mais ambicioso. Não o mais bonito. O mais terminável.
>
> Lista o que falta. Honestamente. Provavelmente são umas [ajustar: 4–5] coisas: um README, um botão que não funciona, uma rota que dá erro, um deploy.
>
> Faz só essas.
>
> **Domingo.** Coloca no ar. Onde for. Vercel, Render, Railway, Netlify, Fly, GitHub Pages. Tem um botão "deploy" em cada um.
>
> **Domingo à noite.** Manda o link pra uma pessoa. Uma só. Pode ser sua mãe, seu amigo dev, um colega de trabalho.
>
> Não pra elogiar. Pra usar.
>
> Segunda-feira você vai ter uma coisa que [ajustar: 90%] dos seus concorrentes diretos não tem: um projeto seu, funcionando, no ar, que outra pessoa já testou.
>
> Em uma semana você pode estar mostrando esse link em entrevista. Em três meses, esse mesmo link pode ter te rendido uma vaga.
>
> Não é exagero. Eu vejo isso acontecer toda semana.
>
> Bora?
>
> Quem topa, comenta o nome do projeto que vai colocar no ar.
>
> #desafio #carreiratech #devjr

---

## Como usar esse documento

1. **Abra o calendário** (`CALENDARIO-EDITORIAL.xlsx`) para marcar data de publicação de cada post.
2. **Personalize os `[ajustar: ...]`** — eles são apenas sugestões; troque pelo número/nome real da sua história. A força do tom narrativo é a verdade.
3. **Não publique em ordem rígida** — se acontecer alguma coisa na sua semana que combina mais com o post de quarta, troca de ordem. Editorial é guia, não jaula.
4. **Repita o que funcionar** — depois do post 12, olhe os 3 com mais engajamento e escreva variações. O LinkedIn premia consistência de tema, não novidade constante.
