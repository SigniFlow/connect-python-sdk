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
from SigniFlowconnect.model.action_field import ActionField
from SigniFlowconnect.model.proxy_allowed_field import ProxyAllowedField
from SigniFlowconnect.model.token_field import TokenField
globals()['ActionField'] = ActionField
globals()['ProxyAllowedField'] = ProxyAllowedField
globals()['TokenField'] = TokenField
from SigniFlowconnect.model.add_workflow_step_v2_request import AddWorkflowStepV2Request


class TestAddWorkflowStepV2Request(unittest.TestCase):
    """AddWorkflowStepV2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddWorkflowStepV2Request(self):
        """Test AddWorkflowStepV2Request"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AddWorkflowStepV2Request()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()