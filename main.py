import fitz  # PyMuPDF
from pathlib import Path

def processar_pdfs():
    # Configurações de caminhos
    input_dir = Path("./input")
    output_dir = Path("./output")
    texto_para_remover = "cpf - nome"

    # 1. Localizar todos os PDFs em pastas e subpastas (recursivo)
    arquivos_pdf = list(input_dir.rglob("*.pdf"))
    
    if not arquivos_pdf:
        print("Nenhum arquivo PDF encontrado na pasta ./input")
        return

    print(f"Encontrados {len(arquivos_pdf)} arquivos para processar.")

    for caminho_entrada in arquivos_pdf:
        # 2. Definir o caminho de saída espelhando a estrutura original
        # O .relative_to(input_dir) pega apenas a parte do caminho após './input'
        caminho_relativo = caminho_entrada.relative_to(input_dir)
        caminho_saida = output_dir / caminho_relativo

        # 3. Garantir que a pasta de destino exista
        caminho_saida.parent.mkdir(parents=True, exist_ok=True)

        print(f"Processando: {caminho_relativo}...")

        try:
            # 4. Lógica de Redação (o que você já tinha)
            doc = fitz.open(caminho_entrada)
            houve_alteracao = False

            for page in doc:
                areas = page.search_for(texto_para_remover)
                if areas:
                    houve_alteracao = True
                    for area in areas:
                        page.add_redact_annot(area, fill=(1, 1, 1))  # Cor branca
                    page.apply_redactions()

            # 5. Salvar o arquivo processado
            doc.save(camin_saida, garbage=4, deflate=True)
            doc.close()
            
        except Exception as e:
            print(f"Erro ao processar {caminho_entrada}: {e}")

    print("\nConcluído! Verifique a pasta ./output")

if __name__ == "__main__":
    processar_pdfs()