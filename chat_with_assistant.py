import json
from access_token import *
from sentence_transformers import SentenceTransformer
import random 

from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

class GDPR_AI_Assistant():
    def __init__(self, 
                 data_path="data/chunked_data/gdpr_clean.json",
                 embedding_model="intfloat/multilingual-e5-large-instruct",
                 generator_model="meta-llama/Meta-Llama-3-8B-Instruct"):
        self.data_path = data_path
        self.embedding_model = embedding_model 
        self.generator_model = generator_model
        self.store = {}
        
    def _prepare_data(self):
        with open(self.data_path) as f: 
            gdpr = json.load(f)
        
        self.original_text = []
        for chapter in gdpr.keys():
            for article in gdpr[chapter].keys():
                self.original_text.append(Document(page_content=gdpr[chapter][article], id=chapter+'-'+article, metadata={'Chapter':chapter, 'Article':article}))
    
    def _create_vector_store(self):
        embedding_model = HuggingFaceEmbeddings(model_name=self.embedding_model,
                                                encode_kwargs={"normalize_embeddings": True})

        self.vectorstore = FAISS.from_documents(
            self.original_text,
            embedding=embedding_model)
        
    def _prepare_pipeline(self, system_prompt):
        self.system_prompt = (f"""
                         {system_prompt}
                         """
                         "\n\n"
                         "{context}")
        
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_prompt),
                ("human", "{input}"),
            ]
            )
        
        self.llm = HuggingFaceEndpoint(
        repo_id=self.generator_model,
        task="text-generation",
        do_sample=True,
        temperature=0.1,
        repetition_penalty=1.1,
        return_full_text=False,
        max_new_tokens=500,
        huggingfacehub_api_token=my_huggingface_token
        )
        self.retriever = self.vectorstore.as_retriever()
        self.question_answer_chain = create_stuff_documents_chain(self.llm, self.prompt)
        self.rag_chain = create_retrieval_chain(self.retriever, self.question_answer_chain)
        self.conversational_rag_chain = RunnableWithMessageHistory(
            self.rag_chain,
            self._get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
            )
        
    def _get_session_history(self, session_id):
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()
        return self.store[session_id]
            
    def chat_with_llm(self, question, session_new):
        if session_new:
            self.session_id = random.random()
        return print(self.conversational_rag_chain.invoke({"input": question}, config={"configurable": {"session_id": self.session_id}})["answer"])
    
    def create_session(self):
        self._prepare_data()
        print('Data Prepared')
        self._create_vector_store()
        print('Vector Store Created')
    
    def set_system_prompt(self, prompt):
        self._prepare_pipeline(prompt)
        print('Pipeline Built')
        
my_assistant = GDPR_AI_Assistant()
my_assistant.create_session()
my_assistant.set_system_prompt("""
                               Using the information contained in the context, give a comprehensive answer to the question.
                               Respond only to the question asked, response should be concise and relevant to the question.
                               If the answer cannot be deduced from the context, do not give an answer.
                               """)
my_assistant.chat_with_llm('How can I transfer data between countries?', True)