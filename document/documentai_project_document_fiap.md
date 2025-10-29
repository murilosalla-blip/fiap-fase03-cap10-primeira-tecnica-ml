# FIAP - Projeto Acadêmico
## Fase 3 - Capítulo 10: A primeira técnica de aprendizado de máquina

### 1. Introdução
Este documento apresenta a aplicação de técnicas iniciais de aprendizado de máquina em dados de solo e clima, com o objetivo de prever o produto agrícola mais adequado às condições apresentadas.

### 2. Visão Geral
- **Base:** produtos_agricolas.csv  
- **Variáveis:** N, P, K, temperature, humidity, pH, rainfall, label  
- **Ferramentas:** Python, pandas, seaborn, scikit-learn, Jupyter Notebook  

### 3. Desenvolvimento
- **EDA (5 gráficos):** histogramas, countplot, correlação, boxplot, scatter.  
- **Perfil ideal:** médias/medianas globais das variáveis.  
- **Comparação:** top 3 culturas mais frequentes.  
- **Modelagem:** 5 algoritmos (KNN, Logistic Regression, Decision Tree, Random Forest, SVM).  

### 4. Resultados
- Matrizes de confusão e métricas macro (accuracy, precision, recall, f1).  
- Tabela comparativa dos modelos.  
- Random Forest e SVM apresentaram melhor performance (exemplo).  

### 5. Conclusões
- O exercício demonstrou a utilidade do ML para apoio à agricultura.  
- Cada cultura possui um perfil distinto em relação ao solo e clima.  
- Random Forest se destacou pela robustez, enquanto KNN teve menor desempenho.  

### 6. Limitações
- Não houve tuning de hiperparâmetros.  
- Possível desbalanceamento de classes.  

### 7. Próximos passos
- Aplicar validação cruzada.  
- Usar GridSearchCV para otimizar hiperparâmetros.  
- Avaliar técnicas de balanceamento de dados.  

### 8. Referências
- Documentação oficial scikit-learn  
- Material FIAP Cap. 10  
