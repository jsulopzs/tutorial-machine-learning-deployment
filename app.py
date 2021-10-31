import flask
import pickle

with open(f'model/linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template(template_name_or_list='index.html'))

    if flask.request.method == 'POST':
        acceleration = flask.request.form['acceleration']
        weight = flask.request.form['weight']

        acceleration = float(acceleration)
        weight = float(weight)

        input_variables = [[acceleration, weight]]
        prediction = model.predict(input_variables)[0]
        prediction = round(prediction, 2)

        return flask.render_template(template_name_or_list='index.html', result=prediction)


if __name__ == '__main__':
    app.run()
