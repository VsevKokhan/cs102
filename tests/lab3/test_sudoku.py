import unittest
from src.lab3 import sudoku


class SudokuTestCase(unittest.TestCase):
    def test_group(self):
        values = [1, 2, 3, 4]
        needed_groups = [[1, 2], [3, 4]]
        actual_groups = sudoku.group(values, 2)
        self.assertEqual(needed_groups, actual_groups)

        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        needed_groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        actual_groups = sudoku.group(values, 3)
        self.assertEqual(needed_groups, actual_groups)

    def test_get_row(self):
        puzzle = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        pos = (0, 0)
        needed_row = ['1', '2', '.']
        actual_row = sudoku.get_row(puzzle, pos)
        self.assertEqual(needed_row, actual_row)

        puzzle = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        pos = (1, 0)
        needed_row = ['4', '.', '6']
        actual_row = sudoku.get_row(puzzle, pos)
        self.assertEqual(needed_row, actual_row)

        puzzle = [['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]
        pos = (2, 0)
        needed_row = ['.', '8', '9']
        actual_row = sudoku.get_row(puzzle, pos)
        self.assertEqual(needed_row, actual_row)

    def test_get_col(self):
        puzzle = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        pos = (0, 0)
        needed_col = ['1', '4', '7']
        actual_col = sudoku.get_col(puzzle, pos)
        self.assertEqual(needed_col, actual_col)

        puzzle = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        pos = (0, 1)
        needed_col = ['2', '.', '8']
        actual_col = sudoku.get_col(puzzle, pos)
        self.assertEqual(needed_col, actual_col)

        puzzle = [['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]
        pos = (0, 2)
        needed_col = ['3', '6', '9']
        actual_col = sudoku.get_col(puzzle, pos)
        self.assertEqual(needed_col, actual_col)

    def test_get_block(self):
        grid = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ]

        pos = (0, 1)
        needed_block = ['5', '3', '.', '6', '.', '.', '.', '9', '8']
        actual_block = sudoku.get_block(grid, pos)
        self.assertEqual(needed_block, actual_block)

        pos = (4, 7)
        needed_block = ['.', '.', '3', '.', '.', '1', '.', '.', '6']
        actual_block = sudoku.get_block(grid, pos)
        self.assertEqual(needed_block, actual_block)

        pos = (8, 8)
        needed_block = ['2', '8', '.', '.', '.', '5', '.', '7', '9']
        actual_block = sudoku.get_block(grid, pos)
        self.assertEqual(needed_block, actual_block)

    def test_find_empty_positions(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        needed_pos = (0, 2)
        actual_pos = sudoku.find_empty_positions(grid)
        self.assertEqual(needed_pos, actual_pos)

        grid = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        needed_pos = (1, 1)
        actual_pos = sudoku.find_empty_positions(grid)
        self.assertEqual(needed_pos, actual_pos)

        grid = [['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]
        needed_pos = (2, 0)
        actual_pos = sudoku.find_empty_positions(grid)
        self.assertEqual(needed_pos, actual_pos)

    def test_find_possible_values(self):
        grid = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ]

        pos = (0, 2)
        needed_values = {'1', '2', '4'}
        actual_values = sudoku.find_possible_values(grid, pos)
        self.assertEqual(needed_values, actual_values)

        pos = (4, 7)
        needed_values = {'2', '5', '9'}
        actual_values = sudoku.find_possible_values(grid, pos)
        self.assertEqual(needed_values, actual_values)

    def test_solve(self):
        grid = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]

        needed_solution = [
             ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
             ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
             ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
             ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
             ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
             ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
             ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
             ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
             ['3', '4', '5', '2', '8', '6', '1', '7', '9']
        ]

        actual_solution = sudoku.solve(grid)
        self.assertEqual(needed_solution, actual_solution)

    def test_check_solution(self):
        good_solution = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9']
        ]
        self.assertTrue(sudoku.check_solution(good_solution))

        not_solved = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '.']
        ]
        self.assertFalse(sudoku.check_solution(not_solved))

        bad_solution = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '5', '8', '3', '4', '2', '4', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '7', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '9', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '6']
        ]
        self.assertFalse(sudoku.check_solution(bad_solution))

    def test_generate_sudoku(self):
        grid = sudoku.generate_sudoku(40)
        needed_unknown = 41
        actual_unknown = sum(1 for row in grid for e in row if e == ".")
        self.assertEqual(needed_unknown, actual_unknown)
        solution = sudoku.solve(grid)
        solved = sudoku.check_solution(solution)
        self.assertTrue(solved)

        grid = sudoku.generate_sudoku(1000)
        needed_unknown = 0
        actual_unknown = sum(1 for row in grid for e in row if e == ".")
        self.assertEqual(needed_unknown, actual_unknown)
        solution = sudoku.solve(grid)
        solved = sudoku.check_solution(solution)
        self.assertTrue(solved)

        grid = sudoku.generate_sudoku(0)
        needed_unknown = 81
        actual_unknown = sum(1 for row in grid for e in row if e == ".")
        self.assertEqual(needed_unknown, actual_unknown)
        solution = sudoku.solve(grid)
        solved = sudoku.check_solution(solution)
        self.assertTrue(solved)

if __name__ == '__main__':
    unittest.main()
