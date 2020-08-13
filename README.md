# FullThrottle
http://santosh3372.pythonanywhere.com/testapp
Running version of the application can be found at: http://abhishekrana254.pythonanywhere.com/testapp/

If you want to run the application on a local server follow the below steps : clone the application

git clone https://github.com/Abhishekrana254/testsite
Run the following command for running the server:

python manage.py runserver
if you run this on a local server the app can be accessed on http://localhost:8000/testapp and the populated data will be shown there.

Custom management command for populating the database with dummy data

python manage.py populate <data_points> <activity_period_number> <timestamps_after_year>
eg: python manage.py populate 2 3 2020 data_points is the number of users activity_period_number is the number of activity periods for each user year is the year after which you need the random timestamps

everytime it will remove the old data and populate the models with new data altogether
