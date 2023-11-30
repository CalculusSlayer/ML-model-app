from models import run_dnn_model
import pandas as pd

# Run `python3 dnn.py > dnn_out.txt` to test the dnn model
# separately from the fullstack app and see stdout in a separate text file
def main():
    # Load the dataset
    coalindia_dataset = pd.read_csv("Datasets/COALINDIA.csv")

    # Initialize list of dropped features
    dropped_features = ['Date', 'Symbol',
                        'Series', 'Trades', 'Turnover',
                        'Deliverable Volume', '%Deliverble',
                        'Last', 'VWAP', 'Prev Close']
    cleaned_coalindia_dataset = coalindia_dataset.drop(dropped_features, axis=1)
    run_dnn_model(cleaned_coalindia_dataset)


if __name__ == '__main__':
    main()