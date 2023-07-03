import os

from dagster import Definitions, load_assets_from_modules
from dagster_dbt import DbtCliClientResource

from dagster_gcp_pandas import BigQueryPandasIOManager

from tutorial_dbt_dagster import assets
from tutorial_dbt_dagster.assets import DBT_PROFILES, DBT_PROJECT_PATH

resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
    ),
   # "io_manager": BigQueryPandasIOManager(database=os.path.join(project=DBT_PROJECT_PATH)),
}

defs = Definitions(assets=load_assets_from_modules([assets]), resources=resources)
