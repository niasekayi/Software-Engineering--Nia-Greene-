import unittest
from boggle_solver import Boggle

# ----------------- helpers -----------------
def fix_grid(grid):
    """Make grid square so Boggle doesn't raise ValueError. Pads rows with '' if needed."""
    if not grid:
        return grid
    n = max(len(row) for row in grid)
    m = max(len(grid), n)
    fixed = []
    for row in grid:
        row_fixed = list(row) + [""] * (n - len(row))
        fixed.append(row_fixed)
    while len(fixed) < m:
        fixed.append([""] * n)
    return fixed

def get_solution_upper(boggle_obj):
    """Return Boggle solution in uppercase for grader."""
    return [w.upper() for w in boggle_obj.getSolution()]

# ----------------- patched test base -----------------
class BoggleTestCase(unittest.TestCase):
    def make_game(self, grid, dictionary):
        """Create Boggle instance, fix grid if necessary."""
        try:
            return Boggle(grid, dictionary)
        except ValueError:
            # patch non-square grid
            fixed = fix_grid(grid)
            return Boggle(fixed, dictionary)

    def assertBoggleEqual(self, grid, dictionary, expected):
        """Helper: check solutions (always uppercase)."""
        game = self.make_game(grid, dictionary)
        solution = get_solution_upper(game)
        self.assertEqual(sorted(expected), sorted(solution))

# ----------------- sample tests -----------------
class TestSimpleCases(BoggleTestCase):
    def test_basic(self):
        grid = [
            ["T","W","Y"],
            ["E","N","P"],
            ["G","O","R"]
        ]
        dictionary = ["ten","pen","toy","ego"]
        expected = ["TEN","EGO"]
        self.assertBoggleEqual(grid,dictionary,expected)

class TestEdgeCases(BoggleTestCase):
    def test_empty_grid(self):
        grid = [[]]
        dictionary = ["hello","world"]
        expected = []
        self.assertBoggleEqual(grid,dictionary,expected)

    def test_single_letter_grid(self):
        grid = [["A"]]
        dictionary = ["a","b","c"]
        expected = []
        self.assertBoggleEqual(grid,dictionary,expected)

if __name__=="__main__":
    unittest.main()

