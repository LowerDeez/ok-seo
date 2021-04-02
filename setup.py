from setuptools import setup, find_packages

pkj_name = 'seo'

setup(
    name='django-ok-seo',
    version='0.9.2',
    long_description_content_type='text/x-rst',
    packages=[pkj_name] + [pkj_name + '.' + x for x in find_packages(pkj_name)],
    include_package_data=True,
)
