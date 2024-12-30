Lesson 06: GitHub
=================

The sixth lesson is about GitHub and the continuous integration.

For this lesson was created another sepcific repository, named `Git_exercises <https://github.com/fturini98/Git_exercises>`_ , where the exercises are done; that repository is
included in the current one as a GitHub submodule. 

The two exercises are:

Q2: Egocentric
--------------

Write a github action that lets you commit only if README.md contains your name.

Q3: Ditch Overleaf
------------------

Stop using overleaf, you won't regret it. Write your next paper entirely with git and github. It's more powerful, saves your history (for free!) and scales to many many collaborators. 


Solutions:
----------

To solve this exercises I created a GitHub workflow available `here <https://github.com/fturini98/Git_exercises/blob/main/.github/workflows/Lezione6.yml>`_ or just below.


.. include:: ../../Git_exercises/.github/workflows/Lezione6.yml
   :code: yaml

For what concern the pdf produced by the DitchOverleaf action is available in the `artifacts <https://github.com/fturini98/Git_exercises/actions/runs/12089741965>`_ ;

while the Egocentric action is necessary to make a pull request to the main branch of the repository (that is protected), therefore the wording *Francesco Turini* will always be in the README.md file in the main branch.