import joblib
import pandas as pd
from fastapi.encoders import jsonable_encoder

from src import params


def construct_df(input):
    df = pd.DataFrame(jsonable_encoder(input))
    df = df.set_axis([
        'Patient Age at Treatment',
        'Total Number of Previous IVF cycles',
        'Total number of IVF pregnancies',
        'Total number of live births - conceived through IVF',
        'Type of Infertility - Female Primary',
        'Type of Infertility - Female Secondary',
        'Type of Infertility - Male Primary',
        'Type of Infertility - Male Secondary',
        'Type of Infertility -Couple Primary',
        'Type of Infertility -Couple Secondary',
        'Cause  of Infertility - Tubal disease',
        'Cause of Infertility - Ovulatory Disorder',
        'Cause of Infertility - Male Factor',
        'Cause of Infertility - Patient Unexplained',
        'Cause of Infertility - Endometriosis',
        'Cause of Infertility - Cervical factors',
        'Cause of Infertility - Partner Sperm Concentration',
        'Cause of Infertility -  Partner Sperm Morphology',
        'Causes of Infertility - Partner Sperm Motility',
        'Fresh Cycle',
        'Frozen Cycle',
        'Eggs Thawed',
        'Fresh Eggs Collected',
        'Eggs Mixed With Partner Sperm',
        'Embryos Transfered'
    ], axis=1, inplace=False)

    return df


def predict(input):
    model = joblib.load(f'./{params.model}')

    x_input = construct_df(input)
    y_predicted = model.predict(x_input)

    return y_predicted
