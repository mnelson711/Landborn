from setuptools import find_packages, setup

setup(
    name='landborn',
    packages=find_packages(include=['landborn']),
    version='0.1.1',
    description='Landborn Visualization Library',
    author='Molly Nelson',
    install_requires=['pandas', 'numpy', 'matplotlib'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==8.0.0'],
    test_suite='tests'
)