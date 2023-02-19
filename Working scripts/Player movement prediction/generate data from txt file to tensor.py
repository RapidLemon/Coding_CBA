import numpy as np

def generate_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    X_train = []
    y_train = []
    
    for line in lines:
        positions = line.strip().split()
        input_pos = positions[:-1]
        output_pos = positions[1:]
        
        # Convert positions to one-hot vectors
        input_vec = np.zeros((len(input_pos), 26))
        output_vec = np.zeros((len(output_pos), 26))
        for i, pos in enumerate(input_pos):
            row, col = ord(pos[0]) - ord('A'), int(pos[2:])
            input_vec[i, row] = 1
        for i, pos in enumerate(output_pos):
            row, col = ord(pos[0]) - ord('A'), int(pos[2:])
            output_vec[i, row] = 1
        
        X_train.append(input_vec)
        y_train.append(output_vec)
    
    return X_train, y_train

#Refined_training_data = generate_data(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Raw_Training_Data.txt")
trainingX = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Training_ready_data.TF_MX_DATA", "w")
trainingY = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Training_ready_data.TF_MY_DATA", "w")
#trainingX.write(Refined_training_data[0])
#trainingY.write(Refined_training_data[1])
trainingX.close()
trainingY.close()

#Refined_testing_data = generate_data(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Raw_Testing_Data.txt")
testingX = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Testing_ready_data.TF_MX_DATA", "w")
testingY = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Testing_ready_data.TF_MY_DATA", "w")
#testingX.write(Refined_training_data[0])
#testingY.write(Refined_training_data[1])
testingX.close()
testingY.close()

"""
Refined_training_data = generate_data(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Raw_Training_Data.txt")
trainingX = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Training_ready_data.TF_MX_DATA", "w")
trainingY = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Training_ready_data.TF_MY_DATA", "w")
trainingX.write(X_train)
trainingY.write(y_train)
trainingX.close()
trainingY.close()

#Refined_testing_data = generate_data(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Raw_Testing_Data.txt")
testingX = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Testing_ready_data.TF_MX_DATA", "w")
testingY = open(r"C:\Users\Tocom\OneDrive\Documents\python stuff\Coding CBA\Working scripts\Player movement prediction\Training data\Testing_ready_data.TF_MY_DATA", "w")
testingX.write(X_test)
testingY.write(y_test)
testingX.close()
testingY.close()
#"""