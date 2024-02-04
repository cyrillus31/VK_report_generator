import os
import unicodedata

from jinja2 import Environment, FileSystemLoader
import pdfkit

cwd = os.getcwd()
PDF_STORAGE_PATH = os.path.join(cwd, "PDF")

if not os.path.exists(PDF_STORAGE_PATH):
    os.makedirs(PDF_STORAGE_PATH)

env = Environment(loader=FileSystemLoader("static/templates"))


def unicode_normalize(string: str):
    return unicodedata.normalize("NFKC", string)

def from_string_to_pdf(template_name: str, pdf_name: str, context: dir, location: str = PDF_STORAGE_PATH) -> str:

    template = env.get_template(template_name)
    rendered_html = template.render(context)

    file_path = os.path.join(PDF_STORAGE_PATH, f"{pdf_name}.pdf")
    pdfkit.from_string(rendered_html, file_path)

    return file_path
