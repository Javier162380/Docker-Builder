import os
from typing import List, Dict

import docker
import logging
from rq.job import Job
from worker import conn


class Builder:

    def __init__(self, build_instance, job_id):

        self.build_instance = build_instance
        self.docker_instance = docker.APIClient()
        self.job = Job(job_id, conn)

    @property
    def format_image_name(self):
        build_repository = (f"{self.build_instance.image_registry}/"
                            if self.build_instance.image_registry else '')
        return f"{build_repository}{self.build_instance.image_name}"

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

    def update_job_stream(self, message: List[dict]):

        if self.job.meta == {}:
            self.job.meta = [message]
        else:
            self.job.meta = self.job.meta + message

        self.job.save_meta()

    def build_image(self):

        generator_object = self.docker_instance.build(
                path=self.dockerfile_path, dockerfile=self.dockerfile_name, tag=self.build_instance.image_name,
                buildargs=self.build_instance.args if self.build_instance.args else {},
                decode=True)

        for stream in generator_object:
            yield stream

    def tag_image(self, tag):
        
        return self.docker_instance.tag(self.build_instance.image_name, self.format_image_name, tag=tag)

    def push_image(self, tag):
        generator_object =  self.docker_instance.push(
                self.format_image_name, tag=tag, stream=True, decode=True)

        for stream in generator_object:
            yield stream

    def execute(self):

        ##Building Image.
        self.update_job_stream([{'stream':f'Building docker image params {self.build_instance}'}])
        for stream in self.build_image():
           self.update_job_stream([stream])

        ## Pushing and tagging images
        if self.build_instance.image_registry:
            self.update_job_stream([{'stream': f'Docker Image build pushing to {self.format_image_name}'}])
            for tag in self.build_instance.tags:
                tagged_image = self.tag_image(tag)
                if tagged_image:
                    for stream in self.push_image(tag):
                        self.update_job_stream([stream])
                else:
                    self.update_job_stream([{'stream': f'Unabled to tag image {self.build_instance.format_image_name} with tag {tag}'}])
                self.update_job_stream([{'stream': f'Docker Image successfully push to {self.format_image_name}:{tag}'}])
