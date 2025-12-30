from prompts import generate_paper_analysis_prompt
from pydantic_classes import PaperCard
from langchain_core.output_parsers import JsonOutputParser
from groq_call import run_groq_api
import json
import pandas as pd
import os

def generate_feed(paper_contents):
    try:
        parser = JsonOutputParser(pydantic_object=PaperCard)
        results = []
        for url, content in paper_contents.items():
            paper_content = content['results'][0]["raw_content"]
            prompt = generate_paper_analysis_prompt(paper_content)
            response = run_groq_api(prompt)
            response_parsed = parser.parse(response)
            response_parsed["url"] = url
            results.append(response_parsed)
        
        results_df = pd.DataFrame(results)
        
        if os.path.exists("data/history.csv"):
            existing_df = pd.read_csv("data/history.csv")
            df = pd.concat((existing_df,results_df))
            df.to_csv('data/history.csv',index=False)
        else:
            results_df.to_csv("data/history.csv",index=False)
        
        return results
    except:
        return None
        
if __name__ == "__main__":
    paper_contents = json.load(open("data/paper_content.json","r"))
    generate_feed(paper_contents)