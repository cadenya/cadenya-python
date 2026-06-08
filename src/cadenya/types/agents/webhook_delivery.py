# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .webhook_delivery_data import WebhookDeliveryData
from ..shared.operation_metadata import OperationMetadata

__all__ = ["WebhookDelivery"]


class WebhookDelivery(BaseModel):
    data: WebhookDeliveryData
    """Webhook delivery details."""

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """
