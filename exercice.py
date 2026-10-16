import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton

class FenetreInteractive(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercice 2 : Les événements")
        self.resize(400, 150)

        # --- Création des widgets ---
        self.label_prenom = QLabel("Prénom :")
        self.champs_saisie = QLineEdit()
        self.bouton_validation = QPushButton("Valider")
        
        # Nouveau Label pour afficher la réponse 
        self.label_resultat = QLabel("En attente de saisie...")

        # --- Layouts ---
        layout_h = QHBoxLayout()
        layout_h.addWidget(self.label_prenom)
        layout_h.addWidget(self.champs_saisie)
        layout_h.addWidget(self.bouton_validation)
        

        layout_v = QVBoxLayout()
        layout_v.addLayout(layout_h)
        layout_v.addWidget(self.label_resultat) # On place le résultat en dessous
        
        self.setLayout(layout_v)

        # --- Connexion du signal au slot (À coder) ---
        # TODO : Connecter le clic du bouton à self.afficher_message
        self.bouton_validation.clicked.connect(self.afficher_message)
        

        self.show()

    # --- Création de la méthode (À coder) ---
    def afficher_message(self):
        # TODO : Récupérer le texte de self.champs_saisie
        saisie = self.champs_saisie.text()
        # TODO : Modifier le texte de self.label_resultat
        self.label_resultat.setText(f"Bonjour {saisie}")
        pass

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Calculatrice(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercice 3 : L'additionneur")
        
        # --- 1. Création des widgets ---
        self.champ_nombre1 = QLineEdit()
        self.label_plus = QLabel("+")
        self.champ_nombre2 = QLineEdit()
        self.bouton_calculer = QPushButton("Calculer")
        self.label_resultat = QLabel("Résultat : ?")
        
        # --- 2. Mise en page (Layouts) ---
        # Une ligne horizontale avec les champs et le bouton
        layout_h = QHBoxLayout()
        layout_h.addWidget(self.champ_nombre1)
        layout_h.addWidget(self.label_plus)
        layout_h.addWidget(self.champ_nombre2)
        layout_h.addWidget(self.bouton_calculer)
        
        # Un layout vertical pour mettre le résultat sous la ligne
        layout_v = QVBoxLayout()
        layout_v.addLayout(layout_h)
        layout_v.addWidget(self.label_resultat)
        
        self.setLayout(layout_v)
        
        # --- 3. Connexion (À coder) ---
        # TODO : Connecte le clic du bouton à la méthode self.additionner
        self.bouton_calculer.clicked.connect(self.additionner)

        
        self.show()

    def additionner(self):
        # --- 4. Logique du calcul (À coder) ---
        # TODO : Récupère le texte de champ_nombre1 et champ_nombre2
        nombre1 = self.champ_nombre1.text()
        nombre2 = self.champ_nombre2.text()
        # TODO : Convertis ces textes en nombres entiers (avec int())
        nombre1_convertis = int(nombre1)
        nombre2_convertis = int(nombre2)
        # TODO : Calcule la somme
        somme = nombre1_convertis + nombre2_convertis
        # TODO : Affiche le résultat dans label_resultat
        self.label_resultat.setText(f"le resultat et : {somme}")
        pass

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

# ==========================================
# 1. LE MODÈLE (Gestion des données)
# ==========================================
class Modele:
    def __init__(self):
        # Notre base de données ultra-complexe : une simple liste Python !
        self.articles = []

    def ajouter_article(self, article: str):
        # TODO : Ajoute la variable 'article' à la liste 'self.articles'
        self.articles.append(article)
        
        pass

    def obtenir_texte_articles(self) -> str:
        # TODO : Transforme la liste en un seul texte séparé par des virgules et le retourne.
        # Astuce Python : tu peux utiliser ", ".join(self.articles)
        return ", ".join(self.articles)  
        pass


# ==========================================
# 2. LA VUE (L'interface graphique)
# ==========================================
class Vue(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma Liste de Courses MVC")
        self.resize(300, 150)

        # --- Création des widgets ---
        self.champ_saisie = QLineEdit()
        self.bouton_ajouter = QPushButton("Ajouter")
        self.label_liste = QLabel("Votre liste est vide.")

        # --- Mise en page (Layouts) ---
        layout_h = QHBoxLayout()
        layout_h.addWidget(self.champ_saisie)
        layout_h.addWidget(self.bouton_ajouter)

        layout_v = QVBoxLayout()
        layout_v.addLayout(layout_h)
        layout_v.addWidget(self.label_liste)
        self.setLayout(layout_v)
        
        

    def afficher_liste(self, texte: str):
        # TODO : Modifie le texte de 'self.label_liste' avec la variable 'texte'
        self.label_liste.setText(f"{texte}")
        pass

    def effacer_champ(self):
        # Méthode bonus déjà codée pour nettoyer le champ après un ajout !
        self.champ_saisie.clear()


# ==========================================
# 3. LE CONTRÔLEUR (Le chef d'orchestre)
# ==========================================
class Controleur:
    def __init__(self, modele, vue):
        self.modele = modele
        self.vue = vue

        # TODO : Connecte le clic du bouton 'ajouter' de la vue à la méthode 'self.action_ajouter'
        # Attention à bien passer par self.vue pour atteindre le bouton !
        self.vue.bouton_ajouter.clicked.connect(self.action_ajouter)
        

    def action_ajouter(self):
        # C'est ici que la magie MVC opère. Suis ces étapes dans l'ordre :
        
        # 1. TODO : Récupère le texte tapé dans le champ de saisie de la vue
        info = self.vue.champ_saisie.text()
        
        # 2. TODO : Envoie ce texte au Modèle en utilisant sa méthode ajouter_article()
        self.modele.ajouter_article(info)
        
        # 3. TODO : Récupère la liste mise à jour en appelant obtenir_texte_articles() du Modèle
        new_text = self.modele.obtenir_texte_articles()
        
        # 4. TODO : Envoie ce nouveau texte à la Vue avec sa méthode afficher_liste()
        self.vue.afficher_liste(new_text)
        
        # 5. On appelle la méthode pour vider le champ (déjà fait pour toi)
        self.vue.effacer_champ()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # On instancie nos trois briques MVC
    le_modele = Modele()
    la_vue = Vue()
    le_controleur = Controleur(le_modele, la_vue)

    # On affiche la vue
    la_vue.show()
    sys.exit(app.exec())
