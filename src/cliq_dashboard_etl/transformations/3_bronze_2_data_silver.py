from pyspark import pipelines as dp
from databricks.sdk.runtime import spark
from pyspark.sql.functions import year, month, day, weekofyear,isnan, when

@dp.table
def records_silver_3():
  df = spark.readStream.table("records_bronze_1")
  df = (df
        .withColumn("YEAR", year(df.DATE))
        .withColumn("MONTH", month(df.DATE))
        .withColumn("DAY", day(df.DATE))
        .withColumn("WEEK", weekofyear(df.DATE))
        .withColumn(
          "INTERVAL", 
          when(isnan(df.INTERVAL), 4.0).otherwise(df.INTERVAL)
        )
        )

  df2 = df.select("UID","DATE","CHECKIN","CHECKOUT","INTERVAL","YEAR","MONTH","DAY","WEEK")

  return df2

