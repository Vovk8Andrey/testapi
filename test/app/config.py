import os
from dotenv import load_dotenv
from starlette.config import Config


dir_path = os.path.dirname(os.path.realpath(__file__)) #получаем urm нашей директории, где находится наш проект
root_dir = dir_path[:-3] #то, где находится, наша бд
config = Config(f'{root_dir}.env')


SQLALCHEMY_DATABASE_URL = f'sqlite:///{root_dir}' + config('DB_NAME', cast=str)



http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = os.environ.get("KEY")
secret = os.environ.get("SECRET")
filepath = r"C:\Users\999\PycharmProjects\test\app\photo\dvoe.jpg"
attributes="gender,age,ethnicity"
