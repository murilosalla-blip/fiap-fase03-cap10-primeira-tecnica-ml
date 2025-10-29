# FIAP - Fase 3 - Capítulo 10  
## A primeira técnica de aprendizado de máquina  

**Aluno:** Murilo Salla  
**RM:** 568041  
**Professor(a):** [Preencher com o nome]  

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

## 📂 Estrutura de Pastas
├── .github/
│ └── .githubproblem-report.md
├── assets/
│ └── [gráficos e prints de evidências]
├── config/
│ ├── requirements.txt
│ ├── .env.example
│ └── configreadme.md
├── data/
│ └── produtos_agricolas.csv
├── document/
│ ├── documentai_project_document_fiap.md
│ └── other/
├── scripts/
│ ├── readme.md
│ └── [scripts auxiliares *.py]
├── src/
│ └── cap10_ml/
│ └── [códigos auxiliares *.py]
├── MuriloSalla_RM568041_fase3_cap10.ipynb
└── README.md

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