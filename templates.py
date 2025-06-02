import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'AI-Career-Advisor'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/api.py",
    f"src/match_score.py",        
    f"src/utils.py",
    f"job_descriptions/job_description.txt"
    f"resumes/sample_resume.txt"
    "requirements.txt",


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")