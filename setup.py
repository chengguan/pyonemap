from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = 'pyonemap',
    version = '0.7.0',
    packages = find_packages(),
    install_requires = [
        'requests',
    ],
    author = 'Teo Cheng Guan',
    author_email = 'chengguan.teo@gmail.com',
    description = 'A Python package for interacting with OneMap API',
    long_description=long_description,  # Read from README.md
    long_description_content_type="text/markdown",
    url = 'https://github.com/chengguan/pyonemap',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
