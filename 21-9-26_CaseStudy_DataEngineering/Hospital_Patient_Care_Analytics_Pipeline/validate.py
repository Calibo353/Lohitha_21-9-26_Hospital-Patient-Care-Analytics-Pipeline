def validate_data(patients_df, appointments_df):
    print("\nSTEP 3: Validating hospital data...")

    # -----------------------------
    # Validate patient data
    # -----------------------------

    required_patient_columns = [
        "patient_id",
        "patient_name",
        "age",
        "gender",
        "registration_date"
    ]

    for column in required_patient_columns:
        if patients_df[column].isna().any():
            raise ValueError(
                f"Patient data contains missing values in '{column}'."
            )

    if patients_df["patient_id"].duplicated().any():
        raise ValueError("Duplicate patient IDs found.")

    if not patients_df["age"].between(0, 120).all():
        raise ValueError("Patient age must be between 0 and 120.")

    print("Patient data validation successful!")

    # -----------------------------
    # Validate appointment data
    # -----------------------------

    required_appointment_columns = [
        "appointment_id",
        "patient_id",
        "appointment_date",
        "department",
        "doctor_name",
        "wait_time_minutes",
        "status"
    ]

    for column in required_appointment_columns:
        if appointments_df[column].isna().any():
            raise ValueError(
                f"Appointment data contains missing values in '{column}'."
            )

    if appointments_df["appointment_id"].duplicated().any():
        raise ValueError("Duplicate appointment IDs found.")

    if (appointments_df["wait_time_minutes"] < 0).any():
        raise ValueError("Wait time cannot be negative.")

    # Ensure every appointment references an existing patient
    patient_ids = set(patients_df["patient_id"])
    appointment_patient_ids = set(appointments_df["patient_id"])

    unknown_patient_ids = appointment_patient_ids - patient_ids

    if unknown_patient_ids:
        raise ValueError(
            "Appointments reference unknown patient IDs: "
            f"{unknown_patient_ids}"
        )

    print("Appointment data validation successful!")
    print("All data validation checks passed!")

    return True