DEBUG = 0


class VectorEntry():
    def __init__(self, page_content, metadata={}):
        # Example: page_content='The loaded git repo name is myrepo'
        self.page_content = page_content
        #  Example: metadata={'source': 'path/to/file.py',
        # 'file_path': 'path/to/file.py', 'file_name': 'file.py',
        # 'file_type': '.py'}
        self.metadata = metadata


def std_response():
    response = {
        "error": False,
        "content": "",
    }
    return response
