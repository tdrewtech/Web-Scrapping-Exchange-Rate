from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/history/SGD/USD/T')
soup = BeautifulSoup(url_get.content,"html.parser")

table = soup.find('table', attrs={'class':'table table-striped table-hover table-hover-solid-row table-simple history-data'})
tr = table.find_all('tr')
temp = [] #initiating a tuple

for row in tr:
    tds = row.find_all('td')
    try:
        date = tds[0].text
        day = tds[1].text
        rate = tds[2].text
        desc = tds[3].text
        temp.append([date , day, rate, desc])
    except:
        pass

temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp, columns = ('date','day','rate','desc'))

#insert data wrangling here
df['rate'] = df['rate'].str.replace("SGD","")
df['rate'] = df['rate'].astype('float64')

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'SGD {df["rate"].mean().round(2)}'

	# generate plot
	ax = df.plot(figsize = (20,9))
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]


	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)
