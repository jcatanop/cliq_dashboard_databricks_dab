from pyspark import pipelines as dp
from databricks.sdk.runtime import spark
from pyspark.sql.functions import year, month, day, weekofyear

@dp.table()
@dp.expect("overhours_shift_ck", "INTERVAL < 10")
def shifts_by_day_5():
    users = spark.read.table("users_silver_2")

    df = spark.read.table("worked_hours_by_day_4")
    df =(df
        .withColumn("YEAR", year(df.DATE))
        .withColumn("MONTH", month(df.DATE))
        .withColumn("DAY", day(df.DATE))
        .withColumn("WEEK", weekofyear(df.DATE))
    )
    return df.join(users, "UID")