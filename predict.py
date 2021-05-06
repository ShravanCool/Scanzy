from tensorflow import keras
from keras.preprocessing import image
import numpy as np

def predict(img, model_path):
    """
    Method to take the given input image, 
    load the model, and predict if the given
    image has presence of Covid or not.
    """
    print(image)

    img = image.load_img(img, target_size = (224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    classifier = keras.models.load_model(model_path)

    result = classifier.predict(img)

    return result # '1' if normal, '0' if Covid


