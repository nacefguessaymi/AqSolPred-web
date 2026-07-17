"""
Created on Sun Oct 18 14:54:37 2020

@author: Murat Cihan Sorkun
"""

######################
# Import libraries
######################
import base64
import pickle

import pandas as pd
import predefined_models
import streamlit as st
import xgboost
from PIL import Image
from rdkit import Chem
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.neural_network import MLPRegressor


######################
# Custom function
######################
## Calculate molecular descriptors


######################
# Page Title
######################


# st.set_page_config(page_title="AqSolPred: Online Solubility Prediction Tool")


st.write("""# AqSolPred: Aqueous Solubility Prediction Tool""")

st.image("static/solubility-factors.png", use_column_width=False)


######################
# Input molecules (Side Panel)
######################

st.sidebar.write("**Type SMILES below**")

## Read SMILES input
SMILES_input = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C\nCC(=O)OC1=CC=CC=C1C(=O)O"

SMILES = st.sidebar.text_area("then press ctrl+enter", SMILES_input)
SMILES = SMILES.split("\n")
SMILES = list(filter(None, SMILES))


st.sidebar.write("""---------**OR**---------""")
st.sidebar.write("""**Upload a file with a column named 'SMILES'** (Max:2000)""")


uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    # data
    SMILES = data["SMILES"]


# st.header('Input SMILES')
# SMILES[1:] # Skips the dummy first item

# Use only top 300
if len(SMILES) > 2000:
    SMILES = SMILES[0:2000]

## Calculate molecular descriptors
df_results = pd.DataFrame(SMILES, columns=["SMILES"])
df_results["LogS (AqSolPred v1.1s)"] = pred_consensus
df_results = df_results.round(3)


st.header("Predicted LogS values")
df_results  # Skips the dummy first item

# download=st.button('Download Results File')
# if download:
csv = df_results.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings
linko = f'<a href="data:file/csv;base64,{b64}" download="aqsolpred_predictions.csv">Download csv file</a>'
st.markdown(linko, unsafe_allow_html=True)

st.header("Computed molecular descriptors")
generated_descriptors  # Skips the dummy first item


st.write("""
# About AqSolPred

AqSolPred is a highly accurate solubility prediction model that consists of a consensus of 3 ML algorithms (Neural Nets, Random Forest, and XGBoost). It is developed using a quality-oriented data selection method described in [1] and trained on AqSolDB [2], the largest publicly available aqueous solubility dataset.

AqSolPred showed a top performance (0.348 LogS Mean Absolute Error) on the Huuskonen benchmark dataset [3].

**version:** 1.1s (lite version of v1.0 described in the paper without random forest model)

If you are using the predictions from AqSolPred in your work, please cite these papers: [1, 2]

[1] Sorkun, M. C., Koelman, J.M.V.A. & Er, S. (2021). [Pushing the limits of solubility prediction via quality-oriented data selection](https://www.cell.com/iscience/fulltext/S2589-0042(20)31158-5), iScience, 24(1), 101961.

[2] Sorkun, M. C., Khetan, A., & Er, S. (2019).  [AqSolDB, a curated reference set of aqueous solubility and 2D descriptors for a diverse set of compounds](https://www.nature.com/articles/s41597-019-0151-1). Scientific data, 6(1), 1-8.

[3] Huuskonen, J. Estimation of aqueous solubility for a diverse set of organic compounds based on molecular topology. Journal of Chemical Information and Computer Sciences 40, 773–777 (2000).

Special thanks: This web app is developed based on the tutorials and the template of [DataProfessor's repository](https://github.com/dataprofessor/code/tree/master/streamlit/part7). 

                                                                                         
**Contact:** [Murat Cihan Sorkun](https://www.linkedin.com/in/murat-cihan-sorkun/)

""")
