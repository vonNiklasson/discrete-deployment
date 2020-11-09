from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='discrete-deployment',
    version='0.1.3',
    author="Johan Niklasson",
    author_email="johan@niklasson.me",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vonNiklasson/discrete-deployment",
    install_requires=[
        'click==7.1.2',
        'python-dotenv==0.15.0',
        'PyYAML==5.3.1',
        'python-slugify==4.0.1',
    ],
    entry_points='''
        [console_scripts]
        ddep=discrete_deployment.main:cli
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
