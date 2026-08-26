# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.

# Predicting Short-Term SPY Volatility for Portfolio Risk Management

## Project Summary

Financial markets can experience rapid changes in volatility, creating uncertainty for portfolio managers when making investment and risk management decisions. This project aims to examine whether historical market data can be used to predict short-term future volatility of the SPDR S&P 500 ETF (SPY). Using historical price and trading information, the project will develop a predictive model for future realized volatility.

Accurate volatility forecasts can help portfolio managers better understand short-term market risk and make more informed decisions about portfolio exposure. Rather than attempting to predict whether SPY will rise or fall, this project focuses on predicting the magnitude of market fluctuations, which is directly relevant to portfolio risk management.

## Stakeholder & User Context

The primary stakeholder is a **portfolio manager or risk manager** responsible for managing portfolio exposure and controlling investment risk.

The stakeholder needs a clear and timely estimate of expected short-term market volatility. A higher predicted volatility level may indicate increased market uncertainty and could lead the stakeholder to review portfolio exposure or risk limits. The stakeholder therefore cares about the accuracy, stability, interpretability, and practical usefulness of the volatility forecast.

## Useful Answer & Decision

This is primarily a **predictive** problem.

The project will produce a forecast of short-term future realized volatility for SPY based on historical market information. Model performance will be evaluated using appropriate prediction-error metrics such as **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.

The final output should help the stakeholder answer:

**How much market volatility should we expect in the short term, and does the predicted level of risk warrant reviewing current portfolio exposure?**

## Assumptions & Constraints

* Historical SPY market data are sufficiently accurate and available for analysis.
* Historical patterns in volatility contain some information that may help predict future volatility.
* The project focuses on market-level volatility represented by SPY rather than individual-stock risk.
* The model will use information that would have been available at the time of prediction to avoid look-ahead bias.
* The scope is limited to short-term volatility forecasting rather than predicting the direction of SPY returns.
* Model complexity will be kept appropriate for the available data and the scope of the course project.

## Known Unknowns / Risks

* Volatility patterns may change across different market regimes.
* Extreme events may be difficult to predict using historical information.
* Strong historical predictive performance may not persist in future market conditions.
* Different definitions of short-term realized volatility may affect model results.
* A statistically accurate forecast may not necessarily lead to economically meaningful portfolio decisions.

## Goals → Lifecycle → Deliverables Mapping

| Goal                                                                 | Lifecycle Stage                                                | Deliverable                                        |
| -------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------- |
| Define the volatility forecasting problem and stakeholder decision   | Problem Framing & Scoping                                      | README and stakeholder context                     |
| Establish the project environment and workflow                       | Tooling Setup                                                  | GitHub repository and project folder structure     |
| Develop the Python skills required for the analysis                  | Python Fundamentals                                            | Reproducible Python notebooks and scripts          |
| Obtain historical SPY market data                                    | Data Acquisition / Ingestion                                   | Raw SPY market dataset                             |
| Organize and store project data                                      | Data Storage                                                   | Structured data files in `data/`                   |
| Clean and prepare historical market data                             | Data Preprocessing                                             | Cleaned analysis-ready dataset                     |
| Identify unusual observations and extreme market movements           | Outlier Analysis                                               | Outlier analysis and documentation                 |
| Understand historical returns and volatility patterns                | Exploratory Data Analysis                                      | EDA notebook and visualizations                    |
| Construct predictors and the future volatility target                | Feature Engineering                                            | Model-ready feature dataset                        |
| Predict short-term SPY volatility                                    | Modeling (Regression / Time Series / Classification)           | Predictive volatility model                        |
| Evaluate forecast performance and communicate model risks            | Evaluation & Risk Communication                                | MAE, RMSE, model comparison, and risk discussion   |
| Communicate findings to the stakeholder                              | Results Reporting, Delivery Design & Stakeholder Communication | Final report and stakeholder-facing visualizations |
| Make the analysis reusable                                           | Productization                                                 | Reusable forecasting workflow                      |
| Apply the model to new observations and assess performance over time | Deployment & Monitoring                                        | Forecasting and monitoring process                 |
| Connect project components into a reproducible workflow              | Orchestration & System Design                                  | End-to-end project pipeline                        |

## Repo Plan

The project repository will follow the course folder structure:

```text
project/
├── README.md
├── data/
├── src/
├── notebooks/
└── docs/
```

* `data/` will contain raw and processed datasets.
* `src/` will contain reusable Python functions and scripts.
* `notebooks/` will contain exploratory analysis, feature engineering, and modeling work.
* `docs/` will contain stakeholder-facing documentation and other project materials.

The repository will be updated throughout the project lifecycle, with major changes committed and pushed to GitHub as each stage is completed.

