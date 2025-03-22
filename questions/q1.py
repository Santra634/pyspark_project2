# q1. Highest rated movies

from pyspark.sql.functions import desc
def high_rating(tablename):
    rating = tablename.select("title", "rating").orderBy(desc('rating'))
    return rating

