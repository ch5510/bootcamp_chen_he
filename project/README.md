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