FROM apache/airflow:2.4.2
RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --no-cache-dir apache-airflow-providers-apache-spark==4.1.0
