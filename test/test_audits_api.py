"""
    SigniFlow OpenAPI Spec v1

    ## SigniFlow API used to automate esignature workflow creation and management.   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@signiflow.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import SigniFlowconnect
from SigniFlowconnect.api.audits_api import AuditsApi  # noqa: E501


class TestAuditsApi(unittest.TestCase):
    """AuditsApi unit test stubs"""

    def setUp(self):
        self.api = AuditsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_get_audit_document(self):
        """Test case for post_get_audit_document

        Get Audit Document  # noqa: E501
        """
        pass

    def test_post_get_document_audit(self):
        """Test case for post_get_document_audit

        Get Document Audit  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
