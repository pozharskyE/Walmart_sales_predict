import matplotlib.pyplot as plt
from math import ceil

def feature_subplots_from_Xy(labels, X, y, num_of_cols=2):
    from math import ceil

    num_of_rows = ceil(len(labels) / num_of_cols)
    fig, axs = plt.subplots(num_of_rows, num_of_cols)
    
    for label in labels:
        for row in range(num_of_rows):
            for col in range(num_of_cols):
                axs[row, col].scatter(X[label], y)
    plt.show()
        

def feature_subplots_from_df(df, feature_labels, target_label, num_of_cols=2):
    from math import ceil

    num_of_rows = ceil(len(feature_labels) / num_of_cols)
    fig, axs = plt.subplots(num_of_rows, num_of_cols, figsize=(2,4))
    
    counter = 0
    while counter < len(feature_labels):
        for row in range(num_of_rows):
            for col in range(num_of_cols):
                axs[row, col].scatter(df[feature_labels[counter]], df[target_label])
                counter += 1
    plt.show()
