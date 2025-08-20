from setuptools import setup, find_packages

setup(
    name="siya_billing",
    version="1.0.0",
    description="Auto create Patient/Customer/Address/Contact, Sales Invoice & Payment",
    author="SR Developer",
    author_email="webdevelopersriaas@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
