"""Job example: standalone, loads local .env, logs and exits with code.

- Keep this file self-contained so Render can run it directly.
- Use `python-dotenv` to read `.env` in the same folder for local dev.
"""
from pathlib import Path
import logging
import sys
import os

from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables from job-local .env (local dev). Render will supply envs.
env_path = Path(__file__).with_name('.env')
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

def main() -> int:
    # Example config from env
    example_val = os.getenv('EXAMPLE_KEY', None)

    logger.info('Starting job_example')
    logger.info('This is example job — logs will show this message when it runs.')
    if not example_val:
        logger.warning('EXAMPLE_KEY not set — using default behavior')

    try:
        # Put your job logic here
        logger.info('Running job logic...')
        # Simulate work
        logger.info(f'example key value: {example_val}')

        # Success
        logger.info('Job finished successfully')
        return 0
    except Exception as exc:
        logger.exception('Job failed: %s', exc)
        return 2

if __name__ == '__main__':
    code = main()
    sys.exit(code)
