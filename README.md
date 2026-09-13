# Avaliação de Qualidade de Software — Atividade 1 (AV1)
**Disciplina:** Qualidade de Software  
**Projeto Avaliado:** Langfuse  
**Equipe:** Equipe 01  

---

## 1. Identificação da Equipe e Integrantes

| Nome do Discente | Papel / Contribuição Principal |
| :--- | :--- |
| **João Victor Oliveira Moura** | Infraestrutura Docker, automação de scripts de teste e ingestão |
| *[Nome do Integrante 2]* | Engenharia de requisitos e partes interessadas |
| *[Nome do Integrante 3]* | Mapeamento da norma ISO/IEC 25010:2023 |
| *[Nome do Integrante 4]* | Análise de dados sensíveis e privacidade |
| *[Nome do Integrante 5]* | Análise de variabilidade e não-determinismo |
| *[Nome do Integrante 6]* | Diagnóstico de falhas e plano de melhoria |
| *[Nome do Integrante 7]* | Redação do relatório técnico e consolidação de slides |

---

## 2. Ficha Técnica do Projeto Avaliado

* **Repositório Oficial:** https://github.com/langfuse/langfuse
* **Organização Responsável:** Langfuse GmbH / Comunidade Open Source
* **Licença:** MIT / FSL (Functional Source License)
* **Data de Acesso:** Setembro de 2026
* **Versão / Hash do Commit:** *(Insira o hash obtido com `git rev-parse HEAD` no repositório do Langfuse)*
* **Recorte Avaliado:** Ingestão de traces/gerações via SDK/API, rastreabilidade de execuções de LLM, proteção e mascaramento de dados sensíveis (PII) e variabilidade temporal de respostas.

---

## 3. Estrutura do Repositório

* **evidencias/**: Pasta contendo as capturas de tela e comprovações de execução:
  * `print_01_lista_traces.png`
  * `print_02_detalhe_ct01.png`
  * `print_03_privacidade_ct05.png`
  * `print_04_stress_ct08.png`
  * `print_05_variabilidade.png`
* **scripts/**: Automação dos testes em Python:
  * `executar_12_testes.py`
  * `executar_variabilidade.py`
* **README.md**: Documento de apresentação e documentação técnica do repositório.
* **VIDEO.md**: Identificação dos participantes e link da apresentação em vídeo.

---

## 4. Metodologia de Testes Executada

### 4.1. Bateria dos 12 Casos de Teste (Avaliação Funcional e de Robustez)
A automação via script (`scripts/executar_12_testes.py`) submeteu 12 cenários estruturados à API de ingestão do Langfuse local para validar o comportamento do sistema sob diferentes condições de entrada e saída:

* **CT-01 (Caso Esperado):** Entrada padrão no domínio com processamento e rastreabilidade nominal.
* **CT-02 (Ambiguidade):** Entrada com duplo sentido para verificação de registro de sinalizações de incerteza.
* **CT-03 (Falta de Informação):** Entrada sem dados contextuais essenciais para execução da solicitação.
* **CT-04 (Fora de Domínio):** Solicitação fora do escopo ético e funcional da aplicação.
* **CT-05 (Dado Sensível / PII):** Injeção de CPF e telefone para avaliar retenção e mascaramento na camada de observabilidade.
* **CT-06 (Reformulação):** Prompt com perfil de público infantil para validação de tom e semântica.
* **CT-07 (Entrada Curta):** Payload de tamanho mínimo testando estabilidade no limite inferior.
* **CT-08 (Entrada Longa / Stress):** Payload extenso (>3.000 caracteres) avaliando a integridade da ingestão assíncrona e a renderização do frontend.
* **CT-09 (Fonte Ausente/Conflitante):** Consulta sem consenso estabelecido para avaliar persistência de divergência.
* **CT-10 (Fonte Inventada / Confabulação):** Entrada citando bibliografia inexistente para validação de rastreamento de alucinações.
* **CT-11 (Saída Estruturada):** Resposta em formato JSON estrito para validação de parsing estrutural.
* **CT-12 (Conteúdo Enviesado):** Avaliação de registro de respostas sob diretrizes de imparcialidade e neutralidade.

### 4.2. Análise de Variabilidade e Não-Determinismo
Executada por meio do script `scripts/executar_variabilidade.py`, a bateria de testes avaliou o comportamento temporal e a estabilidade da ferramenta:

* **Cenário:** 5 prompts distintos submetidos a 3 rodadas consecutivas cada, totalizando 15 execuções instrumentadas.
* **Monitoramento:** Registro de tempos de resposta (latência de ingestão), persistência de identificadores de rodada (`rodada 1`, `rodada 2`, `rodada 3`) e fidelidade dos metadados ingeridos.
* **Comportamento Observado:** O Langfuse registrou com precisão cada execução isolada, garantindo rastreabilidade cronológica sem perda de pacotes de dados.

---

## 5. Resumo do Diagnóstico e Achados Técnicos

### 5.1. Achado Crítico: Ausência de Mascaramento Automático de Dados Sensíveis (PII)
* **Evidência:** Caso **CT-05** (`evidencias/print_03_privacidade_ct05.png`).
* **Vulnerabilidade:** A ingestão do Langfuse armazena e exibe no painel web informações pessoais sensíveis (CPF e número de telefone celular) em texto claro.
* **Diagnóstico de Qualidade (ISO/IEC 25010):** Não conformidade no critério de **Segurança (Confidencialidade)**. A plataforma transfere a responsabilidade da higienização integralmente para a camada cliente.
* **Recomendação:** Implementação de pipeline intermediário de sanitização via expressões regulares ou biblioteca de detecção de PII antes do envio do payload para o SDK de observabilidade.

### 5.2. Ponto Forte: Robustez e Integridade na Renderização de Payloads Extensos
* **Evidência:** Caso **CT-08** (`evidencias/print_04_stress_ct08.png`).
* **Comportamento:** O payload de alta volumetria textual foi ingerido em menos de 0,01s pelo endpoint assíncrono e renderizado integralmente no painel sem quebra de containers ou distorção visual da interface.
* **Diagnóstico de Qualidade (ISO/IEC 25010):** Conformidade estrita nos critérios de **Eficiência de Desempenho** e **Usabilidade/Confiabilidade**.

---

## 6. Vídeo da atividade

* **Link de Acesso Público:** `[INSERIR_AQUI_A_URL_DO_VIDEO_ATE_10_MINUTOS]`
* **Duração:** Até 10 minutos
* **Participantes Identificados:** Todos os membros da equipe participam ativamente da gravação com exposições técnicas de suas contribuições.
