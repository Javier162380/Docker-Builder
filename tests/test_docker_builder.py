import pytest
from docker import APIClient
from docker_builder.builder import Builder


def test_build_instance(TestBuilder):
    assert TestBuilder.build_instance.dockerfile == 'Dockerfile'
    assert TestBuilder.build_instance.image_name == 'test'
    assert TestBuilder.build_instance.tags == ['prod', 'latest']
    assert TestBuilder.format_image_name == 'test/prod:latest'
    assert TestBuilder.dockerfile_path == ''
    assert TestBuilder.dockerfile_name == 'Dockerfile'


def test_build_instance_composition(TestBuilder):
    assert isinstance(TestBuilder.docker_instance, APIClient)


def test_build_image(TestBuilder, mocker):
    mocker.patch.object(APIClient, 'build')

    TestBuilder.build_image()

    APIClient.build.assert_called_once_with(path='',
                                            dockerfile='Dockerfile',
                                            tag='test/prod:latest',
                                            buildargs={})


def test_execute(TestBuilder, mocker):
    mocker.patch.object(Builder, 'build_image')

    TestBuilder.execute()

    assert Builder.build_image.call_count == 1
