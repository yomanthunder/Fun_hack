import os 
from dotenv import load_dotenv
from mira_sdk import MiraClient,Flow
load_dotenv()
api_key = os.getenv("MIRA_API_KEY")

client = MiraClient(config={"API_KEY": api_key})

flow = Flow(source="flow.yaml")

input_dict = {"topic": "Hard Life", "style": "Lil Wayne"}

response = client.flow.test(flow, input_dict)

print(response)