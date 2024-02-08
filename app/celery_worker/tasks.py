import os

from jinja2 import Environment, FileSystemLoader
import pdfkit

from celery_worker.celery_config import celery_app
from config import settings

pdf_storage_path = settings.pdf_storage_path

if not os.path.exists(pdf_storage_path):
    os.makedirs(pdf_storage_path)

env = Environment(loader=FileSystemLoader("static/templates"))

@celery_app.task
def create_pdf_and_return_path(template_name, pdf_name, context: dir, location: str) -> str:
    template = env.get_template(template_name)
    rendered_html = template.render(context)
    file_path = os.path.join(location, f"{pdf_name}.pdf")
    rendered_html = template.render(context)
    pdfkit.from_string(rendered_html, file_path)
    return file_path

class PDF:
    def __init__(self, template_name: str, pdf_name: str, context: dir, location: str = pdf_storage_path):
        self.template_name = template_name
        self.pdf_name = pdf_name
        self.context = context
        self.location = location

    async def create(self) -> str:
        file_path = create_pdf_and_return_path(self.template_name, self.pdf_name, self.context, self.location)
        self.file_path = file_path
        return file_path

    async def delete(self) -> None:
        os.remove(self.file_path)




