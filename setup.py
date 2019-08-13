from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="qg.xmlsec.binding.init",
    version="0.1.0",
    description="A simple package for dm.xmlsec.binding initialization",
    author="Taras Dyshkant",
    author_email="hitori@quintagroup.org",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.quintagroup.com/hitori/qg.xmlsec.binding.init",
    packages=find_packages(),
    namespace_packages=["qg",
                        "qg.xmlsec",
                        "qg.xmlsec.binding",
    ],
    install_requires=["setuptools",
                      "dm.xmlsec.binding>=2.0",
                      "zope.component",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
