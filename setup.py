
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

setup(
    name='pytextgame',
    version='0.0.4',
    description="Cross-Platform Python Text Game Library",
    long_description=readme + '\n\n' + history,
    author="John Stilley",
    url='https://github.com/thejollysin/pytextgame',
    packages=['pytextgame'],
    package_data={
        'pytextgame': ['resources/*.png', 'resources/*.ttf'],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pytextgame',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='test'
)
