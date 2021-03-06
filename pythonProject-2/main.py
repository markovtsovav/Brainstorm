import pandas as pd
from flask import Flask, request, render_template
from keras.models import load_model

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def compute():
    result = ''
    error = dict()
    if request.method == 'POST':
        data = request.form
        try:
            df3 = {k:[float(v)] for k,v in data.items()}
        except ValueError:
            for k,v in data.items():
                try:
                    float(v)
                except ValueError:
                    error['name'] = k
                    error['value'] = v
                    break
        if not error:
            input = pd.DataFrame(data=df3)
            result = model.predict(input)[0][0]
    return render_template('templat2.html', result=result, error=error)


if __name__ == '__main__':
    model = load_model('./brainstorm_mlp/')
    app.run(host='localhost', port=8081, debug=True)