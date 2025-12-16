import os
import sys
import logging

logging_str = ['%(asctime)s: %(levelname)s: %(module)s: %(message)s']
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Handlers: always include StreamHandler; add FileHandler only if writable
handlers = [logging.StreamHandler(sys.stdout)]
try:
    os.makedirs(log_dir, exist_ok=True)
    # Test writability by attempting to open the file in append mode
    with open(log_filepath, "a"):
        pass
    handlers.insert(0, logging.FileHandler(log_filepath))
except Exception:
    # In read-only environments (e.g., some notebooks), skip file logging
    pass

logging.basicConfig(
    level=logging.INFO,
    format=logging_str[0],
    handlers=handlers,
)

logger = logging.getLogger("text_summarizer")