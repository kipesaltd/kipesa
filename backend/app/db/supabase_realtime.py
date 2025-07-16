from app.core.config import get_settings
from loguru import logger
from supabase import create_client

settings = get_settings()
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


def subscribe_to_table(table_name: str, callback):
    # Example: subscribe to changes in a table
    logger.info(
        f"Subscribing to real-time changes on {table_name}"
    )
    # This is a placeholder; actual implementation depends on supabase-py real-time support
    # supabase.realtime.subscribe(table_name, callback)
    pass


# Usage example:
# def on_income_source_change(payload):
#     logger.info(
#         f"Income source changed: {payload}"
#     )
# subscribe_to_table("income_sources", on_income_source_change)
