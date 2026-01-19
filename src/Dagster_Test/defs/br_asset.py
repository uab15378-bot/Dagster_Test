from dagster import asset, Output  # <--- Added Output import
import random
from datetime import datetime

@asset
def br_asset():
    """
    Sample asset named 'br_asset' with visible Metadata.
    """
    # 1. Simulate fetching dummy data
    total_users = random.randint(1000, 5000)
    active_users = int(total_users * random.uniform(0.4, 0.8))

    # 2. Create the dictionary
    metrics = {
        "status": "Branch Deployment Success",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_users": total_users,
        "active_users": active_users
    }

    # 3. Return as Output with Metadata (This makes it visible in UI)
    return Output(
        value=metrics,      # The actual data passed to downstream assets
        metadata=metrics    # The data shown in the UI
    )