## Project Structure

project/
├── data/
│   ├── raw/          # Original unmodified data
│   └── processed/    # Cleaned and transformed data
├── notebooks/        # Exploratory analysis and modeling notebooks
├── src/              # Reusable Python source code
├── docs/             # Project documentation
├── reports/          # Final reports and outputs
├── model/            # Saved model files
├── README.md         # Project overview and documentation
├── .gitignore        # Files excluded from version control
└── requirements.txt  # Python dependencies

## Data Storage

The project separates raw and processed data into two directories:

- `data/raw/` stores the original SPY market data acquired during the data ingestion stage.
- `data/processed/` will store cleaned and transformed datasets created during later preprocessing and feature engineering stages.

Raw SPY market data are currently stored in CSV format because CSV files are simple, portable, and easy to inspect. Processed datasets may later be stored in Parquet format to preserve data types and support more efficient storage and loading.

Data paths are configured using environment variables in the local `.env` file. The pipeline reads `DATA_DIR_RAW` and `DATA_DIR_PROCESSED` using `os.getenv()` rather than relying on machine-specific absolute paths. The `.env` file is excluded from version control, while `.env.example` documents the required configuration.

The project pipeline reloads stored SPY data with pandas and validates key fields such as the date and closing price columns before the data are used in later stages.

## Data Preprocessing

Raw SPY market data are cleaned before exploratory analysis and modeling.

The preprocessing pipeline:

- converts the `date` column to pandas datetime format,
- converts `close` values to numeric format,
- removes observations with missing dates or closing prices,
- removes duplicate trading dates,
- removes non-positive closing prices,
- sorts observations chronologically,
- and resets the DataFrame index.

Missing SPY closing prices are not imputed because artificial price values could distort subsequent return and volatility calculations. Since the project uses daily market data, each trading date is expected to correspond to one observation.

Feature scaling is not applied at this stage. Scaling decisions will be made later based on the modeling approach to reduce the risk of data leakage.

The cleaned dataset is stored in `data/processed/spy_clean.csv`.

## Outlier Analysis

Potential outliers are identified using the IQR rule applied to SPY daily returns. An observation is flagged when its return falls below Q1 − 1.5×IQR or above Q3 + 1.5×IQR.

Outliers are flagged rather than automatically removed. Extreme daily returns may represent genuine market stress events, such as crash or rebound days, and these observations are directly relevant to a volatility forecasting project.

The analysis therefore retains extreme observations in the primary dataset while comparing summary statistics with and without IQR-flagged observations as a sensitivity check.

Z-score detection may be used as a secondary diagnostic, but it is not used as the primary rule because financial returns may exhibit heavy tails and may not be approximately normally distributed.

Any future removal or winsorization of extreme observations will be reported explicitly and evaluated through sensitivity analysis.

## EDA Insights

1. SPY closing prices show a long-term upward trend, so the price level itself may not be stationary and may be less appropriate than returns for short-term volatility modeling.

2. Daily returns are centered near zero but contain several extreme positive and negative observations.

3. The return distribution shows heavy tails, suggesting that extreme market movements occur more frequently than would be expected under a normal distribution.

4. Large absolute returns appear to cluster in particular periods, suggesting volatility persistence.

5. These findings motivate the use of lagged returns and rolling volatility measures as candidate features in the next stage.

## Feature Engineering

The following features are constructed from historical SPY market data for short-term volatility forecasting:

- **daily_return** — one-day percentage change in SPY closing price.
- **abs_return** — absolute daily return, representing the magnitude of market movement independent of direction.
- **return_5d** — percentage change in SPY price over the previous five trading days.
- **rolling_vol_5** — standard deviation of daily returns over the previous five trading days, representing recent short-term volatility.
- **rolling_vol_20** — standard deviation of daily returns over the previous twenty trading days, representing the broader recent volatility environment.
- **lag_return_1** — previous trading day's return.
- **lag_abs_return_1** — magnitude of the previous trading day's return.

These features are motivated by the persistence and clustering of financial market volatility observed during exploratory data analysis.

The modeling target is **future_vol_5d**, representing realized volatility over the next five trading days. Predictor features use only information available at or before the prediction date to reduce the risk of look-ahead bias.

## Modeling Assumptions and Risks

- The regression assumes that the engineered predictors have an approximately linear relationship with future volatility.
- Financial time-series observations may exhibit autocorrelation, so residual independence may not hold perfectly.
- Volatility may exhibit heteroskedasticity and heavy-tailed prediction errors, especially during market stress periods.
- The chronological train-test split prevents future observations from being used to train models for earlier periods.
- Results describe predictive relationships and should not be interpreted as causal effects.