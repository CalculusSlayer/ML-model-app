from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
from dnn import run_dnn_model

app = FastAPI()

# FastAPI server using port 8000 while react app using port 3000
# If your React app is served from a different port or domain than your FastAPI server, 
# you will encounter CORS (Cross-Origin Resource Sharing) issues. 
# To resolve this, configure CORS in your FastAPI application:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        return JSONResponse(status_code=400, content={"message": "Invalid file type"})

    # Read the contents of the file
    dataset = pd.read_csv(file.file)
    
    # Process the CSV file (to feed to ML model)
    # Initialize list of dropped features
    dropped_features = ["Date", "Symbol",
                        "Series", "Trades", "Turnover",
                        "Deliverable Volume", "%Deliverble",
                        "Last", "VWAP", "Prev Close"]
    cleaned_dataset = dataset.drop(dropped_features, axis=1)

    # run ML model
    Y_test_original, Y_pred_original, mse, train_loss, validation_loss = run_dnn_model(cleaned_dataset)

    # Convert numpy arrays to lists for JSON serialization
    Y_test_list = Y_test_original.flatten().tolist()
    Y_pred_list = Y_pred_original.flatten().tolist()

    # mse is probably already a scalar, but ensure it's a native Python type, not numpy type
    mse_value = float(mse)

    # Respond with a message or result
    return {
        "mse": mse_value,
        "Y_test": Y_test_list,
        "Y_pred": Y_pred_list,
        "train loss": train_loss,
        "validation loss": validation_loss
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)