from models import run_ann_model
import pandas as pd

# Run `python3 ann.py > ann_out.txt` to test the ann model
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
    run_ann_model(cleaned_coalindia_dataset)


if __name__ == '__main__':
    main()