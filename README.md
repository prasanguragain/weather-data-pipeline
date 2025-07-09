# 🌦 Weather Data Pipeline

This project automates the ingestion, transformation, and visualization of weather data using a modern data stack:

- **Python API**: Fetches real-time weather via Weatherstack API  
- **PostgreSQL**: Stores raw weather data  
- **Airflow**: Orchestrates the ingestion and dbt processes as DAGs  
- **dbt**: Transforms & models raw data for analytics  
- **Superset**: Provides a BI dashboard to explore and visualize data  
- **Docker Compose**: Defines all services in a clean, reproducible setup

---

##  Repository Structure
weather-data-pipeline/
├── api_request/ # Python modules: fetch & insert weather API data
├── airflow/
│ └── dags/
│ └── weather_api_orchestrator.py
├── dbt/
│ ├── my_project/ # dbt project
│ └── profiles.yml # or symlink to ~/.dbt/profiles.yml
├── postgres/ # DB init scripts for Airflow & Superset
├── docker/
│ ├── .env.example # Sample env file (never commit secrets)
│ └── superset_config.py # Superset config via Docker
├── docker-compose.yml # Orchestration of all services
├── .gitignore
└── README.md
