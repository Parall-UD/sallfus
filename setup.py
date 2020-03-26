from distutils.core import setup
setup(
  name = 'sallfus',
  packages = ['scrapeasy', 'sallfus.fusion'],
  version = '0.1',
  license='MIT',
  description = 'Satellite image fusion on CPU and GPU/GPU',
  author = 'Parall UD',
  author_email = 'parallud2019@gmail.com',
  url = 'https://github.com/joelbarmettlerUZH/Scrapeasy',
  download_url = 'https://github.com/joelbarmettlerUZH/Scrapeasy/archive/pypi-0_1_3.tar.gz',
  keywords = ['fusion', 'cuda', 'images', 'Satellite', 'quality'],
  install_requires=[
          'numpy',
          'skimage',
          'pycuda',
          'skcuda',
          'cupy',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.6',
  ],
)
