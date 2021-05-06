from tensorflow.keras import load_model
from keras.preprocessing import image
import numpy as np

def predict(image, model_path):
    """
    Method to take the given input image, 
    load the model, and predict if the given
    image has presence of Covid or not.
    """

    img = image.load_img(image, target_size = (224, 244))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)

    classifier = load_model(model_path)

    result = classifier.predict(img)

    return result # '0' if normal, '1' if Covid


