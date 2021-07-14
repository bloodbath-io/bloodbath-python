from setuptools import find_packages, setup
setup(
    name='bloodbath',
    packages=find_packages(include=['bloodbath']),
    version='1.0.0',
    description='Python wrapper for Bloodbath',
    author='Laurent Schaffner',
    author_email='laurent.schaffner.code@gmail.com',
    home_page='https://github.com/bloodbath-io/bloodbath-python',
    license='MIT',
    install_requires=['requests==2.26.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.4'],
    test_suite='tests',
)