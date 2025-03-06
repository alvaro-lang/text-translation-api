# Text Translation API

Python version: Python 3.9.6

API made in Django with the app Django Rest Framework.

---

App which allows you to translate text into any language of your choice, offering the ability to adjust the translation tone between formal or informal based on your needs. Additionally, for your convenience, you can use voice input to dictate the text you want to translate, eliminating the need to type manually. Also, when you log in, you will have access to your translation history.

## App setup

### 1. Create Virtual environment

```sh
python -m venv <venv_name>
```
### 2. Activate Virtual environment

```sh
<venv_name>\Scripts\activate
```

### 3. Install dependencies with "requirements.txt"

```sh
pip install -r requirements.txt
```

## Endpoints

### Register

Route:

```
api/auth/register
```

Input:

```
{
    "username": "",
    "password": ""
}
```


### Login

```
api/auth/login
```

### Translate text formal or informal

Route:

```
api/translation/translate
```

Input:

```
{
    "source_text": "",
    "language": "",
    "style": ""
}
```

### Translations history

Get your user account's translation history

```
api/translation/history
```