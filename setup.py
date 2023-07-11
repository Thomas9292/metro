from setuptools import setup

setup(
    name='metro',
    version='0.0.1',
    packages=['metro'],
    entry_points={
        'console_scripts': [
            'metro = metro.__main__:main'
        ]
    },
    install_requires=[
        'numpy',
        'pygame',
    ]
)