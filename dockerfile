FROM apache/airflow:2.4.2
USER root
RUN apt-get update \
 && apt-get install -y procps \
 && apt-get install -y wget
# Install OpenJDK-17
RUN apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64/
RUN export JAVA_HOME

USER airflow
RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --no-cache-dir apache-airflow-providers-apache-spark==4.1.0
RUN wget --no-verbose -P /home/airflow/jars "https://jdbc.postgresql.org/download/postgresql-42.7.4.jar"