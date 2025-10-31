from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

def load_dataset():
    """Carrega o conjunto de dados Wine do sklearn.
    Retorna:
        X (np.array): Dados de entrada.
        y (np.array): Rótulos de destino.
    """
    X, y = load_wine(return_X_y=True)
    return X, y


def train_model(X, y):
    """Treina um modelo de floresta aleatória no conjunto de dados Wine.
    Parâmetros:
        X (np.array): Dados de entrada.
        y (np.array): Rótulos de destino.
        Retorna:
            model (RandomForestClassifier): Modelo treinado.
    """
    #Definir o modelo
    model = RandomForestClassifier(n_estimators=2, random_state=1, max_depth=1)

    #Treinar o modelo
    model = model.fit(X, y)

    #Avaliar o treinamento do modelo
    print(f"Acurácia do modelo: {model.score(X, y)}")
    return model

def save_model(model, filepath):
    """Salva o modelo treinado em um arquivo pickle.
    Parâmetros:
        model (qualquer): modelo treinado para ser salvo.
        filepath (str): o caminho do arquivo onde o modelo treinado será salvo.
    """
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)

def main():
    """
    A função principal que executa as etapas de treinamento do modelo.
    Esta função carrega o conjunto de dados Wine usando a função load_dataset(),
    treina um modelo de floresta aleatória nos dados carregados usando a função train_model(),
    e retorna o modelo treinado.
    """
    #Carregar o conjunto de dados
    X, y = load_dataset()

    #Treinar o modelo
    model = train_model(X, y)

    #Salvar o modelo treinado
    save_model(model, 'model/random_forest_wine_model.pkl')

    return

if __name__ == "__main__":
    main()