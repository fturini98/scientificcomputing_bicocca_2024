import os
import re
import numpy as np
import pytest

from BicoccaCoursePython2024.seconda_lezione import Game_life

class TestBicoccaCoursePython2024:
    def test_hello(self):
        print('Hello')
    
    @pytest.mark.parametrize("relative_path", ["Esercizi/BicoccaCoursePython2024"]) 
    def test_np_power(self, relative_path):
        """
        Checks if there is an incorrect usage of `np.power(10.` without a decimal point 
        (i.e., `10.`) in the codebase. This is crucial because certain older versions 
        of numpy (e.g., those used with numba or TensorFlow) may produce incorrect results.
        
        Args:
            relative_path (str): Relative path to the directory containing source files.
        """
        # Get the absolute path from the relative path.
        absolute_path = os.path.abspath(relative_path)

        # Ensure the specified path exists.
        if not os.path.exists(absolute_path):
            pytest.fail(f"The specified path does not exist: {absolute_path}")

        # Regular expression to match `np.power(10.` without the decimal point after `10`.
        pattern = r'np\.power\(10[^\.\)]'

        # Recursively search through all `.py` files in the directory.
        for root, _, files in os.walk(absolute_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        match = re.search(pattern, content)
                        if match:
                            pytest.fail(f"Found incorrect usage of `np.power(10.` without decimal "
                                        f"in file: {file_path}")

#=============Game of life testing==========================
    def test_default_initial_condition(self):
        """
        Verify that the initial condition is the one expected
        """
        game = Game_life()  
        
        print(np.sum(game.grid))
        assert np.sum(game.grid) == 5
        assert 1 in game.grid

    def test_gen1(self):
        """
        Verify that the  `next_gen` function produce the expected value.
        """
        game = Game_life()

        # Next gen evaluation
        game.next_gen()

        # The expected next gen
        expected_grid = np.zeros((100,100), dtype=int)
        expected_grid[20, 20:22] = 1
        expected_grid[21, 20] = 1
        expected_grid[22, 20:23] = 1
        if not np.array_equal(game.grid, expected_grid):
            pytest.fail(f"The expected grid is{expected_grid} but the next gen is {game.grid}")
    
    def test_gen_10(self):
        '''
        Test that the game of life still reproduce the 10 generation using a snapshot
        '''
        life=Game_life()
        
        direc='Esercizi/BicoccaCoursePython2024/test/'
        
        snap10=np.load(direc+'PoP10_GameOfLife.npy')
        
        for i in range(0,10):
            #Generate the new pop. 10
            life.next_gen()
        new10_gen=life.grid
        
        #Compare the new population with the expected old pop10
        assert np.array_equal(new10_gen,snap10)

