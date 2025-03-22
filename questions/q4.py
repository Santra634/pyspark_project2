# q4. Indian movies released in 2025 with highest voting average

from pyspark.sql.functions import desc,col
def indian_movies(tablename):
    indian_2025 = tablename.filter((col("country") == "India") & (col("release_year") == 2025)) .orderBy(desc("vote_average"))
    i=indian_2025.select("title", "vote_average", "language")
    return i
