import main
import unittest

mockCity = [[' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', 'D', ' ', ' ', ' '],
        [' ', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+'],
        ['1', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|'], 
        [' ', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+'], 
        ['2', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|'], 
        [' ', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+'], 
        ['3', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|'], 
        [' ', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+'], 
        ['4', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|'], 
        [' ', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '+']]

class test_MainMenu_function(unittest.TestCase):
    def test_MainMenu(self):
        print("\nTest MainMenu\nStart")
        self.assertIsNone(main.mainMenu())
        print("\nEnd")

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
        self.assertTrue(main.loadSavedGame('savedGame'))
    def test_if_Saved_Game_is_not_present(self):
        self.assertEqual(main.loadSavedGame('fake'),'')

class test_loadSavedBuildingPools_function(unittest.TestCase):
    def test_if_loadSavedBuildingPools_is_present(self):
        print("\nTest savedBuildingPools")
        results = main.loadSavedBuildingPools('savedBuildingPools')
        self.assertEqual(results["Building"][0],"BCH")
        self.assertEqual(results["Building"][1],"FAC")
        self.assertEqual(results["Building"][2],"HSE")
        self.assertEqual(results["Building"][3],"SHP")
        self.assertEqual(results["Building"][4],"HWY")
    def test_if_loadSavedBuildingPools_is_not_present(self):
        self.assertEqual(main.loadSavedBuildingPools('fake'),'')

class test_loadSavedTurns_function(unittest.TestCase):
    def test_if_Saved_Turns_is_present(self):
        print("\nTest Saved Turns")
        self.assertTrue(main.loadSavedTurns('savedTurns'))
    def test_if_Saved_Turns_is_not_present(self):
        self.assertEqual(main.loadSavedBuildingPools('fake'),'')

class test_viewCity_function(unittest.TestCase):
    def test_viewCity(self):
        self.assertIsNone(main.viewCity(mockCity))

class test_ViewCurrentScore_function(unittest.TestCase):
    def test_ScoreCalculation(self):
        mockCity = main.loadSavedGame('testScore')
        self.assertEqual(main.ViewCurrentScore(mockCity),50)

class test_saveGame_function(unittest.TestCase):
    def test_saveGame(self):
        mockCity = main.loadSavedGame('testScore')
        mockbPool = main.initBuildingPools()
        main.saveGame(mockCity,mockbPool,1)
        self.assertTrue(main.loadSavedGame('savedGame'))
        results = main.loadSavedBuildingPools('savedBuildingPools')
        self.assertEqual(results["Building"][0],"BCH")
        self.assertEqual(results["Copies"][0],8)
        self.assertEqual(results["Building"][1],"FAC")
        self.assertEqual(results["Copies"][1],8)
        self.assertEqual(results["Building"][2],"HSE")
        self.assertEqual(results["Copies"][2],8)
        self.assertEqual(results["Building"][3],"SHP")
        self.assertEqual(results["Copies"][3],8)
        self.assertEqual(results["Building"][4],"HWY")
        self.assertEqual(results["Copies"][4],8)
        self.assertTrue(main.loadSavedTurns('savedTurns'))

if __name__ == "__main__":
    unittest.main()

# pytest -v --html=report.html --self-contained-html
