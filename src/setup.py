from distutils.core import setup
setup(name='my2ca',
      version='2.0',
      packages=['my2ca', 'my2ca.codegen', 'my2ca.docgen', 'my2ca.lp', 'my2ca.mysqlcon', 'my2ca.ui', 'my2ca.utest'],
      author='Samith Sandanayake',
      author_email='sam.the.devel@gmail.com',
      description='MySQL to Cassandra migration tool',
      license='GPLv2',
      requires=[
          'pyparsing',
          'MySQLdb',
          'PySide',
          'sqlparse',
          'mako',
      ],
      )

