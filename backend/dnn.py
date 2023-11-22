# dnn.py
# This file runs our 11 layer DNN model

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

def run_dnn_model(dataset):
    # Initialize "global" variables
    # and helper functions
    learning_rate_default = 1e-5

    # Initialize number of hidden layers
    hidden_layers = 11
    print(f"{'~'*15} Building DNN model with {hidden_layers} hidden layers{'~'*15}\n")

    # SETTING THE TARGET VARIABLE (Y) AND SELECTING THE FEATURES (X):
    X = dataset.drop('Close', axis=1).values
    Y = dataset['Close'].values.reshape(-1, 1)

    # SCALING DATA
    scaler_X = MinMaxScaler()
    X = scaler_X.fit_transform(X)
    scaler_Y = MinMaxScaler()
    Y = scaler_Y.fit_transform(Y)

    # Creating a Training Set and a Test Set for Stock Market Prediction:
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, shuffle=False)

    # Building DNN model with 11 hidden layers
    model = Sequential()

    # Input layer
    # Input layer will have same number of neurons as number of feature variables
    model.add(Dense(64, input_dim=X_train.shape[1], activation='tanh'))

    # Hidden layers
    # Play around with number of neurons in each hidden layer.
    # Too many neurons leads to overcomplexity, not enough means too simple
    # Tanh activation function here is used b/c it is recommended to use
    # when there are more hidden layers.
    for _ in range(hidden_layers-1):
        model.add(Dense(128, activation='tanh'))
        model.add(Dropout(0.1)) # This helps with preventing overfitting

    # Output layer
    # Output layer will have 1 neuron b/c there's only 1 target variable
    model.add(Dense(1))

    # Changing learning rate here with Adam's optimization.
    # Learning rate is static at the moment, but we can explore
    # dynamically changing learning rates later.

    # Normal learning rate ~ 1e-3 to 1e-4, but here it
    # is 1e-5.
    optimizer = Adam(learning_rate=learning_rate_default)
    model.compile(optimizer=optimizer, loss='mean_squared_error')

    # Train DNN model
    # Play around with epochs, batch_size values
    history = model.fit(X_train, Y_train, epochs=100, batch_size=32, validation_data=(X_test, Y_test), verbose=2)

    # Making a prediction based on DNN model:
    Y_pred = model.predict(X_test)

    # We gotta inverse_transform below values since
    # we scaled them above
    Y_test_original = scaler_Y.inverse_transform(Y_test)
    Y_pred_original = scaler_Y.inverse_transform(Y_pred)

    train_loss = history.history['loss']
    validation_loss = history.history['val_loss']

    print(f"Y_test_original: {Y_test_original}")
    print(f"Y_pred_original: {Y_pred_original}")
    print(f"history: {history},\n\
    history.history: {history.history},\n\
    train loss: {history.history['loss']},\n\
    validation loss: {history.history['val_loss']}\n")

    # Error report
    mse = mean_squared_error(Y_test_original, Y_pred_original)
    print(f"Mean Squared Error (DNN): {mse}")

    return Y_test_original, Y_pred_original, mse, train_loss, validation_loss



# Run `python3 dnn.py > dnn_model_output.txt` to test the DNN model
# separately from the fullstack app and see stdout in a separate text file
if __name__ == '__main__':
    # Load the dataset
    coalindia_dataset = pd.read_csv("Datasets/COALINDIA.csv")

    # Initialize list of dropped features
    dropped_features = ['Date', 'Symbol',
                        'Series', 'Trades', 'Turnover',
                        'Deliverable Volume', '%Deliverble',
                        'Last', 'VWAP', 'Prev Close']
    cleaned_coalindia_dataset = coalindia_dataset.drop(dropped_features, axis=1)
    run_dnn_model(cleaned_coalindia_dataset)