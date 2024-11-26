# GDPR NLP Assistant
This repository contains the data, exploratory analysis and chat bot code that I have developed.

The repository is structured as follows:
## Data
It has 2 folders:
- original_data: It contains the original GDPR Text in PDF Format
- chunked_data: It contains the text chunked and cleaned in JSON Format, originating from code/data_prep/read_chunk_clean.ipynb

## Code
It has 3 folders:

### Data_prep
It contains the code to parse the original GDPR Text and create a JSON with the following structure: {Chapter: {Article: Text}}. The text is cleaned via punctuation removal, lemmatization and extra white spaces removal.

### Exploration
It contains 2 notebooks: 
- data_exploarion.ipynb: It explores the GDPR Textual Data by: Computing token and bigrams frequencies in each chapter, Exploring TF-IDF clusters, Exploring clusters through LLM representations and Exploring Topics via LDA
- network_analysis.ipynb: It explores GDPR relationships between articles and chapters. Specifically, articles and chapters represent nodes whereas edges refer to citations of other GDPR Articles. 

### LLM_RAG_Assistant
It contains 4 scripts:
- chat_app.py: It contains the code to create a chat interface via Streamlit (see the embedded video)
- chat_with_assistant.py: It contains the code to create a RAG Assistant
- evaluate_rag_model.ipynb: It contains code to evaluate the RAG Assistant against a general purpose LLM on the EXIN Privacy & Data Protection Foundation Test
- rag_qa.py: It contains the EXIN Privacy & Data Protection Foundation questions and answers

## RAG Assistant Demo
The video below represents a Demo of how to interact with the GDPR RAG Assistant

https://github.com/user-attachments/assets/f6de44df-735b-4051-80e5-abc8142df495
