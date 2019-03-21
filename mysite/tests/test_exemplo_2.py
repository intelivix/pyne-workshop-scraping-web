import pytest

from core.models import Exemplo


class TestExemploModel(object):

    @pytest.mark.django_db
    def test_exemplo_save(self, fixture_exemplo):
        assert fixture_exemplo is not None
        exemplo = Exemplo.objects.create(
            name="Fulano Beltrano Litrano",
            age=500
        )
        assert exemplo.name == 'Fulano Beltrano Litrano'
        assert exemplo.age == 500
