"""Job template — standalone, self-contained job script.

- Loads `.env` from same folder during local development using python-dotenv.
- Reads config from environment variables (preferred in Render production).
- Returns exit codes: 0 success, non-zero failure.
"""
from pathlib import Path
import logging
import os
import sys

from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Load local .env when present (local dev convenience)
env_path = Path(__file__).with_name('.env')
if env_path.exists():
    load_dotenv(dotenv_path=env_path)


def run_job() -> None:
    """Put job logic here. Keep it small and idempotent."""
    # Example access to an env var
    example_key = os.getenv('EXAMPLE_KEY')

    logger.info('This is job_template — starting job')
    if not example_key:
        logger.warning('EXAMPLE_KEY not set — run with a .env file locally or set env var in Render')

    # Example work (replace with your real logic)
    logger.info('Performing dummy work...')
    # Simulate reading/writing, calling APIs, etc.
    logger.info('example key value: %s', example_key)


def main() -> int:
    try:
        run_job()
        logger.info('Job completed successfully')
        return 0
    except Exception as exc:
        logger.exception('Job failed: %s', exc)
        return 1


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
