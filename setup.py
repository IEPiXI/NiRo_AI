from setuptools import setup, find_packages

setup(
    name='niro_ai_package',
    version='0.0.1',
    author='Nicolas Freitag, Robert Krug',
    author_email='krg.rbrt@gmail.com',
    description='Python package for playing around with AI',
    url='https://github.com/IEPiXI/proj_NiRo_AI',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'kagglehub'
    ],
    python_requires='>=3.10',
)
