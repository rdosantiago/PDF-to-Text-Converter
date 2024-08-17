import os
import PyPDF2

class PDFHandler:
    def __init__(self, pdf_path, output_path):
        self.pdf_path = pdf_path
        self.output_path = output_path

    def read_pdf(self):
        with open(self.pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            content = ""
            for page_number in range(len(reader.pages)):
                page = reader.pages[page_number]
                content += page.extract_text()
            return content

    def save_to_txt(self, content):
        with open(self.output_path, 'w', encoding='utf-8') as file:
            file.write(content)

def main():
    pdf_path = r'C:\Users\rdosa\source\repos\PythonApplication3\Bloqueio-Sisbajud.pdf'
    output_path = r'C:\Users\rdosa\source\repos\PythonApplication3\resultado.txt'
    
    pdf_handler = PDFHandler(pdf_path, output_path)
    content = pdf_handler.read_pdf()
    pdf_handler.save_to_txt(content)

if __name__ == "__main__":
    main()
