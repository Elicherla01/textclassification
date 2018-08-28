import pandas as pd
consumercompliants = pd.read_csv('/Users/ravindraprasad/Ravindra/fasttext/fasttext/data/consumer/Consumer_Complaints.csv')

from io import StringIO
col = ['Product', 'Consumer complaint narrative']
consumercompliants = consumercompliants[col]
consumercompliants = consumercompliants[pd.notnull(consumercompliants['Consumer complaint narrative'])]
consumercompliants.columns = ['Product', 'Consumer_complaint_narrative']
consumercompliants.head()
