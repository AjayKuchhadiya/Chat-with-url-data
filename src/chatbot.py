from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

template = """
**Task:** You are a skilled question-answering agent. Your objective is to analyze the content delimited by #### and respond to the query delimited by &&&& based on that content.

**Expected Behavior:**
- Provide a precise answer to the query based on the given content.

**Points to Consider:**
1. Ensure your response adheres strictly to the provided instructions.
2. Do not include any explanations in your response.

####  
{scraped_content} 
####

&&&&  
{user_query}
&&&&
"""

llm = ChatGroq(temperature=0.0, model_name="Llama3-8b-8192")
prompt = PromptTemplate(template=template, input_variables=["scraped_content", "user_query"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

def generate_response(query, content):
    try:
        # Combine the query and content into one input for memory handling
        response = llm_chain.invoke({"scraped_content": content, "user_query": query})
        return response
    except Exception as e:
        print(f"An error occurred during LLM invocation: {e}")
        return None

def read_scraped_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

# Read the scraped data
content = read_scraped_data('text_storage.txt')
if not content:
    print("No content available to process.")
else:
    while True:
        try:
            query = input('\n\nEnter your query: ')
            response = generate_response(query, content)
            
            if response:
                print('\n\nResponse to your query: ', response['text'])
            else:
                print("Unable to generate a response.")
            
            exit_input = input("\n\nIf you wish to exit, type 'y': ").strip().lower()
            if exit_input == 'y':
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
