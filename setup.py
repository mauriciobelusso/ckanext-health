from setuptools import setup, find_packages

setup(
    name='ckanext-health',
    version='0.1',
    description='CKAN Health Monitoring Extension',
    author='Seu Nome',
    author_email='seuemail@example.com',
    url='https://github.com/seuusuario/ckanext-health',
    packages=find_packages(),
    install_requires=[
        'ckan'
    ],
    entry_points='''
        [ckan.plugins]
        health=ckanext.health.plugin:HealthPlugin
    ''',
    include_package_data=True,
    zip_safe=False
)
