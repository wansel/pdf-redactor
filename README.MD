# PDF Redactor 📄🚫

Script Python automatizado para busca e remoção definitiva (redação) de termos sensíveis em múltiplos arquivos PDF, preservando a estrutura de pastas original.

## 🚀 Funcionalidades
* **Busca Recursiva:** Processa todos os PDFs em pastas e subpastas.
* **Redação Real:** Remove o texto do arquivo (não apenas esconde com tarja).
* **Preservação de Estrutura:** Espelha a árvore de diretórios do `input` para o `output`.

## 🛠️ Pré-requisitos
* Python 3.8 ou superior
* WSL2 (Recomendado para usuários Windows) ou Linux/macOS

## 🏁 Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone git@github.com:wansel/pdf-redactor.git
    cd pdf-processor
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure suas variáveis de ambiente:**
    Use o arquivo chamado `.env.example` na raiz do projeto como base para o .env:
    ```bash
    cp .env.example .env
    ```
    Edite o `.env` e adicione o termo que deseja remover, igual aparece no PDF:
    ```env
    TEXTO_PARA_REMOVER="Seu Nome Aqui - 000.000.000-00"
    PASTA_INPUT="./input"
    PASTA_OUTPUT="./output"
    ```

## 📂 Como Usar

1.  Coloque os arquivos PDF que deseja processar dentro da pasta `./input`. Você pode organizar em subpastas se preferir.
2.  Execute o script:
    ```bash
    python3 main.py
    ```
3.  Os arquivos processados estarão na pasta `./output`, mantendo a mesma organização de pastas original.

## ⚠️ Observações de Segurança
* Este projeto utiliza o método `apply_redactions()` do PyMuPDF, que remove fisicamente os caracteres do PDF.
* **Nunca** envie seu arquivo `.env` para o GitHub. Ele já está incluído no `.gitignore`.
* Sempre confira o resultado final fazendo uma busca (Ctrl+F) no PDF gerado.
