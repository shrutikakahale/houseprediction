from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression






app = Flask(__name__)

# Load the dataset
data = pd.read_csv("Housing.csv")

# Separate features and target variable
features = data.drop(columns=['price', 'prefarea', 'parking', 'mainroad'])
y = data['price']

# Use pandas get_dummies for 'Gender'
nfeatures = pd.get_dummies(features)

X_train, X_test, y_train, y_test = train_test_split(nfeatures, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model using X_train and y_train
model.fit(X_train, y_train)


def predict_pricing(user_input):
    
    user_input = pd.get_dummies(user_input)

    
    user_input = user_input.reindex(columns=nfeatures.columns, fill_value=0)



    prediction = model.predict(user_input)[0]
    return prediction


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        area = int(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        stories = int(request.form['stories'])
        guestroom = request.form['guestroom']
        basement = request.form['basement']
        hotwaterheating = request.form['hotwaterheating']
        airconditioning = request.form['airconditioning']
        furnishingstatus = request.form['furnishingstatus']
        
        user_input_data = pd.DataFrame({'area': [area], 'bedrooms': [bedrooms], 'bathrooms': [bathrooms], 
                                        'stories': [stories], 'guestroom': [guestroom], 
                                        'basement': [basement], 'hotwaterheating': [hotwaterheating], 
                                       'airconditioning': [airconditioning], 'furnishingstatus': [furnishingstatus]})
        prediction = predict_pricing(user_input_data)
        return render_template('home.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)