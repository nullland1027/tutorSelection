LOCAL_APP_CODE = 'tutorselection'
LOCAL_SECRET_KEY = 'your_secret_key'

LOCAL_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': LOCAL_APP_CODE,
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'post': 3306,
    },
}

PASSWORD_KEY = "your_password_key"
TOKEN_KEY = "your_token_key"