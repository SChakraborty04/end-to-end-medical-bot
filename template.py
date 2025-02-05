import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]
for filepath in list_of_files:
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    Path(filepath).touch()
    logging.info(f"File created: {filepath}")