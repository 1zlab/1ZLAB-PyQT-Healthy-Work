import os
from setuptools import find_packages, setup


setup(
    name='healthywork',
    version='1.1.0',
    packages=['healthywork'],
    include_package_data=True,
    license='MIT License',
    description='生活不止有屏幕上的代码,还有诗和远方.',
    url='https://github.com/Fuermohao/Healthy-Work',
    author='Fuermohao',
    author_email='Fuermohao@outlook.com',
    platforms='Linux,Unix,Windows',
    keywords='HealthyWork',
    install_requires=['pyqt5'],
    entry_points={
        'console_scripts': [
            'healthywork = healthywork.app:cli'
        ]
    }
)
