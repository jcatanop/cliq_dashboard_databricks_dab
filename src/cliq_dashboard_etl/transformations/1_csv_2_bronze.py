from pyspark import pipelines as dp
from databricks.sdk.runtime import spark
from pyspark.sql.functions import current_timestamp
#
# This file read data from csv file and create a bronze table "records_bronze_1"
#

@dp.table
@dp.expect("valid_checkout_ck", "NOT isnan(INTERVAL)")
def records_bronze_1():

    df = (
        spark.readStream
        .format("csv") 
        .option("header",True)
        .schema(
            """
            UID INT,
            NAME STRING,
            DATE DATE,
            CHECKIN STRING,
            CHECKOUT STRING,
            INTERVAL DOUBLE
            """
        ) 
        .csv("/Volumes/cliq_records/jorgeenriquecatano/data-csv/")
        )
    return (
        df
        .withColumn("ingestion_time", current_timestamp())
        .withColumn("file_name", df["_metadata"]["file_path"])
    )