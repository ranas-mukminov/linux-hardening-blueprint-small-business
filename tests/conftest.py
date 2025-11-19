import sys
from pathlib import Path

CLI_DIR = Path(__file__).resolve().parents[1] / "cli"
if str(CLI_DIR) not in sys.path:
    sys.path.insert(0, str(CLI_DIR))
