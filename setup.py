import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="happy_config",
    version="0.0.3",
    author="Yichen Xu",
    author_email="yichen.x@outlook.com",
    description="Managing ML experiment configuation with joy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GraphCL/happy_config",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['pyyaml', 'nni'],
)
