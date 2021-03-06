"""
    SigniFlow OpenAPI Spec v1

    ## SigniFlow API used to automate esignature workflow creation and management.   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@signiflow.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import SigniFlowconnect
from SigniFlowconnect.model.auto_expire import AutoExpire
from SigniFlowconnect.model.auto_remind import AutoRemind
from SigniFlowconnect.model.doc_extension import DocExtension
from SigniFlowconnect.model.priority import Priority
from SigniFlowconnect.model.token_field import TokenField
globals()['AutoExpire'] = AutoExpire
globals()['AutoRemind'] = AutoRemind
globals()['DocExtension'] = DocExtension
globals()['Priority'] = Priority
globals()['TokenField'] = TokenField
from SigniFlowconnect.model.create_workflow_request import CreateWorkflowRequest


class TestCreateWorkflowRequest(unittest.TestCase):
    """CreateWorkflowRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateWorkflowRequest(self):
        """Test CreateWorkflowRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateWorkflowRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
