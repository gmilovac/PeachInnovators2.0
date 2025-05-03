import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split, KFold
from tensorflow.keras.regularizers import l2

data = pd.read_csv('/Users/adamvonbismarck/Desktop/CS1951A/final-project-peach-innovators/data_deliverable/data'
                   '/full_data/final-data.csv')

X = data[[ 'Piece Number', 'Seat', 'Watts', 'Catch Angle', 'Finish Angle',
          'Catch Slip', 'Finish Slip', 'Length', 'Effective Length', 'Rate']]
y = data['Speed']

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

fold_no = 1
all_mse = []
test_RMSE = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    model = create_model()
    print(f'Training for fold {fold_no}...')
    history = model.fit(X_train, y_train, epochs=100, batch_size=64, verbose=1, validation_data=(X_test, y_test))

    # Evaluate the model
    test_loss, test_mse = model.evaluate(X_test, y_test, verbose=0)
    all_mse.append(test_mse)

    # Calculate additional metrics
    mean_speed = np.mean(y_test)
    variance_speed = np.var(y_test)
    test_rmse = tf.math.sqrt(test_mse).numpy()
    rmse_percentage = (test_rmse / mean_speed) * 100
    test_RMSE.append(test_rmse)

    print(f'Fold {fold_no} Results:')
    print(f'Mean Boat Speed: {mean_speed} m/s')
    print(f'Variance of Boat Speed: {variance_speed}')
    print(f'Test RMSE: {test_rmse}')
    print(f'RMSE as a percentage of Mean Boat Speed: {rmse_percentage:.2f}%')

    fold_no += 1

# Average performance metrics
print('Overall performance:')
print(f'Average MSE across all folds: {np.mean(all_mse)}')
print(f'Standard Deviation MSE across all folds: {np.std(all_mse)}')
print(f'Average RMSE across all folds: {np.mean(test_RMSE)}')
