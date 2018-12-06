from setuptools import setup, find_packages

pkj_name = 'seo'

with open('requirements.txt') as f:
    requires = f.read().splitlines()


setup(
    name='django-ok-seo',
    version='0.1.6',
    description='Django seo app',
    long_description=open('README.md').read(),
    author='Oleg Kleschunov',
    author_email='igorkleschunov@gmail.com',
    url='https://github.com/LowerDeez/ok-seo',
    packages=[pkj_name] + [pkj_name + '.' + x for x in find_packages(pkj_name)],
    include_package_data=True,
    license='MIT',
    install_requires=requires,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ]

)