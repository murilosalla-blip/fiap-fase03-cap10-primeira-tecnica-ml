# Scripts - Capítulo 10

Esta pasta contém scripts auxiliares do projeto. Eles são independentes do notebook principal, mas seguem o mesmo padrão de boas práticas.

- **make_dataset.py**  
  Responsável por carregar o dataset original (`produtos_agricolas.csv`) e executar passos iniciais de preparação (ex.: ajustes de encoding, limpeza de dados).  
  > Observação: neste capítulo optamos por usar o CSV diretamente em `data/`, mas o script foi mantido como referência de boas práticas.

- **run_eda.py**  
  Gera automaticamente os principais gráficos de análise exploratória (histogramas, boxplots, matriz de correlação, scatterplots, countplot) e salva os resultados na pasta `assets/`.  
  Este script facilita a coleta de evidências para o README e para o documento acadêmico (`documentai_project_document_fiap.md`).

- **train.py**
  Automatiza o treinamento dos modelos de machine learning fora do notebook, salvando métricas e modelos treinados.

- **evaluate.py**
  Consolida as métricas dos modelos em uma tabela comparativa e gera matrizes de confusão em lote.

- **readme.md**  
  Este arquivo explicativo da pasta, conforme padrão do template.
