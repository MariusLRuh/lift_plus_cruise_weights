from distutils.core import setup

setup(
    name='lift_plus_cruise_weights',
    version='0',
    packages=[
        'lift_plus_cruise_weights',
    ],
    install_requires=[
        'openmdao',
        'csdl',
        'csdl_om',
    ],
)