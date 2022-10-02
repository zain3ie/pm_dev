def filter(df):
    ref_feature = [
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
        'Embryos Transfered',
        'Live Birth Occurrence',
        'Number of Live Births'
    ]
    df = df[ref_feature]

    return df


def patient_age_at_reatment(df):
    age_mapping = {
        '18 - 34': 0,
        '35-37': 1,
        '38-39': 2,
        '40-42': 3,
        '43-44': 4,
        '45-50': 5
    }

    df = df[df['Patient Age at Treatment'] != '999']
    df['Patient Age at Treatment'] = df['Patient Age at Treatment'].map(age_mapping)

    return df


def live_birth_occurrence(df):
    df['Live Birth Occurrence'] = df['Live Birth Occurrence'].fillna(0)
    df = df.drop('Number of Live Births', axis=1)

    return df


def remove_missing_data(df):
    df = df[df['Fresh Cycle'].notnull()]

    return df


def clearing_data(df):
    df = df[df['Total Number of Previous IVF cycles'] != '>=5']
    df = df[df['Total number of IVF pregnancies'] != '>=5']
    df = df[df['Fresh Eggs Collected'] != '> 50']
    df = df[df['Eggs Mixed With Partner Sperm'] != '> 50']

    return df
