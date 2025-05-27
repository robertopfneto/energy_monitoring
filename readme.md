Em settings.py adicionar:

AUTH_USER_MODEL = 'bytegreen.Funcionario'

Em INSTALLED_APPS:
    'bytegreen',
    'rest_framework'