import pandas as pd
df = pd.read_csv("Resources/cities.csv")
df.to_html("Resources/cities.html",index=False,classes=["table","table-striped","table-hover"])
