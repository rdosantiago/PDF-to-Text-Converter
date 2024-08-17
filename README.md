# PDF-to-Text-Converter
Este repositório contém um script Python para a extração de texto de arquivos PDF e salvamento do conteúdo em um arquivo de texto (.txt). Utiliza a biblioteca PyPDF2 para ler e extrair o texto das páginas do PDF. **O texto gerando não serve para leitura humana, ele deve ser usado como fonte para extração de dados via Regex**.

# Funcionalidades
- **Leitura de PDF**: Lê o conteúdo de um arquivo PDF e extrai o texto de todas as suas páginas.
- **Salvamento em Arquivo de Texto**: Salva o texto extraído em um arquivo de texto (.txt) especificado pelo usuário.

# Estrutura do Código
### Classe 'PDFHandler':
- **__init__**: Inicializa o caminho do arquivo PDF e o caminho de saída para o arquivo de texto.
- **read_pdf**: Lê e extrai o texto de todas as páginas do PDF.
- **save_to_txt**: Salva o conteúdo extraído em um arquivo de texto.

### Função 'main':
- Define os caminhos dos arquivos PDF e de saída.
- Instancia a classe PDFHandler.
- Chama os métodos para ler o PDF e salvar o texto extraído.

# Como Utilizar
#### 1) Clone este repositório.
#### 2) Instale as dependências necessárias (ex. PyPDF2).
#### 3) Defina os caminhos do arquivo PDF e do arquivo de saída no script.
#### 4) Execute o script Python.

# Pré-requisitos
- Python 3.x
- PyPDF2

# Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

# Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
