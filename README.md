# Monika

Currently running on Rasa shell:
![](https://i.imgur.com/00A3pKw.png)


## Requirements
- Python 3.8
-
- Rasa 2.0.0rc4

## Usage

First, create a virtual environment for the packages in the folder where the repository was cloned (recommended):

```console
foo@bar ~ % python3 -m venv env
```

Activate the environment:

```console
foo@bar ~ % source env/bin/activate
```

Install the requirements:

```console
(env)foo@bar ~ % python3 -m pip install -r requirements.txt
```

The installation may take some time. Aftewards, call her by using the 'rasa shell' command

```console
(env)foo@bar ~ % rasa shell
```
