# FIAP - Fase 3 - Capítulo 10  
## A primeira técnica de aprendizado de máquina  

## GitHub: https://github.com/murilosalla-blip/fiap-fase03-cap10-primeira-tecnica-ml

* Grupo:
* RM568500 - Elias da Silva de Souza
* RM567816 - Julia Duarte de Carvalho
* RM568041 - Murilo Salla
* RM567895 - Vitório Stevanatto Compri Paciulo

## 👩‍🏫 Professores
* Tutor(a): Ana Cristina dos Santos
* Coordenador(a): André Godoi Chiovato

---

## 📌 Descrição
Este projeto faz parte da Fase 3 – Capítulo 10 da graduação em Inteligência Artificial da FIAP.  
O objetivo é realizar a primeira experiência prática com **técnicas de aprendizado de máquina**, aplicando modelos preditivos em um dataset de condições de solo e clima para prever o melhor produto agrícola.

### Atividades realizadas:
- Análise exploratória com **5 gráficos obrigatórios** (histogramas, correlação, boxplots, scatter, countplot).  
- Definição de um **perfil ideal de solo/clima** e comparação com **3 culturas** distintas.  
- Treinamento de **5 modelos de Machine Learning**: KNN, Regressão Logística, Decision Tree, Random Forest, SVM.  
- Avaliação com métricas: *accuracy*, *precision (macro)*, *recall (macro)*, *f1-score (macro)*.  
- Comparação entre modelos e análise das matrizes de confusão.  

---

## 📁 Estrutura de Pastas

* `.github/`: arquivos de configuração específicos do GitHub.  
* ` assets/`: prints e gráficos de evidências (EDA, análises estatísticas, modelos de ML).  
* ` config/`: arquivos de configuração e ajustes do projeto (.env.example, requirements.txt, configreadme.md).  
* ` data/`: bases utilizadas no projeto (ex.: produtos_agricolas.csv).  
* ` document/`: documentação oficial do projeto (documentai_project_document_fiap.md).  
* ` document/other/`: documentos auxiliares.  
* ` scripts/`: scripts auxiliares de automação (make_dataset.py, run_eda.py, etc.).  
* ` src/`: código-fonte principal da Fase 3 (cap10_ml/ com os módulos de ML).  
MuriloSalla_RM568041_fase3_cap10.ipynb: notebook principal com a atividade do Capítulo 10.  
README.md: guia geral do projeto (este arquivo).  

---

## ▶️ Como executar
1. Criar e ativar o ambiente virtual:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r config/requirements.txt
2. Executar o notebook:
   jupyter notebook MuriloSalla_RM568041_fase3_cap10.ipynb
3. Conferir gráficos e resultados gerados em assets/.

## 🎥 Evidências
### Notebook executado: MuriloSalla_RM568041_fase3_cap10.ipynb
### Gráficos salvos em assets/