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


class Look(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, content_metadata_id=None, view_count=None, favorite_count=None, last_accessed_at=None, content_favorite_id=None, title=None, user=None, query_id=None, description=None, short_url=None, space=None, public=None, public_slug=None, user_id=None, space_id=None, model=None, public_url=None, embed_url=None, image_embed_url=None, google_spreadsheet_formula=None, excel_file_url=None, created_at=None, deleted_at=None, updated_at=None, last_updater_id=None, deleter_id=None, deleted=None, last_viewed_at=None, is_run_on_load=None, can=None):
        """
        Look - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'content_metadata_id': 'int',
            'view_count': 'int',
            'favorite_count': 'int',
            'last_accessed_at': 'datetime',
            'content_favorite_id': 'int',
            'title': 'str',
            'user': 'UserIdOnly',
            'query_id': 'int',
            'description': 'str',
            'short_url': 'str',
            'space': 'SpaceBase',
            'public': 'bool',
            'public_slug': 'str',
            'user_id': 'int',
            'space_id': 'str',
            'model': 'LookModel',
            'public_url': 'str',
            'embed_url': 'str',
            'image_embed_url': 'str',
            'google_spreadsheet_formula': 'str',
            'excel_file_url': 'str',
            'created_at': 'datetime',
            'deleted_at': 'datetime',
            'updated_at': 'datetime',
            'last_updater_id': 'int',
            'deleter_id': 'int',
            'deleted': 'bool',
            'last_viewed_at': 'datetime',
            'is_run_on_load': 'bool',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'content_metadata_id': 'content_metadata_id',
            'view_count': 'view_count',
            'favorite_count': 'favorite_count',
            'last_accessed_at': 'last_accessed_at',
            'content_favorite_id': 'content_favorite_id',
            'title': 'title',
            'user': 'user',
            'query_id': 'query_id',
            'description': 'description',
            'short_url': 'short_url',
            'space': 'space',
            'public': 'public',
            'public_slug': 'public_slug',
            'user_id': 'user_id',
            'space_id': 'space_id',
            'model': 'model',
            'public_url': 'public_url',
            'embed_url': 'embed_url',
            'image_embed_url': 'image_embed_url',
            'google_spreadsheet_formula': 'google_spreadsheet_formula',
            'excel_file_url': 'excel_file_url',
            'created_at': 'created_at',
            'deleted_at': 'deleted_at',
            'updated_at': 'updated_at',
            'last_updater_id': 'last_updater_id',
            'deleter_id': 'deleter_id',
            'deleted': 'deleted',
            'last_viewed_at': 'last_viewed_at',
            'is_run_on_load': 'is_run_on_load',
            'can': 'can'
        }

        self._id = id
        self._content_metadata_id = content_metadata_id
        self._view_count = view_count
        self._favorite_count = favorite_count
        self._last_accessed_at = last_accessed_at
        self._content_favorite_id = content_favorite_id
        self._title = title
        self._user = user
        self._query_id = query_id
        self._description = description
        self._short_url = short_url
        self._space = space
        self._public = public
        self._public_slug = public_slug
        self._user_id = user_id
        self._space_id = space_id
        self._model = model
        self._public_url = public_url
        self._embed_url = embed_url
        self._image_embed_url = image_embed_url
        self._google_spreadsheet_formula = google_spreadsheet_formula
        self._excel_file_url = excel_file_url
        self._created_at = created_at
        self._deleted_at = deleted_at
        self._updated_at = updated_at
        self._last_updater_id = last_updater_id
        self._deleter_id = deleter_id
        self._deleted = deleted
        self._last_viewed_at = last_viewed_at
        self._is_run_on_load = is_run_on_load
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this Look.
        Unique Id

        :return: The id of this Look.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Look.
        Unique Id

        :param id: The id of this Look.
        :type: int
        """

        self._id = id

    @property
    def content_metadata_id(self):
        """
        Gets the content_metadata_id of this Look.
        Id of content metadata

        :return: The content_metadata_id of this Look.
        :rtype: int
        """
        return self._content_metadata_id

    @content_metadata_id.setter
    def content_metadata_id(self, content_metadata_id):
        """
        Sets the content_metadata_id of this Look.
        Id of content metadata

        :param content_metadata_id: The content_metadata_id of this Look.
        :type: int
        """

        self._content_metadata_id = content_metadata_id

    @property
    def view_count(self):
        """
        Gets the view_count of this Look.
        Number of times viewed in the Looker web UI

        :return: The view_count of this Look.
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """
        Sets the view_count of this Look.
        Number of times viewed in the Looker web UI

        :param view_count: The view_count of this Look.
        :type: int
        """

        self._view_count = view_count

    @property
    def favorite_count(self):
        """
        Gets the favorite_count of this Look.
        Number of times favorited

        :return: The favorite_count of this Look.
        :rtype: int
        """
        return self._favorite_count

    @favorite_count.setter
    def favorite_count(self, favorite_count):
        """
        Sets the favorite_count of this Look.
        Number of times favorited

        :param favorite_count: The favorite_count of this Look.
        :type: int
        """

        self._favorite_count = favorite_count

    @property
    def last_accessed_at(self):
        """
        Gets the last_accessed_at of this Look.
        Time that the Look was last accessed by any user

        :return: The last_accessed_at of this Look.
        :rtype: datetime
        """
        return self._last_accessed_at

    @last_accessed_at.setter
    def last_accessed_at(self, last_accessed_at):
        """
        Sets the last_accessed_at of this Look.
        Time that the Look was last accessed by any user

        :param last_accessed_at: The last_accessed_at of this Look.
        :type: datetime
        """

        self._last_accessed_at = last_accessed_at

    @property
    def content_favorite_id(self):
        """
        Gets the content_favorite_id of this Look.
        Content Favorite Id

        :return: The content_favorite_id of this Look.
        :rtype: int
        """
        return self._content_favorite_id

    @content_favorite_id.setter
    def content_favorite_id(self, content_favorite_id):
        """
        Sets the content_favorite_id of this Look.
        Content Favorite Id

        :param content_favorite_id: The content_favorite_id of this Look.
        :type: int
        """

        self._content_favorite_id = content_favorite_id

    @property
    def title(self):
        """
        Gets the title of this Look.
        Look Title

        :return: The title of this Look.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Look.
        Look Title

        :param title: The title of this Look.
        :type: str
        """

        self._title = title

    @property
    def user(self):
        """
        Gets the user of this Look.
        User

        :return: The user of this Look.
        :rtype: UserIdOnly
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Look.
        User

        :param user: The user of this Look.
        :type: UserIdOnly
        """

        self._user = user

    @property
    def query_id(self):
        """
        Gets the query_id of this Look.
        Query Id

        :return: The query_id of this Look.
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """
        Sets the query_id of this Look.
        Query Id

        :param query_id: The query_id of this Look.
        :type: int
        """

        self._query_id = query_id

    @property
    def description(self):
        """
        Gets the description of this Look.
        Description

        :return: The description of this Look.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Look.
        Description

        :param description: The description of this Look.
        :type: str
        """

        self._description = description

    @property
    def short_url(self):
        """
        Gets the short_url of this Look.
        Short Url

        :return: The short_url of this Look.
        :rtype: str
        """
        return self._short_url

    @short_url.setter
    def short_url(self, short_url):
        """
        Sets the short_url of this Look.
        Short Url

        :param short_url: The short_url of this Look.
        :type: str
        """

        self._short_url = short_url

    @property
    def space(self):
        """
        Gets the space of this Look.
        Space of this Look

        :return: The space of this Look.
        :rtype: SpaceBase
        """
        return self._space

    @space.setter
    def space(self, space):
        """
        Sets the space of this Look.
        Space of this Look

        :param space: The space of this Look.
        :type: SpaceBase
        """

        self._space = space

    @property
    def public(self):
        """
        Gets the public of this Look.
        Is Public

        :return: The public of this Look.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this Look.
        Is Public

        :param public: The public of this Look.
        :type: bool
        """

        self._public = public

    @property
    def public_slug(self):
        """
        Gets the public_slug of this Look.
        Public Slug

        :return: The public_slug of this Look.
        :rtype: str
        """
        return self._public_slug

    @public_slug.setter
    def public_slug(self, public_slug):
        """
        Sets the public_slug of this Look.
        Public Slug

        :param public_slug: The public_slug of this Look.
        :type: str
        """

        self._public_slug = public_slug

    @property
    def user_id(self):
        """
        Gets the user_id of this Look.
        User Id

        :return: The user_id of this Look.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Look.
        User Id

        :param user_id: The user_id of this Look.
        :type: int
        """

        self._user_id = user_id

    @property
    def space_id(self):
        """
        Gets the space_id of this Look.
        Space Id

        :return: The space_id of this Look.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """
        Sets the space_id of this Look.
        Space Id

        :param space_id: The space_id of this Look.
        :type: str
        """

        self._space_id = space_id

    @property
    def model(self):
        """
        Gets the model of this Look.
        Model

        :return: The model of this Look.
        :rtype: LookModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this Look.
        Model

        :param model: The model of this Look.
        :type: LookModel
        """

        self._model = model

    @property
    def public_url(self):
        """
        Gets the public_url of this Look.
        Public Url

        :return: The public_url of this Look.
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """
        Sets the public_url of this Look.
        Public Url

        :param public_url: The public_url of this Look.
        :type: str
        """

        self._public_url = public_url

    @property
    def embed_url(self):
        """
        Gets the embed_url of this Look.
        Embed Url

        :return: The embed_url of this Look.
        :rtype: str
        """
        return self._embed_url

    @embed_url.setter
    def embed_url(self, embed_url):
        """
        Sets the embed_url of this Look.
        Embed Url

        :param embed_url: The embed_url of this Look.
        :type: str
        """

        self._embed_url = embed_url

    @property
    def image_embed_url(self):
        """
        Gets the image_embed_url of this Look.
        Image Embed Url

        :return: The image_embed_url of this Look.
        :rtype: str
        """
        return self._image_embed_url

    @image_embed_url.setter
    def image_embed_url(self, image_embed_url):
        """
        Sets the image_embed_url of this Look.
        Image Embed Url

        :param image_embed_url: The image_embed_url of this Look.
        :type: str
        """

        self._image_embed_url = image_embed_url

    @property
    def google_spreadsheet_formula(self):
        """
        Gets the google_spreadsheet_formula of this Look.
        Google Spreadsheet Formula

        :return: The google_spreadsheet_formula of this Look.
        :rtype: str
        """
        return self._google_spreadsheet_formula

    @google_spreadsheet_formula.setter
    def google_spreadsheet_formula(self, google_spreadsheet_formula):
        """
        Sets the google_spreadsheet_formula of this Look.
        Google Spreadsheet Formula

        :param google_spreadsheet_formula: The google_spreadsheet_formula of this Look.
        :type: str
        """

        self._google_spreadsheet_formula = google_spreadsheet_formula

    @property
    def excel_file_url(self):
        """
        Gets the excel_file_url of this Look.
        Excel File Url

        :return: The excel_file_url of this Look.
        :rtype: str
        """
        return self._excel_file_url

    @excel_file_url.setter
    def excel_file_url(self, excel_file_url):
        """
        Sets the excel_file_url of this Look.
        Excel File Url

        :param excel_file_url: The excel_file_url of this Look.
        :type: str
        """

        self._excel_file_url = excel_file_url

    @property
    def created_at(self):
        """
        Gets the created_at of this Look.
        Time that the Look was created.

        :return: The created_at of this Look.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Look.
        Time that the Look was created.

        :param created_at: The created_at of this Look.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """
        Gets the deleted_at of this Look.
        Time that the Look was deleted.

        :return: The deleted_at of this Look.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """
        Sets the deleted_at of this Look.
        Time that the Look was deleted.

        :param deleted_at: The deleted_at of this Look.
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Look.
        Time that the Look was updated.

        :return: The updated_at of this Look.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Look.
        Time that the Look was updated.

        :param updated_at: The updated_at of this Look.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def last_updater_id(self):
        """
        Gets the last_updater_id of this Look.
        Id of User that last updated the look.

        :return: The last_updater_id of this Look.
        :rtype: int
        """
        return self._last_updater_id

    @last_updater_id.setter
    def last_updater_id(self, last_updater_id):
        """
        Sets the last_updater_id of this Look.
        Id of User that last updated the look.

        :param last_updater_id: The last_updater_id of this Look.
        :type: int
        """

        self._last_updater_id = last_updater_id

    @property
    def deleter_id(self):
        """
        Gets the deleter_id of this Look.
        Id of User that deleted the look.

        :return: The deleter_id of this Look.
        :rtype: int
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """
        Sets the deleter_id of this Look.
        Id of User that deleted the look.

        :param deleter_id: The deleter_id of this Look.
        :type: int
        """

        self._deleter_id = deleter_id

    @property
    def deleted(self):
        """
        Gets the deleted of this Look.
        Whether or not a look is deleted.

        :return: The deleted of this Look.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this Look.
        Whether or not a look is deleted.

        :param deleted: The deleted of this Look.
        :type: bool
        """

        self._deleted = deleted

    @property
    def last_viewed_at(self):
        """
        Gets the last_viewed_at of this Look.
        Time last viewed in the Looker web UI

        :return: The last_viewed_at of this Look.
        :rtype: datetime
        """
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(self, last_viewed_at):
        """
        Sets the last_viewed_at of this Look.
        Time last viewed in the Looker web UI

        :param last_viewed_at: The last_viewed_at of this Look.
        :type: datetime
        """

        self._last_viewed_at = last_viewed_at

    @property
    def is_run_on_load(self):
        """
        Gets the is_run_on_load of this Look.
        auto-run query when Look viewed

        :return: The is_run_on_load of this Look.
        :rtype: bool
        """
        return self._is_run_on_load

    @is_run_on_load.setter
    def is_run_on_load(self, is_run_on_load):
        """
        Sets the is_run_on_load of this Look.
        auto-run query when Look viewed

        :param is_run_on_load: The is_run_on_load of this Look.
        :type: bool
        """

        self._is_run_on_load = is_run_on_load

    @property
    def can(self):
        """
        Gets the can of this Look.
        Operations the current user is able to perform on this object

        :return: The can of this Look.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Look.
        Operations the current user is able to perform on this object

        :param can: The can of this Look.
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
        if not isinstance(other, Look):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other