import pytest

from ..models import Correspondencia
from model_bakery import baker

@pytest.mark.django_db
def test_correspondencia_model():
    """Should create a a Correspondencia."""
    correspondence = baker.make(Correspondencia, )