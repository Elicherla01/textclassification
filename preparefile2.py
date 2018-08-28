import pandas as pd
consumercompliants = pd.read_csv('/Users/ravindraprasad/Ravindra/fasttext/fasttext/data/consumer/Consumer_Complaints.csv')

from io import StringIO
col = ['Product', 'Consumer complaint narrative']
consumercompliants = consumercompliants[col]
consumercompliants = consumercompliants[pd.notnull(consumercompliants['Consumer complaint narrative'])]
consumercompliants.columns = ['Product', 'Consumer_complaint_narrative']


#consumercompliants['Product'] = consumercompliants['Product'].replace(' ', '_', regex=True)
consumercompliants['Product']=['__label__'+s.replace(' or ', '$').replace(', or ','$').replace(',','$').replace(' ','_').replace(',','__label__').replace('$$','$').replace('$',' __label__').replace('___','__') for s in consumercompliants['Product']]
consumercompliants['Product']

consumercompliants['Consumer_complaint_narrative']= consumercompliants['Consumer_complaint_narrative'].replace('\n',' ', regex=True).replace('\t',' ', regex=True)

#consumercompliants['Consumer_complaint_narrative']=consumercompliants['Consumer_complaint_narrative'][1:-1]
consumercompliants.to_csv(r'/Users/ravindraprasad/Ravindra/fasttext/fasttext/data/consumer/Consumer_Complaints_finalv4.txt', index=False, sep=' ', header=False, quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
