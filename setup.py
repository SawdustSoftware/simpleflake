from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='simpleflake',
    author='Mali Akmanalp (Custommade Ventures)',
    description='Twitter snowflake compatible super-simple distributed ID generator.',
    url='https://github.com/SawdustSoftware/simpleflake',
    version='0.1.3',
    packages=['simpleflake', ],
    package_dir={'simpleflake': ''},
    license='MIT',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta'
    ],
)
