from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='simpleflake',
    author='Mali Akmanalp (Custommade Ventures)',
    author_email='mali+simpleflake@custommade.com',
    description='Twitter snowflake compatible super-simple distributed ID generator.',
    url='https://github.com/SawdustSoftware/simpleflake',
    version='0.1.5',
    packages=['simpleflake', ],
    package_dir={'simpleflake':'simpleflake'},
    license='MIT',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta'
    ],
)
