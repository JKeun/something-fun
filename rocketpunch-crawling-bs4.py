import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.DataFrame(columns=["company", "description", "link"])

for page in range(50):
    response = requests.get("https://www.rocketpunch.com/companies?page={}".format(page))
    dom = BeautifulSoup(response.content, "html.parser")
    elements = dom.select("#company-list div.content")

    for element in elements:
        company_name = element.select_one('strong').string
        link = element.select_one('a').attrs.get('href')
        description = element.select_one('div.description').string
                                        
        df.loc[len(df)] = [company_name, description, link]
df
