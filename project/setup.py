from setuptools import setup, find_packages

setup(
    name= 'CLInTool',
    version= '0.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires= [],
    entry_points= {
        'console_scripts': [
            'CLInTool = CLInTool.main:main'
        ]
    }
)