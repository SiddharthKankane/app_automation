import os
from pathlib import Path

# ==============================================================================
# 1. DIRECTORY STRUCTURE PATHS
# ==============================================================================
# Resolves the absolute root directory of your test automation framework
BASE_DIR = Path(__file__).parent.resolve()

# Directory path for dynamic and manual test data matrices
DATA_DIR = BASE_DIR / "data"

# Automatically verify and create the data directory layout if it doesn't exist
DATA_DIR.mkdir(parents=True, exist_ok=True)