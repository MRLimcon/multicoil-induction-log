from numpy.distutils.misc_util import Configuration
from numpy.distutils.core import setup as setup
from numpy.distutils.core import Extension

ext_modules = [
    Extension("induction_log_tools.fortran_bins.petroleum_probability",
              sources=['data_analysis/conductivity_resistivity_to_probability.f95']),
    Extension("induction_log_tools.fortran_bins.data_feeder",
              sources=['data_feeding/data_feeder.f95']),
    Extension("induction_log_tools.fortran_bins.fourier_hankel_transform",
              sources=['data_transformation/magnetic_to_resistivity/fourier_hankel_transform.f95']),
    Extension("induction_log_tools.fortran_bins.voltage_to_conductivity",
              sources=['data_transformation/voltage_conductivity/voltage_to_conductivity.f95']),
]


def configuration(parent_package='', top_path=None):
    config = Configuration('induction_log_tools')
    return config


setup(
    name='induction_log_tools',
    version='0.0.1',
    author='MRLimcon',
    scripts=[
        'data_feeder.py',
        'dataframe_utils.py',
        'pde_solver.py'
    ],
    url='https://github.com/MRLimcon/numerical_module',
    license='LICENSE',
    description='An open source tool to analyze outputs from multicoil induction log.',
    long_description=open('README.md').read(),
    configuration=configuration,
    ext_modules=ext_modules,
    install_requires=[
       "numpy",
       "scipy",
       "pandas"
    ]
)
