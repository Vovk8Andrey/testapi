import os

from starlette.config import Config


dir_path = os.path.dirname(os.path.realpath(__file__)) #получаем urm нашей директории, где находится наш проект
root_dir = dir_path[:-3] #то, где находится, наша бд
config = Config(f'{root_dir}.env')


SQLALCHEMY_DATABASE_URL = f'sqlite:///{root_dir}' + config('DB_NAME', cast=str)



http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = "eLDJn7Sp7wxI_aLLIDMsWuvoHkntKHxk"
secret = "tmnqp2i_Gijk_7T9U7nHdwUpTW61pvga"
filepath = r"C:\Users\999\PycharmProjects\test\app\photo\dvoe.jpg"
attributes="gender,age,ethnicity"