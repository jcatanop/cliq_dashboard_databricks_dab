from pyspark import pipelines as dp
from databricks.sdk.runtime import spark
from pyspark.sql.functions import year, month, day, weekofyear,isnan, when, col, isnan


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
            when(
                (isnan(col("INTERVAL"))) & (col("CHECKIN") < "12:00"),
                8,
            )
            .when(
                (isnan(col("INTERVAL"))) & (col("CHECKIN") > "12:00"),
                4,
            )
            .when(
                (col("CHECKOUT") < col("CHECKIN")) & (col("CHECKIN") < "12:00"),
                8,
            )
            .when(
                (col("CHECKOUT") < col("CHECKIN")) & (col("CHECKIN") > "12:00"),
                4,
            )
            .otherwise(col("INTERVAL"))
        )
      )

  df2 = df.select("UID","DATE","CHECKIN","CHECKOUT","INTERVAL","YEAR","MONTH","DAY","WEEK")

  return df2

