# ML-model-app
Stock Predictor app using DNN, ANN, or Perceptron!

Email Nayeel at *naimtiaz@ucdavis.edu* for any problems regarding setup, running the app, or any questions in general. He can get on a quick zoom call with you.

## Set up Instructions

1) Navigate to root directory `/ML-model-app`

2) Run `python -m venv ecs171` to create virtual environment
in the root directory

3) On mac OS, run `source ecs171/bin/activate` in root directory to activate virtual environment. On windows, run `.\ecs171\Scripts\activate` in root directory

4) Backend/misc scripts setup:
    
    4a) Navigate to backend directory: `cd backend`
    
    4b) Ensure your vitual environment is on and then run `pip install -r requirements.txt` to install python dependencies for the `backend` and other scripts in `misc_source_code`
    
    4c) Navigate back to root directory `/ML-model-app`

5) Frontend setup:
    
    5a) Navigate to frontend directory: `cd frontend`
    
    5b) Run `npm install` or `npm i` to install node dependencies
    
    5c) Navigate back to root directory `/ML-model-app`

6) Download our main dataset here: *https://github.com/CalculusSlayer/Stocks-DBs/blob/main/COALINDIA.csv* 

    Or any of the datasets hosted here: *https://github.com/CalculusSlayer/Stocks-DBs*

7) Done!

## Run main application

1) Make sure your environment is setup properly and your virtual environment is activated.

2) Navigate to backend directory and start uvicorn server by running `python3 main.py` or `python main.py`

3) Open new terminal tab/window and navigate to frontend directory and run react app by running `npm run start`

4) After the app launches on your browser, select a file from your computer (make sure you downloaded the COALINDIA.csv file or any other datasets from the repository) and also select a model to run.

5) Select okay when prompted to and after the second prompt the Actual close value vs. Predicted close value graph, Training Loss vs. Validation Loss graph, MSE, and R^2 should show up.

6) Repeat steps 4-5 for other datasets and models if you would like to while the app is still running

6) To stop the app, press `crtl + c` on both the terminal tabs/windows where you ran the backend server and the frontend client.

## Files