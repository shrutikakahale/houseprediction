This is a Flask web application that predicts housing prices based on various features like area, number of bedrooms, bathrooms, stories, and more. The application uses a trained Linear Regression model to make price predictions based on user input.

Features
Predict Housing Prices: Users can input details about a house (area, number of bedrooms, bathrooms, etc.) through an HTML form, and the app will predict the house price.
Model Training: The model is trained using a real estate dataset (Housing.csv) and uses scikit-learn's LinearRegression algorithm.
User-friendly Web Interface: The app provides an easy-to-use form where users can enter house features and get instant price predictions.
Data Preprocessing: The app uses pandas for data cleaning and pamdas dummies encoding of categorical variables.
Model Explanation
The model uses Linear Regression to predict the price of a house based on the following features:

Area
Number of Bedrooms
Number of Bathrooms
Number of Stories
Guestroom (yes/no)
Basement (yes/no)
Hot Water Heating (yes/no)
Air Conditioning (yes/no)
Furnishing Status (furnished/unfurnished)
Data Preprocessing
The features are one-hot encoded using pandas.get_dummies to handle categorical variables.
The dataset is split into training and testing sets using train_test_split from scikit-learn.
The model is trained using the training set (X_train, y_train) and evaluated on the test set (X_test, y_test).
