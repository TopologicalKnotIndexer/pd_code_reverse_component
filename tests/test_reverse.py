from copy import deepcopy
import unittest

from pd_code_reverse_component import reverse_component


TREFOIL = [[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]
HOPF = [[2, 3, 1, 4], [4, 1, 3, 2]]


class ReverseComponentTests(unittest.TestCase):
    def test_reversal_is_an_involution_without_mutation(self):
        source = deepcopy(TREFOIL)
        reversed_code = reverse_component(source, 1)
        self.assertEqual(reverse_component(reversed_code, 1), TREFOIL)
        self.assertEqual(source, TREFOIL)

    def test_only_selected_hopf_component_labels_are_remapped(self):
        result = reverse_component(HOPF, 1)
        for before, after in zip(HOPF, result):
            for old, new in zip(before, after):
                if old in {3, 4}:
                    self.assertEqual(new, old)

    def test_missing_label_returns_equal_distinct_copy(self):
        result = reverse_component(TREFOIL, 999)
        self.assertEqual(result, TREFOIL)
        self.assertIsNot(result, TREFOIL)


if __name__ == "__main__":
    unittest.main()
