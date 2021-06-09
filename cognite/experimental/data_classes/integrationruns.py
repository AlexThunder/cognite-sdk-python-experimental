from cognite.client.data_classes._base import *
from cognite.client.data_classes.shared import TimestampRange


class IntegrationRun(CogniteResource):
    """A representation of a IntegrationRun.

    Args:
        external_id (str): The external ID of related integration provided by the client. Must be unique for the resource type.
        status (str): success/failure/seen.
        message (str): failure message.
        created_time (int): The number of milliseconds since 00:00:00 Thursday, 1 January 1970, Coordinated Universal Time (UTC), minus leap seconds.
        cognite_client (CogniteClient): The client to associate with this object.
    """

    def __init__(
        self,
        external_id: str = None,
        status: str = None,
        message: str = None,
        created_time: int = None,
        cognite_client=None,
    ):
        self.external_id = external_id
        self.status = status
        self.message = message
        self.created_time = created_time
        self._cognite_client = cognite_client


class IntegrationWithStatusesUpdate(CogniteUpdate):
    class _PrimitiveIntegrationWithStatusesUpdate(CognitePrimitiveUpdate):
        def set(self, value: Any) -> "IntegrationWithStatusesUpdate":
            return self._set(value)


class IntegrationRunUpdate(CogniteUpdate):
    class _PrimitiveIntegrationRunUpdate(CognitePrimitiveUpdate):
        def set(self, value: Any) -> "IntegrationRunUpdate":
            return self._set(value)


class IntegrationRunList(CogniteResourceList):
    _RESOURCE = IntegrationRun
    _UPDATE = IntegrationRunUpdate


class StringFilter(CogniteFilter):
    """No description.

    Args:
        substring (str): failure message part.
    """

    def __init__(
        self, substring: str = None,
    ):
        self.substring = substring


class IntegrationRunFilter(CogniteFilter):
    """No description.

    Args:
        external_id (str): The external ID of related integration provided by the client. Must be unique for the resource type.
        statuses (List[str]): success/failure/seen.
        message (StringFilter): failure message filter.
        created_time (Union[Dict[str, Any], TimestampRange]): Range between two timestamps.
        cognite_client (CogniteClient): The client to associate with this object.
    """

    def __init__(
        self,
        external_id: str = None,
        statuses: List[str] = None,
        message: StringFilter = None,
        created_time: Union[Dict[str, Any], TimestampRange] = None,
        cognite_client=None,
    ):
        self.external_id = external_id
        self.statuses = statuses
        self.message = message
        self.created_time = created_time
        self._cognite_client = cognite_client

    @classmethod
    def _load(cls, resource: Union[Dict, str], cognite_client=None):
        instance = super(IntegrationRunFilter, cls)._load(resource, cognite_client)
        if isinstance(resource, Dict):
            if instance.created_time is not None:
                instance.created_time = TimestampRange(**instance.created_time)
        return instance
