import json
import requests
from plankapy import *

def main():
    # Planka API-Instanz erstellen
    planka_instance = Planka(
        url='http://141.45.212.242:9000',
        username='demo1',
        password='demo1'
    )
    
    # Project Controller erstellen
    project_controller = Project(instance=planka_instance)
    list_controller = List(instance=planka_instance)
    
    # Liste der Projektnamen abrufen
    project_names = project_controller.get_project_names()
    
    
    # Projektnamen ausgeben
    print("Projekt-Namen:")
    for name in project_names:
        print(name)




if __name__ == "__main__":
    main()