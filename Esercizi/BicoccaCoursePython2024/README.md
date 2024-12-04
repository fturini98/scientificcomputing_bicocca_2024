# BicoccaCoursePython2024
Python package to solve the exercices of the Bicocca's phD python course.
The python package as a module for each lesson:
- Lesson 01 module ([prima_lezione](#prima_lezione))
- Lesson 02 module ([seconda_lezione](#seconda_lezione))
- Lesson 03 module ([terza_lezione](#terza_lezione))
- Lesson 04 module ([quarta_lezione](#quarta_lezione))
- [Lesson 08](#lesson-08) has no module (test, and package deployment)


## prima_lezione

## seconda_lezione

## terza_lezione

## quarta_lezione

## Lesson 08

The last lesson is about building a package and then **testing** and deploying it.  
I've completed the exercises related to:  
- the tests (**Q2: My own test**)  
- and the deployment (**Q1: I love pip**)

### Tests' Exercise (Q2: My own test)

For the test exercise, I wrote a class ([TestBicoccaCoursePython2024](test/ottava_lezione_test.py)) with 4 methods:

- ***test_np_power***: This test ensures that there is no occurrence of `np.power(10., x)` without the dot in the codebase. This is important because some older versions of NumPy (e.g., those used with Numba or TensorFlow) don't automatically convert `10` to a float, which introduces a bug when performing the power of 10 operation.

- Tests for the [Game_life](src/BicoccaCoursePython2024/seconda_lezione.py) class:

    - ***test_default_initial_condition***: This test checks that the default initial conditions of the game are as expected.
    
    - ***test_gen1***: This test checks that the first generation of the game is what is expected.
    
    - ***test_gen_10***: This test ensures that the 10th generation still matches the one obtained in the first run of the code. It compares the current grid state with a saved snapshot [PoP10_GameOfLife.npy](test/PoP10_GameOfLife.npy).

After that, through the GitHub actions ([Lezione8_tests.yml](../../.github/workflows/Lezione8_tests.yml)), I manage continuous integration to ensure that the code passes the tests with every push. If the code doesn't pass the tests, it's not possible to create a pull request on GitHub's main branch (which is protected by the rules set on the site).

### Deployment

Since the package is built using a *project.toml* and a *setup.cfg* file, deploying it is straightforward:

- Install the *build* and *twine* packages:
    ```bash
    pip install build twine
    ```

- Build the package's distribution in its directory:
   ```
   python -m build
   ```

- Deploy to the [test pypi](https://test.pypi.org/project/BicoccaCoursePython2024/) site

    ```
    twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u __token__ -p <pypitest-token>
    ```
Now the package is avaiable [here](https://test.pypi.org/project/BicoccaCoursePython2024/), and it's possible to install it with:

```
pip install --index-url https://test.pypi.org/simple/ BicoccaCoursePython2024
```

#### Deployment to Test PyPI with Continuous Integration
Since the package is still in development, I manage deployment through continuous integration after a pull request to the ***deployment*** branch.
To pull to this branch is necessary to pass the following actions:
- [Test Lezione8](../../.github/workflows/Lezione8_tests.yml): makes all the tests for the package.

- [CheckTag](../../.github/workflows/ControlTag.yml): Check that the current verision has a tag. 
