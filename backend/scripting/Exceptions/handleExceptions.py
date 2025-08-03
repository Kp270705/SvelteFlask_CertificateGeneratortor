
class CertificateError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        # print(f"in certificate error...")
