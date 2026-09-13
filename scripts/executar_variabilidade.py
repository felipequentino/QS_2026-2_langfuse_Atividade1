import time
from langfuse import Langfuse

langfuse = Langfuse(
    public_key="pk-lf-7d007ddd-78c7-42cf-824f-39352524412e",
    secret_key="sk-lf-02674e34-0642-43fd-8cd4-a521183fbaba",
    host="http://localhost:3000"
)

prompts = [
    ("VAR-01", "Defina teste de regressao em uma frase."),
    ("VAR-02", "Diga tres causas de alucinacao em IA generativa."),
    ("VAR-03", "Traduza qualidade de software para o ingles."),
    ("VAR-04", "Qual a diferenca entre erro, defeito e falha?"),
    ("VAR-05", "Explique o que e RAG em LLMs.")
]

print("Iniciando bateria de variabilidade (5 prompts x 3 repeticoes)...")

for id_var, prompt in prompts:
    print(f"\nExecutando {id_var}...")
    for rodada in range(1, 4):
        inicio = time.time()
        
        obs = langfuse.start_observation(
            name=f"{id_var} - Rodada {rodada}",
            as_type="generation",
            model="modelo-teste-variacao",
            input=prompt,
            metadata={"rodada": rodada, "grupo": "variabilidade", "prompt_id": id_var}
        )
        obs.update(output=f"Resposta simulada rodada {rodada} para: {prompt}")
        obs.end()
        
        duracao = round(time.time() - inicio, 3)
        print(f"  -> Rodada {rodada} processada ({duracao}s)")
        time.sleep(0.1)

print("\nEnviando dados de variabilidade ao Langfuse...")
langfuse.flush()
print("Variabilidade concluida com sucesso!")
