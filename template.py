import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Python.DataAnalysis"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/components/preprocessor.py",
    f"src/{project_name}/logging/__init__.py", 
    f"src/{project_name}/exceptionhandler/__init__.py", 
    f"src/{project_name}/utils/helper.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/OlympicsDataAnalysis.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
