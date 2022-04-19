
## Introduction
This project is a demo for FilmSTAT, the company I'll be launching this year.  The focus will be machine learning plugins for post production software geared towards color science transforms.  
The first half of my pipeline inputs a folder of images that contain images of the sample test chart.  Then outputs a SQL database of rgb coordinates for each swatch color per chart.  
The second half converts the database to a numpy array,trains an ANN on the dataset and outputs the saved model.
The model is demoed here through Heiroku 


## Tricky Package Installs
OpenEXR is a difficult to install, but google colab makes the install as easy as:

```pip install OpenEXR```

The notebook is available to run data_enginnering.py with OpenEXR

    


