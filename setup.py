try:
    from numpy.distutils.core import Extension
    from numpy.distutils.core import setup as setup
    from numpy.distutils.misc_util import Configuration
    import scipy
    import pandas
    import pyhank

except:
    import pip
    pip.main(["install", "numpy"])
    pip.main(["install", "scipy"])
    pip.main(["install", "pandas"])
    pip.main(["install", "pyhank"])

    from numpy.distutils.core import Extension
    from numpy.distutils.core import setup as setup
    from numpy.distutils.misc_util import Configuration
    import scipy
    import pandas
    import pyhank


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
    config.add_include_dirs(["/usr/include/fgsl/"])
    return config


setup(
    name='induction_log_tools',
    version='0.0.1',
    author='MRLimcon',
    scripts=[
        'data_feeder.py',
        'data_analysis.py',
        'transformation_hankel.py',
        'transformation_voltage_to_conductivity.py'
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
       "pandas",
       "pyhank"
    ]
)
