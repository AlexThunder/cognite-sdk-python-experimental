import pytest

from cognite.experimental import CogniteClient
from cognite.experimental.data_classes import ContextualizationJob, EntityMatchingModel
from cognite.experimental.exceptions import ModelFailedException

COGNITE_CLIENT = CogniteClient()
EMAPI = COGNITE_CLIENT.entity_matching


class TestEntityMatchingIntegration:
    def test_fit(self):
        entities = ["a-1", "b-2"]
        model = EMAPI.fit(entities)
        assert isinstance(model, EntityMatchingModel)
        assert "Queued" == model.status

        job = model.predict("a1")
        assert "Completed" == model.status
        assert isinstance(job, ContextualizationJob)
        assert "Queued" == job.status
        assert {"input", "predicted", "score"} == set(job.result["items"][0].keys())
        assert "Completed" == job.status
        EMAPI.delete(model)

    def test_ml_fit(self):
        entities_from = [{"id": 1, "name": "xx-yy"}]
        entities_to = [{"id": 2, "name": "yy"}]
        model = EMAPI.fit_ml(match_from=entities_from, match_to=entities_to, true_matches=[(1, 2)], model_type="bigram")
        assert isinstance(model, EntityMatchingModel)
        assert "Queued" == model.status

        job = model.predict_ml(match_from=[{"name": "foo-bar"}], match_to=[{"name": "foo-42"}])
        assert "Completed" == model.status
        assert isinstance(job, ContextualizationJob)
        assert "Queued" == job.status
        assert {"matches", "matchFrom"} == set(job.result["items"][0].keys())
        assert "Completed" == job.status
        EMAPI.delete(model)
