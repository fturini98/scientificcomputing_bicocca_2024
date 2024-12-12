# Appunti
## Creare e Muoversi tra i vari branch
Per creare un nuovo branch e spostarsi su quello:
```
git checkout -b <nome nuovo branch>
```
per vedere la lisa di tutti i branc:
```
git branch
```
 - Il branch che si evidenza è quello su cui stai lavorando, in alternativa usa:
 ```
 git status
 ```
Per muoversi tra i vari branch:
```
git checkout <branch su cui ci si vuole spostare>
```
## Push e pull su vari branch
Dato che il git remote non ha piu' un branch univico nelle azioni di push e pull sarà necessario specificarlo, quindi:
```
git pull <remote name> <branch name>

git push <remote name> <branch name>
```