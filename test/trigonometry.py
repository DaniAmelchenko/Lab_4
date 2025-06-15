from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        angle = float(request.form.get('angle'))
        precision = int(request.form.get('precision'))
        unit = request.form.get('unit')
        func = request.form.get('function')
        if unit == 'degrees':
            angle = math.radians(angle)
        try:
            if func == 'sin':
                result = round(math.sin(angle), precision)
            elif func == 'cos':
                result = round(math.cos(angle), precision)
            elif func == 'tan':
                result = round(math.tan(angle), precision)
            elif func == 'cot':
                tan_value = math.tan(angle)
                if abs(tan_value) < 1e-15:
                    result = 'Undefined'
                else:
                    result = round(1 / tan_value, precision)
        except Exception as e:
            result = f'Error: {str(e)}'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
