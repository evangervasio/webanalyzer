import similar

class SimilarApi:
    def __init__(self, website):
        self.website = website

    def call_api_once(self):
        response = similar.similarGet(self.website)
        return response
