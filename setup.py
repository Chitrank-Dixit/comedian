from setuptools import setup

setup(
    name="sideeffect",
    version="0.1.0",
    packages=["sefct"],
    entry_points={"console_scripts": ["sefct = sefct.__main__:checkCommand"]},
    install_requires=["click"],
)
