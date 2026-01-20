from dagster import asset, Output 
import os
import random
from datetime import datetime

@asset
def br_asset():
    """
    Sample asset named 'br_asset' with visible Metadata.
    """
    current_env = os.getenv("ENV_VARIABLE", "Unknown Environment")

    total_users = random.randint(1000, 5000)
    active_users = int(total_users * random.uniform(0.4, 0.8))

    metrics = {
        "status": "Success",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment_source": current_env, 
        "total_users": total_users,
        "active_users": active_users
    }

    return Output(
        value=metrics,
        metadata=metrics
    )
    
