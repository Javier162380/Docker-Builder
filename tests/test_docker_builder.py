import pytest
from docker import APIClient
from docker_builder.builder import Builder
from rq.job import Job


def test_build_instance(TestBuilderNoRepository):
    assert TestBuilderNoRepository.build_instance.dockerfile == 'Dockerfile'
    assert TestBuilderNoRepository.build_instance.image_name == 'test'
    assert TestBuilderNoRepository.build_instance.tags == ['prod', 'latest']
    assert TestBuilderNoRepository.format_image_name == 'test'
    assert TestBuilderNoRepository.dockerfile_path == ''
    assert TestBuilderNoRepository.dockerfile_name == 'Dockerfile'


def test_build_instance_composition(TestBuilderNoRepository):
    assert isinstance(TestBuilderNoRepository.docker_instance, APIClient)
    assert isinstance(TestBuilderNoRepository.job, Job)


# def test_build_image(TestBuilderNoRepository, mocker):
#     mocker.patch.object(APIClient, 'build')

#     TestBuilderNoRepository.build_image()

#     APIClient.build.assert_called_once_with(path='',
#                                             dockerfile='Dockerfile',
#                                             tag='test',
#                                             buildargs={})


def test_execute(TestBuilderNoRepository, mocker):
    mocker.patch.object(Builder, 'build_image')
    mocker.patch.object(Builder, 'tag_image')
    mocker.patch.object(Builder, 'push_image')

    TestBuilderNoRepository.execute()

    assert Builder.build_image.call_count == 1
    assert Builder.tag_image.call_count == 0
    assert Builder.push_image.call_count == 0
