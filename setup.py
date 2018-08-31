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
    python_requires='>=3.5',
    py_modules=['rrn'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
