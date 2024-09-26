import numpy as np
import scipy.linalg as la
import tensorflow as tf

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b= np.array([1, 2, 3])

a_transposed = a.T
c = a @ a_transposed

print("A @ A^T:\n", c)

det_a = np.linalg.det(a)
print(f"Determinante de A: {det_a}")

if det_a == 0:
    print("\nA matriz é singular, portanto não é possível resolver diretamente o sistema linear.")
    x = la.pinv(a) @ b
    print("Solução usando a pseudo-inversa:\n\n", x)
else:
    x = la.solve(a, b)
    print("Solução do sistema Ax = b:\n", x)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, input_shape=(784,)),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Activation('softmax'),
])

model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001), 
             loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
             metrics = ['accuracy'],)

(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape((-1,784))
x_test = x_test.reshape((-1,784))
x_train = x_train / 255
x_test = x_test / 255

model.fit(x_train, y_train, batch_size = 64, epochs = 5)
model.evaluate(x_test, y_test, verbose = 2)