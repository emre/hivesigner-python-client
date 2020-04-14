from setuptools import setup

setup(
    name='hivesigner',
    version='0.1.0',
    packages=['hivesigner'],
    url='https://github.com/emre/hivesigner',
    license='MIT',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='Python client library of Hivesigner',
    install_requires=["requests", "responses"]
)
