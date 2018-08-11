from flask import Flask, render_template
import mlab
from models.river import River
app = Flask(__name__)

mlab.connect()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/africa')
def africa():
    all_rivers = River.objects(continent = "Africa")
    return render_template('rivers.html', all_rivers= all_rivers)

@app.route('/S.America')
def s_america():
    all_rivers = River.objects(continent = "S. America", lenght__lt = 1000)
    return render_template('rivers.html', all_rivers= all_rivers)

if __name__ == '__main__':
  app.run(debug=True)
 