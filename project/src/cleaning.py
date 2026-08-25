import pandas as pd


def clean_spy_data(df):
    """
    Clean raw SPY market data for downstream analysis.

    Steps:
    1. Convert the date column to datetime.
    2. Convert close prices to numeric.
    3. Remove rows with missing date or close values.
    4. Remove duplicate dates.
    5. Remove non-positive close prices.
    6. Sort observations chronologically.
    7. Reset the DataFrame index.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw SPY market data containing `date` and `close`.

    Returns
    -------
    pandas.DataFrame
        Cleaned SPY dataset.
    """

    df_clean = df.copy()

    df_clean["date"] = pd.to_datetime(
        df_clean["date"],
        errors="coerce"
    )

    df_clean["close"] = pd.to_numeric(
        df_clean["close"],
        errors="coerce"
    )

    df_clean = df_clean.dropna(
        subset=["date", "close"]
    )

    df_clean = df_clean.drop_duplicates(
        subset=["date"]
    )

    df_clean = df_clean[
        df_clean["close"] > 0
    ]

    df_clean = df_clean.sort_values(
        "date"
    )

    df_clean = df_clean.reset_index(
        drop=True
    )

    return df_clean