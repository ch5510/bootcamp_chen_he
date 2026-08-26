import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def regression_metrics(y_true, y_pred):
    """
    Calculate regression performance metrics.
    """

    return {
        "MAE": mean_absolute_error(
            y_true,
            y_pred
        ),

        "RMSE": mean_squared_error(
            y_true,
            y_pred
        ) ** 0.5,

        "R2": r2_score(
            y_true,
            y_pred
        )
    }


def bootstrap_rmse(
    y_true,
    y_pred,
    n_boot=1000,
    seed=42
):
    """
    Estimate uncertainty around RMSE
    using bootstrap resampling.
    """

    rng = np.random.default_rng(seed)

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    n = len(y_true)

    rmse_values = []

    for _ in range(n_boot):

        idx = rng.integers(
            0,
            n,
            size=n
        )

        rmse = mean_squared_error(
            y_true[idx],
            y_pred[idx]
        ) ** 0.5

        rmse_values.append(rmse)

    return np.array(rmse_values)