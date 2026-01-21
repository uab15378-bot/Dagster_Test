from dagster import Definitions
from .assets import monitoring_asset
from .jobs import monitoring_job  # import your job

defs = Definitions(
    assets=[monitoring_asset],
    jobs=[monitoring_job],  # include the job here
)
