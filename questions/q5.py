# q5. popular movies with their genres,ratings and lang

from pyspark.sql.functions import desc,col

def popular_movies(tablename):
    popular =tablename.withColumn("popularity", col("popularity").cast("int")).orderBy(desc("popularity"))
    p=popular.select("title", "popularity", "genres", "rating", "language")
    return p
