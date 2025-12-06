from pyspark import pipelines as dp
from databricks.sdk.runtime import spark

@dp.table()
@dp.expect("overhours_shift_ck", "INTERVAL < 10")
def shifts_by_day_5():
    users = spark.read.table("users_silver_2")

    df = spark.read.table("worked_hours_by_day_4")

    return df.join(users, "UID")