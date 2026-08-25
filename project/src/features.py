import pandas as pd


def create_spy_features(df):
   

    df = df.copy()
    df = df.sort_values("date").reset_index(drop=True)

    df["daily_return"] = df["close"].pct_change()

    df["abs_return"] = df["daily_return"].abs()

    df["return_5d"] = df["close"].pct_change(5)

    df["rolling_vol_5"] = (
        df["daily_return"]
        .rolling(window=5)
        .std()
    )

    df["rolling_vol_20"] = (
        df["daily_return"]
        .rolling(window=20)
        .std()
    )

    df["lag_return_1"] = (
        df["daily_return"]
        .shift(1)
    )

    df["lag_abs_return_1"] = (
        df["abs_return"]
        .shift(1)
    )

    return df

def create_future_volatility_target(
    df,
    horizon=5
):


    df = df.copy()

    future_vol = (
        df["daily_return"]
        .rolling(window=horizon)
        .std()
        .shift(-horizon)
    )

    df[f"future_vol_{horizon}d"] = future_vol

    return df