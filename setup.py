from setuptools import setup, find_packages

VERSION = "1.2.0"


setup(
    name="pkt-docs-dev",
    version=VERSION,
    url="https://github.com/coconut3-dev/dev_docs_pkt_cash.github.io",
    license="MIT",
    author="PKT",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "mkdocs.themes": [
            "moonstone = mkdocs_moonstone",
        ]
    },
    zip_safe=False,
)
