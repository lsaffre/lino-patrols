.. _patrols.models:

===================
Lino-patrols models
===================

Ce qui est fait (structure actuelle):

.. actors_overview:: 
    lino_patrols.Employees
    lino_patrols.Areas
    lino_patrols.Teams
    lino_patrols.Members
    lino_patrols.Patrols
    lino_patrols.WorkDays
    
Discussion    
----------
    
**Day** : Calendrier général avec les jours fériés. 

**Mission** (name,secteur,difficulty,priority,nb_teams,récurrence) : 
Liste signalétique des missions à assumer.
Exemple:

============================ ======== ================================
Nom                          Secteur  Récurrence
============================ ======== ================================
Piscine Neptunium            1        tous les jours
Pelouses Brusilia            1
Parc de la Jeunesse          1
Maison des Arts              1 
Bibliothèque Sésame          2
Place Stephenson             6
Place Gaucheret              6
Bibliothèque 1001 pages      6
Frésias/Chemin Creux/Bichon  3
Kituro                       3
Garages Fleurs/Espaces verts 3
Pelouses Cheminées Duployé   5

Ramadan                      x        une fois dans l’année
Vol dans véhicules           x        plusieurs fois dans l’année
Vol à la tire                x        plusieurs fois dans l’année
Rosace                       x        plusieurs fois dans l’année 

Hotel communal               x        tous les jeudis et mercredis 
============================ ======== ================================

Les **Demandes de congé** (avec leur raison) s'encodent dans 
:ref:`patrols.lino_patrols.WorkDays`.



  Disponibilty (tel gardien demande congé tel jour)

**MissionDays** "Missions prévues" : date, mission, nb_teams

**Calendrier des missions**
ou l'on voit que tel jour j'ai prévu telles missions dans mon secteur,
et j'ai autant d'agents en congé... 
donc je reporte mission "sensibilation vol" à une autre date.

- Patrol : une equipe qui patrouille tel jour "à tel endroit" --> "telle mission".

**horaire général** = WorkDays

Table virtuelle:
par Agent:
récupération des prestations we


- chef de service doit pouvoir manuellement modifier voire créer les équipes

- 35 gardiens (agents) en tout

- on encodera l'historique


Par mission :
"priorité" : permet de décider en cas de maladie

tous les deux mois les binomes changent
les agents changent de secteur tous les 4 mois
les agents changent de pole tous les 12 mois

mission indépendante d'un secteur donné:
"stib" : mission quotidienne. à voir si cela fait partie d'un
marchés il y 4 marchés par semaine à Schaerbeek

hotel communal : chaque jour il y a une équipe
: le jeudi il y a plus d'


**Génération des équipes**

On les génère pour une période donnée (toute l'année). 
Lino efface chaque fois toutes les données qui ne sont pas encore "utilisées".

Par agent on fait une liste 
des "candidats possibles à faire équipe":
à priori tous ceux qui sont actifs et dans le meme secteur.
Parmi ceux-ci, filtrons ceux avec qui il a déjà été ensemble.
(Comment régler le cas d'un agent qui a déjà fait équipe avec 
tous les autres agents...)
  
Puis on ajoute d'autres contraintes, p.ex. 

- horaire H1 ou H2
- nombre de jours ou l'équipe sera incomplète 
  (selon la liste des jours qu'ils ont pris congé)
  (càd le chef devra trouver un remplaçant

Puis on passe cela comme Problème à 
`python-constraint <http://labix.org/python-constraint>`_

**Attribution des horaires**

- horaires = Timetables
- Ceux qui travaillent en équipe doivent avoir le meme horaire
- Les horaires tournent de manière individuelle par agent
   
Reference list of all database models
-------------------------------------

.. actor:: lino_patrols.Employees
.. actor:: lino_patrols.Areas
.. actor:: lino_patrols.Teams
.. actor:: lino_patrols.Members
.. actor:: lino_patrols.Patrols
.. actor:: lino_patrols.WorkDays

