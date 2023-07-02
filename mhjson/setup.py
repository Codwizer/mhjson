"""Run "python setup.py install" to install mhjson."""

from setuptools import setup

try:
    with open('README.md') as f:
        long_description = f.read()

except Exception:
    long_description = """
    `mhjson` is a simple, elegant Python package to Query over any
    type of JSON Data. It'll make your life easier by giving the
    flavour of an ORM-like query on your JSON.

    More information at: https://github.com/CodWize/mhjson.
"""


setup(name="mhjson",
      packages=['mhjson'],
      version='1.0.0',
      description="Query over Json file",
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: '
          'Python Modules',
          'Programming Language :: Python :: 3',
      ],
      author='Serega',
      author_email='nikitatihomirov19@yandex.ru',
      license='MIT',
      url="https://github.com/CodWize/mhjson",
      keywords=['Python', 'plugin'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['setuptools>=38.6.0'],
      )
