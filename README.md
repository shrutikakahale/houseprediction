# Housing Price Prediction Web App

This is a Flask web application that predicts housing prices based on various features like area, number of bedrooms, bathrooms, stories, and more. The application uses a trained Linear Regression model to make price predictions based on user input.<br><br>

### Features
- **Predict Housing Prices**: Users can input details about a house (area, number of bedrooms, bathrooms, etc.) through an HTML form, and the app will predict the house price.<br>
- **Model Training**: The model is trained using a real estate dataset (`Housing.csv`) and uses scikit-learn's `LinearRegression` algorithm.<br>
- **User-friendly Web Interface**: The app provides an easy-to-use form where users can enter house features and get instant price predictions.<br>
- **Data Preprocessing**: The app uses `pandas` for data cleaning and `pandas.get_dummies` encoding of categorical variables.<br><br>

### Model Explanation
The model uses **Linear Regression** to predict the price of a house based on the following features:<br>
- Area<br>
- Number of Bedrooms<br>
- Number of Bathrooms<br>
- Number of Stories<br>
- Guestroom (yes/no)<br>
- Basement (yes/no)<br>
- Hot Water Heating (yes/no)<br>
- Air Conditioning (yes/no)<br>
- Furnishing Status (furnished/unfurnished)<br><br>

### Data Preprocessing
- The features are one-hot encoded using `pandas.get_dummies` to handle categorical variables.<br>
- The dataset is split into training and testing sets using `train_test_split` from `scikit-learn`.<br><br>

