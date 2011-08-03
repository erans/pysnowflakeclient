import os
from distutils.core import setup

# also update version in __init__.py
version = '0.1'

setup(
    name="pysnowflakeclient",
    version=version,
    keywords=["snowflake", "pysnowflake"],
    long_description="",
    description="Python Snowflake Client",
    author="Eran Sandler",
    author_email="eran@sandler.co.il",
    url="http://github.com/erans/pysnowflakeclient",
    license="Apache Software License",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=['pysnowflakeclient', 'pysnowflakeclient.Snowflake'],
    install_requires=['thrift>=0.61'],
    requires=['thrift (>=0.61)'],
    download_url="http://github.com/downloads/erans/pysnowflakeclient/pysnowflakeclient-%s.tar.gz" % version,
)