from ui.streamlit_ui import show_pdf_data, show_pdf_uploader
from utils.pdf_reader import extract_text_from_pdf

is_pdf_uploaded,pdf_file = show_pdf_uploader()

if is_pdf_uploaded:
    is_extracted, extracted_text = extract_text_from_pdf(pdf_file)
    show_pdf_data(is_extracted, extracted_text)