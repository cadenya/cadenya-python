# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .upload_info import UploadInfo
from .upload_spec import UploadSpec
from .shared.resource_metadata import ResourceMetadata

__all__ = ["Upload"]


class Upload(BaseModel):
    """A handle representing a single file upload flow.

    Clients call CreateUpload
     to receive a short-lived presigned URL, PUT the file directly to object
     storage, then reference the upload by id when creating or updating
     resources that accept binary content.

     Uploads are one-shot: once consumed by a creating or updating resource the
     upload transitions to UPLOAD_STATUS_CONSUMED and cannot be reused. Unused
     uploads expire and are garbage-collected.
    """

    info: UploadInfo

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: UploadSpec
