# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class BagStoreDetailed(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BagStoreDetailed - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'detail_type': 'str',
            'name': 'str',
            'description': 'str',
            'store_type': 'str',
            'store_data': 'object',
            'created': 'datetime',
            'default_file_store': 'str'
        }

        self.attribute_map = {
            'detail_type': 'detail_type',
            'name': 'name',
            'description': 'description',
            'store_type': 'store_type',
            'store_data': 'store_data',
            'created': 'created',
            'default_file_store': 'default_file_store'
        }

        self._detail_type = None
        self._name = None
        self._description = None
        self._store_type = None
        self._store_data = None
        self._created = None
        self._default_file_store = None

    @property
    def detail_type(self):
        """
        Gets the detail_type of this BagStoreDetailed.


        :return: The detail_type of this BagStoreDetailed.
        :rtype: str
        """
        return self._detail_type

    @detail_type.setter
    def detail_type(self, detail_type):
        """
        Sets the detail_type of this BagStoreDetailed.


        :param detail_type: The detail_type of this BagStoreDetailed.
        :type: str
        """
        self._detail_type = detail_type

    @property
    def name(self):
        """
        Gets the name of this BagStoreDetailed.


        :return: The name of this BagStoreDetailed.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BagStoreDetailed.


        :param name: The name of this BagStoreDetailed.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this BagStoreDetailed.
        More information about this store.

        :return: The description of this BagStoreDetailed.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BagStoreDetailed.
        More information about this store.

        :param description: The description of this BagStoreDetailed.
        :type: str
        """
        self._description = description

    @property
    def store_type(self):
        """
        Gets the store_type of this BagStoreDetailed.
        Type of store.

        :return: The store_type of this BagStoreDetailed.
        :rtype: str
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        """
        Sets the store_type of this BagStoreDetailed.
        Type of store.

        :param store_type: The store_type of this BagStoreDetailed.
        :type: str
        """
        self._store_type = store_type

    @property
    def store_data(self):
        """
        Gets the store_data of this BagStoreDetailed.
        Data that is specific to the store type.

        :return: The store_data of this BagStoreDetailed.
        :rtype: object
        """
        return self._store_data

    @store_data.setter
    def store_data(self, store_data):
        """
        Sets the store_data of this BagStoreDetailed.
        Data that is specific to the store type.

        :param store_data: The store_data of this BagStoreDetailed.
        :type: object
        """
        self._store_data = store_data

    @property
    def created(self):
        """
        Gets the created of this BagStoreDetailed.
        Date and time this store was added to the bazaar.

        :return: The created of this BagStoreDetailed.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this BagStoreDetailed.
        Date and time this store was added to the bazaar.

        :param created: The created of this BagStoreDetailed.
        :type: datetime
        """
        self._created = created

    @property
    def default_file_store(self):
        """
        Gets the default_file_store of this BagStoreDetailed.
        Name of the default file store (empty if no default store)

        :return: The default_file_store of this BagStoreDetailed.
        :rtype: str
        """
        return self._default_file_store

    @default_file_store.setter
    def default_file_store(self, default_file_store):
        """
        Sets the default_file_store of this BagStoreDetailed.
        Name of the default file store (empty if no default store)

        :param default_file_store: The default_file_store of this BagStoreDetailed.
        :type: str
        """
        self._default_file_store = default_file_store

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

