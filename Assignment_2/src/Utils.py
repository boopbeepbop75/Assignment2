from pathlib import Path
import Utils as U

PROJECT_DIR = Path(__file__).parent.parent
CLEAN_DATA_FOLDER = (PROJECT_DIR / 'data_clean').resolve()
RAW_DATA_FOLDER = (PROJECT_DIR / 'data_raw').resolve()

data = (U.RAW_DATA_FOLDER / 'data_raw.csv').resolve()
clean_data = (U.CLEAN_DATA_FOLDER / 'data_clean.csv').resolve()
