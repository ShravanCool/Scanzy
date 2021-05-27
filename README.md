# Scanzy

Scanzy is a simple web-application, which can be used for detecting the presence of covid-19. It uses a pre-trained convolutional neural network model and takes a chest x-ray image as its input, which is provided by the user.

## Directions for setting up environment-

To install the source, pre-requisites include-

- Python 3.6 or above
- Dependencies from requirements.txt file

First, clone this repository onto your system. Then, create a virtual environment and install the packages from requirements.txt:
```
cd path/to/folder
virtualenv venv -p python3.6  //or any other name and version
source venv/bin/activate
```
Now, install the python dependencies from requirements.txt:
```
pip install -r requirements.txt
```

## Directions to execute-

Inside the main project directory, run the following command to start the server-
```py
python app.py run
```

Now open the link shown in the terminal in any browser of your choice.

