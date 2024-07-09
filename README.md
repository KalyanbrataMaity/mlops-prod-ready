# MLOps-Production-Ready-Machine-Learning-Project

- Python 3.6 or above
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com
- Flowchart: https//whimsical.com/
- MLOps Tool: https://www.evidentlyai.com
- MongoDB: https://account.mongodb.com/account/login

## Git commands
- Push to github
```
git add .
git commit -m "commit message"
git push origin main 
```

## How to run?
- First create and activate an environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
- Install required packages
```bash
python3 -m pip install requirements.txt
```

NOTE: You will see ``` -e . ```. This is used to set up the project as my local package. Once you run the requirements.txt, it will search for the constructor files ```__init__.py``` and wherever it finds the file it will consider that folder as a local package. This will help to import files as packages like: ```from us_visa.components import data_ingestion```. Now if do ```pip list``` operation you will see us_visa has been added in the installed packages list.
