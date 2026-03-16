import pdfplumber
import docx


def extract_text_from_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text


def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)

    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)


def parse_resume(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)

    else:
        raise ValueError("Unsupported file format")