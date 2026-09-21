import pandas as pd
from config import HOSPITAL_DATA_FILE


def extract_data():
    print("\nSTEP 1: Extracting hospital data...")

    # Check whether the input file exists
    if not HOSPITAL_DATA_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {HOSPITAL_DATA_FILE}"
        )

    # Read combined hospital data
    hospital_df = pd.read_csv(HOSPITAL_DATA_FILE)

    if hospital_df.empty:
        raise ValueError("Hospital data file is empty.")

    print("Combined hospital data loaded successfully.")
    print(f"Total records: {len(hospital_df)}")

    # Patient columns
    patient_columns = [
        "patient_id",
        "patient_name",
        "age",
        "gender",
        "registration_date"
    ]

    # Appointment columns
    appointment_columns = [
        "appointment_id",
        "patient_id",
        "appointment_date",
        "department",
        "doctor_name",
        "wait_time_minutes",
        "status"
    ]

    # Check required columns
    required_columns = set(patient_columns + appointment_columns)
    missing_columns = required_columns - set(hospital_df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing columns in CSV: {sorted(missing_columns)}"
        )

    # Extract unique patients
    patients_df = (
        hospital_df[patient_columns]
        .drop_duplicates(subset=["patient_id"])
        .copy()
    )

    # Extract appointments
    appointments_df = hospital_df[appointment_columns].copy()

    print(f"Patients extracted: {len(patients_df)}")
    print(f"Appointments extracted: {len(appointments_df)}")

    return patients_df, appointments_df