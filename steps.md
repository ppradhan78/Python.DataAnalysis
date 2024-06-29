STEPS:
Github Repository Setup
1)Create a git Repo

Virtual enviroment Setup

2)Create Virtual enviroment
python -m venv <venvname>
python -m venv venv_pda
or
conda create -n <venvname> python=<version> -y
3)Activate Virtual enviroment
  run the activate script from script folder
 .\<venvname>\Scripts\activate
 .\venv_pda\Scripts\activate
 or
conda activate <venvname>
 Project templete structure Setup

 4)template.py
 5) run template.py to create Project templete structure
 python template.py

 Installation of package 
pip install -r requirements.txt
 Research 
Jupiter .ipynb file before execute select the kernal
streamlit run app.py