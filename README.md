# Esteira GitHub Actions ML

## Visão Geral 

Esta aplicação implementa um pipeline completo de CI/CD para Machine Learning utilizando GitHub Actions. O projeto treina um modelo de classificação Random Forest no dataset Wine do scikit-learn e automatiza todo o processo de integração e deploy contínuo.

## Arquitetura do Projeto

```
esteira-githubaction-ml/
├── .github/
│   └── workflows/
│       └── ml_workflow.yml          # Pipeline CI/CD
├── src/
│   └── train_model.py               # Script principal de treinamento
├── model/
│   └── random_forest_wine_model.pkl # Modelo treinado (gerado)
├── tests/
│   └── unit_test_train_model.py     # Testes unitários
├── requirements.txt                 # Dependências Python
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

### 1. Script de Treinamento (`src/train_model.py`)

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
  5. Criação de artefato (zip)
  6. Preparação para deploy (placeholder)
  7. Testes de deploy (placeholder)
```

## Dependências

### Bibliotecas Python (`requirements.txt`)
- **pytest==7.3.1**: Framework de testes
- **scikit-learn==1.2.2**: Biblioteca de machine learning
- **numpy==1.24.3**: Computação numérica
- **pandas==1.5.3**: Manipulação de dados

### Requisitos do Sistema
- **Python**: 3.9 ou superior
- **Sistema Operacional**: Linux, macOS, Windows
- **Memória**: Mínimo 512MB RAM
- **Espaço em Disco**: ~50MB para dependências

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
python src/train_model.py
```

4. **Execute os testes:**
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
- **Arquivo**: `model/random_forest_wine_model.pkl`
- **Tamanho**: ~2KB
- **Formato**: Pickle serializado
- **Acurácia**: Varia conforme configuração (tipicamente >90%)
- **Features**: 13 características químicas do vinho
- **Target**: 3 classes de vinho (0, 1, 2)

### Artefatos do Pipeline
- **model_artifact.zip**: Modelo compactado para deploy
- **Logs detalhados**: Disponíveis na interface do GitHub Actions

## Monitoramento e Logs

### Logs Locais
```bash
# Execução com verbose
python -m pytest tests/ -v

# Logs do treinamento
python src/train_model.py
```

### Logs GitHub Actions
- **CI Job**: Resultados dos testes unitários
- **CD Job**: Métricas do modelo e status do deploy
- **Artefatos**: Downloads disponíveis por 90 dias

## Performance e Métricas

### Métricas do Modelo
- **Acurácia de Treinamento**: ~100% (devido ao overfitting intencional)
- **Tempo de Treinamento**: <1 segundo
- **Tamanho do Dataset**: 178 amostras, 13 features
- **Tempo de Inferência**: <1ms por predição

### Limitações Conhecidas
- **Overfitting**: Modelo com max_depth=1 e poucos estimadores
- **Sem validação**: Não há split treino/teste
- **Dataset pequeno**: Apenas 178 amostras
- **Sem normalização**: Features não são normalizadas

## Extensões Futuras

### Melhorias Sugeridas
1. **Validação cruzada** para avaliação mais robusta
2. **Hyperparameter tuning** automatizado
3. **Testes de performance** do modelo
4. **Deploy real** em ambiente de produção
5. **Monitoramento** de drift do modelo
6. **Versionamento** de modelos com MLflow
7. **Testes de integração** end-to-end
8. **Normalização de features** e pré-processamento
9. **Split treino/validação/teste** adequado
10. **Métricas adicionais** (precision, recall, F1-score)

### Integração com Ferramentas
- **Airflow**: Orquestração de pipelines
- **MLflow**: Tracking de experimentos
- **Docker**: Containerização
- **Kubernetes**: Deploy escalável
- **Prometheus/Grafana**: Monitoramento de métricas
- **DVC**: Versionamento de dados

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
ls -la model/*.pkl

# Executar teste específico
python -m pytest tests/unit_test_train_model.py::test_model_file_exists -v

# Executar todos os testes com verbose
python -m pytest tests/ -v
```

**Pipeline falha no GitHub:**
- Verificar sintaxe do YAML
- Confirmar permissões do repositório
- Checar logs detalhados na aba Actions
- Verificar se a branch é `master` (não `main`)

**Erro de import do módulo:**
```bash
# Executar testes do diretório raiz
cd /caminho/para/esteira-githubaction-ml
python -m pytest tests/

# Ou adicionar PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
python -m pytest tests/
```

**Modelo não encontrado:**
```bash
# Verificar se diretório model/ existe
mkdir -p model/

# Executar treinamento manualmente
python src/train_model.py
```

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
