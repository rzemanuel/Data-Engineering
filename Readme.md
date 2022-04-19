
## Introduction
This project is a demo for FilmSTAT, the company I'll be launching this year.  The focus will be machine learning plugins for post production software geared towards color science transforms. 

The first half of my pipeline inputs a folder of images that contain images of the sample test chart.  Then outputs a SQL database of rgb coordinates for each swatch color per chart.  [data_engineering](https://github.com/rzemanuel/Data-Engineering/blob/main/data_engineering.py) will run this pipeline and create a database named 'White_Balance.db" To run this pipeline please see the required source images below.

The second half converts the database to a numpy array,trains an ANN on the dataset and outputs the saved model.
The model is demoed here through Heiroku  [ml_pipeline](https://github.com/rzemanuel/Data-Engineering/blob/main/ml_pipeline.py) will run this pipleine, if you would like to use a copy of "White_Balance.db" please find it here:
https://drive.google.com/file/d/1-eDrTsaiuIWoH3D-bEBGw-8H8h0b2cQB/view?usp=sharing
and place it in the 'pipeline' folder.


## Tricky Package Installs
OpenEXR is a difficult to install, but google colab makes the install as easy as:

```pip install OpenEXR```

This [notebook](https://github.com/rzemanuel/Data-Engineering/blob/main/Pipeline.ipynb) is available to run data_enginnering.py in google colab with OpenEXR. The repo will need to be move to google drive to reference files with google colab.



## Source Images

Source images can be found here: https://drive.google.com/drive/folders/1JDudc9VQm-RswkKT0eEUfZ1wxD_uxBUF?usp=sharing.  Download the entire foloder to the working directory prior to running data_enginnering.py.

For Unit Testing, the following test image:

https://drive.google.com/file/d/1lTfMdNlErCDYHDFWLFA4r-NUiAyWRU0S/view?usp=sharing

will need to be added to [unittesting](https://github.com/rzemanuel/Data-Engineering/tree/main/unittests) to run unittest1.py.

    


