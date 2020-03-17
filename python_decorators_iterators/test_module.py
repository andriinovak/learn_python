import unittest

from unittest.mock import Mock, call

import module
from module import main_routine


class test_module(unittest.TestCase):
    def test_main_routine_calls_Manager_methods(self):
        """Test methods calls one by one."""

        module.Manager.a = Mock()
        module.Manager.b = Mock()
        module.Manager.c = Mock()

        main_routine()

        module.Manager.a.assert_called()
        module.Manager.b.assert_called()
        module.Manager.c.assert_called_with("c_args")

    def test_main_routine_calls_Manager_methods_variant1(self):
        """Other way is to mock whole class and compare it's calls."""

        module.Manager = Mock()

        module.Manager.a = Mock()
        module.Manager.b = Mock()
        module.Manager.c = Mock()

        main_routine()

        expected_calls = [call(), call().a(), call().b(), call().c("c_args")]
        print(module.Manager.mock_calls)
        # remember to mock class where it is used (in module) not in test
        assert module.Manager.mock_calls == expected_calls


if __name__ == "__main__":
    unittest.main()
