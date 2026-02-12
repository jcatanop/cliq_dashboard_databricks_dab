from pyspark import pipelines as dp
from databricks.sdk.runtime import spark

# this script create a table with user 

@dp.table
def users_silver_2():
    df = spark.readStream.table("records_bronze_1")
    df2 = df.dropDuplicates(["UID", "NAME"])
    df2 = df2.select("UID", "NAME")
    return df2