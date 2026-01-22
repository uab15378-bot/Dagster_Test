from dagster import define_asset_job, ScheduleDefinition

# This creates a "Job" named 'api_trigger_job' that runs ONLY 'br_asset'
# This gives you a stable name to call from Postman.
api_trigger_job = define_asset_job(
    name="api_trigger_job",
    selection="br_asset"
)


br_asset_test_schedule = ScheduleDefinition(
    name="br_asset_test_schedule",
    job=api_trigger_job,
    cron_schedule="*/5 * * * *",  # Every 5 minutes
)