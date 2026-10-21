# 00. Definição do problema

> **Rascunho.** Os trechos marcados com ✎ são decisões ou verificações que precisam ser confirmadas pelo autor antes de o documento ser considerado final.

## Contexto e problema

Quem procura vaga em tecnologia precisa decidir quais ferramentas aprender e o que destacar no currículo. A informação para decidir está nos textos das vagas, que são livres, espalhados por várias fontes e frequentemente repetidos entre elas. Ninguém consegue ler vagas suficientes para formar uma visão fundamentada, e olhar apenas as vagas de uma empresa ou de um portal dá uma imagem parcial.

Já existem projetos que contam tecnologias em vagas brasileiras, como o Vagômetro (https://vagometro.vercel.app/, código em https://github.com/leo-holanda/vagometro) e o Openings, que agrega vagas publicadas como issues no GitHub. Segundo a descrição pública dos autores, o Vagômetro publica rankings de tecnologias, modalidades e senioridade e tem uma função de "match" entre um perfil de busca e cada vaga. Eles respondem bem à pergunta **"o que aparece nas vagas?"**.

Este projeto parte da pergunta seguinte: **"dado o meu perfil, o que está faltando, e com que confiança posso afirmar isso?"**

### O que este projeto acrescenta ✎

> Confirmar lendo o código e a documentação do Vagômetro antes de manter estas afirmações. Se algum item já existir lá, reescrever o parágrafo.

1. **Extração de skills com qualidade medida.** Uma amostra de vagas é rotulada à mão e a extração é avaliada com precisão, recall e F1, com as limitações descritas.
2. **Análise agregada de lacunas.** Em vez de uma porcentagem por vaga, o resultado lista as skills que mais aparecem nas vagas e não estão no perfil, com intervalo de confiança.
3. **Foco em back-end, dados e automação**, com metodologia, fontes e vieses documentados e reprodutíveis.

## Usuários

- **Profissionais e estudantes de TI** que querem saber quais skills aparecem nas vagas e quais faltam no seu perfil.
- **O autor**, que usa o resultado para orientar o próprio currículo e estudos.
- **Quem avalia o projeto** (recrutadores, pares), que precisa conseguir rodá-lo e entender as decisões.

## Perguntas que o sistema responde

Todas se referem às **vagas coletadas das fontes listadas abaixo**, para as áreas de back-end, dados e automação, no Brasil e remoto, no período de coleta. Nenhuma afirma algo sobre o mercado inteiro.

Definições usadas:

- **Skill:** tecnologia, ferramenta ou prática que consta na taxonomia do projeto (por exemplo, PostgreSQL, Docker, FastAPI).
- **Menção:** a skill aparece no texto da vaga, seja como requisito ou como diferencial. Separar obrigatório de desejável fica fora do MVP ✎.

| # | Pergunta | Métrica |
|---|---|---|
| P1 | Quais skills aparecem com mais frequência, por fonte, senioridade e modalidade? | Proporção de vagas que mencionam a skill, com intervalo de confiança de Wilson (95%) |
| P2 | Dado um perfil (lista de skills), qual é a cobertura e quais são as lacunas? | Cobertura por vaga = skills da vaga presentes no perfil ÷ skills da vaga. Lacuna = frequência das skills ausentes, em ordem decrescente |
| P3 | Qual é a qualidade da extração de skills? | Precisão, recall e F1 em uma amostra rotulada à mão, por skill e global |
| P4 | Os resultados mudam de uma fonte para outra? | Diferença de proporção por skill entre fontes, com intervalo de confiança |

## Fora de escopo

| Item | Motivo |
|---|---|
| Recomendar vagas ou candidatar-se automaticamente | Não é o problema, e aumenta o risco legal e ético |
| Ler PDF de currículo no MVP | A entrada é uma lista de skills, o que evita tratar dado pessoal e complexidade de extração de PDF |
| Afirmações sobre o mercado de TI como um todo | A amostra vem de fontes abertas e não é representativa |
| Republicar o texto integral das vagas | Questões de termos de uso e direitos autorais. O sistema exibe título, empresa, link e skills extraídas ✎ |
| Extração por LLM no MVP | Só entra como comparação posterior, medida com as mesmas métricas |
| Análise de tendências no tempo | Issues do GitHub têm histórico, mas Lever e Greenhouse só mostram vagas abertas e o histórico começa no início da coleta ✎ decidir se entra em fase posterior |

## Fontes e viés

| Fonte | O que oferece | Viés provável | Como estimar o viés |
|---|---|---|---|
| Issues do GitHub (backend-br, frontendbr e repositórios Python) | Volume e histórico longo; título e labels padronizados | Muitas vagas de intermediárias de recrutamento; pouco conteúdo de dados e automação; labels diferentes por repositório; vagas que ficam abertas sem manutenção ✎ | Proporção de vagas por empresa; comparar com a amostra manual |
| Lever | Descrição completa, modalidade e tipo de contrato, sem chave de API | Só empresas que usam Lever e que foram incluídas na lista do autor; tende a startups e multinacionais; só vagas abertas | Registrar a lista de empresas e o critério usado para montá-la |
| Greenhouse | Descrição completa, sem chave de API | Mesmo viés do Lever; a API não expõe modalidade, que precisa ser inferida do texto | Idem |

**Fora do projeto:** LinkedIn (termos de uso proíbem coleta automatizada). Gupy fica como possibilidade futura, depois de ler os termos ✎.

**Estimativa do tamanho do viés.** Coletar à mão, para uso pessoal e sem automação, cerca de 50 vagas de portais não cobertos e comparar as proporções das principais skills com as do pipeline. É uma estimativa grosseira, que deve ser descrita como tal.

## Critérios de sucesso

1. **Qualidade do extrator.** Amostra rotulada com pelo menos 100 vagas ✎, com precisão, recall e F1 reportados por skill e globalmente. Meta inicial de F1 ≥ 0,80 ✎ (hipótese; se não for atingida, o resultado é reportado com a análise dos erros).
2. **Respostas reais.** P1 a P4 respondidas com dados reais e intervalos de confiança.
3. **Tamanho mínimo de amostra.** Nenhuma proporção é reportada para um estrato com menos de 30 vagas ✎.
4. **Reprodutibilidade.** Em um clone novo, `make up && make test` funciona, o CI fica verde e o pipeline pode ser reexecutado sem duplicar dados.
5. **Comparação com o Vagômetro.** Confrontar as dez skills mais frequentes em uma fonte em comum (issues do GitHub) e discutir as diferenças.
6. **Documentação.** README com problema, resultados, limitações e como rodar.

## Ameaças à validade

- **Seleção da amostra:** as fontes não representam o mercado; a lista de empresas do Lever e do Greenhouse é escolhida pelo autor.
- **Duplicatas:** a mesma vaga aparece mais de uma vez, na mesma fonte ou em fontes diferentes, e infla as proporções.
- **Vagas fechadas ou desatualizadas:** issues sem manutenção continuam abertas.
- **Extração:** falsos positivos (um benefício de "curso de inglês" não é requisito de inglês), falsos negativos (sinônimos, grafias diferentes) e termos ambíguos (Go, R, C).
- **Rotulagem por uma só pessoa:** o viés do rotulador afeta as métricas. Mitigação: segunda rotulagem em uma subamostra e medida de concordância ✎.
- **Taxonomia influenciada pelo autor:** a lista de skills reflete o que o autor conhece. Mitigação: derivar candidatos a partir dos próprios textos.
- **Mudança nas fontes:** APIs e formatos podem mudar, o que afeta a coleta e a comparabilidade ao longo do tempo.

## Riscos legais e éticos

- Ler os termos de uso de cada fonte antes de coletar; respeitar limites de requisição e identificar o coletor.
- **LGPD:** não armazenar dados pessoais de quem publica a vaga (nome, perfil, contato). Guardar só os campos da vaga.
- O perfil informado pelo usuário é dado pessoal. A decisão sobre onde ele é processado está na ADR 0002.

## Decisões pendentes ✎

- Tendências no tempo entram no escopo?
- Tamanho da amostra rotulada e meta de F1.
- Política de exibição do texto das vagas.