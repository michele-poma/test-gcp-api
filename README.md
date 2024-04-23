<h1> GCP API </h1>

### INDEX
- [Descriprion](#Description)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Workflow](#Workflow)
- [Class Diagram](#Class Diagram)

### Description
The aim of this repository is that to uses Google Cloud API to test them.

It uses:
1. Google Cloud Storage
2. Google Cloud BigQuery

### Requirements
* Python v3.10+
* Poetry v1.8.2


### Installation
###### Ubuntu
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
###### Windows
Open PowerShell and execute the following command:

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
if you have installed Python through the Microsoft Store, replace py with python in the command above.


The installation script will suggest adding the folder with the poetry executable to the PATH variable. Do that by running the following command:
```bash
$Env:Path += ";C:\Users\<USER>\AppData\Roaming\Python\Scripts"; setx PATH "$Env:Path"
```
To verify the installation, run the following command:
```bash
poetry --version
```
To create the poetry environment, execute the following command:
```bash
poetry lock
poetry install
```

### Workflow
<p align="center">
  <img src="img/workflow.png?raw=true" />
</p>

### Class Diagram
<p align="center">
  <img src="img/classDiagram.png?raw=true" />
</p>