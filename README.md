# Cliq Dashboard Databricks DAB

This repository contains a **Databricks Asset Bundle (DAB)** project designed to process and optimize **check-in and check-out** records from *Cliq*.
Through a **declarative pipeline**, the project transforms raw data into a clean, reliable dataset ready for use in an **analytical dashboard**.

---

## Key Features

* Ingestion of check-in and check-out records from CSV files.
* Job triggered automatically upon file arrival.
* Data cleansing, normalization, and standardization.
* Declarative pipeline built using Databricks Asset Bundles (DAB).
* Generation of optimized tables ready for analytics and dashboarding.
* Reproducible and portable architecture, version-controlled through DAB.
* Data quality validation using expectations.

---

## Project Architecture

The project leverages essential components from the Databricks ecosystem:

* **Databricks Asset Bundles (DAB)** for packaging configurations, pipelines, and assets.
* **Declarative workflows** for pipeline execution.
* **Notebooks** and ETL scripts for data processing.
* **Delta Lake** as the primary data storage format.

> The repository structure follows recommended practices for DAB-based projects, ensuring consistent deployments across environments.

---

## Dashboard Purpose

The pipeline produces a final table designed to support dashboards that provide:

* Visualization of check-in and check-out times per user.
* Calculation of daily working shifts.
* Average working hours per day grouped by week.
* Total weekly hours worked.

---

## Repository Structure

```
cliq_dashboard_databricks_dab/
├── databricks.yml
├── fixtures/
├── pyproject.toml
├── README.md
├── resources/
│   ├── cliq_dashboard_etl.pipeline.yml
│   └── cliq_dashboard_job.job.yml
├── src/
│   ├── cliq_dashboard_etl/
│   │   ├── explorations/
│   │   │   ├── explore_data.py
│   │   │   └── sample_exploration.ipynb
│   │   ├── README.md
│   │   ├── setup/
│   │   │   ├── reset_catalog.py
│   │   │   └── setup.py
│   │   └── transformations/
│   │       ├── 1_csv_2_bronze.py
│   │       ├── 2_bronze_2_users_silver.py
│   │       ├── 3_bronze_2_data_silver.py
│   │       ├── 4_silver_2_sum_by_day_gold.py
│   │       └── 5_view_shifts_gold.py
│   ├── img/
│   │   └── pipeline.png
│   └── sample_notebook.ipynb
├── tests/
│   └── conftest.py
└── uv.lock
```

---

## Using This Project with the CLI

Databricks Workspaces and IDE extensions provide graphical interfaces for interacting with this project, but it can also be used directly via the CLI:

1. Authenticate to your Databricks workspace:

   ```
   databricks configure
   ```

2. Deploy a development copy of the project:

   ```
   databricks bundle deploy --target dev
   ```

   *(“dev” is the default target, so the `--target` flag is optional.)*

   This deploys all resources defined in the project.
   For example, it deploys a pipeline named
   **[dev yourname] cliq_dashboard_etl**
   which you can find under **Jobs & Pipelines** in your workspace.

3. To deploy a production version:

   ```
   databricks bundle deploy --target prod
   ```

   The default template includes a job scheduled to run the pipeline daily
   (defined in `resources/sample_job.job.yml`).
   This schedule is automatically paused in development mode.
   More details: [https://docs.databricks.com/dev-tools/bundles/deployment-modes.html](https://docs.databricks.com/dev-tools/bundles/deployment-modes.html)

4. To run a job or pipeline:

   ```
   databricks bundle run
   ```

5. To run tests locally:

   ```
   uv run pytest
   ```

---

## Getting Started

Choose how you want to work with this project:

**(a)** Directly in your Databricks Workspace:
[https://docs.databricks.com/dev-tools/bundles/workspace](https://docs.databricks.com/dev-tools/bundles/workspace)

**(b)** Locally using an IDE such as Cursor or VS Code:
[https://docs.databricks.com/dev-tools/vscode-ext.html](https://docs.databricks.com/dev-tools/vscode-ext.html)

**(c)** Using command-line tools:
[https://docs.databricks.com/dev-tools/cli/databricks-cli.html](https://docs.databricks.com/dev-tools/cli/databricks-cli.html)

If you're developing with an IDE, dependency management uses **uv**:

* Ensure the UV package manager is installed:
  [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)
* Install project dependencies:

  ```
  uv sync --dev
  ```

---

## Contributing

Contributions are welcome!
If you want to improve the pipeline, enhance documentation, or extend the ETL logic, please open an **issue** or submit a **pull request**.

