# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Dialect(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, label=None, supports_cost_estimate=None, supports_upload_tables=None, persistent_table_indexes=None, persistent_table_sortkeys=None, persistent_table_distkey=None, supports_streaming=None, automatically_run_sql_runner_snippets=None, connection_tests=None, can=None):
        """
        Dialect - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'label': 'str',
            'supports_cost_estimate': 'bool',
            'supports_upload_tables': 'bool',
            'persistent_table_indexes': 'str',
            'persistent_table_sortkeys': 'str',
            'persistent_table_distkey': 'str',
            'supports_streaming': 'bool',
            'automatically_run_sql_runner_snippets': 'bool',
            'connection_tests': 'list[str]',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'name': 'name',
            'label': 'label',
            'supports_cost_estimate': 'supports_cost_estimate',
            'supports_upload_tables': 'supports_upload_tables',
            'persistent_table_indexes': 'persistent_table_indexes',
            'persistent_table_sortkeys': 'persistent_table_sortkeys',
            'persistent_table_distkey': 'persistent_table_distkey',
            'supports_streaming': 'supports_streaming',
            'automatically_run_sql_runner_snippets': 'automatically_run_sql_runner_snippets',
            'connection_tests': 'connection_tests',
            'can': 'can'
        }

        self._name = name
        self._label = label
        self._supports_cost_estimate = supports_cost_estimate
        self._supports_upload_tables = supports_upload_tables
        self._persistent_table_indexes = persistent_table_indexes
        self._persistent_table_sortkeys = persistent_table_sortkeys
        self._persistent_table_distkey = persistent_table_distkey
        self._supports_streaming = supports_streaming
        self._automatically_run_sql_runner_snippets = automatically_run_sql_runner_snippets
        self._connection_tests = connection_tests
        self._can = can

    @property
    def name(self):
        """
        Gets the name of this Dialect.
        The name of the dialect

        :return: The name of this Dialect.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Dialect.
        The name of the dialect

        :param name: The name of this Dialect.
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """
        Gets the label of this Dialect.
        The human-readable label of the connection

        :return: The label of this Dialect.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Dialect.
        The human-readable label of the connection

        :param label: The label of this Dialect.
        :type: str
        """

        self._label = label

    @property
    def supports_cost_estimate(self):
        """
        Gets the supports_cost_estimate of this Dialect.
        Whether the dialect supports query cost estimates

        :return: The supports_cost_estimate of this Dialect.
        :rtype: bool
        """
        return self._supports_cost_estimate

    @supports_cost_estimate.setter
    def supports_cost_estimate(self, supports_cost_estimate):
        """
        Sets the supports_cost_estimate of this Dialect.
        Whether the dialect supports query cost estimates

        :param supports_cost_estimate: The supports_cost_estimate of this Dialect.
        :type: bool
        """

        self._supports_cost_estimate = supports_cost_estimate

    @property
    def supports_upload_tables(self):
        """
        Gets the supports_upload_tables of this Dialect.
        Whether the dialect supports uploading tables

        :return: The supports_upload_tables of this Dialect.
        :rtype: bool
        """
        return self._supports_upload_tables

    @supports_upload_tables.setter
    def supports_upload_tables(self, supports_upload_tables):
        """
        Sets the supports_upload_tables of this Dialect.
        Whether the dialect supports uploading tables

        :param supports_upload_tables: The supports_upload_tables of this Dialect.
        :type: bool
        """

        self._supports_upload_tables = supports_upload_tables

    @property
    def persistent_table_indexes(self):
        """
        Gets the persistent_table_indexes of this Dialect.
        PDT index columns

        :return: The persistent_table_indexes of this Dialect.
        :rtype: str
        """
        return self._persistent_table_indexes

    @persistent_table_indexes.setter
    def persistent_table_indexes(self, persistent_table_indexes):
        """
        Sets the persistent_table_indexes of this Dialect.
        PDT index columns

        :param persistent_table_indexes: The persistent_table_indexes of this Dialect.
        :type: str
        """

        self._persistent_table_indexes = persistent_table_indexes

    @property
    def persistent_table_sortkeys(self):
        """
        Gets the persistent_table_sortkeys of this Dialect.
        PDT sortkey columns

        :return: The persistent_table_sortkeys of this Dialect.
        :rtype: str
        """
        return self._persistent_table_sortkeys

    @persistent_table_sortkeys.setter
    def persistent_table_sortkeys(self, persistent_table_sortkeys):
        """
        Sets the persistent_table_sortkeys of this Dialect.
        PDT sortkey columns

        :param persistent_table_sortkeys: The persistent_table_sortkeys of this Dialect.
        :type: str
        """

        self._persistent_table_sortkeys = persistent_table_sortkeys

    @property
    def persistent_table_distkey(self):
        """
        Gets the persistent_table_distkey of this Dialect.
        PDT distkey column

        :return: The persistent_table_distkey of this Dialect.
        :rtype: str
        """
        return self._persistent_table_distkey

    @persistent_table_distkey.setter
    def persistent_table_distkey(self, persistent_table_distkey):
        """
        Sets the persistent_table_distkey of this Dialect.
        PDT distkey column

        :param persistent_table_distkey: The persistent_table_distkey of this Dialect.
        :type: str
        """

        self._persistent_table_distkey = persistent_table_distkey

    @property
    def supports_streaming(self):
        """
        Gets the supports_streaming of this Dialect.
        Suports streaming results

        :return: The supports_streaming of this Dialect.
        :rtype: bool
        """
        return self._supports_streaming

    @supports_streaming.setter
    def supports_streaming(self, supports_streaming):
        """
        Sets the supports_streaming of this Dialect.
        Suports streaming results

        :param supports_streaming: The supports_streaming of this Dialect.
        :type: bool
        """

        self._supports_streaming = supports_streaming

    @property
    def automatically_run_sql_runner_snippets(self):
        """
        Gets the automatically_run_sql_runner_snippets of this Dialect.
        Should SQL Runner snippets automatically be run

        :return: The automatically_run_sql_runner_snippets of this Dialect.
        :rtype: bool
        """
        return self._automatically_run_sql_runner_snippets

    @automatically_run_sql_runner_snippets.setter
    def automatically_run_sql_runner_snippets(self, automatically_run_sql_runner_snippets):
        """
        Sets the automatically_run_sql_runner_snippets of this Dialect.
        Should SQL Runner snippets automatically be run

        :param automatically_run_sql_runner_snippets: The automatically_run_sql_runner_snippets of this Dialect.
        :type: bool
        """

        self._automatically_run_sql_runner_snippets = automatically_run_sql_runner_snippets

    @property
    def connection_tests(self):
        """
        Gets the connection_tests of this Dialect.
        Array of names of the tests that can be run on a connection using this dialect

        :return: The connection_tests of this Dialect.
        :rtype: list[str]
        """
        return self._connection_tests

    @connection_tests.setter
    def connection_tests(self, connection_tests):
        """
        Sets the connection_tests of this Dialect.
        Array of names of the tests that can be run on a connection using this dialect

        :param connection_tests: The connection_tests of this Dialect.
        :type: list[str]
        """

        self._connection_tests = connection_tests

    @property
    def can(self):
        """
        Gets the can of this Dialect.
        Operations the current user is able to perform on this object

        :return: The can of this Dialect.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Dialect.
        Operations the current user is able to perform on this object

        :param can: The can of this Dialect.
        :type: dict(str, bool)
        """

        self._can = can

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Dialect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other