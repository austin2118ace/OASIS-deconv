# setup.py
# run with:         python setup.py build_ext -i
# clean up with:    python setup.py clean --all

import numpy as np
from setuptools.extension import Extension
from setuptools import find_packages, setup
from Cython.Build import cythonize


ext_modules = [Extension("oasis.oasis_methods",
                         sources=["oasis/oasis_methods.pyx"],
                         include_dirs=[np.get_include()],
                         language="c++")]

setup(name='oasis.oasis_methods',
      ext_modules=cythonize(ext_modules,compiler_directives={'cdivision': True}),
)
