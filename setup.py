from setuptools import setup, find_packages

pkj_name = 'seo'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    "Framework :: Django :: 1.11",
    "Framework :: Django :: 2.0",
    "Framework :: Django :: 2.1",
    "Framework :: Django :: 2.2",
]


setup(
    name='django-ok-seo',
    version='0.4.2',
    description='Django seo app',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    author='Oleg Kleschunov',
    author_email='igorkleschunov@gmail.com',
    url='https://github.com/LowerDeez/ok-seo',
    packages=[pkj_name] + [pkj_name + '.' + x for x in find_packages(pkj_name)],
    include_package_data=True,
    license='MIT',
    classifiers=CLASSIFIERS
)
