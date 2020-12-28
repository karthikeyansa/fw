from setuptools import find_packages, setup

setup(
    name='jsonfile_crd',
    packages=find_packages(include=['jsonfile_crd']),
    version='1.0.6',
    description='Libraries to perform CRD over JSON file',
    author='Karthikeyan',
    authors_email=['karthikeyansa39@gmail.com'],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)