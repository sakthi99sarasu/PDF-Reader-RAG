import pymupdf

def extract_text_from_pdf(pdf_file)-> tuple[bool, str]:
    """
        Extracts text from an uploaded PDF file.

        Args:
            uploaded_file:
                Streamlit uploaded PDF.

            Returns:
        Extracted text as a string.

    Raises:
        ValueError:
            If the PDF is invalid.
    """
    if pdf_file is not None:
        try:
            pdf_file_data = pdf_file.read()
            doc = pymupdf.open(stream=pdf_file_data)
            if doc.needs_pass:
                doc.close()
                return False, "The PDF file is password-protected. Please provide a valid PDF file."
            # Check if the file is a completely different format (like an image or text file)
            # PyMuPDF can open images, so doc.type_number identifies the true format
            # 1 = PDF, 2 = XPS, 3 = EPUB, 4 = CBZ, 5 = FB2, 6 = MOBI
            elif "pdf" not in doc.metadata.get("format", "").lower() :
                doc.close()
                return False, "The uploaded file is not a valid PDF. Please provide a valid PDF file."
            else:
                text = ""
                for page in doc:
                    text += page.get_text()
                doc.close()
                return True, text
        except pymupdf.FileDataError:
            # Raise an explicit error for corrupted files instead of printing
            raise ValueError(f"File '{pdf_file.name}' is corrupted or not a valid PDF file structure.")
    else:
        raise ValueError("No PDF file provided. Please upload a PDF file to extract text.")
