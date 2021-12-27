from setuptools import setup, find_packages

setup(name='DiscogsAPI',
      version='0.1',
      description='to fill...',
    #   url='http://github.com/...',
      author='SimCo',
      author_email='si.colonna92@gmail.com',
      # package_dir={"": "discogsapi"},
      packages=find_packages(),
      install_requires=[
          'pandas',
          'oauth2',
          'requests',
      ],
      zip_safe=False)