from setuptools import setup, find_packages
from setuptools.command.test import test as SetuptoolsTestCommand
import locking


class RunTestsCommand(SetuptoolsTestCommand):
    def initialize_options(self):
        SetuptoolsTestCommand.initialize_options(self)
        self.test_suite = "override"

    def finalize_options(self):
        SetuptoolsTestCommand.finalize_options(self)
        self.test_suite = None

    def run(self):
        SetuptoolsTestCommand.run(self)
        self.with_project_on_sys_path(self.run_tests)

    def run_tests(self):
        import os
        import subprocess
        import sys

        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join(sys.path)

        cmd = [sys.executable, 'test_project/manage.py', 'test']
        errno = subprocess.call(cmd, env=env)

        raise SystemExit(errno)

setup(
    name="django-db-locking",
    version=locking.__version__,
    url='https://github.com/vikingco/django-db-locking/',
    license='BSD',
    description='Database locking',
    long_description=open('README.rst', 'r').read(),
    author='VikingCo',
    packages=find_packages('.'),
    cmdclass={'test': RunTestsCommand},
    tests_require=['django', 'freezegun'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
