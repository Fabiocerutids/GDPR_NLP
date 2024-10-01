import json
from access_token import *
from sentence_transformers import SentenceTransformer
import time
import os 

from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
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
        self.vectorstore.save_local("data/vectorstore")
        
    def _load_vector_store(self):
        embedding_model = HuggingFaceEmbeddings(model_name=self.embedding_model,
                                                encode_kwargs={"normalize_embeddings": True})
        self.vectorstore = FAISS.load_local("data/vectorstore", embedding_model, allow_dangerous_deserialization=True)
        
    def _prepare_pipeline(self, system_prompt, temperature, max_new_tokens):
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
        temperature=temperature,
        repetition_penalty=1.1,
        return_full_text=False,
        max_new_tokens=max_new_tokens,
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
        
#    def _summarize_history(self):
#        stored_messages = self.store[self.session_id]
#        prompt_template = """Write a concise summary of the following:
#                            "{text}"
#                            CONCISE SUMMARY:"""
#        prompt = PromptTemplate.from_template(prompt_template)
#        llm = HuggingFaceEndpoint(
#            repo_id=self.generator_model,
#            task="text-generation",
#            do_sample=True,
#            temperature=0.1,
#            repetition_penalty=1.1,
#            return_full_text=False,
#            max_new_tokens=400,
#            huggingfacehub_api_token=my_huggingface_token
#            )
#        llm_chain = LLMChain(llm=llm, prompt=prompt)
#        stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
#        return stuff_chain.run(stored_messages)
        
    def _get_session_history(self, session_id):
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()       
        return self.store[session_id]
            
    def chat_with_llm(self, question, session_new):
        if session_new:
            self.session_id = time.strftime("%b %d %Y %H:%M:%S", time.localtime())
        print(self.store)
        return self.conversational_rag_chain.invoke({"input": question}, config={"configurable": {"session_id": self.session_id}})["answer"]
    
    def create_session(self):
        self._prepare_data()
        print('Data Prepared')
        if 'vectorstore' in os.listdir('data'):
            self._load_vector_store()
        else:
            self._create_vector_store()
        print('Vector Store Created')
    
    def set_system_parameters(self, prompt, temperature=0.1, max_new_tokens=500):
        self._prepare_pipeline(prompt, temperature, max_new_tokens)
        print('Pipeline Built')
        self.store = {}