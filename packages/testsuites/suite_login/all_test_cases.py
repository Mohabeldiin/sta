"""foo"""

from packages.testsuites.suite_login.test_01_login import test_01_login
from packages.testsuites.suite_login.test_02_login import test_02_login
from packages.testsuites.suite_login.test_03_login import test_03_login
from packages.testsuites.suite_login.test_04_login import test_04_login
from packages.testsuites.suite_login.test_05_login import test_05_login
from packages.testsuites.suite_login.test_06_login import test_06_login
from packages.testsuites.suite_login.test_07_login import test_07_login
from packages.testsuites.suite_login.test_08_login import test_08_login
from packages.testsuites.suite_login.test_09_login import test_09_login
from packages.testsuites.suite_login.test_10_login import test_10_login
from packages.testsuites.suite_login.test_11_login import test_11_login
from packages.testsuites.suite_login.test_12_login import test_12_login
from packages.testsuites.suite_login.test_13_login import test_13_login
from packages.testsuites.suite_login.test_14_login import test_14_login
from packages.testsuites.suite_login.test_15_login import test_15_login
from packages.testsuites.suite_login.test_16_login import test_16_login
from packages.testsuites.suite_login.test_17_login import test_17_login
from packages.testsuites.suite_login.test_18_login import test_18_login
from packages.testsuites.suite_login.test_19_login import test_19_login
from packages.testsuites.suite_login.test_20_login import test_20_login
from packages.testsuites.suite_registration.init import project_logger, unittest


logger = project_logger("Registration Test Suite")

logger.info("Collecting Registration Test Suite")


suite = unittest.TestSuite()
runner = unittest.TextTestRunner()

suite.addTest(unittest.makeSuite(test_01_login))
suite.addTest(unittest.makeSuite(test_02_login))
suite.addTest(unittest.makeSuite(test_03_login))
suite.addTest(unittest.makeSuite(test_04_login))
suite.addTest(unittest.makeSuite(test_05_login))
suite.addTest(unittest.makeSuite(test_06_login))
suite.addTest(unittest.makeSuite(test_07_login))
suite.addTest(unittest.makeSuite(test_08_login))
suite.addTest(unittest.makeSuite(test_09_login))
suite.addTest(unittest.makeSuite(test_10_login))
suite.addTest(unittest.makeSuite(test_11_login))
suite.addTest(unittest.makeSuite(test_12_login))
suite.addTest(unittest.makeSuite(test_13_login))
suite.addTest(unittest.makeSuite(test_14_login))
suite.addTest(unittest.makeSuite(test_15_login))
suite.addTest(unittest.makeSuite(test_16_login))
suite.addTest(unittest.makeSuite(test_17_login))
suite.addTest(unittest.makeSuite(test_18_login))
suite.addTest(unittest.makeSuite(test_19_login))
suite.addTest(unittest.makeSuite(test_20_login))

logger.info("Registration Test Suite Completed")

logger.info("Running Registration Test Suite")

result = runner.run(suite)

print(result.testsRun-len(result.failures))