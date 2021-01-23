from setuptools import setup, find_packages
setup(
	name='my_good_site',
	version='2.5.0',
	license='GPLv3',
	author_email='jero98772@protonmail.com',
	author='jero98772',
	description='my good place with good proyects ',
	url='https://jero98772.pythonanywhere.com/',
	packages=find_packages(),
    install_requires=['Flask', 'tensorflow', 'numpy', 'opencv-python', 'removebg', ' pycrypto ', 'influxdb', 'matplotlib'],
    include_package_data=True,
	)
