from pathlib import Path

import dash_html_components as html

from ...api_doc import ApiDoc
from ...helpers import ExampleContainer, HighlightedSource
from ...metadata import get_component_metadata
from .columns import cards as cards_columns
from .content_types import cards as cards_content_types
from .group import cards as cards_group
from .simple import cards as cards_simple

HERE = Path(__file__).parent

cards_simple_source = (HERE / "simple.py").read_text()
cards_content_type_source = (HERE / "content_types.py").read_text()
cards_group_source = (HERE / "group.py").read_text()
cards_columns_source = (HERE / "columns.py").read_text()

content = [
    html.H2("Card"),
    ExampleContainer(cards_simple),
    HighlightedSource(cards_simple_source),
    html.H4("Card content types"),
    ExampleContainer(cards_content_types),
    HighlightedSource(cards_content_type_source),
    html.H4("Card group"),
    ExampleContainer(cards_group),
    HighlightedSource(cards_group_source),
    html.H4("Card columns"),
    ExampleContainer(cards_columns),
    HighlightedSource(cards_columns_source),
    ApiDoc(
        get_component_metadata("src/components/card/CardDeck.js"),
        component_name="CardDeck",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardGroup.js"),
        component_name="CardGroup",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardColumns.js"),
        component_name="CardColumns",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/Card.js"),
        component_name="Card",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardHeader.js"),
        component_name="CardHeader",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardBody.js"),
        component_name="CardBody",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardFooter.js"),
        component_name="CardFooter",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardTitle.js"),
        component_name="CardTitle",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardSubtitle.js"),
        component_name="CardSubtitle",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardLink.js"),
        component_name="CardLink",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardImg.js"),
        component_name="CardImg",
    ),
    ApiDoc(
        get_component_metadata("src/components/card/CardImgOverlay.js"),
        component_name="CardImgOverlay",
    ),
]
