from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key
import os
os.environ['OPENAI_API_KEY'] = openapi_key
llm = OpenAI(temperature=0.6)
def generate_dishes(vegetable,cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['vegetable','cuisine'],
        template="Suggest me only two simple dish to cook something using {vegetable} in {cuisine} style"
    )
    dish_name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="dishes_name")
    prompt_template_item = PromptTemplate(
        input_variables=['dishes_name'],
        template="Give me the receipes for the {dishes_name}"
    )
    receipe_chain = LLMChain(llm=llm, prompt=prompt_template_item, output_key="receipe_items")
    cooking_chain = SequentialChain(
        chains=[dish_name_chain, receipe_chain],
        input_variables=['vegetable','cuisine'],
        output_variables=['dishes_name', 'receipe_items'])
    response = cooking_chain({'vegetable' : vegetable,'cuisine' : cuisine})
    return response

if __name__ == "__main__":
    print(generate_dishes("Potatoe","Indian"))
