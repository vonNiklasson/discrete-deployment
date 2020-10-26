from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='discrete-integration',
    version='0.1.1',
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
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires='>=3.5',
)
