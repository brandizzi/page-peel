import os.path
import itertools
import pkgutil

import confeitaria.server
import confeitaria.interfaces


class ServingPage(confeitaria.interfaces.Page):

    def __init__(self, root_dir):
        self.root_dir = root_dir

    def index(self):
        request = self.get_request()
        try:
            path = os.path.join(*request.path_args)
        except TypeError:
            path = ''

        try:
            content = get_content_from_fs(self.root_dir, path)
        except IOError:
            content = get_content_from_package(__name__, path)

        return content

def get_content_from_fs(root_dir, path, default_file='index.html'):
    fs_path = os.path.join(root_dir, path)

    if os.path.exists(fs_path) and os.path.isdir(fs_path):
        fs_path = os.path.join(fs_path, default_file)

    return open(fs_path).read()

def get_content_from_package(
        package_name, path, template_dir='template',
        default_file='index.html'):

    try:
        content = pkgutil.get_data(
            package_name, os.path.join(template_dir, path))
    except IOError:
        content = pkgutil.get_data(
            package_name, os.path.join(template_dir, path, 'index.html'))    

    return content

if __name__ == '__main__':
    page = ServingPage(root_dir='/home/adam/sandbox')
    confeitaria.server.Server(page).run()
