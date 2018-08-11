from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return(' Không sử dụng render_template ')

@app.route('/bmi/<int:weight>/<int:height>')
def calc_bmi(weight, height):
    BMI = weight/((height*height)*(10**(-4)))
    if BMI < 16:
        return ('Your BMI = ' + str(BMI) + ' =====> BMI < 16: Severely underweigh')
    elif BMI < 18.5:
        return('Your BMI = ' + str(BMI) + " =====> 16 <= BMI < 18,5: Underweight !!")
    elif BMI < 25:
        return('Your BMI = ' + str(BMI) + " =====> 18,5 <= BMI < 25 Normal !!")
    elif BMI < 30:
        return('Your BMI = ' + str(BMI) + " =====> 25 <= BMI < 30 Overweight !!")
    else :
        return('Your BMI = ' + str(BMI) + " =====> BMI > 30 Obese !!")
    

if __name__ == '__main__':
  app.run(debug=True)
 