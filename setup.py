from setuptools import setup, find_packages

setup(
    name='tmdb-cli',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'typer==0.16.0',
        'shellingham==1.5.4',
        'typing_extensions==4.14.1',
        'urllib3==2.5.0',
        # add more if needed
    ],
    entry_points={
        'console_scripts': [
            'tmdb = tmdb_cli.main:app',
        ],
    },
)
