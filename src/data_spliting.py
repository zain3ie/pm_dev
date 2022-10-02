from sklearn.model_selection import train_test_split


def spliting(df):
    x = df.drop(['Live Birth Occurrence'], axis = 1)
    y = df['Live Birth Occurrence'].astype(int)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=6)
    x_test, x_valid, y_test, y_valid = train_test_split(x_test, y_test, test_size=0.2, random_state=6)

    return x_train, x_test, x_valid, y_train, y_test, y_valid
