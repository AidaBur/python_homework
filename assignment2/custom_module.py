# custom_module.py

secret = None

def set_secret(new_secret):
    global secret
    secret = new_secret

def get_secret():
    return secret
