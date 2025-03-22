# q2. Highest rated deepika padukone movies

from pyspark.sql.functions import desc,col
def dp(tablename):
    dp_movies = tablename.where(col("cast").contains("Deepika Padukone"))
    d=dp_movies.select("title", "rating").orderBy(desc('rating'))
    return d
