# 🌦️ Weather Data Pipeline

This project automates the **ingestion**, **transformation**, and **visualization** of weather data using a modern data stack:

- **Python API**: Fetches real-time weather via Weatherstack API  
- **PostgreSQL**: Stores raw weather data  
- **Airflow**: Orchestrates the ingestion and dbt processes as DAGs  
- **dbt**: Transforms & models raw data for analytics  
- **Superset**: Provides a BI dashboard to explore and visualize data  
- **Docker Compose**: Defines all services in a clean, reproducible setup

---

## 📁 Repository Structure

```
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
```

---

## ✅ Prerequisites

- Docker & Docker Compose  
- Python 3 (for running scripts outside Docker)  
- *(Optional)* dbt Core for local transformations  

---

## 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/prasanguragain/weather-data-pipeline.git
   cd weather-data-pipeline
   ```

2. Copy the `.env.example` to `.env` and add required secrets  
   ```bash
   cp docker/.env.example .env
   ```

3. Run all services using Docker Compose  
   ```bash
   docker-compose up --build
   ```

4. Access services:  
   - Airflow: [http://localhost:8080](http://localhost:8080)  
   - Superset: [http://localhost:8088](http://localhost:8088)  

5. Explore:  
   - Airflow DAG for orchestration  
   - Superset dashboard for weather insights  

---

## 🧹 Cleanup

To stop and remove all services and volumes:

```bash
docker-compose down -v
```

---

## 🛠 Development Tips

- Use `venv` and install requirements if testing scripts locally  
- Modify DAGs in `airflow/dags/`  
- Edit dbt models in `dbt/my_project/models/`  
- Customize Superset in `docker/superset_config.py`  

---

## 🔐 Security & Best Practices

- Never commit secrets or API keys — use `.env` files  
- Add volumes, logs, etc., to `.gitignore`  
- Secure Superset, Airflow, and PostgreSQL for production deployments  

---

## 📈 Next Steps

- Add unit tests for Python scripts and dbt models  
- Set up CI/CD pipelines  
- Publish images to Docker Hub or GitHub Packages  

---

## 📜 License

MIT License  
© 2025 Prasan Guragain

> Permission is hereby granted, free of charge, to any person obtaining a copy  
> of this software and associated documentation files (the "Software"), to deal  
> in the Software without restriction...

*See the [LICENSE](./LICENSE) file for full details.*

---

## ✨ Enjoy building and visualizing weather insights!
