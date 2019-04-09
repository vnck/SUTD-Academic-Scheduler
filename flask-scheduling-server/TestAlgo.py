import unittest
import models
import Scheduler
class TestAlgo(unittest.TestCase):

    @unittest.expectedFailure
    def test_reqError(self):
        
        """
        Non freshmore class have freshmore cohort class requirement
        Should result in error as requirements do not match
        """
        models.createTestDB("data1/")
        Scheduler.startAlgo()

    @unittest.expectedFailure
    def test_CourseNotFound(self):
        """
        A student group is assigned a course that is not in the course list
        """
        models.createTestDB("data2/")
        Scheduler.startAlgo()

if __name__ == "__main__":
    unittest.main()