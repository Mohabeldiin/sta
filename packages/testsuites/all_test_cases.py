"""foo"""

from packages.testsuites.suite_registration.test_19_registration import Test_19_Registration
from packages.testsuites.suite_registration.test_18_registration import Test_18_Registration
from packages.testsuites.suite_registration.test_17_registration import Test_17_Registration
from packages.testsuites.suite_registration.test_16_registration import Test_16_Registration
from packages.testsuites.suite_registration.test_15_registration import Test_15_Registration
from packages.testsuites.suite_registration.test_14_registration import Test_14_Registration
from packages.testsuites.suite_registration.test_13_registration import Test_13_Registration
from packages.testsuites.suite_registration.test_12_registration import Test_12_Registration
from packages.testsuites.suite_registration.test_11_registration import Test_11_Registration
from packages.testsuites.suite_registration.test_10_registration import Test_10_Registration
from packages.testsuites.suite_registration.test_09_registration import Test_09_Registration
from packages.testsuites.suite_registration.test_08_registration import Test_08_Registration
from packages.testsuites.suite_registration.test_07_registration import Test_07_Registration
from packages.testsuites.suite_registration.test_06_registration import Test_06_Registration
from packages.testsuites.suite_registration.test_05_registration import Test_05_Registration
from packages.testsuites.suite_registration.test_04_registration import Test_04_Registration
from packages.testsuites.suite_registration.test_03_registration import Test_03_Registration
from packages.testsuites.suite_registration.test_02_registration import Test_02_Registration
from packages.testsuites.suite_registration.test_01_registration import Test_01_User_Interface
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

suite_login = unittest.TestSuite()
suite_registration = unittest.TestSuite()
runner = unittest.TextTestRunner()

suite_registration.addTest(unittest.makeSuite(Test_01_User_Interface))
suite_registration.addTest(unittest.makeSuite(Test_02_Registration))
suite_registration.addTest(unittest.makeSuite(Test_03_Registration))
suite_registration.addTest(unittest.makeSuite(Test_04_Registration))
suite_registration.addTest(unittest.makeSuite(Test_05_Registration))
suite_registration.addTest(unittest.makeSuite(Test_06_Registration))
suite_registration.addTest(unittest.makeSuite(Test_07_Registration))
suite_registration.addTest(unittest.makeSuite(Test_08_Registration))
suite_registration.addTest(unittest.makeSuite(Test_09_Registration))
suite_registration.addTest(unittest.makeSuite(Test_10_Registration))
suite_registration.addTest(unittest.makeSuite(Test_11_Registration))
suite_registration.addTest(unittest.makeSuite(Test_12_Registration))
suite_registration.addTest(unittest.makeSuite(Test_13_Registration))
suite_registration.addTest(unittest.makeSuite(Test_14_Registration))
suite_registration.addTest(unittest.makeSuite(Test_15_Registration))
suite_registration.addTest(unittest.makeSuite(Test_16_Registration))
suite_registration.addTest(unittest.makeSuite(Test_17_Registration))
suite_registration.addTest(unittest.makeSuite(Test_18_Registration))
suite_registration.addTest(unittest.makeSuite(Test_19_Registration))
suite_login.addTest(unittest.makeSuite(test_01_login))
suite_login.addTest(unittest.makeSuite(test_02_login))
suite_login.addTest(unittest.makeSuite(test_03_login))
suite_login.addTest(unittest.makeSuite(test_04_login))
suite_login.addTest(unittest.makeSuite(test_05_login))
suite_login.addTest(unittest.makeSuite(test_06_login))
suite_login.addTest(unittest.makeSuite(test_07_login))
suite_login.addTest(unittest.makeSuite(test_08_login))
suite_login.addTest(unittest.makeSuite(test_09_login))
suite_login.addTest(unittest.makeSuite(test_10_login))
suite_login.addTest(unittest.makeSuite(test_11_login))
suite_login.addTest(unittest.makeSuite(test_12_login))
suite_login.addTest(unittest.makeSuite(test_13_login))
suite_login.addTest(unittest.makeSuite(test_14_login))
suite_login.addTest(unittest.makeSuite(test_15_login))
suite_login.addTest(unittest.makeSuite(test_16_login))
suite_login.addTest(unittest.makeSuite(test_17_login))
suite_login.addTest(unittest.makeSuite(test_18_login))
suite_login.addTest(unittest.makeSuite(test_19_login))
suite_login.addTest(unittest.makeSuite(test_20_login))

logger.info("Running Registration Test Suite")


def get_result():
    result_login = runner.run(suite_login)
    result_registration = runner.run(suite_registration)
    result = {
        "login_pass": int(result_login.testsRun - result_login.failures),
        "login_fall": result_login.failures,
        "registration_pass": int(result_registration.testsRun - result_registration.failures),
        "registration_fall": result_registration.failures
    }
    return result
