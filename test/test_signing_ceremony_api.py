"""
    SigniFlow OpenAPI Spec v1

    ## SigniFlow API used to automate esignature workflow creation and management.   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@signiflow.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import SigniFlowconnect
from SigniFlowconnect.api.signing_ceremony_api import SigningCeremonyApi  # noqa: E501


class TestSigningCeremonyApi(unittest.TestCase):
    """SigningCeremonyApi unit test stubs"""

    def setUp(self):
        self.api = SigningCeremonyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_multiple_signers_signing_ceremony(self):
        """Test case for post_multiple_signers_signing_ceremony

        Multiple Signers Signing Ceremony  # noqa: E501
        """
        pass

    def test_post_signing_ceremony_v2(self):
        """Test case for post_signing_ceremony_v2

        Signing Ceremony V2  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
