import random
import numpy as np

# Generate random training and testing data and save to file
def generate_mock_data(num_examples, num_moves, filename):
    # Generate mock input and output data
    X_train = np.zeros((num_examples, num_moves, 26))
    y_train = np.zeros((num_examples, 26))
    X_test = np.zeros((num_examples, num_moves, 26))
    y_test = np.zeros((num_examples, 26))

    for i in range(num_examples):
        # Generate a random sequence of positions
        positions = [random.choice(range(26)) for j in range(num_moves)]

        # Set the input and output vectors based on the positions
        for j in range(num_moves):
            if j < num_moves - 1:
                X_train[i, j, positions[j]] = 1
            else:
                y_train[i, positions[j]] = 1
                X_test[i, j, positions[j]] = 1
                y_test[i, positions[j]] = 1

    # Save the data to file
    np.savetxt(r"Working scripts\Player movement prediction\Training data\\" + filename + '_X_train.csv', X_train.reshape((num_examples*num_moves, 26)), delimiter=',')
    np.savetxt(r"Working scripts\Player movement prediction\Training data\\" + filename + '_y_train.csv', y_train.reshape((num_examples, 26)), delimiter=',')
    np.savetxt(r"Working scripts\Player movement prediction\Training data\\" + filename + '_X_test.csv', X_test.reshape((num_examples*num_moves, 26)), delimiter=',')
    np.savetxt(r"Working scripts\Player movement prediction\Training data\\" + filename + '_y_test.csv', y_test.reshape((num_examples, 26)), delimiter=',')

    # Reshape the data to match the expected input shape of the model
    X_train = X_train.reshape((num_examples, num_moves, 26, 1))
    y_train = y_train.reshape((num_examples, 26, 1))
    X_test = X_test.reshape((num_examples, num_moves, 26, 1))
    y_test = y_test.reshape((num_examples, 26, 1))

    return X_train, y_train, X_test, y_test



X_train, y_train, X_test, y_test = generate_mock_data(10, 5, 'mock_data')

# Print the shapes of the generated data
print('X_train shape:', X_train.shape)
print('y_train shape:', y_train.shape)
print('X_test shape:', X_test.shape)
print('y_test shape:', y_test.shape)

print('Number of training examples:', X_train)
print('Number of testing examples:', X_test)
