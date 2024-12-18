Lesson 08
=================================

The last lesson is about building a package and then **testing** and deploying it.  
I've completed the exercises related to:  

- the tests (**Q2: My own test**)  
- the deployment (**Q1: I love pip**)

Tests' Exercise (Q2: My own test)
---------------------------------

For the test exercise, I wrote a class (`TestBicoccaCoursePython2024 <https://github.com/fturini98/scientificcomputing_bicocca_2024/tree/deployment/Esercizi/BicoccaCoursePython2024/test/ottava_lezione_test.py>`_) with 4 methods:

- **test_np_power**:  
  This test ensures that there is no occurrence of ``np.power(10., x)`` without the dot in the codebase.  
  This is important because some older versions of NumPy (e.g., those used with Numba or TensorFlow) don't automatically convert ``10`` to a float, which introduces a bug when performing the power of 10 operation.

- Tests for the `Game_life <https://github.com/fturini98/scientificcomputing_bicocca_2024/tree/deployment/Esercizi/BicoccaCoursePython2024/src/BicoccaCoursePython2024/seconda_lezione.py>`_ class:

    - **test_default_initial_condition**:  
      This test checks that the default initial conditions of the game are as expected.

    - **test_gen1**:  
      This test checks that the first generation of the game is what is expected.

    - **test_gen_10**:  
      This test ensures that the 10th generation still matches the one obtained in the first run of the code.  
      It compares the current grid state with a saved snapshot (`PoP10_GameOfLife.npy <https://github.com/fturini98/scientificcomputing_bicocca_2024/tree/deployment/Esercizi/BicoccaCoursePython2024/test/PoP10_GameOfLife.npy>`_).

After that, through the GitHub actions (`Lezione8_tests.yml <https://github.com/fturini98/scientificcomputing_bicocca_2024/tree/deployment/.github/workflows/Lezione8_tests.yml>`_), I manage continuous integration to ensure that the code passes the tests with every push.  
If the code doesn't pass the tests, it's not possible to create a pull request on GitHub's main branch (which is protected by the rules set on the site).

Deployment (Q1: I love pip)
---------------------------

Since the package is built using a *project.toml* and a *setup.cfg* file, deploying it is straightforward:

- Install the *build* and *twine* packages:
  
  .. code-block:: bash

    pip install build twine

- Build the package's distribution in its directory:
  
  .. code-block:: bash

    python -m build

- Deploy to the `test PyPI <https://test.pypi.org/project/BicoccaCoursePython2024/>`_ site:
  
  .. code-block:: bash

    twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u __token__ -p <pypitest-token>

Now the package is available `here <https://test.pypi.org/project/BicoccaCoursePython2024/>`_, and it's possible to install it with:

.. code-block:: bash

    pip install --index-url https://test.pypi.org/simple/ BicoccaCoursePython2024

Deployment to Test PyPI with Continuous Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since the package is still in development, I manage deployment through continuous integration.
It's possible to deploy it using a   **workflow_dispatch** on GitHub.

 .. note::
    To enable the possibility of activate manually the deployment workfolw it's mandatory that the relative file yml is on the main branch.

The workflow that manages the deployment is defined in `DeploytoTestPyPI.yml <https://github.com/fturini98/scientificcomputing_bicocca_2024/tree/deployment/.github/workflows/DeploytoTestPyPI.yml>`_.  
To make it work properly, it is necessary to add the API token of Test PyPI in the GitHub secrets as follows:

- **TEST_PYPI_USERNAME**: ``__token__``
- **TEST_PYPI_PASSWORD**: ``<Test PyPI Token>``

.. note::

   Because the actions' steps are done as if they are in separate shells, it is important to move the current directory for each step.
