from setuptools import setup

setup(
  name='voicemeeter',
  version='2.0',
  description='Voicemeeter Remote Python API',
  packages=['voicemeeter'],
  install_requires=[
    'toml'
  ],
  extras_require={
    'development': [
      'nose',
      'randomize'
    ]
  }
)
