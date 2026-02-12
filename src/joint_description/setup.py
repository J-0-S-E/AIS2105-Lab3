import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'joint_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/joint_description']),
        ('share/joint_description', ['package.xml']),
        (os.path.join('share', 'joint_description', 'launch'),
         glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kristian',
    maintainer_email='kristian.lokkeberg@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
