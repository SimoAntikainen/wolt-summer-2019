# Wolt Summer 2019 coding task

Two ways to run the project. 

Sensible jupyter notebook,
which calculates the medians, visualizes them and exports the medians
to csv file. 

Alternatively the vizualization can be accessed though
an small web page containing an interactive visualization, that allows
the modification of the selected timeframe (This is horribly overkill).

## Prerequisites

Working installation of python3 and pip.
Built on windows using anaconda python

## Installing
```
pip3 install flask pandas jupyter plotly
```
Or
```
conda install flask pandas jupyter plotly
```
## Running the projects

### Jupyter notebook
Navigate to cd /wolt-summer-2019 and run
```
jupyter notebook
```
Access the contents of the notebook at locationviz.ipynb
### Flask-app
Navigate to cd /wolt-summer-2019 and run
```
python vizbackend.py
```
Access the website at http://localhost:5000 











