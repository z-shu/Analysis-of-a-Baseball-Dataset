import pandas as pd

survey_df = pd.read_csv(r"C:\Users\zukhr\Downloads\survey.csv")

print(survey_df.tail())
print(survey_df.info())