import pandas as pd

from config import (
    CLEAN_PATIENTS_FILE,
    CLEAN_APPOINTMENTS_FILE
)

from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data


def save_cleaned_data(patients_df, appointments_df):
    print("\nSTEP 4: Saving cleaned data...")

    patients_df.to_csv(
        CLEAN_PATIENTS_FILE,
        index=False
    )

    appointments_df.to_csv(
        CLEAN_APPOINTMENTS_FILE,
        index=False
    )

    print("Cleaned CSV files saved successfully!")


def run_pipeline():
    print("\n===================================")
    print(" HOSPITAL PATIENT CARE ANALYTICS")
    print("         ETL PIPELINE")
    print("===================================")

    try:
        # Step 1: Extract
        patients_df, appointments_df = extract_data()

        # Step 2: Transform
        patients_df, appointments_df = transform_data(
            patients_df,
            appointments_df
        )

        # Step 3: Validate
        validate_data(
            patients_df,
            appointments_df
        )

        # Step 4: Save cleaned data
        save_cleaned_data(
            patients_df,
            appointments_df
        )

        # Step 5: Load into MySQL
        load_data(
            patients_df,
            appointments_df
        )

        print("\n===================================")
        print(" ETL PIPELINE COMPLETED SUCCESSFULLY!")
        print("===================================")

    except Exception as error:
        print("\nETL PIPELINE FAILED!")
        print(f"Error: {error}")
        raise


if __name__ == "__main__":
    run_pipeline()