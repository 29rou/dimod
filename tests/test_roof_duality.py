# Copyright 2018 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# ================================================================================================
import unittest

import dimod

from dimod import fix_variables


# class TestFixVariables(unittest.TestCase):
#     def test_3path(self):
#         bqm = dimod.BinaryQuadraticModel.from_ising({'a': 10}, {'ab': -1, 'bc': 1})
#         fixed = dimod.fix_variables(bqm)
#         self.assertEqual(fixed, {'a': -1, 'b': -1, 'c': 1})
