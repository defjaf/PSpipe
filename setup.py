#- 
# setup.py
#-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from numpy.distutils.core import setup, Extension

extensions = [
    Extension(name='pspy.cov_fortran', sources=['pspy/extensions/cov_fortran/cov_fortran.f90',
                                                'pspy/extensions/wigner3j/wigner3j_sub.f'],
              extra_f90_compile_args=['-ffree-line-length-none', '-Wunused-variable']),
    Extension(name='pspy.mcm_fortran', sources=['pspy/extensions/mcm_fortran/mcm_fortran.f90',
                                                'pspy/extensions/wigner3j/wigner3j_sub.f']),
]

config = {
    'description': 'PS PY',
    'author':  "The SO collaboration",
    'url': 'https://github.com/simonsobs/PSpipe',
    'download_url': 'https://github.com/simonsobs/PSpipe',
    'version': '0.0.1',
    'install_requires': [
        'numpy',
        'pixell'
        ],
    'packages': [
        'pspy',
        ],
    'scripts': [],
    'name': 'pspy',
    'include_package_data':True,
    'data_files': [('data/Planck_Parchment_RGB.txt')],
    'ext_modules': extensions
}

setup(**config)

