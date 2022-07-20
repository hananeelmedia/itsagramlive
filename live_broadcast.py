import os
from dotenv import load_dotenv
from pathlib import Path
from ItsAGramLive import ItsAGramLive

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

live = ItsAGramLive(
    username=os.getenv('IGL_USERNAME'),
    password=os.getenv('IGL_PASSWORD')
)

live.start()
