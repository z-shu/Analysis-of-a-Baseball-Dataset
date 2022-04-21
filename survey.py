import pandas as pd

survey_df = pd.read_csv(r"C:\Users\zukhr\Downloads\survey.csv")

# head
print(survey_df.tail())
print(survey_df.info())
print(survey_df.head())