from pydantic import BaseModel, Field


class Input(BaseModel):
    patient_age: int = Field('Patient Age at Treatment')
    previous_ivf: int = Field('Total Number of Previous IVF cycles')
    ivf_pregnancies: int = Field('Total number of IVF pregnancies')
    live_births: int = Field('Total number of live births - conceived through IVF')
    female_primary: int = Field('Type of Infertility - Female Primary')
    female_secondary: int = Field('Type of Infertility - Female Secondary')
    male_primary: int = Field('Type of Infertility - Male Primary')
    male_secondary: int = Field('Type of Infertility - Male Secondary')
    couple_primary: int = Field('Type of Infertility - Couple Primary')
    couple_secondary: int = Field('Type of Infertility - Couple Secondary')
    tubal_desease: int = Field('Cause  of Infertility - Tubal disease')
    ovulatory_disorder: int = Field('Cause of Infertility - Ovulatory Disorder')
    male_factor: int = Field('Cause of Infertility - Male Factor')
    unexplained: int = Field('Cause of Infertility - Patient Unexplained')
    endometriosis: int = Field('Cause of Infertility - Endometriosis')
    cervical_factors: int = Field('Cause of Infertility - Cervical factors')
    sperm_concentration: int = Field('Cause of Infertility - Partner Sperm Concentration')
    sperm_morphology: int = Field('Cause of Infertility -  Partner Sperm Morphology')
    sperm_motility: int = Field('Cause of Infertility - Partner Sperm Motility')
    fresh_cycle: float = Field('Fresh Cycle')
    frozen_cycle: float = Field('Frozen Cycle')
    eggs_thawed: float = Field('Eggs Thawed')
    fresh_eggs: int = Field('Fresh Eggs Collected')
    eggs_mixed: int = Field('Eggs Mixed With Partner Sperm')
    embryos_transfered: int = Field('Embryos Transfered')