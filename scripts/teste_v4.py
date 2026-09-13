import os
from langfuse import Langfuse

os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-7d007ddd-78c7-42cf-824f-39352524412e"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-02674e34-0642-43fd-8cd4-a521183fbaba"
os.environ["LANGFUSE_HOST"] = "http://localhost:3000"

langfuse = Langfuse()

# Na v4 o método padrão de span/trace usa start_as_current_span ou create_event
print("Enviando evento de teste...")
span = langfuse.span(name="teste-conexao-v4")
span.end(output="Conexao validada com sucesso!")

langfuse.flush()
print("Evento flush concluído!")
