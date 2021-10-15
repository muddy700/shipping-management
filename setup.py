from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shipping_management/__init__.py
from shipping_management import __version__ as version

setup(
	name="shipping_management",
	version=version,
	description="Shipping Management System",
	author="Mohamed M Mohamed",
	author_email="mohamedmfaume700@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
