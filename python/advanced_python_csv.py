import pandas as pd 

path = 'faculty.csv'
faculty = pd.read_csv(path)

df_emails = pd.DataFrame()

df_emails['email'] = faculty[u' email']

df_emails.to_csv('emails.csv', header = False, index = False)