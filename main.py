from flask import Flask, render_template, request
from alpha_vantage.timeseries import TimeSeries
import plotly.graph_objects as go
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_name = request.form['company']
        plot_stock_graph(company_name)
        return render_template(f'{company_name}.html')
    return render_template('index.html')


def plot_stock_graph(company_name):
    # Set your API key
    api_key = 'PQ5M1AYGGKKUQOAV'

    # Create an instance of the TimeSeries class
    ts = TimeSeries(key=api_key, output_format='pandas')

    # Get the intraday stock data for the specified symbol
    data, _ = ts.get_intraday(symbol=company_name, interval='1min')

    # Create the plot using Plotly
    fig = go.Figure(data=go.Scatter(x=data.index, y=data['4. close']))
    fig.update_layout(title=f'Stock Data for {company_name}',
                      xaxis_title='Time',
                      yaxis_title='Closing Price')

    # Generate a unique filename based on the company name
    filename = f'templates/{company_name}.html'

    # Save the plot as HTML file with the unique filename
    fig.write_html(filename)


if __name__ == '__main__':
    app.run()