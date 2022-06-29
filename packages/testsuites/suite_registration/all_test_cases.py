"""foo"""

from packages.testsuites.suite_registration.init import project_logger, unittest
from packages.testsuites.suite_registration.test_01_registration import Test_01_User_Interface
from packages.testsuites.suite_registration.test_02_registration import Test_02_Registration
from packages.testsuites.suite_registration.test_03_registration import Test_03_Registration
from packages.testsuites.suite_registration.test_04_registration import Test_04_Registration
from packages.testsuites.suite_registration.test_05_registration import Test_05_Registration
from packages.testsuites.suite_registration.test_06_registration import Test_06_Registration
from packages.testsuites.suite_registration.test_07_registration import Test_07_Registration
from packages.testsuites.suite_registration.test_08_registration import Test_08_Registration
from packages.testsuites.suite_registration.test_09_registration import Test_09_Registration
from packages.testsuites.suite_registration.test_10_registration import Test_10_Registration
from packages.testsuites.suite_registration.test_11_registration import Test_11_Registration
from packages.testsuites.suite_registration.test_12_registration import Test_12_Registration
from packages.testsuites.suite_registration.test_13_registration import Test_13_Registration
from packages.testsuites.suite_registration.test_14_registration import Test_14_Registration
from packages.testsuites.suite_registration.test_15_registration import Test_15_Registration
from packages.testsuites.suite_registration.test_16_registration import Test_16_Registration
from packages.testsuites.suite_registration.test_17_registration import Test_17_Registration
from packages.testsuites.suite_registration.test_18_registration import Test_18_Registration
from packages.testsuites.suite_registration.test_19_registration import Test_19_Registration

logger = project_logger("Registration Test Suite")

suite = unittest.TestSuite()
runner = unittest.TextTestRunner()

suite.addTest(unittest.makeSuite(Test_01_User_Interface))
suite.addTest(unittest.makeSuite(Test_02_Registration))
suite.addTest(unittest.makeSuite(Test_03_Registration))
suite.addTest(unittest.makeSuite(Test_04_Registration))
suite.addTest(unittest.makeSuite(Test_05_Registration))
suite.addTest(unittest.makeSuite(Test_06_Registration))
suite.addTest(unittest.makeSuite(Test_07_Registration))
suite.addTest(unittest.makeSuite(Test_08_Registration))
suite.addTest(unittest.makeSuite(Test_09_Registration))
suite.addTest(unittest.makeSuite(Test_10_Registration))
suite.addTest(unittest.makeSuite(Test_11_Registration))
suite.addTest(unittest.makeSuite(Test_12_Registration))
suite.addTest(unittest.makeSuite(Test_13_Registration))
suite.addTest(unittest.makeSuite(Test_14_Registration))
suite.addTest(unittest.makeSuite(Test_15_Registration))
suite.addTest(unittest.makeSuite(Test_16_Registration))
suite.addTest(unittest.makeSuite(Test_17_Registration))
suite.addTest(unittest.makeSuite(Test_18_Registration))
suite.addTest(unittest.makeSuite(Test_19_Registration))

runner.run(suite)
