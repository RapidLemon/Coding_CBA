import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

# Load the data from file
X_train = np.loadtxt(r"Working scripts\Player movement prediction\Training data\\" +'mock_data_X_train.csv', delimiter=',').reshape((10, 5, 26, 1))
y_train = np.loadtxt(r"Working scripts\Player movement prediction\Training data\\" +'mock_data_y_train.csv', delimiter=',').reshape((10, 26, 1))
X_test = np.loadtxt(r"Working scripts\Player movement prediction\Training data\\" +'mock_data_X_test.csv', delimiter=',').reshape((10, 5, 26, 1))
y_test = np.loadtxt(r"Working scripts\Player movement prediction\Training data\\" +'mock_data_y_test.csv', delimiter=',').reshape((10, 26, 1))

y_train = np.argmax(y_train, axis=2)
y_test = np.argmax(y_test, axis=2)


# Define the model architecture
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(5, 26, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(26, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Evaluate the model on the test set
scores = model.evaluate(X_test, y_test, verbose=0)

# Print the model's loss on the test set
print('Test loss:', scores[0])

# Print the model's accuracy on the test set
print('Test accuracy:', scores[1])
