# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [View Changelog](/app/apiChangelog)    #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ##### Swagger Specification  [⇩ Download Swagger JSON](swagger.json)    ## All API Endpoints  Click to expand a section. 

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Transaction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'transact_id': 'str',
        'account': 'float',
        'currency': 'str',
        'transact_type': 'str',
        'amount': 'float',
        'fee': 'float',
        'transact_status': 'str',
        'address': 'str',
        'tx': 'str',
        'text': 'str',
        'transact_time': 'datetime',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'transact_id': 'transactID',
        'account': 'account',
        'currency': 'currency',
        'transact_type': 'transactType',
        'amount': 'amount',
        'fee': 'fee',
        'transact_status': 'transactStatus',
        'address': 'address',
        'tx': 'tx',
        'text': 'text',
        'transact_time': 'transactTime',
        'timestamp': 'timestamp'
    }

    def __init__(self, transact_id=None, account=None, currency=None, transact_type=None, amount=None, fee=None, transact_status=None, address=None, tx=None, text=None, transact_time=None, timestamp=None):
        """
        Transaction - a model defined in Swagger
        """

        self._transact_id = None
        self._account = None
        self._currency = None
        self._transact_type = None
        self._amount = None
        self._fee = None
        self._transact_status = None
        self._address = None
        self._tx = None
        self._text = None
        self._transact_time = None
        self._timestamp = None
        self.discriminator = None

        self.transact_id = transact_id
        if account is not None:
          self.account = account
        if currency is not None:
          self.currency = currency
        if transact_type is not None:
          self.transact_type = transact_type
        if amount is not None:
          self.amount = amount
        if fee is not None:
          self.fee = fee
        if transact_status is not None:
          self.transact_status = transact_status
        if address is not None:
          self.address = address
        if tx is not None:
          self.tx = tx
        if text is not None:
          self.text = text
        if transact_time is not None:
          self.transact_time = transact_time
        if timestamp is not None:
          self.timestamp = timestamp

    @property
    def transact_id(self):
        """
        Gets the transact_id of this Transaction.

        :return: The transact_id of this Transaction.
        :rtype: str
        """
        return self._transact_id

    @transact_id.setter
    def transact_id(self, transact_id):
        """
        Sets the transact_id of this Transaction.

        :param transact_id: The transact_id of this Transaction.
        :type: str
        """
        if transact_id is None:
            raise ValueError("Invalid value for `transact_id`, must not be `None`")

        self._transact_id = transact_id

    @property
    def account(self):
        """
        Gets the account of this Transaction.

        :return: The account of this Transaction.
        :rtype: float
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this Transaction.

        :param account: The account of this Transaction.
        :type: float
        """

        self._account = account

    @property
    def currency(self):
        """
        Gets the currency of this Transaction.

        :return: The currency of this Transaction.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Transaction.

        :param currency: The currency of this Transaction.
        :type: str
        """

        self._currency = currency

    @property
    def transact_type(self):
        """
        Gets the transact_type of this Transaction.

        :return: The transact_type of this Transaction.
        :rtype: str
        """
        return self._transact_type

    @transact_type.setter
    def transact_type(self, transact_type):
        """
        Sets the transact_type of this Transaction.

        :param transact_type: The transact_type of this Transaction.
        :type: str
        """

        self._transact_type = transact_type

    @property
    def amount(self):
        """
        Gets the amount of this Transaction.

        :return: The amount of this Transaction.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Transaction.

        :param amount: The amount of this Transaction.
        :type: float
        """

        self._amount = amount

    @property
    def fee(self):
        """
        Gets the fee of this Transaction.

        :return: The fee of this Transaction.
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """
        Sets the fee of this Transaction.

        :param fee: The fee of this Transaction.
        :type: float
        """

        self._fee = fee

    @property
    def transact_status(self):
        """
        Gets the transact_status of this Transaction.

        :return: The transact_status of this Transaction.
        :rtype: str
        """
        return self._transact_status

    @transact_status.setter
    def transact_status(self, transact_status):
        """
        Sets the transact_status of this Transaction.

        :param transact_status: The transact_status of this Transaction.
        :type: str
        """

        self._transact_status = transact_status

    @property
    def address(self):
        """
        Gets the address of this Transaction.

        :return: The address of this Transaction.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Transaction.

        :param address: The address of this Transaction.
        :type: str
        """

        self._address = address

    @property
    def tx(self):
        """
        Gets the tx of this Transaction.

        :return: The tx of this Transaction.
        :rtype: str
        """
        return self._tx

    @tx.setter
    def tx(self, tx):
        """
        Sets the tx of this Transaction.

        :param tx: The tx of this Transaction.
        :type: str
        """

        self._tx = tx

    @property
    def text(self):
        """
        Gets the text of this Transaction.

        :return: The text of this Transaction.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Transaction.

        :param text: The text of this Transaction.
        :type: str
        """

        self._text = text

    @property
    def transact_time(self):
        """
        Gets the transact_time of this Transaction.

        :return: The transact_time of this Transaction.
        :rtype: datetime
        """
        return self._transact_time

    @transact_time.setter
    def transact_time(self, transact_time):
        """
        Sets the transact_time of this Transaction.

        :param transact_time: The transact_time of this Transaction.
        :type: datetime
        """

        self._transact_time = transact_time

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Transaction.

        :return: The timestamp of this Transaction.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Transaction.

        :param timestamp: The timestamp of this Transaction.
        :type: datetime
        """

        self._timestamp = timestamp

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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other