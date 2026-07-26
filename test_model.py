import tensorflow as tf
from tensorflow.keras.datasets import mnist
import numpy as np

# Load trained model
model = tf.keras.models.load_model("handwritten_character_model.keras")

# Load test dataset
(_, _), (test_images, test_labels) = mnist.load_data()

# Normalize
test_images = test_images / 255.0

# Select one image
index = 0
prediction = model.predict(np.expand_dims(test_images[index], axis=0))

print("Predicted Digit:", np.argmax(prediction))
print("Actual Digit:", test_labels[index])