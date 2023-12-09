# ML-model-app
Stock Predictor app using DNN, ANN, or Perceptron!

Email Nayeel at *naimtiaz@ucdavis.edu* for any problems regarding setup, running the app, or any questions in general. He can get on a quick zoom call with you.

## Set up Instructions

0) It is recommended to have relatively newer versions of React, ***NPM***, and Python before proceeding to avoid set up problems, especially NPM.

1) Navigate to root directory `/ML-model-app`

2) Run `python -m venv ecs171` to create virtual environment
in the root directory

3) On mac OS, run `source ecs171/bin/activate` in root directory to activate virtual environment. On windows, run `.\ecs171\Scripts\activate` in root directory

4) Backend/misc. scripts setup:
    
    4a) Ensure your vitual environment is on
    
    4b) Then run `pip install -r requirements.txt` from the root directory `/ML-model-app` to install python dependencies for the `backend` and other scripts in `misc_source_code`

5) Frontend setup:
    
    5a) Navigate to frontend directory: `cd frontend`
    
    5b) Run `npm install` or `npm i` to install node dependencies
    
    5c) Navigate back to root directory `/ML-model-app`

6) Download our main dataset here: *https://github.com/CalculusSlayer/Stocks-DBs/blob/main/COALINDIA.csv* 

    Or any of the datasets hosted here: *https://github.com/CalculusSlayer/Stocks-DBs*

7) Done!

## Run main application

1) Make sure your environment is setup properly and your virtual environment is activated (run `source ecs171/bin/activate` in root directory to activate virtual environment)

2) Navigate to backend directory and start uvicorn server by running `python3 main.py` or `python main.py`

3) Open new terminal tab/window and navigate to frontend directory and run react app by running `npm run start`

4) After the app launches on your browser, select a file from your computer (make sure you downloaded the COALINDIA.csv file or any other datasets from the repository) and also select a model to run.

5) Select okay when prompted to and after the second prompt the Actual close value vs. Predicted close value graph, Training Loss vs. Validation Loss graph, MSE, and R^2 should show up.

6) Repeat steps 4-5 for other datasets and models if you would like to while the app is still running

6) To stop the app, press `crtl + c` on both the terminal tabs/windows where you ran the backend server and the frontend client.

## Folders and Files

### ML-Model-App (root directory)

***backend*** - Folder with all the backend related files

***frontend*** - Folder with all the frontend related files

***misc_source_code*** - Folder with other scripts related to our project but not our fullstack app such as a pairplots generator script and neural networks visualizer script. All .py files/scripts in this folder should be runnable by running `python {name of .py file}`. Ex: `python visualizations.py`

***jupyter_files*** - Folder with pre-production jupyter files that were used to aid the creation of our optimized ML models. These files include a heat map and grid search (note these .ipynb files should be run on a jupyter notebook, not via python). Running grid search jupyter file takes around 8-10 hours as for DNN we test 2916 hyperparameters (6-7 hours), for ANN we test 972 parameters (1 hour), and for Perceptron we test 144 parameters (5-10 min).

***requirements.txt*** - Contains all the python modules needed to run the backend server and other miscellaneous scripts in misc_source_code

***README.md*** - This file that contains set up instructions and how to run the main app and other scripts

### backend

***models.py*** - Where our DNN, ANN, and perceptron models are defined

***main.py*** - Where we run our API (fast api) and start our backend server (uvicorn server). This is where we define our main API endpoint that orchestrates the entire process of taking an uploaded CSV file, cleaning the dataset, running the dataset with one of our ML models, and returning a JSON response.

***Datasets*** - Folder that contains the `COALINDIA.csv` dataset so you can run the dnn, ann, and perceptron models on that dataset directly. Navigate to backend directory and run `python models.py` to run all 3 models on the dataset.

***Datasets/COALINDIA.csv*** - Our main dataset containing stock data for the Indian stock: COALINDIA.

***dnn.py*** - Script that runs dnn model on `COALINDIA.csv`. Type `python dnn.py` in the `backend/` directory to run the script

***ann.py*** - Script that runs ann model on `COALINDIA.csv`. Type `python ann.py` in the `backend/` directory to run the script

***perceptron.py*** - Script that runs perceptron model on `COALINDIA.csv`. Type `python perceptron.py` in the `backend/` directory to run the script

### frontend

***src/App.jsx*** - This is the parent component for most of the other components in the `components/` directory.

***src/index.jsx*** - This is the root component and parent component of the App component. This is the highest level in the hierarchy tree and where the `App` component is called

***src/index.css*** - This is the corresponding css file for `src/index.jsx`. Some basic styling is done here.

***src/components*** - Folder containing different components such as `DataVisualization.jsx` and `FileUpload.jsx`

