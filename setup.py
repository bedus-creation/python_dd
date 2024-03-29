import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_dd",
    version="0.0.15",
    author="Bedram Tamang",
    author_email="tmgbedu@gmail.com",
    description="The missing `dd` function in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bedus-creation/python_dd",
    packages=['python_dd'],
    package_dir={'python_dd': 'python_dd'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
