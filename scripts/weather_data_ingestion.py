import os
import psycopg2
from decouple import config
from datetime import datetime


def create_connection():
    return psycopg2.connect(
        dbname=config("DATABASE_NAME"),
        user=config("DATABASE_USER"),
        password=config("DATABASE_PASSWORD"),
        host=config("DATABASE_HOST"),
        port=config("DATABASE_PORT"),
    )


def create_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS WeatherData (
        id SERIAL PRIMARY KEY,
        date DATE NOT NULL,
        station_id VARCHAR(99) NOT NULL,
        max_temperature NUMERIC(5, 2),
        min_temperature NUMERIC(5, 2),
        precipitation NUMERIC(5, 2)
    );
    """
    cursor.execute(create_table_query)


# Process text files and load data into the WeatherData table
def process_files(directory_path, cursor):
    total_records = 0
    file_count = 0

    for filename in os.listdir(directory_path):
        file_count += 1
        file_records = 0

        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)

            with open(file_path, "r") as file:
                for line in file:
                    total_records += 1
                    file_records += 1

                    # Split the data into columns
                    data = line.split()

                    # Check the number of columns
                    if len(data) == 4:
                        date = data[0]
                        station_id = filename[:-4]
                        max_temperature = (
                            None if float(data[1]) == -9999 else float(data[1]) / 10.0
                        )
                        min_temperature = (
                            None if float(data[2]) == -9999 else float(data[2]) / 10.0
                        )
                        precipitation = (
                            None if float(data[3]) == -9999 else float(data[3]) / 10.0
                        )

                        # Insert data into the WeatherData table
                        insert_query = """
                        INSERT INTO WeatherData (date, station_id, max_temperature, min_temperature, precipitation)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (date, station_id) DO NOTHING;  -- To avoid duplicacy
                        """
                        cursor.execute(
                            insert_query,
                            (
                                date,
                                station_id,
                                max_temperature,
                                min_temperature,
                                precipitation,
                            ),
                        )
            print(
                f"The number of records processed for {station_id} are {file_records}"
            )

    return total_records, file_count


def main():
    directory_path = "/ctva-weather-app/wx_data"

    # Connect to PostgreSQL database
    connection = create_connection()
    cursor = connection.cursor()

    # Create the WeatherData table if it doesn't exist
    create_table(cursor)

    start_time = datetime.now()

    # Process files and load data
    total_records, file_count = process_files(directory_path, cursor)

    end_time = datetime.now()
    print(f"Session started at: {start_time}")
    print(f"Session ended at: {end_time}")
    print(f"Total Time: {end_time - start_time}")
    print(f"Total files processed: {file_count}")
    print(f"Total records added in session: {total_records}")

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
