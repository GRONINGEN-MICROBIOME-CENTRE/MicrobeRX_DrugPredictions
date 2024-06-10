"""

"""

__all__ = ["",
]


from importlib_resources import files
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


__PREDICTIONS = files("microberx_drugpredictions.DataBase").joinpath("MicrobeRX_predictions.tsv")


def load_predictions():
    """
    
    """
    logging.info("Loading MicrobeRX predictions...")
    return pd.read_csv(__PREDICTIONS, sep="\t", compression="gzip")
