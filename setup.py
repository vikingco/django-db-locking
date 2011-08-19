from setuptools import setup, find_packages
import locking


setup(
    name="django-locking",
    version=locking.__version__,
    url='https://github.com/citylive/django-locking/',
    license='BSD',
    description='Database locking',
    long_description=open('README.rst', 'r').read(),
    author='City Live',
    packages=find_packages('.'),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
