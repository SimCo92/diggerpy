from setuptools import setup

setup(name='DiscogsAPI',
      version='0.1',
      description='to fill...',
    #   url='http://github.com/storborg/funniest',
      author='SimCo',
    #   author_email='flyingcircus@example.com',
      license='MIT',
    #   packages=,
      install_requires=[
          'pandas',
          'discogs_client',
          'time',
          'requests',
          'json',
      ],
      zip_safe=False)