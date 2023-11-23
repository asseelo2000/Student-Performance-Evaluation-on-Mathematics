# Delete app.py before deployment on AWS.

from flask import Flask, request, render_template


from src.pipeline.predict_pipeline import Predictpipeline, CustomData

application = Flask(__name__)

app = application

# Route to home page


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
            return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=Predictpipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        bestf = 'Keep up the good work'
        abavgf = 'Good work'
        avgf = 'You must work hard'
        failed = 'You Failed'

        print("after Prediction")
        if results >= 100 or results >=90:
            return render_template('home.html',results= 100, feed= bestf)
        elif results <= 90 and results >=70:
            return render_template('home.html',results= results[0], feed= abavgf)
        elif results <= 70 and results >=35:
            return render_template('home.html',results= results[0], feed= avgf)
        elif results < 35:
            return render_template('home.html',results= results[0], feed= failed)
        else:
             return render_template('home.html',results= results[0])
        
    

if __name__=='__main__':
     app.run(debug=False, host='0.0.0.0',port=5000) 
    #  app.run(debug=False, host='0.0.0.0',port=5001) 
     
# print('http://127.0.0.1:5001/predictdata')