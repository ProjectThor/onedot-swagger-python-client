# coding: utf-8

"""
    Wealthport API

    Wealthport provides a simple, lightweight and open Web API based on the Open API 2.0 standard (<a href=\"https://www.openapis.org\" target=\"_blank\">https://www.openapis.org</a>). Our APIs offer a variety of operations related to managing Sources, Folders, Orders and Recipes. There are operations to submit and track Jobs, upload and download data files and many more.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ExistingRecipe(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, created=None, creator=None):
        """
        ExistingRecipe - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'created': 'datetime',
            'creator': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'created': 'created',
            'creator': 'creator'
        }

        self._id = id
        self._name = name
        self._created = created
        self._creator = creator

    @property
    def id(self):
        """
        Gets the id of this ExistingRecipe.
        Unique ID of the recipe

        :return: The id of this ExistingRecipe.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExistingRecipe.
        Unique ID of the recipe

        :param id: The id of this ExistingRecipe.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if id is not None and len(id) > 36:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `36`")
        if id is not None and len(id) < 36:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `36`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ExistingRecipe.
        Name of the recipe

        :return: The name of this ExistingRecipe.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExistingRecipe.
        Name of the recipe

        :param name: The name of this ExistingRecipe.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this ExistingRecipe.
        ISO 8601 Date when the recipe has been created

        :return: The created of this ExistingRecipe.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ExistingRecipe.
        ISO 8601 Date when the recipe has been created

        :param created: The created of this ExistingRecipe.
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created

    @property
    def creator(self):
        """
        Gets the creator of this ExistingRecipe.
        User ID of the user who created the recipe

        :return: The creator of this ExistingRecipe.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this ExistingRecipe.
        User ID of the user who created the recipe

        :param creator: The creator of this ExistingRecipe.
        :type: str
        """
        if creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")
        if creator is not None and len(creator) > 36:
            raise ValueError("Invalid value for `creator`, length must be less than or equal to `36`")
        if creator is not None and len(creator) < 36:
            raise ValueError("Invalid value for `creator`, length must be greater than or equal to `36`")

        self._creator = creator

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
        if not isinstance(other, ExistingRecipe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
