import pytest
import os
import sys
from pathlib import Path

# Adiciona o diretório src ao path
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

import train_model

def test_load_dataset_exists():
    """
    Testa se o método load_dataset existe no módulo train.

    Este teste verificará a existência do método load_dataset no módulo train.
    Se o método não existir, o teste falhará com uma mensagem indicando que o método load_dataset não existe.
    """
    assert hasattr(train_model, 'load_dataset'), "O método load_dataset não existe"

def test_train_model_exists():
    """
    Testa se o método train_model existe no módulo train.

    Este teste verificará a existência do método train_model no módulo train.
    Se o método não existir, o teste falhará com uma mensagem indicando que o método train_model não existe.
    """
    assert hasattr(train_model, 'train_model'), "O método train_model não existe"

def test_save_model_exists():
    """
    Testa se o método save_model existe no módulo train.

    Este teste verificará a existência do método save_model no módulo train.
    Se o método não existir, o teste falhará com uma mensagem indicando que o método save_model não existe.
    """
    assert hasattr(train_model, 'save_model'), "O método save_model não existe"

@pytest.fixture(scope="module")
def train_and_save_model():
    """
    Fixture para treinar e salvar o modelo antes de executar o teste test_model_file_exists.

    Esta função chama a função main() do módulo train para treinar e salvar o modelo.
    Após o término do teste, remove o arquivo 'random_forest_wine_model.pkl'.
    """
    train_model.main()
    yield
    model_path = Path(__file__).parent.parent / 'model' / 'random_forest_wine_model.pkl'
    if model_path.exists():
        model_path.unlink()

def test_model_file_exists(train_and_save_model):
    """
    Testa se o arquivo random_forest_wine_model.pkl foi salvo corretamente.

    Este teste, que depende da fixture train_and_save_model, verificará a existência do arquivo model.pkl no diretório atual.
    Se o arquivo não existir, o teste falhará com uma mensagem indicando que o arquivo model.pkl não foi salvo corretamente.
    """
    model_path = Path(__file__).parent.parent / 'model' / 'random_forest_wine_model.pkl'
    assert model_path.exists(), "O arquivo random_forest_wine_model.pkl não foi salvo corretamente"