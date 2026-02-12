from pyspark import pipelines as dp
from databricks.sdk.runtime import spark
from pyspark.sql.functions import current_timestamp, split, lpad, concat_ws
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
        .csv(f"/Volumes/cliq_records/jorgeenriquecatano/data-csv/")
        )
    return (
        df
        .withColumn("ingestion_time", current_timestamp())
        .withColumn("file_name", df["_metadata"]["file_path"])
        .withColumn("CHECKIN",
            concat_ws(
                ":",
                lpad(split("CHECKIN", ":")[0], 2, "0"),
                lpad(split("CHECKIN", ":")[1], 2, "0"),
            ),
        )
        .withColumn("CHECKOUT",
            concat_ws(
                ":",
                lpad(split("CHECKOUT", ":")[0], 2, "0"),
                lpad(split("CHECKOUT", ":")[1], 2, "0"),
            ),
        )
    )
