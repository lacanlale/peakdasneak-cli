from setuptools import setup
setup(
    name = 'peakdasneak',
    version = '0.1.0',
    packages = ['peakdasneak'],
    entry_points = {
        'console_scripts': [
            'peakdasneak = peakdasneak.__main__:main'
        ]
    }
)