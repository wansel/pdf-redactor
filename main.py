import fitz  # PyMuPDF
import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def processar_pdfs():
    # Busca as configurações das variáveis de ambiente
    texto_para_remover = os.getenv("TEXTO_PARA_REMOVER")
    input_path = os.getenv("PASTA_INPUT", "./input")
    output_path = os.getenv("PASTA_OUTPUT", "./output")

    if not texto_para_remover:
        print("Erro: A variável TEXTO_PARA_REMOVER não foi definida no arquivo .env")
        return

    input_dir = Path(input_path)
    output_dir = Path(output_path)
    
    arquivos_pdf = list(input_dir.rglob("*.pdf"))
    
    if not arquivos_pdf:
        print(f"Nenhum PDF encontrado em {input_dir}")
        return

    print(f"Iniciando processamento de {len(arquivos_pdf)} arquivos...")

    for caminho_entrada in arquivos_pdf:
        caminho_relativo = caminho_entrada.relative_to(input_dir)
        caminho_saida = output_dir / caminho_relativo
        caminho_saida.parent.mkdir(parents=True, exist_ok=True)

        try:
            doc = fitz.open(caminho_entrada)
            
            # Aplica limpeza de metadados (opcional, mas recomendado)
            # doc.scrub(common_metadata=True)

            for page in doc:
                areas = page.search_for(texto_para_remover)
                if areas:
                    for area in areas:
                        # Redige a área (apaga o conteúdo de fato)
                        page.add_redact_annot(area, fill=(1, 1, 1))
                    page.apply_redactions()

            # Salva com compressão
            doc.save(caminho_saida, garbage=4, deflate=True)
            doc.close()
            print(f"Sucesso: {caminho_relativo}")
            
        except Exception as e:
            print(f"Erro em {caminho_relativo}: {e}")

if __name__ == "__main__":
    processar_pdfs()