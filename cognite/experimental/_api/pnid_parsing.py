from typing import Dict, List

from cognite.experimental._context_client import ContextAPI
from cognite.experimental.data_classes import ContextualizationJob


class PNIDParsingAPI(ContextAPI):
    _RESOURCE_PATH = "/context/pnid"

    def parse(
        self, file_id: int, entities: List[str], name_mapping: Dict[str, str] = None, partial_match: bool = False
    ) -> ContextualizationJob:
        """Parse PNID

        Args:
            file_id (int): ID of the file, should already be uploaded in the same tenant.
            entities (List[str]): List of entities to detect
            name_mapping (Dict[str,str]): Optional mapping between entity names and their synonyms in the P&ID. Used if the P&ID contains names on a different form than the entity list (e.g a substring only). The response will contain names as given in the entity list.
            partial_match (bool): Allow for a partial match (e.g. missing prefix).

        Returns:
            ContextualizationJob: Resulting queued job. Note that .results property of this job will block waiting for results."""
        return self._run_job(
            job_path="/parse",
            status_path="/",
            file_id=file_id,
            entities=entities,
            partial_match=partial_match,
            name_mapping=name_mapping,
        )
