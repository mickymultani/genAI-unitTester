import os
import getpass
#note the llama index libary change for imports
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

# Setup OpenAI API key at program run
def setup_api_key():
    os.environ['OPENAI_API_KEY'] = getpass.getpass("Enter OpenAI API Key: ")

# load the prompt from a file
def load_prompt(path="prompt.txt"):
    with open(path, 'r') as file:
        return file.read()

# Create or load index
def load_index(contracts_dir="./contracts", storage_dir="./storage"):
    #  first let's check if storage directory exists and contains the index file
    if not os.path.exists(storage_dir) or not os.path.exists(os.path.join(storage_dir, "docstore.json")):
        print("Index not found, creating a new one...")
        docs = SimpleDirectoryReader(contracts_dir).load_data()
        idx = VectorStoreIndex.from_documents(docs)
        idx.storage_context.persist(persist_dir=storage_dir)
    else:
        print("Loading existing index...")
        storage_ctx = StorageContext.from_defaults(persist_dir=storage_dir)
        idx = load_index_from_storage(storage_ctx)
    return idx

# generate unit tests from indexed documents
def gen_tests():
    prompt = load_prompt()  
    idx = load_index()      
    qe = idx.as_query_engine()
    
    # Make the query explicit in generating unit test code using the prompt
    query = f"{prompt}\n\nPlease follow the prompt"
    result = qe.query(query)
    
    # extract the response text from the query result
    response_text = str(result)  # Convert the Response object to string
    
    # check if the response contains Solidity code or test structure
    if "function" in response_text or "describe(" in response_text:
        print("Generated Unit Tests:\n")
        return response_text
    else:
        return "The model returned an explanation, but no unit test code was generated. Please refine the input or check the document."

if __name__ == "__main__":
    setup_api_key()  
    unit_tests = gen_tests()  
    print(unit_tests)  