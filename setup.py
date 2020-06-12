from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='EResponse',
    version='1.0',
    packages=['eresponse'],
    url='github.com/Beaxhem/eresponse',
    license="mit",
    author='beaxhem',
    author_email='senchukov02@gmail.com',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
