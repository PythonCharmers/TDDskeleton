from setuptools import setup

setup(name='TDDskeleton',
      version='0.0.1',
      description='A structure to help with TDD exercises',
      long_description=open('README.md', encoding="utf8").read(),
      url='https://github.com/shuttle1987/TDDskeleton',
      author='Janis Lesinskis',
      license='AGPL v3',
      packages=['app'],
      classifiers = [
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='testing TDD unit-testing',
      install_requires=[
        # Add any packages your code requires here
      ],
      include_package_data = True,
)
