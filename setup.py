from setuptools import setup, find_packages
import sys

sys.path.append('./src')
sys.path.append('./test')

setup(
    name = 'Sample',
    version = '0.1',
    package = find_packages(),
    test_suite = 'sample_test.suite'
)
