# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog `cliq_records`;
# MAGIC use schema `jorgeenriquecatano`;
# MAGIC show tables;

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from cliq_records.prod.records_bronze_1;

# COMMAND ----------

df=spark.read.format("csv").option("header","true").option("inferSchema","true").load("/Volumes/cliq_records/prod/data-csv")
display(df.count())

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from cliq_records.jorgeenriquecatano.shifts_by_day_5 limit 10;
