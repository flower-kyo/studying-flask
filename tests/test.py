import unittest
from upload_dowload import app
from io import BytesIO
import os
import warnings


class TestUpDownLoad(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True

        # 测试客户端
        self.client = app.test_client()

    def tearDown(self):
        # 清除文件
        if os.path.exists('../my_files/mocked_name_file'):
            os.remove('../my_files/mocked_name_file')

    def test_upload(self):
        """模拟场景1： 提交文件"""
        files = {'file': BytesIO(b"post-data")}
        params = {name: (f, "mocked_name_{}".format(name)) for name, f in files.items()}
        res = self.client.post('/', data=params, content_type='multipart/form-data')
        assert res.status_code == 200
        assert 'mocked_name_' in res.data.decode()

    def test_upload(self):
        """场景2： 下载文件"""
        warnings.simplefilter("ignore", ResourceWarning)
        res = self.client.get('/download/testfile.txt')
        assert res.status_code == 200


if __name__ == '__main__':
    unittest.main()