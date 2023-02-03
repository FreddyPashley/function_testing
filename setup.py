from setuptools import setup, find_packages


setup(
    name='function_testing',
    version='1.0.1',
    license='MIT',
    author="Freddy Pashley",
    author_email='fredpashley1@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/FreddyPashley/function_testing',
    keywords='python function testing',
    install_requires=[],

)