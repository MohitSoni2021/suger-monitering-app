from flask import Flask, render_template, request, redirect, jsonify
import setuptest as ST
from datetime import date, datetime
import metadata as metadatafile

app = Flask(__name__)

databaseHandler = ST.sugarDatabase()


@app.route('/', methods=['POST', 'GET'])
def homePage():
  if request.method == "POST":
    try:
      if list(request.form.keys())[0] == 'delete_id':
        databaseHandler.delete_record(int(request.form.get('delete_id')))
        return redirect('/')

      else:
        return render_template(
            'metafile.html',
            id=databaseHandler.get_single(int(request.form.get('update_id'))),
            sugar_interval_dropdown=metadatafile.Sugar_check_intervals,
            insulin_type_dropdown=metadatafile.Insulin_type_names)
    except:
      pass
    try:
      updated_datalist = [
          request.form.get('Insulin dose'),
          request.form.get('Insulin type'),
          request.form.get('Interval'),
          request.form.get('date'),
          request.form.get('sugar value'),
      ]
      databaseHandler.update_value(updated_datalist,
                                   int(request.form.get('id')))
      return redirect('/')
    except:
      pass
  else:
    return render_template('timer.html',
                           sugarData=databaseHandler.get_data(),
                           average_value=int(
                               databaseHandler.avg_sugar_value()[0][0]),
                           max_sugar_value=databaseHandler.max_sugar_value(),
                           min_sugar_value=databaseHandler.min_sugar_value())
  return render_template('timer.html',
                         sugarData=databaseHandler.get_data(),
                         average_value=int(
                             databaseHandler.avg_sugar_value()[0][0]),
                         max_sugar_value=databaseHandler.max_sugar_value(),
                         min_sugar_value=databaseHandler.min_sugar_value())


@app.route('/new-Record', methods=['POST', 'GET'])
def new_record():
  if request.method == "POST":
    data = [
        request.form.get('sugar value'),
        request.form.get('Interval'),
        request.form.get('Insulin dose'),
        request.form.get('Insulin type'),
        request.form.get('date'),
    ]
    databaseHandler.Insert_data(data)
    return redirect('/')
  else:
    return render_template(
        'form.html',
        sugar_interval_dropdown=metadatafile.Sugar_check_intervals,
        insulin_type_dropdown=metadatafile.Insulin_type_names)


@app.route('/Insulin-dose-predictor', methods=['GET', 'POST'])
def update_record():
  return render_template('update.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
