import streamlit as st

def show_pdf_uploader() -> tuple[bool, str]:
    st.markdown("________________________________________________________________")
    st.title("📄PDF Reader RAG")
    pdf_file = st.file_uploader("Upload a PDF file", accept_multiple_files=False)
    if st.button("Analyse PDF"):
        if pdf_file is not None and pdf_file.type != "application/pdf":
            return False, st.error("The uploaded file is not a valid PDF. Please upload a valid PDF file.")
        elif pdf_file is not None and pdf_file.size > 2 * 1024 * 1024:
            return False, st.error("The uploaded file exceeds the maximum size limit of 2MB. Please upload a smaller PDF file.")
        elif pdf_file is not None:
            st.markdown("File name: \n" + pdf_file.name)
            st.markdown("File size: \n" + str(pdf_file.size) + " bytes")
            st.markdown("✅ PDF uploaded successfully")
            st.markdown("________________________________________________________________")
            return True, pdf_file
        else:
            st.empty()  
            return False, st.error("No file uploaded. Please upload a PDF file to proceed.")
    else:
        return False, None
        

def show_pdf_data(is_extracted: bool, extracted_text: str):
    if is_extracted:
        st.markdown("________________________________________________________________")
        st.title("📄PDF Extracted Text")
        st.markdown(extracted_text)
        st.markdown("________________________________________________________________")
    else:
        st.error(extracted_text)