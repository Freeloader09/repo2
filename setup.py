from setuptools import find_packages, setup

setup(
    name="tutorial_dbt_dagster",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-dbt",
        "pandas",
        "dbt-core",
        "dbt-bigquery",
        "dagster-gcp",
        "dagster-gcp-pandas",
        "plotly",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
