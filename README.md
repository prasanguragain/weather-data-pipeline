# Weather Data Pipeline

"""
This project automates the ingestion, transformation, and visualization of weather data using a modern data stack:

- Python API: Fetches real-time weather via Weatherstack API
- PostgreSQL: Stores raw weather data
- Airflow: Orchestrates the ingestion and dbt processes as DAGs
- dbt: Transforms & models raw data for analytics
- Superset: Provides a BI dashboard to explore and visualize data
- Docker Compose: Defines all services in a clean, reproducible setup
"""

# Repository Structure
# (as text tree)
"""
weather-data-pipeline/
├── api_request/              # Python modules: fetch & insert weather API data
├── airflow/
│   └── dags/
│       └── weather_api_orchestrator.py
├── dbt/
│   ├── my_project/           # dbt project
│   └── profiles.yml          # or symlink to ~/.dbt/profiles.yml
├── postgres/                 # DB init scripts for Airflow & Superset
├── docker/
│   ├── .env.example          # Sample env file (never commit secrets)
│   └── superset_config.py    # Superset config via Docker
├── docker-compose.yml        # Orchestration of all services
├── .gitignore
└── README.md
"""

# Prerequisites
prerequisites = [
    "Docker & Docker Compose",
    "Python 3 (for running scripts outside Docker)",
    "(Optional) dbt Core for local transformations"
]

# Getting Started Instructions
steps = [
    "Clone the repo & copy the .env.example",
    "Run all services using docker-compose",
    "Access Airflow and Superset on respective ports",
    "Explore the Airflow DAG and Superset dashboard"
]

# Cleanup
cleanup_cmd = "docker-compose down -v"

# Development Tips
python_tips = [
    "Use venv and install requirements if testing locally",
    "Modify DAGs in airflow/dags",
    "Edit dbt models in dbt/my_project/models",
    "Customize Superset via docker/superset_config.py"
]

# Security & Best Practices
best_practices = [
    "Do not commit secrets or API keys",
    "Use .gitignore to exclude volumes, logs, etc.",
    "Secure Superset, Airflow, and DB for production"
]

# Next Steps
next_steps = [
    "Write unit tests for Python and dbt",
    "Set up CI/CD",
    "Publish images to Docker Hub or GitHub Packages"
]

# License & Acknowledgements
MIT License

Copyright (c) 2025 Prasan Guragain

Permission is hereby granted, free of charge, to any person obtaining a copy
...
license_info = "MIT License.
print("\nEnjoy building and visualizing weather insights! 🌤️")
