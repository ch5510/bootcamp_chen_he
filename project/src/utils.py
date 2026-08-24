import pandas as pd


def parse_date_column(df, column="Date"):
    """
    Convert a date column to pandas datetime format.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.
    column : str
        Name of the date column.

    Returns
    -------
    pandas.DataFrame
        DataFrame with the converted date column.
    """
    df = df.copy()
    df[column] = pd.to_datetime(df[column])

    return df