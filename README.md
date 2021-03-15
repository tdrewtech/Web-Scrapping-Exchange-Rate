# Web-Scrapping using Beautifulsoup

This project is about simple webscrapping from EXCHANGE-RATES.ORG to obtain information. I also use a simple dashboard flask to display our scrap and visualization results.

## Dependencies

- beautifulSoup4
- Pandas
- flask
- matplotlib

Install the requirements.txt in the following way :

`` python
pip install -r requirements.txt
``


## Steps of my Web Scrapping

* I scrape using `beautiful soup` in my jupyter notebook first.
* Please open the notebook template in this capstone and fill in according to the directions. I have also provided the analysis needed on the notebook.
* The file in this repository is a file that can be used to create a simple dashboard flask.

`` python
table = soup.find('table', attrs={'class':'table table-striped table-hover table-hover-solid-row table-simple history-data'})
tr = table.find_all('tr')
``

* Use the code below to save the scrap that you made into a dataframe.

`` python
df = pd.DataFrame(temp, columns = ('date','day','rate','desc'))
``


* You can also play with the UI in `index.html` where you can follow the comments to find out which parts can be changed.

### Objectives

1. Data on the exchange rate of US Dollar to SGD from `https://www.exchange-rates.org/history/SGD/USD/T`

    * From this page look for `date`, `day of the week`, `daily rate`, and `description`
    * Create a plot of the movement of the USD exchange rate
