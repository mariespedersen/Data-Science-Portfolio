####################################
# Setup Kaggle API
####################################

# Step 1: Open and load the JSON file
import json
with open('../kaggle.json', 'r') as file:
    kaggle_info = json.load(file)
    
# Step 2: Set the Kaggle API key
import os
os.environ['KAGGLE_USERNAME'] = kaggle_info['username']
os.environ['KAGGLE_KEY'] = kaggle_info['key']