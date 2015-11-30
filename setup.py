from setuptools import setup

setup(name='sec_edgar_wrapper',
      version='0.1.1',
      author='Piero Palevsky',
      author_email='ppalevsky@gmail.com',
      install_requires=[
        'beautifulsoup4==4.4.1',
        'lxml==3.5.0',
        'requests==2.8.1',
        'xmltodict==0.9.2'
      ],
      description=('Python Wrapper for SEC Edgar, also contains some specific form parsers')
      )
