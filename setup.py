import setuptools

import rrn

setuptools.setup(
    name='RRN',
    version=rrn.__version__,
    description="Python library for dealing with Resident Registration Number of Korea",
    url='https://github.com/Rainist/rrn',
    author='Sunghyun Hwang',
    author_email='me' '@' 'sunghyunzz.com',
    maintainer='Rainist',
    maintainer_email='engineering' '@' 'rainist.com',
    py_modules=['rrn'],
    install_requires=[
        'typing;python_version<"3.5"'
    ]
)
