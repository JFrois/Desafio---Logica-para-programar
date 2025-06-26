<div class="container">
        <h1>calculadora-media-fiap</h1>
    <h2>📝 Descrição do Projeto</h2>
      <p>
            Este projeto consiste em um script de console que calcula a média final de um aluno da FIAP com base nas notas obtidas ao longo de dois semestres. O programa solicita as notas de Checkpoints, Challenges e Global Solutions, aplica os pesos corretos, e determina o status final do aluno: <strong>Aprovado</strong>, <strong>Reprovado</strong> ou em <strong>Exame</strong>.
        </p>
        <p>
            O script foi desenvolvido como uma solução para o desafio de lógica de programação, incorporando boas práticas como validação de entrada, modularização e um fluxo de execução claro.
        </p>
    <h2>✨ Funcionalidades</h2>
        <ul>
            <li><strong>Cálculo Semestral:</strong> Calcula a média do 1º e 2º semestre de forma independente.</li>
            <li><strong>Cálculo Anual Ponderado:</strong> Consolida as médias semestrais para obter a Média Anual, com pesos de 40% para o primeiro semestre e 60% para o segundo.</li>
            <li><strong>Status do Aluno:</strong> Determina automaticamente se o aluno está aprovado, reprovado ou se precisa realizar o exame.</li>
            <li><strong>Cálculo de Exame:</strong> Para alunos em exame, o programa solicita a nota do exame e calcula a nova média final.</li>
            <li><strong>Validação de Entrada:</strong> Garante que todas as notas inseridas estejam no intervalo válido (0 a 10), solicitando a correção caso contrário.</li>
            <li><strong>Execução Contínua:</strong> Permite que o usuário realize múltiplos cálculos sem precisar reiniciar o programa.</li>
        </ul>
        <h2>⚙️ Lógica de Cálculo</h2>
        <p>O sistema de notas segue uma estrutura bem definida de pesos e médias.</p>
                <details>
            <summary><strong>Clique para ver o detalhamento do 1º Semestre</strong></summary>
            <ul>
                <li><strong>Média dos Checkpoints ($MCP_{1Sem}$):</strong> Média simples das 2 maiores notas entre <code>CP1</code>, <code>CP2</code> e <code>CP3</code>.</li>
                <li><strong>Média do Challenge ($MS_{1Sem}$):</strong> Média simples das notas de <code>Sprint 1</code> e <code>Sprint 2</code>.</li>
                <li><strong>Global Solution ($GS_{1Sem}$):</strong> Nota única da prova semestral.</li>
            </ul>
            A fórmula da média do primeiro semestre ($M_{1Sem}$) é:
            $$M_{1Sem} = \frac{(MCP_{1Sem} \cdot 2) + (MS_{1Sem} \cdot 2) + (GS_{1Sem} \cdot 6)}{10}$$
        </details>
        
  <details>
            <summary><strong>Clique para ver o detalhamento do 2º Semestre</strong></summary>
            <ul>
                <li><strong>Média dos Checkpoints ($MCP_{2Sem}$):</strong> Média simples das 2 maiores notas entre <code>CP4</code>, <code>CP5</code> e <code>CP6</code>.</li>
                <li><strong>Média do Challenge ($MS_{2Sem}$):</strong> Média simples das notas de <code>Sprint 3</code> e <code>Sprint 4</code>.</li>
                <li><strong>Global Solution ($GS_{2Sem}$):</strong> Nota única da prova semestral.</li>
            </ul>
             A fórmula da média do segundo semestre ($M_{2Sem}$) é:
            $$M_{2Sem} = \frac{(MCP_{2Sem} \cdot 2) + (MS_{2Sem} \cdot 2) + (GS_{2Sem} \cdot 6)}{10}$$
        </details>
      <details>
            <summary><strong>Clique para ver o detalhamento da Média Anual e Status</strong></summary>
            A Média Anual (MA) é a média ponderada das notas semestrais:
            $$MA = \frac{(M_{1Sem} \cdot 4) + (M_{2Sem} \cdot 6)}{10}$$
            <ul>
                <li><strong>Aprovado:</strong> $MA \ge 6.0$</li>
                <li><strong>Reprovado:</strong> $MA < 4.0$</li>
                <li><strong>Exame:</strong> $4.0 \le MA < 6.0$
                    <ul>
                        <li>Se em exame, a Média Final (MF) é: $MF = \frac{MA + Nota_{Exame}}{2}$</li>
                    </ul>
                </li>
            </ul>
        </details>
        <h2>🚀 Como Executar</h2>
        <p>Para executar o projeto, siga os passos abaixo:</p>
        <ol>
            <li><strong>Clone o repositório:</strong>
                <pre><code>git clone https://github.com/seu-usuario/calculadora-media-fiap.git</code></pre>
            </li>
            <li><strong>Navegue até o diretório do projeto:</strong>
                <pre><code>cd calculadora-media-fiap</code></pre>
            </li>
            <li><strong>Execute o script Python:</strong>
                <pre><code>python nome_do_seu_arquivo.py</code></pre>
            </li>
            <li>Siga as instruções no terminal para inserir as notas do aluno.</li>
        </ol>
        <h2>🛠️ Tecnologias Utilizadas</h2>
        <ul>
            <li><strong>Python 3:</strong> O projeto foi desenvolvido inteiramente em Python, sem a necessidade de bibliotecas externas.</li>
        </ul>
        <h2>👨‍💻 Autor</h2>
        <p>
            <strong>Juan Frois</strong> - <a href="mailto:contatojuanfrois@gmail.com">contatojuanfrois@gmail.com</a>
        </p>
        <hr>
    </div>
