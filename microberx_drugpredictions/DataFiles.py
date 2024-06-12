"""

"""

__all__ = [
    "load_drugs",
    "load_prediction_descriptors",
    "load_predictions",
    "load_bugdrug_matrix",
    "load_reactiondrug_matrix"
]

from importlib_resources import files
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

__DRUGS = files("microberx_drugpredictions.DataBase").joinpath("DrugBank_Approved_OrallyAdmin.xlsx")
__PREDICTIONS = files("microberx_drugpredictions.DataBase").joinpath("MicrobeRX_predictions.tsv.gz")
__PREDICTIONS_DESCRIPTORS = files("microberx_drugpredictions.DataBase").joinpath("MicrobeRX_Predictions_MolDescriptors.xlsx")
__BUGS_DRUGS = files("microberx_drugpredictions.DataBase").joinpath("Strain_vs_drug.tsv.gz")
__ENZYMES_DRUGS = files("microberx_drugpredictions.DataBase").joinpath("Reaction_vs_drug.tsv.gz")

def load_drugs():
    """
    
    """
    logging.info("Loading MicrobeRX predictions...")
    return pd.read_excel(__DRUGS)

def load_prediction_descriptors():
    """
    
    """
    logging.info("Loading MicrobeRX predictions...")
    return pd.read_excel(__PREDICTIONS_DESCRIPTORS)

def load_predictions():
    """
    
    """
    logging.info("Loading MicrobeRX predictions...")
    return pd.read_csv(__PREDICTIONS, sep="\t", compression="gzip")

def load_bugdrug_matrix():
    """
    
    """
    logging.info("Loading MicrobeRX predictions...")
    return pd.read_csv(__BUGS_DRUGS, sep="\t", compression="gzip",index_col=[0])

def load_reactiondrug_matrix():
    """
    
    """
    logging.info("Loading MicrobeRX predictions...")
    return pd.read_csv(__ENZYMES_DRUGS, sep="\t", compression="gzip",index_col=[0])