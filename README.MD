# Components

## OCR 

Optical Character Recognition is essentially an object detection task where the objects at hand are typed characters.

## HWRT

Similarly to OCR handwritten recognition works in the same manner, but implies handwritten characters instead of tyed characters.

## IE

Information Extraction pipeline analyses a text and extract informations of interest from the text.

## AOD 

Anomaly and Outlier Detection pipeline tackles processing timeseries data and detecting anomalies or outlier which can then be further studied by researchers after being detected.

## CVA

CV Analysis refers to analysing both text and tabular data and looking for different aspects from its analysis and up to classifying a CV into either suspcious/non-suspicious CVs and estimating CVs with a score between 0 and 100 in terms of how suspicious it might be.

## VE

Visualization and explainability is a really important component in checking up the rest of the components. Visualization provides intuitive analysis for the researchers. Explainability ensures learn to perform that tasks at hand for the right reasons (e.g. seeing the right parts of a cv as suspicious or identifying the letters in the right places).

## Utils

Utils contains common parts of code which can be used by any of the above components

# Users

The target users of this functionalities are the researchers in helping them to pursue their analysis, as well as allowing its partial (or total) automatization of some processes.

# Running the code

In order to run the code from this repo you should firstly create an anaconda environment with a version of Python 3.10:

```
conda create -n integritate_env python=3.10
```

Then, activate the environment from the terminal via: 
```
conda activate integritate_env
```
Install the necessary packages from the root of the project with:
```
pip install -r requirements.xt
```
Then run any piece of code you wish.

# Folder system imports problem

If you will encounter any errors related to importing stuff from other Python files from the "src" folder we recommend the following line of code:
```
export PYTHONPATH=\`pwd\`
```
Should fix any path problems.
