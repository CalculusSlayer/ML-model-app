from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

# Run "curl http://localhost:8000" in terminal to test
@app.get("/") # route decorator
def read_root():
    return {"message": "Hello from FastAPI"}

# Run "curl http://localhost:8000/example" in terminal to test
@app.get("/example") # route decorator
def read_example():
    return {"message69": "This is another example endpoint"}

# Run 
# " curl -X POST http://localhost:8000/submit-data -H "Content-Type: application/json" -d '{"key1":"value1", "key2":"value2"}' "
# -X specifies whether it's GET or POST request (no need for GET b/c it's GET by default)
# -H specifies the type of content you are sending. You should always specify as json even though
# it is usually the default for a lot of APIs
# -d specifies the actual content you are sending (json string in this case). You need to wrap it
# around single quotes
@app.post("/submit-data")
def handle_data(item: dict):
    # Process the item here
    return {"received_data": item}


# Define a Pydantic model for the User data
class User(BaseModel):
    name: str
    email: str
    age: int

# 1) Run " curl -X POST http://localhost:8000/create-user -H "Content-Type: application/json" -d '{"name": "Roger", "email": "roger@email.com", "age": 21}' "
# for successful message confirmation.
# 2) Run " curl -X POST http://localhost:8000/create-user -H "Content-Type: application/json" -d '{"name": "Lil Tay", "email": "tay@email.com", "age": 11}' "
# to raise http exception (in this case we raise an exception within this file b/c the user's age is too low).
@app.post("/create-user")
def create_user(user: User):
    # Here, you would typically save the user information to a database
    # For demonstration, we'll just return the user data with a success message

    # Example of a simple validation
    if user.age < 18:
        raise HTTPException(status_code=400, detail="Age must be 18 or above")

    return {"message": "User created successfully", "user": user.dict()}

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        return JSONResponse(status_code=400, content={"message": "Invalid file type"})

    # Read the contents of the file
    dataset = pd.read_csv(file.file)
    
    # Process the CSV file (to feed to ML model)
    # Initialize list of dropped features
    dropped_features = ['Date', 'Symbol',
                        'Series', 'Trades', 'Turnover',
                        'Deliverable Volume', '%Deliverble',
                        'Last', 'VWAP', 'Prev Close']
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