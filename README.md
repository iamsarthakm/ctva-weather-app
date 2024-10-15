# ctva-weather-app

The application stores temperature and rainfall data for different weather stations stated in locations such as Nebraska, Iowa, Illinois, Indiana,  Ohio. The analytics are performed on the data and stored too. The data is exposed using Rest APIs and can be accessed by following the steps given below

## Initial Setup

1. Clone the project git repository

    ```bash
    git clone git@github.com:iamsarthakm/ctva-weather-app.git
    cd ctva-weather-app
    ```

2. Create Virtual Environment and setup envs

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    cp .env.example .env
    ```

3. Ingest weather data and populate analytics

    ```bash
   # slow
    python3 manage.py process_weather_data
    #faster
    python3 scripts/weather_data_ingestion.py 

    python3 manage.py populate_weather_analytics
    ```

4. Run django server to get data using rest apis

    ```bash
    python3 manage.py runserver
    ```

5. Access API documentation(In Local)

    ```bash
    http://localhost:8000/swagger/
    ```
    ### Rest APIs

    The APIs support all 4 basic functions
    1. filtering (station_id, date or year)
    2. pagination
    3. sorting
    4. fields(if need fewer fields in response)


6. Run Unit tests

    ```bash
    python3 manage.py test
    ```


## Tooling

### Stack

- `django` - for web framework
- `postgres` - for database

### Python tooling

- `black` - for formatting
- `flake8` - for linting
- `isort` - for import sorting
- `swagger` - for documentation

## HLD

![image](https://github.com/user-attachments/assets/d4103a73-ea6f-4150-a939-fb07740b38ba)
