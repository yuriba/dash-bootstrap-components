import os
import sys

import dash

from . import themes  # noqa
from ._version import __version__  # noqa
from .table import generate_table_from_df  # noqa

_current_path = os.path.dirname(os.path.abspath(__file__))

METADATA_PATH = os.path.join(_current_path, "metadata.json")

# Dash automatic class creation from `metadata.json` file.

_js_dist = [
    {
        "relative_package_path": "bundle.js",
        "namespace": "dash_bootstrap_components",
    }
]

_css_dist = []


def _setup_js_components(module, path_to_metadata):
    components = dash.development.component_loader.load_components(
        path_to_metadata, "dash_bootstrap_components"
    )
    for component in components:
        setattr(module, component.__name__, component)
        component._js_dist = _js_dist
        component._css_dist = _css_dist


_setup_js_components(sys.modules[__name__], METADATA_PATH)
