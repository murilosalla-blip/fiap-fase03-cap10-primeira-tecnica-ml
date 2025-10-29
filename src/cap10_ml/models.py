# Centralização de criação de modelos (se quiser usar via import nos scripts/notebook)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def make_models():
    return {
        "knn": KNeighborsClassifier(n_neighbors=7),
        "logreg": LogisticRegression(max_iter=1000),
        "decision_tree": DecisionTreeClassifier(max_depth=6),
        "random_forest": RandomForestClassifier(n_estimators=300, max_depth=8, n_jobs=-1),
        "svm": SVC(kernel="rbf", C=2.0, gamma="scale", probability=True),
    }
