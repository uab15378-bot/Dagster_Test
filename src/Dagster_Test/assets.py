import time
import random
from dagster import asset, Output, MetadataValue

@asset
def monitoring_asset(context):
    # ---------------------------------
    # DELAY PIPELINE START (2 minutes)
    # ---------------------------------
    delay_seconds = 200
    context.log.info(f"Delaying pipeline start by {delay_seconds} seconds...")
    time.sleep(delay_seconds)

    # ---------------------------------
    # Simulate pipeline execution
    # ---------------------------------
    total_steps = 6
    step_duration = 30  # seconds per step

    for i in range(total_steps):
        context.log.info(f"Running step {i + 1}/{total_steps}")
        time.sleep(step_duration)

    runtime_seconds = total_steps * step_duration

    # ---------------------------------
    # Success / Failure decision
    # ---------------------------------
    success = random.choice([True, False])

    pipeline_success = 1 if success else 0
    failure_alert = 0 if success else 1  # IMPORTANT for alert chart

    context.log.info(
        f"Pipeline finished with status: {'SUCCESS' if success else 'FAILURE'}"
    )

    if not success:
        context.log.error("ALERT: Pipeline FAILED!")

    # ---------------------------------
    # Emit metrics → AUTO CHARTS
    # ---------------------------------
    yield Output(
        value=None,
        metadata={
            # MAIN STATUS CHART
            "pipeline_success": MetadataValue.int(pipeline_success),

            # RUNTIME CHART
            "runtime_seconds": MetadataValue.int(runtime_seconds),

            # FAILURE ALERT CHART (only spikes on failure)
            "failure_alert": MetadataValue.int(failure_alert),
        },
    )
