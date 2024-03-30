from flask import Flask, render_template, request
from langchain_community.llms.ollama import Ollama
from langchain.chains.llm import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
import warnings
from flask import jsonify 

from flask import Flask

app = Flask(__name__, static_url_path='/static')




# Suppress warnings
warnings.simplefilter('ignore', DeprecationWarning)

# Define the LLM model
llm = Ollama(model="tinyllama", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), temperature=0.9)

# Define the prompt template
prompt = PromptTemplate(input_variables=["topic"], template="give me 5 interesting facts about {topic}?")

# Create LLMChain instance
chain = LLMChain(llm=llm, prompt=prompt)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        topic = request.form['topic']
        facts = chain.run({"topic": topic})
        return jsonify({"facts": facts})



if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)
