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


class CreateWorkflowRequest(ModelNormal):
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
        ('sla_field',): {
            'inclusive_maximum': 0,
            'inclusive_minimum': 0,
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
            'additional_data_field': (str,),  # noqa: E501
            'auto_expire_field': (AutoExpire,),  # noqa: E501
            'auto_remind_field': (AutoRemind,),  # noqa: E501
            'doc_field': (str,),  # noqa: E501
            'doc_name_field': (str,),  # noqa: E501
            'extension_field': (DocExtension,),  # noqa: E501
            'message_field': (str,),  # noqa: E501
            'priority_field': (Priority,),  # noqa: E501
            'sla_field': (int,),  # noqa: E501
            'token_field': (TokenField,),  # noqa: E501
            'due_date_field': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'additional_data_field': 'AdditionalDataField',  # noqa: E501
        'auto_expire_field': 'AutoExpireField',  # noqa: E501
        'auto_remind_field': 'AutoRemindField',  # noqa: E501
        'doc_field': 'DocField',  # noqa: E501
        'doc_name_field': 'DocNameField',  # noqa: E501
        'extension_field': 'ExtensionField',  # noqa: E501
        'message_field': 'MessageField',  # noqa: E501
        'priority_field': 'PriorityField',  # noqa: E501
        'sla_field': 'SLAField',  # noqa: E501
        'token_field': 'TokenField',  # noqa: E501
        'due_date_field': 'DueDateField',  # noqa: E501
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
    def __init__(self, additional_data_field, auto_expire_field, auto_remind_field, doc_field, doc_name_field, extension_field, message_field, priority_field, token_field, *args, **kwargs):  # noqa: E501
        """CreateWorkflowRequest - a model defined in OpenAPI

        Args:
            additional_data_field (str): Sets additional data to be embedded in PDF Meta.
            auto_expire_field (AutoExpire):
            auto_remind_field (AutoRemind):
            doc_field (str): Base64 Encoded String of document
            doc_name_field (str): Name of document to display in SigniFlow
            extension_field (DocExtension):
            message_field (str): Custom message to display to participants
            priority_field (Priority):
            token_field (TokenField):

        Keyword Args:
            sla_field (int): Deprecated field, Pass 0. defaults to 0  # noqa: E501
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
            due_date_field (datetime, none_type): Due date for the document, use in conjunction with Auto Expire.. [optional]  # noqa: E501
        """

        sla_field = kwargs.get('sla_field', 0)
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

        self.additional_data_field = additional_data_field
        self.auto_expire_field = auto_expire_field
        self.auto_remind_field = auto_remind_field
        self.doc_field = doc_field
        self.doc_name_field = doc_name_field
        self.extension_field = extension_field
        self.message_field = message_field
        self.priority_field = priority_field
        self.sla_field = sla_field
        self.token_field = token_field
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)