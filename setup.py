from setuptools import setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

with open('maui/_version.py') as versionfile:
    exec(versionfile.read())

setup(name='maui-tools',
    version=__version__,
    description="Multi-omics Autoencoder Integration",
    author='Jonathan Ronen',
    license='GPLv3',
    author_email='yablee@gmail.com',
    url='https://github.com/BIMSBbioinfo/maui',
    packages=['maui'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'pytest',
        'numpy>=1.14.5',
        'pandas',
        'scipy',
        'scikit-learn',
        'keras',
        'tensorflow',
        'pytest>=3.6.0'
    ],
)
