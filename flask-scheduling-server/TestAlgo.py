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

    @unittest.expectedFailure
    def test_unsatisfiable(self):
        """
        This dataset cannot be satisfied because a lecturer has more lessons than time
        """
        models.createTestDB("data3/")
        Scheduler.startAlgo()

    @unittest.expectedFailure
    def test_noInstructor(self):
        """
        This dataset fails because there is no instructor for a particular course
        """
        models.createTestDB("data4/")
        Scheduler.startAlgo()
if __name__ == "__main__":
    unittest.main()