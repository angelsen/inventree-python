# -*- coding: utf-8 -*-

import setuptools

# The import statement 'from inventree.base import INVENTREE_PYTHON_VERSION' has been commented out to prevent 
# issues during installation (such as unresolved dependencies) when using 'pip install .'.
# Instead, the version number is hardcoded below. This change ensures that setup.py does not rely on any 
# external packages that aren't guaranteed to be installed in the environment at setup time.
# from inventree.base import INVENTREE_PYTHON_VERSION

INVENTREE_PYTHON_VERSION = "0.12.2"

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="inventree",

    version=INVENTREE_PYTHON_VERSION,

    author="Oliver Walters",

    author_email="oliver.henry.walters@gmail.com",

    description="Python interface for InvenTree inventory management system",

    long_description=long_description,

    long_description_content_type='text/markdown',

    keywords="bom, bill of materials, stock, inventory, management, barcode",

    url="https://github.com/inventree/inventree-python/",

    license="MIT",

    packages=setuptools.find_packages(
        exclude=[
            'ci',
            'scripts',
            'test',
        ]
    ),

    install_requires=[
        "requests>=2.27.0"
    ],

    setup_requires=[
        "wheel",
    ],

    python_requires=">=3.8"
)
