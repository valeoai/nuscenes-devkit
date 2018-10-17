from setuptools import setup
from setuptools import find_packages


setup(name='nuscenes',
      version='0.1',
      license='MIT',
      install_requires=['pyquaternion==0.9.2',
                        'tqdm'],
      packages=find_packages())
