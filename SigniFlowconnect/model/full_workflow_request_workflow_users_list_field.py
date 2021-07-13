"""
    SigniFlow OpenAPI Spec v1

    ## SigniFlow API used to automate esignature workflow creation and management.   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@signiflow.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from SigniFlowconnect.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from SigniFlowconnect.model.full_workflow_request_group_step_field import FullWorkflowRequestGroupStepField
    from SigniFlowconnect.model.full_workflow_request_workflow_user_fields_field import FullWorkflowRequestWorkflowUserFieldsField
    globals()['FullWorkflowRequestGroupStepField'] = FullWorkflowRequestGroupStepField
    globals()['FullWorkflowRequestWorkflowUserFieldsField'] = FullWorkflowRequestWorkflowUserFieldsField


class FullWorkflowRequestWorkflowUsersListField(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('email_address_field',): {
            'min_length': 1,
        },
        ('language_code_field',): {
            'min_length': 1,
        },
        ('latitude_field',): {
            'min_length': 1,
        },
        ('longitude_field',): {
            'min_length': 1,
        },
        ('mobile_number_field',): {
            'min_length': 1,
        },
        ('sign_reason_field',): {
            'min_length': 1,
        },
        ('signer_password_field',): {
            'min_length': 1,
        },
        ('user_first_name_field',): {
            'min_length': 1,
        },
        ('user_full_name_field',): {
            'min_length': 1,
        },
        ('user_last_name_field',): {
            'min_length': 1,
        },
        ('preloaded_face_to_face_signers_field',): {
            'min_items': 1,
        },
        ('workflow_user_fields_field',): {
            'min_items': 1,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'action_field': (float,),  # noqa: E501
            'allow_proxy_field': (float,),  # noqa: E501
            'auto_sign_field': (bool,),  # noqa: E501
            'email_address_field': (str,),  # noqa: E501
            'language_code_field': (str,),  # noqa: E501
            'latitude_field': (str,),  # noqa: E501
            'longitude_field': (str,),  # noqa: E501
            'mobile_number_field': (str,),  # noqa: E501
            'sign_reason_field': (str,),  # noqa: E501
            'signer_password_field': (str,),  # noqa: E501
            'user_first_name_field': (str,),  # noqa: E501
            'user_full_name_field': (str,),  # noqa: E501
            'user_last_name_field': (str,),  # noqa: E501
            'group_step_field': (FullWorkflowRequestGroupStepField,),  # noqa: E501
            'preloaded_face_to_face_signers_field': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),  # noqa: E501
            'workflow_user_fields_field': ([FullWorkflowRequestWorkflowUserFieldsField],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'action_field': 'ActionField',  # noqa: E501
        'allow_proxy_field': 'AllowProxyField',  # noqa: E501
        'auto_sign_field': 'AutoSignField',  # noqa: E501
        'email_address_field': 'EmailAddressField',  # noqa: E501
        'language_code_field': 'LanguageCodeField',  # noqa: E501
        'latitude_field': 'LatitudeField',  # noqa: E501
        'longitude_field': 'LongitudeField',  # noqa: E501
        'mobile_number_field': 'MobileNumberField',  # noqa: E501
        'sign_reason_field': 'SignReasonField',  # noqa: E501
        'signer_password_field': 'SignerPasswordField',  # noqa: E501
        'user_first_name_field': 'UserFirstNameField',  # noqa: E501
        'user_full_name_field': 'UserFullNameField',  # noqa: E501
        'user_last_name_field': 'UserLastNameField',  # noqa: E501
        'group_step_field': 'GroupStepField',  # noqa: E501
        'preloaded_face_to_face_signers_field': 'PreloadedFaceToFaceSignersField',  # noqa: E501
        'workflow_user_fields_field': 'WorkflowUserFieldsField',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, action_field, allow_proxy_field, auto_sign_field, email_address_field, language_code_field, latitude_field, longitude_field, mobile_number_field, sign_reason_field, signer_password_field, user_first_name_field, user_full_name_field, user_last_name_field, *args, **kwargs):  # noqa: E501
        """FullWorkflowRequestWorkflowUsersListField - a model defined in OpenAPI

        Args:
            action_field (float): Refers to the order of signatures from the users.
            allow_proxy_field (float): Allow proxy confirmation field.
            auto_sign_field (bool): ### Enable auto sign.  `True = Signature will be applied automaticly False = User will need to login and Sign` 
            email_address_field (str): Workflow user's email addresses.
            language_code_field (str): #### Sets the display language for the user ##### ISO 2 Digit Code  `en = English es = Spanish fr = French` 
            latitude_field (str): Location latitude.
            longitude_field (str): Location longtitude.
            mobile_number_field (str): Group user's mobile number.
            sign_reason_field (str): Reason for signature.
            signer_password_field (str): Face to face user's password.
            user_first_name_field (str): Face to face user's first name.
            user_full_name_field (str): Face to face user's full name.
            user_last_name_field (str): Face to face user's last name.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            group_step_field (FullWorkflowRequestGroupStepField): [optional]  # noqa: E501
            preloaded_face_to_face_signers_field ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Preloaded user's who will be using the face to face signature field.. [optional]  # noqa: E501
            workflow_user_fields_field ([FullWorkflowRequestWorkflowUserFieldsField]): The list of the workflowed documents field.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.action_field = action_field
        self.allow_proxy_field = allow_proxy_field
        self.auto_sign_field = auto_sign_field
        self.email_address_field = email_address_field
        self.language_code_field = language_code_field
        self.latitude_field = latitude_field
        self.longitude_field = longitude_field
        self.mobile_number_field = mobile_number_field
        self.sign_reason_field = sign_reason_field
        self.signer_password_field = signer_password_field
        self.user_first_name_field = user_first_name_field
        self.user_full_name_field = user_full_name_field
        self.user_last_name_field = user_last_name_field
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
