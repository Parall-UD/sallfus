from distutils.core import setup

setup(
    name='sallfus',
    packages=['sallfus', 'sallfus.fusion'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1',
    license='LGPL v3', # La licencia que tenga tu paqeute
    description='Specialized library to carry out the fusion of satellite images using different techniques.',
    author='Parall UD',
    author_email='parallud2019@gmail.com',
    url='https://github.com/Parall-UD/sallfus', # Usa la URL del repositorio de GitHub
    download_url='https://github.com/Parall-UD/sallfus/blob/master/dist/sallfus-0.1.tar.gz', # Te lo explico a continuación
    keywords = ['fusion', 'cuda', 'images', 'Satellite', 'quality'], # Palabras que definan tu paquete
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
