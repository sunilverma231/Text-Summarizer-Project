import os
import sys

# Ensure local package under ./src is importable when running directly
PROJECT_ROOT = os.path.dirname(__file__)
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
	sys.path.insert(0, SRC_PATH)

from text_summarizer.logging import logger


def main() -> None:
	logger.info("This is a log message from main.py")


if __name__ == "__main__":
	main()