[![Documentation](https://img.shields.io/badge/docs-published-brightgreen?label=Documentation)](https://fturini98.github.io/scientificcomputing_bicocca_2024)

![Tests Passed](https://img.shields.io/github/actions/workflow/status/fturini98/scientificcomputing_bicocca_2024/Lezione8_tests.yml?label=Tests%20Passed)


# BicoccaCoursePython2024
Python package to solve the exercices of the Bicocca's phD python course.
**Download and Install**:
```
pip install --index-url https://test.pypi.org/simple/ BicoccaCoursePython2024
```

***Documentation avaiable*** [here](https://fturini98.github.io/scientificcomputing_bicocca_2024
)

The python package as a module for each lesson:
- Lesson 01 module ([prima_lezione](#prima_lezione))
- Lesson 02 module ([seconda_lezione](#seconda_lezione))
- Lesson 03 module ([terza_lezione](#terza_lezione))
- Lesson 04 module ([quarta_lezione](#quarta_lezione))
- [Lesson 08](#lesson-08) has no module (test, and package deployment)

# Modules
## prima_lezione

## seconda_lezione

## terza_lezione

## quarta_lezione

## Lesson 08

The last lesson is about building a package and then **testing** and deploying it.  
I've completed the exercises related to:  
- the tests (**Q2: My own test**)  
- the deployment (**Q1: I love pip**)

### Tests' Exercise (Q2: My own test)

For the test exercise, I wrote a class ([TestBicoccaCoursePython2024](test/ottava_lezione_test.py)) with 4 methods:

- ***test_np_power***: This test ensures that there is no occurrence of `np.power(10., x)` without the dot in the codebase. This is important because some older versions of NumPy (e.g., those used with Numba or TensorFlow) don't automatically convert `10` to a float, which introduces a bug when performing the power of 10 operation.

- Tests for the [Game_life](src/BicoccaCoursePython2024/seconda_lezione.py) class:

    - ***test_default_initial_condition***: This test checks that the default initial conditions of the game are as expected.
    
    - ***test_gen1***: This test checks that the first generation of the game is what is expected.
    
    - ***test_gen_10***: This test ensures that the 10th generation still matches the one obtained in the first run of the code. It compares the current grid state with a saved snapshot [PoP10_GameOfLife.npy](test/PoP10_GameOfLife.npy).

After that, through the GitHub actions ([Lezione8_tests.yml](../../.github/workflows/Lezione8_tests.yml)), I manage continuous integration to ensure that the code passes the tests with every push. If the code doesn't pass the tests, it's not possible to create a pull request on GitHub's main branch (which is protected by the rules set on the site).

### Deployment (Q1: I love pip)

Since the package is built using a *project.toml* and a *setup.cfg* file, deploying it is straightforward:

- Install the *build* and *twine* packages:
    ```bash
    pip install build twine
    ```

- Build the package's distribution in its directory:
   ```bash
   python -m build
   ```

- Deploy to the [test pypi](https://test.pypi.org/project/BicoccaCoursePython2024/) site

    ```bash
    twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u __token__ -p <pypitest-token>
    ```
Now the package is avaiable [here](https://test.pypi.org/project/BicoccaCoursePython2024/), and it's possible to install it with:

```bash
pip install --index-url https://test.pypi.org/simple/ BicoccaCoursePython2024
```

#### Deployment to Test PyPI with Continuous Integration
Since the package is still in development, I manage deployment through continuous integration after a pull request to the ***deployment*** branch.
To pull to this branch is necessary to pass the following actions:
- [Test Lezione8](../../.github/workflows/Lezione8_tests.yml): makes all the tests for the package.

- [CheckTag](../../.github/workflows/CheckTag.yml): Check that the current verision has a tag.

The workflow that manage this is defined in [DeploytoTestPyPI.yml](../../.github/workflows/DeploytoTestPyPI.yml).
To make work it properly it's necessary to add the API token of Test PyPI in the GitHub secrets as follow:

- The **TEST_PYPI_USERNAME**= \__token__
- The **TEST_PYPI_PASSWORD**= \<Test PyPi Token>

***Note***:
 Because the actions' steps are done as if they are in separate shell, is important to move the current directory for each step.

## Documentation
An additional feature that I added to this package is the documentation. The documentation is generated with **sphinx** package to make it more easily.

### First initialization
To use **sphinx** is necessary to install it with:
```bash
pip install sphinx
```
if one want to use the read the docs theme is necessary also to install it:
```bash
pip install sphinx-rtd-theme
```
After that in the main folder of the project create the **doc** folder with:
```bash
sphinx-quickstart
```
- ***Note***:
Choose the option **NO** for the *Separate source and build directories* question.

This generate the necessary files for making sphinx work properly.
#### Modify the conf.py file
Is possible to modify some sphinx configuration in the [conf.py](./docs/conf.py) file to activate several features:
-   For the  read the docs theme
    ```python
       html_theme = 'sphinx_rtd_theme'
    ```
- For the autodoc extension
    ```python
    extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    ]
    ```
- To ensure that sphinx find the right folder:
    ```python
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../src'))# Add the main directory project to the path
    ```

#### Generate the restructured text file
Sphinx to generate the documentation uses the ***rst*** files. Te first time is possible to generate a rst file for each module using simply: 
```bash
sphinx-apidoc -o docs -F --separate <src/package_name folder>
```
#### Build the html pages
To build the effective html pages one must call in the *doc* folder:
- for Linux
    ```bash
    ./make html
    ```
- for Windows:
    ```bash
    ./make.bat html
    ```
If had already build the documentation, and you want to generate a new version, is usefull to clean up the buil by:
```
./make.bat clean
```

this is because some times sphinx dosen't create the new build for the pages that are not modified and this could generate some problems with the index.



### Documentation with continuos integration
Because the file are changed for every commit, is usefull to build the documentation trought the continuos integration.
I've done that using the [BuildDocumentation](../../.github/workflows/BuildDocumentation.yml) workflow. This build the documentation for each deployed version of the package and make it aviable on the **GitHub pages** of the repository.

***Note***: To activate the url of the pages is important to go to the GitHub's settings/pages and select the branch responsable of the documentation.

After that the documetation will be aviabel at:
```bash
    https://<GitHub-user>.github.io/<GitHub-repository-name>
```
### Badges
It's possible to show the badges in the README.md for the documentation and the single workflow status.
Is possible to personalize the badge as follow:
- Choose the branch on wich check toe workflow status add to the url:
    ```bash
    ?branch=<branch name>
    ```
- Choose the label of the badge:
    ```bash
    ?label=<branch name>
    ```
***Note:*** The space in the url are substituted with **%20**