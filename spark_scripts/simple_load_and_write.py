from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option('driver', 'org.postgresql.Driver') \
    .option("url", "jdbc:postgresql://kabandb01:5432/") \
    .option("dbtable", "kaban.source_table") \
    .option("user", "kaban") \
    .option("password", "kaban") \
    .load()

df.write \
    .format("jdbc") \
    .option('driver', 'org.postgresql.Driver') \
    .option("url", "jdbc:postgresql://kabandb02:5432/") \
    .option("dbtable", "kaban.destination_table") \
    .option("user", "kaban") \
    .option("password", "kaban") \
    .mode('append') \
    .save()
