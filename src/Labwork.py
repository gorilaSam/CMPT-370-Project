from Image import Image


class LabTest:
    """
    Contains data for a singular lab test.
    """

    def __init__(self):
        """
        Default Constructor.
        Initializes result as an empty result.
        """
        self.test = {
            'result': LabResult(),
            'request': LabRequest()
        }

    def make_request(self, request):
        """
        Sets the data for the lab test's request form.
        :param request: A JSON converted to a dictionary.
        """
        self.test['request'] = LabRequest(request['sender'], request['recipient'], request['patient_ID'],
                                          request['details'])

    def get_request(self):
        """
        :return: The request as a string.
        """
        return self.test['request'].get_request()

    # TODO: Figure out how to host images on our server.
    def enter_results(self, result, images):
        """
        Sets the data for the lab test's result form.
        :param result: A string representing the text results of the test (i.e. bloodwork did not contain marijuana)
        :param images: A list containing some sort of representation of our images.
        """
        self.test['result'].set_result(result)
        self.test['result'].set_images(images)

    def get_results(self):
        """
        :return: Tuple of text results, list of images.
        """
        return self.test['result'].get_results()


class LabRequest:
    """
    Container for a singular lab request form associated with a lab test.
    """

    def __init__(self, sender='', recipient='', patient_ID=0, details=''):
        """
        Default Constructor.
        :param sender: ID of medical professional.
        :param recipient: ID of lab technician.
        :param patient_ID: ID of patient.
        :param details: Description of request (date, type of request)
        """
        self.request = {
            'requested_by': sender,
            'sent_to': recipient,
            'patient_ID': patient_ID,
            'details': details
        }

    def set_request(self, details):
        """
        Sets the details line of the form (dates, type of request)
        :param details: Description of request (date, type of request)
        """
        self.request['details'] = details

    # TODO: Figure out how we're going to display it on the React side.
    def get_request(self):
        """
        :return: Information on the request as a string.
        """
        request = "sent by: " + self.request['requested_by'] \
                  + ", sent to: " + self.request['sent_to'] \
                  + ", patient ID: " + str(self.request['patient_ID']) \
                  + ", details: " + self.request['details']
        return request


class LabResult:
    """
    Container for a lab result associated with a lab test.
    """

    def __init__(self, result="", images=None):
        """
        Default Constructor.
        :param result: The text body of the result.
        :param images: A list of images associated with the result.
        """

        self.result = {
            'result': result,
            'images': images
        }

        if images is None:
            self.result['images'] = []

    def set_result(self, result):
        """
        Sets the text body of the result.
        :param result: String representing the result.
        """
        self.result['result'] = result

    def get_result(self):
        """
        :return: Text body of the result.
        """
        return self.result['result']

    # TODO: Figure out how to store images on a server.
    def set_images(self, images):
        """
        Sets the list of images of the result.
        :param images: List of images.
        """
        self.result['images'] = images

    # TODO: Figure out how to store images on a server.
    def get_images(self):
        """
        :return: List of images associated with the result.
        """
        return self.result['images']

    def get_results(self):
        """
        :return: A tuple containing first the text body of the result and then the images associated with the result.
        """
        return self.get_result(), self.get_images()
