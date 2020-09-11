# Project to learn integrating sklearn models with Django on a House prediction dataset.
In case using own model, First build the ML model, serialize it and use.   
I made the model with jupyter and serialized it with pickle "pickle.dump(lm,open(r"lm.pkl","wb"))".  
This command will create lm.pkl in same directory as your jupyter notebook. copy this pkl file to django yourApp folder and paste it.  

## Installation

Download the project, extract, open cmd/terminal in project directory.  

## Usage

```
python manage.py runserver

```
to run on public ip or domain name: use 

```
python manage.py runserver 0.0.0.0:8000

```
port 8000 needs to be forwarded

## Technology 
* Python
* jango
* Html/css


