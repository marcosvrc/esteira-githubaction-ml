# Esteira GitHub Actions ML

## Visão Geral

Esta aplicação implementa um pipeline completo de CI/CD para Machine Learning utilizando GitHub Actions. O projeto treina um modelo de classificação Random Forest no dataset Wine do scikit-learn e automatiza todo o processo de integração e deploy contínuo.

## Arquitetura do Projeto

```
esteira-githubaction-ml/
├── .github/
│   └── workflows/
│       └── ml_workflow.yml          # Pipeline CI/CD
├── tests/
│   └── unit_test_train_model.py     # Testes unitários
├── train_model.py                   # Script principal de treinamento
├── requirements.txt                 # Dependências Python
├── random_forest_wine_model.pkl     # Modelo treinado (gerado)
└── README.md                        # Esta documentação
```

## Funcionalidades

### 🤖 Modelo de Machine Learning
- **Algoritmo**: Random Forest Classifier
- **Dataset**: Wine Dataset (sklearn)
- **Características**: 13 features químicas do vinho
- **Classes**: 3 tipos de vinho
- **Configuração**: 2 estimadores, profundidade máxima 1, random_state=1

### 🔄 Pipeline CI/CD
- **Integração Contínua (CI)**: Execução automática de testes unitários
- **Deploy Contínuo (CD)**: Treinamento e armazenamento do modelo
- **Trigger**: Push na branch `master`
- **Artefatos**: Modelo serializado em formato pickle

## Componentes Detalhados

### 1. Script de Treinamento (`train_model.py`)

#### Funções Principais:

**`load_dataset()`**
- Carrega o dataset Wine do scikit-learn
- **Retorna**: Tupla (X, y) com features e labels

**`train_model(X, y)`**
- Treina modelo Random Forest
- **Parâmetros**: 
  - `X`: Array numpy com features
  - `y`: Array numpy com labels
- **Retorna**: Modelo treinado
- **Avaliação**: Exibe acurácia no conjunto de treinamento

**`save_model(model, filepath)`**
- Serializa modelo usando pickle
- **Parâmetros**:
  - `model`: Modelo treinado
  - `filepath`: Caminho para salvar o arquivo

**`main()`**
- Orquestra todo o pipeline de treinamento
- Executa carregamento → treinamento → salvamento

### 2. Testes Unitários (`tests/unit_test_train_model.py`)

#### Testes Implementados:

**Testes de Existência de Métodos:**
- `test_load_dataset_exists()`: Verifica se função load_dataset existe
- `test_train_model_exists()`: Verifica se função train_model existe  
- `test_save_model_exists()`: Verifica se função save_model existe

**Teste de Integração:**
- `test_model_file_exists()`: Verifica se modelo é salvo corretamente
- Utiliza fixture `train_and_save_model` para setup/teardown

#### Fixture:
- `train_and_save_model`: Executa treinamento completo e limpa arquivo após teste

### 3. Pipeline GitHub Actions (`.github/workflows/ml_workflow.yml`)

#### Job CI (Integração Contínua):
```yaml
Trigger: Push na branch master
Runner: ubuntu-latest
Python: 3.9
Etapas:
  1. Checkout do código
  2. Setup Python 3.9
  3. Instalação de dependências
  4. Execução de testes unitários
```

#### Job CD (Deploy Contínuo):
```yaml
Dependência: Job CI deve passar
Runner: ubuntu-latest
Python: 3.9
Etapas:
  1. Checkout do código
  2. Setup Python 3.9
  3. Instalação de dependências
  4. Treinamento do modelo
  5. Criaç
  7. Testes de deploy (placeholder)
```

## Dependências

### Bibliotecas Python (`requirements.txt`)
- **pytest==7.3.1**: Framework de testes
- **scikit-learn==1.2.2**: Biblioteca de machine learning
- **numpy==1.24.3**: Computação numérica
- **pandas==1.5.3**: Manipulação de dados

## Como Usar

### Pré-requisitos
- Python 3.9+
- Git
- Conta GitHub com Actions habilitado

### Instalação Local

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd esteira-githubaction-ml
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute o treinamento:**
```bash
python train_model.py
```

4. **Execute os testes:**ão de artefato (zip)
  6. Preparação para deploy (placeholder)
```bash
python -m pytest tests/unit_test_train_model.py
```

### Execução via GitHub Actions

1. **Faça push para a branch master:**
```bash
git add .
git commit -m "Trigger ML pipeline"
git push origin master
```

2. **Acompanhe a execução:**
   - Acesse a aba "Actions" no GitHub
   - Monitore os jobs CI e CD
   - Verifique logs e artefatos gerados

## Resultados Esperados

### Modelo Treinado
- **Arquivo**: `random_forest_wine_model.pkl`
- **Tamanho**: ~2KB
- **Formato**: Pickle serializado
- **Acurácia**: Varia conforme configuração (tipicamente >90%)

### Artefatos do Pipeline
- **model_artifact.zip**: Modelo compactado para deploy
- **Logs detalhados**: Disponíveis na interface do GitHub Actions

## Monitoramento e Logs

### Logs Locais
```bash
# Execução com verbose
python -m pytest tests/ -v

# Logs do treinamento
python train_model.py
```

### Logs GitHub Actions
- **CI Job**: Resultados dos testes unitários
- **CD Job**: Métricas do modelo e status do deploy
- **Artefatos**: Downloads disponíveis por 90 dias

## Extensões Futuras

### Melhorias Sugeridas
1. **Validação cruzada** para avaliação mais robusta
2. **Hyperparameter tuning** automatizado
3. **Testes de performance** do modelo
4. **Deploy real** em ambiente de produção
5. **Monitoramento** de drift do modelo
6. **Versionamento** de modelos com MLflow
7. **Testes de integração** end-to-end

### Integração com Ferramentas
- **Airflow**: Orquestração de pipelines
- **MLflow**: Tracking de experimentos
- **Docker**: Containerização
- **Kubernetes**: Deploy escalável

## Troubleshooting

### Problemas Comuns

**Erro de dependências:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Falha nos testes:**
```bash
# Verificar se arquivo foi gerado
ls -la *.pkl

# Executar teste específico
python -m pytest tests/unit_test_train_model.py::test_model_file_exists -v
```

**Pipeline falha no GitHub:**
- Verificar sintaxe do YAML
- Confirmar permissões do repositório
- Checar logs detalhados na aba Actions

## Contribuição

### Padrões de Desenvolvimento
1. **Testes**: Sempre adicionar testes para novas funcionalidades
2. **Documentação**: Atualizar README para mudanças significativas
3. **Versionamento**: Usar semantic versioning
4. **Code Review**: Pull requests obrigatórios

### Estrutura de Commits
```
feat: adiciona nova funcionalidade
fix: corrige bug
docs: atualiza documentação
test: adiciona ou modifica testes
refactor: refatora código sem mudança funcional
```

## Licença

Este projeto está sob licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, abra uma issue no repositório GitHub.

---

**Última atualização**: $(date)
**Versão**: 1.0.0
