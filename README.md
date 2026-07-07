## Pdf reader using RAG

As a user, I want the application to extract text from an uploaded PDF so that I can view its contents before moving to the RAG pipeline.

## Architeture

``` flow chart

                   User
                  │
                  ▼
              app.py
                  │
      ┌───────────┼────────────┐
      │           │            │
      ▼           ▼            ▼
 streamlit_ui  pdf_reader   chunker
      │                        │
      │                        ▼
      │                  embedding_service
      │                        │
      │                        ▼
      │                  vector_store
      │                        │
      │                        ▼
      │                    retriever
      │                        │
      │                        ▼
      │                    gemini_service
      │
      └──────────────► Display Result

```      