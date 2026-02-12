from pyspark import pipelines as dp
from pyspark.sql.functions import sum as _sum

@dp.table()
def worked_hours_by_day_4():
    df = spark.readStream.table("records_silver_3")
    df2 = (df
        .groupBy("DATE", "UID", "WEEK")
        .agg(_sum("INTERVAL").alias("INTERVAL"))
    )

    return df2