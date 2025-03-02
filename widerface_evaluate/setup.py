"""
WiderFace evaluation code
author: wondervictor
mail: tianhengcheng@gmail.com
copyright@wondervictor
"""

from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy
import platform
import os

extra_compile_args = []
extra_link_args = []

if platform.system() == 'Darwin' and platform.machine() == 'arm64':
    os.environ["CFLAGS"] = "-arch arm64"
    os.environ["ARCHFLAGS"] = "-arch arm64"
    extra_compile_args.extend(["-arch", "arm64"])
    extra_link_args.extend(["-arch", "arm64"])

package = Extension(
    'bbox',
    ['box_overlaps.pyx'],
    include_dirs=[numpy.get_include()],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args
)
setup(ext_modules=cythonize([package]))
