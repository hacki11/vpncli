from distutils.core import setup
setup(
  name = 'vpncli',
  packages = ['vpncli'],
  version = '0.1',
  license='apache-2.0',
  description = 'generic command line vpn client adapter for automation',
  author = 'Juergen Schmid',
  author_email = 'jur.schmid@gmail.com',
  url = 'https://github.com/hacki11/vpncli',
  download_url = 'https://github.com/hacki11/vpncli/archive/0.1.tar.gz',
  keywords = ['vpn', 'cisco', 'fortinet', 'vpnclient'],   #
  install_requires=[
          'keepasshttp',
      ],
  entry_points={
    'console_scripts': ['vpncli=vpncli:main'],
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)