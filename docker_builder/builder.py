import os

import docker


class Builder:

    def __init__(self, build_instance):

        self.build_instance = build_instance
        self.docker_instance = docker.APIClient()

    @property
    def format_image_name(self):
        return f"{self.build_instance.image_name}/{':'.join(self.build_instance.tags)}"

    @property
    def dockerfile_path(self):
        path, dockerfile = os.path.split(self.build_instance.dockerfile)

        if dockerfile == '':
            return './'

        return path

    @property
    def dockerfile_name(self):
        path, dockerfile = os.path.split(self.build_instance.dockerfile)

        if dockerfile == '':
            return path

        return dockerfile

    def build_image(self):
        return [output for output in self.docker_instance.build(
            path=self.dockerfile_path,
            dockerfile=self.dockerfile_name,
            tag=self.format_image_name,
            buildargs=self.build_instance.args if self.build_instance.args else {}
        )]

    def execute(self):

        self.build_image()
