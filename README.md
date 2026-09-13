# Avaliação de Qualidade de Software — Atividade 1 (AV1)
**Disciplina:** Qualidade de Software  
**Projeto Avaliado:** Langfuse  
**Equipe:** Equipe 01  

---

## 1. Identificação da Equipe e Integrantes

| Nome do Discente | Papel / Contribuição Principal |
| :--- | :--- |
| **João Victor Moura** | Infraestrutura Docker, automação de scripts de teste e ingestão |
| *[Nome do Integrante 2]* | Engenharia de requisitos e partes interessadas |
| *[Nome do Integrante 3]* | Mapeamento da norma ISO/IEC 25010:2023 |
| *[Nome do Integrante 4]* | Análise de dados sensíveis e privacidade |
| *[Nome do Integrante 5]* | Análise de variabilidade e não-determinismo |
| *[Nome do Integrante 6]* | Diagnóstico de falhas e plano de melhoria |
| *[Nome do Integrante 7]* | Redação do relatório técnico e consolidação de slides |

---

## 2. Ficha Técnica do Projeto Avaliado

* **Repositório Oficial:** [https://github.com/langfuse/langfuse](https://github.com/langfuse/langfuse)
* **Organização Responsável:** Langfuse GmbH / Comunidade Open Source
* **Licença:** MIT / FSL (Functional Source License)
* **Data de Acesso:** Setembro de 2026
* **Versão / Hash do Commit:** *(Insira o hash obtido com `git rev-parse HEAD` no repositório do Langfuse)*
* **Recorte Avaliado:** Ingestão de traces/gerações via SDK/API, rastreabilidade de execuções de LLM, proteção e mascaramento de dados sensíveis (PII) e variabilidade temporal de respostas.

---

## 3. Estrutura do Repositório

```text
├── evidencias/                # Capturas de tela e comprovações de execução
│   ├── print_01_lista_traces.png
│   ├── print_02_detalhe_ct01.png
│   ├── print_03_privacidade_ct05.png
│   ├── print_04_stress_ct08.png
│   └── print_05_variabilidade.png
├── scripts/                   # Automação de testes em Python
│   ├── executar_12_testes.py
│   └── executar_variabilidade.py
├── README.md                  # Este documento
└── VIDEO.md                   # Identificação de participantes e link da apresentação

4. Metodologia de Testes Executada
4.1. Bateria dos 12 Casos de Teste (Seção 7)
Foram projetados e automatizados 12 cenários de teste cobrindo limites operacionais, coerência factual e riscos de segurança da informação:

CT-01 (Caso Esperado): Resposta no domínio e fundamentada.

CT-02 (Ambiguidade): Entrada com duplo sentido e sinalização de incerteza.

CT-03 (Falta de Informação): Solicitação de contexto prévio para ações sensíveis.

CT-04 (Fora de Domínio): Recusa objetiva de solicitações fora do escopo ético/funcional.

CT-05 (Dado Sensível / PII): Avaliação de retenção de CPF e telefone sem higienização prévia.

CT-06 (Reformulação): Ajuste de linguagem para perfis de público distintos.

CT-07 (Entrada Curta): Tratamento de payloads mínimos sem falhas de comunicação.

CT-08 (Entrada Longa / Stress): Resiliência da interface e da API para payloads com mais de 3.000 caracteres.

CT-09 (Fonte Ausente/Conflitante): Sinalização de divergência científica ou ausência de consenso.

CT-10 (Fonte Inventada / Confabulação): Tratamento de referências bibliográficas inexistentes.

CT-11 (Saída Estruturada): Validação de formato rígido de retorno (JSON Schema).

CT-12 (Conteúdo Enviesado): Avaliação de imparcialidade e conformidade com neutralidade.

4.2. Análise de Variabilidade e Não-Determinismo (Seção 8)
Foram submetidos 5 prompts distintos em 3 repetições cronometradas (15 observações no total).

O Langfuse monitorou a oscilação de latência da rede e atestou a consistência na persistência de parâmetros de temperatura e metadados.

5. Resumo do Diagnóstico e Achados Críticos
Achado Crítico (Privacidade / PII): A ingestão nativa do Langfuse armazena dados de identificação pessoal (como CPF e telefone) em texto claro no banco de dados e nos painéis da interface caso a camada cliente não execute um pré-processamento de sanitização.

Resiliência e Layout: A aplicação demonstrou conformidade nos fluxos assíncronos de ingestão, mantendo a integridade visual da interface mesmo sob injeção de grandes blocos textuais (CT-08).

Vídeo da atividade
Link de Acesso Público: [INSERIR_AQUI_A_URL_DO_VIDEO_ATE_10_MINUTOS]

Duração: Até 10 minutos

Participantes Identificados: Todos os membros da equipe participam ativamente da gravação com exposições técnicas de suas contribuições.
