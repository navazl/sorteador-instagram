from sorteador import sorteio
from flask import Flask, render_template, request, send_file


app = Flask("Sorteio Instagram")

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/result')
def result():
  url = request.args.get('url')
  winners = request.args.get('winners')
  sort = sorteio(str(url), int(winners))
  return render_template('result.html', p_sorteadas=sort[0], n_total=sort[1])



app.run(host='0.0.0.0')

