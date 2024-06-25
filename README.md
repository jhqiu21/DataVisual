# DataVisual

Your data visualization platform and personal working log

## General Intro

This is a online data visualization log build using Python and Django, aiming for providing a platform keeping track and visualizing your data set while you can also log your idea and some important result of your data analysis.

## Features
This project is still under going, there is the features of this tool:

- Register
- Log in
- Log out
- Add a new topic
- Delete target topic and all entries associated with it
- Add a new entry associate with a specific topic
- Delete a target entry associate with a specific topic
- upload file and perform a specific data analysis method (Undergoing)

## Set up

- Create virtual environment in `visual_log` dir
```
python -m venv venv
```
- Activate virtual environment
```
source venv/bin/activate
```
- third step : install package and ibrary from requirements.txt
```
pip install -r requirements.txt
```
- Run django server
```
python manage.py runserver
```

## Data Set Source

We currently focus on [TCGA Data Set](https://www.cancer.gov/ccg/research/genome-sequencing/tcga) to analysis the distribution of different cancer.

## Common Skills

You may refer to the following folder in the repo for more details

- [common plot](mpl/)
- [api_visual](api_visual/python_repos.py)
- [file_visual](file_visual/)

## Test Data File

- [TCGA Clinical Data Set](TCGA/)

## Contribute

If you are have a particular new method and more modern technology to apply in this project, please send merge request!