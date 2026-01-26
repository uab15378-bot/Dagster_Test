from dagster import define_asset_job

monitoring_job = define_asset_job(
    name="monitoring_job",
    selection=["monitoring_asset"],
)
