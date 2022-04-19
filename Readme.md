
## Introduction
This project is a demo for FilmSTAT, the company I'll be launching this year.  The focus will be machine learning plugins for post production software geared towards color science transforms. 

My project is about camera white balance control in post production.  Having the ability to change in camera controls after the fact usually requires RAW aquisition formats that have strict patents.  Many camera manufactureres that don't have access to RAW format licensing in camera, so the resort to recording RAW formats outside the camera.  This requires an external recorder which is a added cost for camera operators and productions.  Using ANN regression modeling, this project aims to create a pipeline for training a model to approximate in the non-linear camera transforms for white balance control, to allow for RAW control without an external recorder.  The pipeline web application will demo the post production controls that are possible with white balance. 

The pipeline will be updated in near future to convert the trained model into a transform in C to integrate with post production software. 

The first half of my pipeline inputs a folder of images that contain images of the sample test chart.  Then outputs a SQL database of rgb coordinates for each swatch color per chart.  [Data_Engineering](https://github.com/rzemanuel/Data-Engineering/blob/main/data_engineering.py) will run this pipeline and create a database named 'White_Balance.db" To run this pipeline please see the required source images below.

The second half converts the database to a numpy array, trains an ANN on the dataset and outputs the saved model.
[ML_Pipeline](https://github.com/rzemanuel/Data-Engineering/blob/main/ml_pipeline.py) will run this pipleine, if you would like to use a copy of "White_Balance.db" please find it here:
[White_Balance.db](https://drive.google.com/file/d/1-eDrTsaiuIWoH3D-bEBGw-8H8h0b2cQB/view?usp=sharing)
and place it in the working directory folder.


## Tricky Package Installs
OpenEXR is a difficult to install, but google colab makes the install as easy as:

```pip install OpenEXR```

This [notebook](https://github.com/rzemanuel/Data-Engineering/blob/main/Pipeline.ipynb) is available to run data_enginnering.py in google colab with OpenEXR. It's easiest to move this repo to google drive to reference files with google colab.



## Source Images

[Source images](https://drive.google.com/drive/folders/1JDudc9VQm-RswkKT0eEUfZ1wxD_uxBUF?usp=sharing) will needed in order to run data_engineering.py from scratch.  Download the foloder and add it to the working directory prior to running data_enginnering.py.

For Unit Testing, you will need this [test image](https://drive.google.com/file/d/1lTfMdNlErCDYHDFWLFA4r-NUiAyWRU0S/view?usp=sharing). Add it to [unittesting](https://github.com/rzemanuel/Data-Engineering/tree/main/unittests) to run unittest1.py.

    
## Web Application
The model is demoed here through Heiroku here:

