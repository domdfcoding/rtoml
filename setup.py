import re
from pathlib import Path

from setuptools import setup
from setuptools_rust import Binding, RustExtension

# VERSION is set in Cargo.toml
cargo = (Path(__file__).resolve().parent / 'Cargo.toml').read_text()
VERSION = re.search('version *= *"(.*?)"', cargo).group(1)

setup(
    name='rtoml',
    version=VERSION,
    rust_extensions=[RustExtension('rtoml._rtoml', binding=Binding.PyO3)],
)
