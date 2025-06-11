import time
import signal
import sys
import logging
import os
from fake_store_analyzer import main_analyzer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def signal_handler(sig, frame):
    logging.info("Shutdown signal received, exiting gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def run_service(interval_minutes):
    interval_seconds = interval_minutes * 60
    while True:
        try:
            logging.info("Running fake_store_analyzer...")
            results = main_analyzer()
            logging.info(f"Results: {results}")
        except Exception as e:
            logging.error(f"Error during analysis: {e}", exc_info=True)
        logging.info(f"Sleeping for {interval_minutes} minutes...")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    INTERVAL_MINUTES = float(os.getenv("INTERVAL_MINUTES", 0.5))
    run_service(INTERVAL_MINUTES)