import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import KFold
from tensorflow.keras.regularizers import l2

raw_data = pd.read_csv('/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/final-data-with-watts-stats.csv')

normalized_data = pd.read_csv('/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/normalized_outputs_v3.csv')

assert len(raw_data) == len(normalized_data), "Datasets must have the same number of rows."

X = raw_data[['Piece Number', 'Seat', 'Watts', 'Catch Angle', 'Finish Angle',
              'Catch Slip', 'Finish Slip', 'Length', 'Effective Length', 'Rate']]
y_raw = raw_data['Speed']
y_normalized = normalized_data['Normalized Speed']

tf.random.set_seed(57)

def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(16, activation='leaky_relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(12, activation='leaky_relu'),
        tf.keras.layers.Dense(8, activation='leaky_relu'),
        tf.keras.layers.Dense(1)
    ])
    optimizer = tf.keras.optimizers.Adam(0.01)
    model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mean_squared_error'])
    return model

kf = KFold(n_splits=4, shuffle=True, random_state=42)

def train_and_evaluate(y, label="Speed"):
    fold_no = 1
    all_mse = []
    test_rmse = []

    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        model = create_model()
        print(f'\nTraining for fold {fold_no} using {label}...')
        history = model.fit(X_train, y_train, epochs=100, batch_size=64, verbose=0, validation_data=(X_test, y_test))

        test_loss, test_mse = model.evaluate(X_test, y_test, verbose=0)
        all_mse.append(test_mse)

        mean_speed = np.mean(y_test)
        variance_speed = np.var(y_test)
        rmse = tf.math.sqrt(test_mse).numpy()
        rmse_pct = (rmse / mean_speed) * 100
        test_rmse.append(rmse)

        print(f'Fold {fold_no} Results ({label}):')
        print(f'Mean: {mean_speed:.4f}, Variance: {variance_speed:.4f}')
        print(f'Test RMSE: {rmse:.4f} ({rmse_pct:.2f}% of mean)')
        fold_no += 1

    print(f'\nOverall Performance using {label}:')
    print(f'Avg MSE: {np.mean(all_mse):.4f}, Std MSE: {np.std(all_mse):.4f}, Avg RMSE: {np.mean(test_rmse):.4f}\n')

# Peach Innovators
train_and_evaluate(y_raw, label="Speed")

# Peach Innovators 2.0
train_and_evaluate(y_normalized, label="Average Normalized Speed")
