# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .widget_info import WidgetInfo
from .widget_spec import WidgetSpec
from .shared.resource_metadata import ResourceMetadata

__all__ = ["Widget"]


class Widget(BaseModel):
    """Widget is an embeddable chat surface bound to a single agent.

    Each widget
     owns a globally unique, immutable DNS label under the widgets domain
     (e.g. "k7m2xq9fp4wn.widgets.cadenya.com"): one widget = one hostname = one
     origin allowlist = one agent binding. Browsers talk to the widget host with
     session bearer tokens minted server-side via WidgetSessionService.
    """

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: WidgetSpec
    """WidgetSpec is the user-provided configuration for a widget."""

    state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_ARCHIVED"]
    """The current lifecycle state of the widget.

    Output only. Widgets are created STATE_ACTIVE; use the :archive and :unarchive
    actions to transition between states.
    """

    info: Optional[WidgetInfo] = None
    """WidgetInfo provides read-only server-derived data about a widget."""
