from dagster import asset
import random
from datetime import datetime

@asset
def br_asset():
    """
    Sample asset named 'br_asset' for the Branch Deployment PoC.
    """
    # 1. Simulate fetching dummy data
    total_users = random.randint(1000, 5000)
    active_users = int(total_users * random.uniform(0.4, 0.8))

    # 2. Return the data
    return {
        "status": "Branch Deployment Success",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_users": total_users,
        "active_users": active_users
    }