import pandas as pd
import mysql.connector

from config import DB_CONFIG


def create_tables(connection):
    cursor = connection.cursor()

    # Patient table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id VARCHAR(50) PRIMARY KEY,
            patient_name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            gender VARCHAR(20) NOT NULL,
            registration_date DATE NOT NULL
        )
    """)

    # Appointment table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id VARCHAR(50) PRIMARY KEY,
            patient_id VARCHAR(50) NOT NULL,
            appointment_date DATE NOT NULL,
            department VARCHAR(100) NOT NULL,
            doctor_name VARCHAR(100) NOT NULL,
            wait_time_minutes INT NOT NULL,
            status VARCHAR(50) NOT NULL,
            FOREIGN KEY (patient_id)
                REFERENCES patients(patient_id)
        )
    """)

    connection.commit()
    cursor.close()

    print("Database tables created successfully!")


def load_patients(connection, patients_df):
    cursor = connection.cursor()

    query = """
        INSERT INTO patients (
            patient_id,
            patient_name,
            age,
            gender,
            registration_date
        )
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            patient_name = VALUES(patient_name),
            age = VALUES(age),
            gender = VALUES(gender),
            registration_date = VALUES(registration_date)
    """

    values = []

    for _, row in patients_df.iterrows():
        registration_date = pd.to_datetime(
            row["registration_date"]
        ).date()

        values.append((
            str(row["patient_id"]),
            str(row["patient_name"]),
            int(row["age"]),
            str(row["gender"]),
            registration_date
        ))

    if values:
        cursor.executemany(query, values)
        connection.commit()

    print(f"Loaded {len(values)} patient records.")

    cursor.close()


def load_appointments(connection, appointments_df):
    cursor = connection.cursor()

    query = """
        INSERT INTO appointments (
            appointment_id,
            patient_id,
            appointment_date,
            department,
            doctor_name,
            wait_time_minutes,
            status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            patient_id = VALUES(patient_id),
            appointment_date = VALUES(appointment_date),
            department = VALUES(department),
            doctor_name = VALUES(doctor_name),
            wait_time_minutes = VALUES(wait_time_minutes),
            status = VALUES(status)
    """

    values = []

    for _, row in appointments_df.iterrows():
        appointment_date = pd.to_datetime(
            row["appointment_date"]
        ).date()

        values.append((
            str(row["appointment_id"]),
            str(row["patient_id"]),
            appointment_date,
            str(row["department"]),
            str(row["doctor_name"]),
            int(row["wait_time_minutes"]),
            str(row["status"])
        ))

    if values:
        cursor.executemany(query, values)
        connection.commit()

    print(f"Loaded {len(values)} appointment records.")

    cursor.close()


def load_data(patients_df, appointments_df):
    connection = None

    try:
        print("\nSTEP 5: Loading data into MySQL...")

        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            print("Connected to MySQL successfully!")

        create_tables(connection)

        load_patients(connection, patients_df)
        load_appointments(connection, appointments_df)

        print("Data loading completed successfully!")

    except mysql.connector.Error as error:
        raise RuntimeError(
            f"MySQL database error: {error}"
        ) from error

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")