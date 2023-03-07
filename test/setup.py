from setuptools import setup

setup(
    name='app-example',
    version='0.0.1',
    author='Vovk Andrey',
    description='FastAPI app',
    install_requires=[
        'fastapi==0.92.0',
        'uvicorn==0.20.0',
        'SQLAlchemy==2.0.4',
        'requests==2.28.2',
        'pytest==7.2.1',
    ],
    scripts=['app/main.py', 'scripts/create_db.py']
)
