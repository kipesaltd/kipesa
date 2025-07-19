from loguru import logger


async def send_email_background(email: str, subject: str, body: str):
    # Placeholder for async email sending logic
    logger.info(f"Sending email to {email}: {subject}")
    # Simulate async work
    # await some_async_email_lib.send(email, subject, body)
    pass


async def process_heavy_calculation(data):
    # Placeholder for heavy async calculation
    logger.info(f"Processing heavy calculation for {data}")
    # await some_async_calculation(data)
    pass
 