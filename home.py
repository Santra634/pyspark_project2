from data_loading import create_df
import logs.log_fn as log

data_path='data/netflix_movies_detailed_up_to_2025.csv'

try:
    netflix = create_df(data_path, True)
    netflix.show()
    print('df created')
    log.log_info('dataframe created successfully')

except Exception as e:
    print('error', e)
    log.log_error(e)

from questions.q1 import high_rating
try:
    out1= high_rating(netflix)
    out1.show()
    out1.write.csv('results/ques1',header=True,mode='overwrite')
    log.log_info('ques1 file is executed and output is generated')
except Exception as e:
    log.log_error(e)

from questions.q2 import dp
try:
    out1= dp(netflix)
    out1.show()
    out1.write.csv('results/ques2',header=True,mode='overwrite')
    log.log_info('ques2 file is executed and output is generated')
except Exception as e:
    log.log_error(e)

from questions.q3 import director
try:
    out1= director(netflix)
    out1.show()
    out1.write.csv('results/ques3',header=True,mode='overwrite')
    log.log_info('ques3 file is executed and output is generated')
except Exception as e:
    log.log_error(e)

from questions.q4 import indian_movies
try:
    out1= indian_movies(netflix)
    out1.show()
    out1.write.csv('results/ques4',header=True,mode='overwrite')
    log.log_info('ques4 file is executed and output is generated')
except Exception as e:
    log.log_error(e)

from questions.q5 import popular_movies
try:
    out1= popular_movies(netflix)
    out1.show()
    out1.write.csv('results/ques5',header=True,mode='overwrite')
    log.log_info('ques5 file is executed and output is generated')
except Exception as e:
    log.log_error(e)