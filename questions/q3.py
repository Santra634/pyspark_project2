# q3. Director with most no of movies

from pyspark.sql.functions import desc,col,count

def director(tablename):
    dir_count = tablename.filter(col("director").isNotNull()) .groupBy("director").agg(count("title").alias("no_of_movies")).orderBy(desc("no_of_movies"))
    return dir_count
