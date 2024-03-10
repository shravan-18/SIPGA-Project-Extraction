from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import pandas as pd

from functions import *

# Load environment variables from .env file
load_dotenv()
# Access environment variables
api_key = os.getenv("OPENAI_API_KEY")


def process_spreadsheet(project_title, project_description, OPENAI_API_KEY=api_key):

    template = """Given the following details, I want you to check whether the project is related to AI, Machine
                    Learning, or Deep Learning. If yes, respond with "yes". If not respond with "no". No other response
                    is allowed. 
                    
                    Project Title: {ProjectTitle}
                    Project Description: {ProjectDescription}
                    """

    prompt = PromptTemplate(
        input_variables=["ProjectTitle", "ProjectDescription"],
        template=template,
    )

    # Format the prompt with the project title and description
    prompt.format(
        ProjectTitle=project_title, ProjectDescription=project_description
    )

    llm = ChatOpenAI(
        openai_api_key=os.getenv(OPENAI_API_KEY), temperature=0, model="gpt-3.5-turbo"
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    # Invoke the model with the formatted prompt
    response = chain.run({"ProjectTitle": project_title, "ProjectDescription": project_description})

    return response == "yes"


if __name__ == "__main__":
    df = load_csv("SIPGA_Project_List.csv")
    AI_DF = pd.DataFrame(columns=df.columns)

    for index, row in df.iterrows():
        print(f'Currently Checking Row: {index+1}')
        ProjectTitle = row["Project Title"]
        ProjectDescription = row["Project Description"]
        llm_response = process_spreadsheet(ProjectTitle, ProjectDescription)

        if llm_response:
            AI_DF = pd.concat([AI_DF, pd.DataFrame([row])], ignore_index=True)

    # Reset the index of the new DataFrame
    AI_DF.reset_index(drop=True, inplace=True)
    AI_DF.to_csv("Sipga_AI_Projects.csv")
