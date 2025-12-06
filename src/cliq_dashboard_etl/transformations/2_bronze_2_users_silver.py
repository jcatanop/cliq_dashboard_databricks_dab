from pyspark import pipelines as dp
from databricks.sdk.runtime import spark

# this script create a table with user 

@dp.table
def users_silver_2():
    df = spark.sql("select UID,NAME from `records_bronze_1` group by NAME,UID")
    return (df)

# TODO: hay que ver si se puede hacer streaming

#    return spark.sql("create or refresh streaming table `users_silver_2` as select UID,NAME from stream `records_bronze_1` group by NAME,UID")
