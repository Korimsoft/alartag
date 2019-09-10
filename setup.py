import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alartag",
    version="0.0.2",
    author="Korimsoft",
    author_email="korimsoft@gmail.com",
    description="Automatic author/album tagging of music files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/korimsoft/alartag",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT",
        "Operating System :: OS Independent",
    ],
    scripts=['alartag'],
    python_requires='>=3.6',
    install_requires='mutagen'
)