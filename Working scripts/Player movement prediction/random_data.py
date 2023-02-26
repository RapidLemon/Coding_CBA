import random
import numpy as np

# Generate random training and testing data and save to file
def generate_mock_data(num_examples, num_moves, filename):

    # Generate random data
    X = np.random.rand(num_examples, num_moves, 26)
    y = np.random.randint(2, size=(num_examples, 26))

    # Split the data into training and testing sets
    train_ratio = 0.8
    num_train = int(num_examples * train_ratio)
    X_train, y_train = X[:num_train], y[:num_train]
    X_test, y_test = X[num_train:], y[num_train:]


    # Reshape the data for compatibility with the model
    X_train = X_train.reshape((num_train, num_moves, 26, 1))
    y_train = y_train.reshape((num_train, 26, 1))
    X_test = X_test.reshape((num_examples - num_train, num_moves, 26, 1))
    y_test = y_test.reshape((num_examples - num_train, 26, 1))


    # Save the training and testing data as CSV files
    filename = 'random_data'
    np.savetxt(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\\" + filename + '_X_train.csv', X_train.reshape((num_train*num_moves, 26)), delimiter=',')
    np.savetxt(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\\" + filename + '_y_train.csv', y_train.reshape((num_train, 26)), delimiter=',')
    np.savetxt(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\\" + filename + '_X_test.csv', X_test.reshape(((num_examples-num_train)*num_moves, 26)), delimiter=',')
    np.savetxt(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\\" + filename + '_y_test.csv', y_test.reshape(((num_examples-num_train), 26)), delimiter=',')

    return X_train.reshape((num_train*num_moves, 26)), y_train.reshape((num_train, 26)), X_test.reshape(((num_examples-num_train)*num_moves, 26)), y_test.reshape(((num_examples-num_train), 26))



X_train, y_train, X_test, y_test = generate_mock_data(10, 5, 'mock_data')

# Print the shapes of the generated data
print('X_train shape:', X_train.shape)
print('y_train shape:', y_train.shape)
print('X_test shape:', X_test.shape)
print('y_test shape:', y_test.shape)

print('Number of training examples:', X_train.shape[0])
print('Number of testing examples:', X_test.shape[1])
