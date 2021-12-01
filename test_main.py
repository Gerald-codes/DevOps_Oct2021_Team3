import main
import unittest


class test_loadCity_function(unittest.TestCase):
    def test_With_Correct_Start_file(self):
        print("\nTest LoadCity")
        self.assertTrue(main.loadCity('start.csv'))
    def test_With_inCorrect_Start_file(self):
        self.assertFalse(main.loadCity('fake.txt'))

class test_initBuildingPools_function(unittest.TestCase):
    def test_if_array_is_correct(self):
        print("\nTest initBuildingPools")
        results = main.initBuildingPools()
        self.assertEqual(results["Building"][0],"BCH")
        self.assertEqual(results["Building"][1],"FAC")
        self.assertEqual(results["Building"][2],"HSE")
        self.assertEqual(results["Building"][3],"SHP")
        self.assertEqual(results["Building"][4],"HWY")
        self.assertEqual(results["Copies"][0],8)
        self.assertEqual(results["Copies"][1],8)
        self.assertEqual(results["Copies"][2],8)
        self.assertEqual(results["Copies"][3],8)
        self.assertEqual(results["Copies"][4],8)

class test_loadSavedGame_function(unittest.TestCase):
    def test_if_Saved_Game_is_present(self):
        print("\nTest Save Game")
        self.assertTrue(main.loadSavedGame())

class test_loadSavedBuildingPools_function(unittest.TestCase):
    def test_if_array_is_correct(self):
        print("\nTest loadSavedBuildingPools")
        results = main.loadSavedBuildingPools()
        self.assertEqual(results["Building"][0],"BCH")
        self.assertEqual(results["Building"][1],"FAC")
        self.assertEqual(results["Building"][2],"HSE")
        self.assertEqual(results["Building"][3],"SHP")
        self.assertEqual(results["Building"][4],"HWY")

class test_loadSavedBuildingPools_function(unittest.TestCase):
    def test_if_Saved_Turns_is_present(self):
        print("\nTest Saved Turns")
        self.assertTrue(main.loadSavedTurns())
        
if __name__ == "__main__":
    unittest.main()