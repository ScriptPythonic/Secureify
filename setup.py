from setuptools import setup, find_packages

setup(
    name='Secureify',
    version='0.1.0',
    author='Quadri Basit Ayomide',
    author_email='Quadribasit04@gmail.com',
    description='A password strength checker to help users create strong passwords.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ScriptPythonic/Secureify',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # added soon 
    ],
)
