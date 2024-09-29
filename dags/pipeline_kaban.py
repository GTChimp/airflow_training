from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

# from airflow.providers.common.sql.operators.sql import *
with DAG(dag_id='spark_etl_test', start_date=datetime(2023, 1, 1)
        , schedule='@daily', catchup=False) as dag:
    create_table1 = PostgresOperator(
        postgres_conn_id='kabandb01'
        , task_id='create_table01'
        , sql='''
        CREATE SCHEMA IF NOT EXISTS kaban;
        CREATE TABLE IF NOT EXISTS kaban.source_table (
        num_field numeric
        ,txt_field text);
        
        truncate table kaban.source_table;
        
        insert into kaban.source_table values(1,2::text);
        '''
    )

    create_table2 = PostgresOperator(
        postgres_conn_id='kabandb02'
        , task_id='create_table02'
        , sql='''
        CREATE SCHEMA IF NOT EXISTS kaban;
        CREATE TABLE IF NOT EXISTS kaban.destination_table (
        num_field numeric
        ,txt_field text);
        
        truncate table kaban.destination_table;
        '''

    )

    spark = SparkSubmitOperator(
        task_id='spark_wtf',
        conn_id='spark_cluster',
        jars='/home/airflow/jars/postgresql-42.7.4.jar',
        application='spark_scripts/simple_load_and_write.py',
        name='ggggg',

        #conf={'jars':'${SPARK_HOME}/jars/postgresql-42.7.4.jar'}
    )

    create_table1 >> create_table2 >> spark
