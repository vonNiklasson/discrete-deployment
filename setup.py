from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='discrete-integration',
    version='0.1.0',
    author="Johan Niklasson",
    author_email="johan@niklasson.me",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vonNiklasson/discrete-integration",
    py_modules=['discrete-integration'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        di=discrete_integration.main:cli
    ''',
    classifiers=[],
    python_requires='>=3.5',
)
