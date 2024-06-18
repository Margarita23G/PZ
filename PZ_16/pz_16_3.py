import pickle

from pz_16_1 import Matrix
from pz_16_2 import Car


def save_def(filename, objects):
    with open(filename, 'wb') as file:
        pickle.dump(objects, file)


def load_def(filename):
    with open(filename, 'rb') as file:
        objects = pickle.load(file)
    return objects


matrix1 = Matrix([[1, 2], [3, 4]], 2, 2)

matrix2 = Matrix([[5, 6], [7, 8]], 2, 2)

car = Car(150, 1600, 4)

objects = [matrix1, matrix2, car]
save_def("objects.pkl", objects)

loaded_objects = load_def("objects.pkl")

print("Загруженная матрица 1:")
print(loaded_objects[0])
print("\nЗагруженная матрица 2:")
print(loaded_objects[1])
print("\nЗагруженная машина:")
loaded_objects[2].display_info()
