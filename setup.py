# setup.py, config file for distutils

from distutils.core import setup
from distutils.command.install_data import install_data
import os


class smart_install_data(install_data):
    def run(self):
        #need to change self.install_dir to the actual library dir
        install_cmd = self.get_finalized_command('install')
        self.install_dir = getattr(install_cmd, 'install_lib')
        return install_data.run(self)


setup(name='EasyDialogs for Windows',
      version='46691.0',
      description='EasyDialogs for Windows',
      author='Jimmy Retzlaff',
      author_email='jimmy@retzlaff.com',
      url='http://www.averdevelopment.com/python',
      license='MIT',
      long_description='Makes it easy to display simple dialogs on Windows',
      classifiers=[  # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
        ],
      platforms='Windows',
      packages=['EasyDialogs'],
      package_dir={'EasyDialogs' : 'EasyDialogs'},
      data_files=[('EasyDialogs', [
                        'license.txt',
                        'EasyDialogsResources.rc',
                        'resource.h',
                        'changes.txt',
                        'README.md',
                        'manifest.in',
                       ]
                  )
                 ],
      cmdclass = {'install_data': smart_install_data},
     )
