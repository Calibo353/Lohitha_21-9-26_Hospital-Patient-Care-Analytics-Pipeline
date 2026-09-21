import pandas as pd


def transform_data(patients_df, appointments_df):
    print("\nSTEP 2: Transforming hospital data...")

    patients_df = patients_df.copy()
    appointments_df = appointments_df.copy()

    # -----------------------------
    # Transform patient data
    # -----------------------------

    # Remove extra spaces from text columns
    for column in ["patient_id", "patient_name", "gender"]:
        patients_df[column] = (
            patients_df[column]
            .astype("string")
            .str.strip()
        )

    # Convert age to numeric
    patients_df["age"] = pd.to_numeric(
        patients_df["age"],
        errors="coerce"
    )

    # Convert registration date
    patients_df["registration_date"] = pd.to_datetime(
        patients_df["registration_date"],
        errors="coerce"
    )

    # Normalize gender formatting
    patients_df["gender"] = (
        patients_df["gender"]
        .str.capitalize()
    )

    print("Patient data transformation completed!")

    # -----------------------------
    # Transform appointment data
    # -----------------------------

    for column in [
        "appointment_id",
        "patient_id",
        "department",
        "doctor_name",
        "status"
    ]:
        appointments_df[column] = (
            appointments_df[column]
            .astype("string")
            .str.strip()
        )

    # Convert appointment date
    appointments_df["appointment_date"] = pd.to_datetime(
        appointments_df["appointment_date"],
        errors="coerce"
    )

    # Convert wait time to numeric
    appointments_df["wait_time_minutes"] = pd.to_numeric(
        appointments_df["wait_time_minutes"],
        errors="coerce"
    )

    # Normalize status formatting
    appointments_df["status"] = (
        appointments_df["status"]
        .str.capitalize()
    )

    print("Appointment data transformation completed!")

    return patients_df, appointments_df