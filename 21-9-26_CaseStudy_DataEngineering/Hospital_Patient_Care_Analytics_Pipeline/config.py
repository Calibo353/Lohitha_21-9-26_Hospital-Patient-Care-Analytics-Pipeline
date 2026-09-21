from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = DATA_DIR / "output"

# Input file
HOSPITAL_DATA_FILE = DATA_DIR / "hospital_data.csv"

# Output files
CLEAN_PATIENTS_FILE = OUTPUT_DIR / "clean_patients.csv"
CLEAN_APPOINTMENTS_FILE = OUTPUT_DIR / "clean_appointments.csv"

# MySQL configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Lohi@353",
    "database": "hospital_analytics"
}

# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)