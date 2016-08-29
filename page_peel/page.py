import os.path
import itertools
import pkgutil

import lxml.html

import confeitaria.server
import confeitaria.interfaces


class ServingPage(confeitaria.interfaces.Page):

    def __init__(self, store):
        self.store = store

    def index(self, edit=False):
        request = self.get_request()

        try:
            path = os.path.join(*request.path_args)
        except TypeError:
            path = ''

        content = self.store.read(path)

        if edit:
            editor_content = self.store.read('editor.html')

            editor_doc = lxml.html.fromstring(editor_content)

            textarea = editor_doc.find_class('doc-content')
            if len(textarea) < 1:
                raise NoElement(
                    'Element textarea with class doc-content not found')

            textarea[0].value = content

            content = lxml.html.tostring(editor_doc)

        return content

    def action(self, content=None):
        request = self.get_request()

        try:
            path = os.path.join(*request.path_args)
        except TypeError:
            path = ''

        self.store.write(path, content)

class Store(object):

    def __init__(self, root_dir, package):
        self.root_dir = root_dir
        self.package = package

    def read(self, path):
        try:
            content = get_content_from_fs(self.root_dir, path)
        except IOError:
            content = get_content_from_package(self.package, path)

        return content

    def write(self, path, content):
        write_content_to_fs(self.root_dir, path, content)

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

def write_content_to_fs(root_dir, path, content, default_file='index.html'):
    fs_path = os.path.join(root_dir, path)

    if os.path.exists(fs_path) and os.path.isdir(fs_path):
        fs_path = os.path.join(fs_path, default_file)

    with open(fs_path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    store = Store(root_dir='/home/adam/sandbox', package=__name__)
    page = ServingPage(store=store)

    confeitaria.server.Server(page).run()
