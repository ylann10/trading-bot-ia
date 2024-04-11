# Trade-Bot-IA

## Installation

### Python

#### Installation
  * Windows :
    Rendez vous directement sur le site de [Python](https://www.python.org/)
  * Linux :
    
    ```
    sudo apt update
    sudo apt install python3
    ```
1. Crééz votre environnement virtuel
   
   ```
   python3 -m pip install virtualenv
   python3 -m virtualenv venv
   ```
2. Démarrez votre environnement
    * Windows :
      * `venv\Scripts\activate`
    * Linux :
      * `source venv/bin/activate`

#### Dépendances

```
python -m pip install -r requirements.txt
```

## Configuration

Liste des variables : 
* MODEL (defaut: "model.kara")
  * Nom du modèle utilisé lors de la suvegarde de celui-ci 
  * **Ne pas retirer l'extension ".kara"**
* DATA_LIMIT (defaut: 3650) (5 ans)
  * Nombre de jours de statistiques qui seront récupérées depuis l'API de Binance
* MAX_EPOCHS (defaut: None)
  * Nombre d'itérations maximum avant que l'apprentissage ne s'arrête
* MAX_LOSS (defaut: 0.01)
  * Loss correspond à la différence entre la donnée attendue et la donnée trouvée
  * Idem, quand la valeur demandée sera atteinte, l'apprentissage s'arrêtera.

## Execution

```
python main.py
```