from pyramid.httpexceptions import HTTPForbidden
from pyramid.view import view_config

from cornice import Service


import serialization_schema_validators
from data_mapper import *

import json

teaсher_info = Service(name='teaсhers',
                    path='/teaсhers/{teachername}',
                    description='Get and set teaсher data.')


@teaсher_info.get()
def get_teaсhers(request):
    """Returns the public information about a **teaсher**.

    If the teaсher does not exists, returns an empty dataset.
    """
    dataMapper = TeacherDataMapper()
    teachername = request.matchdict['teachername']
    teacher= dataMapper.get_teacher_by_name(teachername)

    teacher_json = json.dumps(teacher)
    return {'success': True, 'teacher':teacher_json}


class_op = Service(name='class',
                    path='/class',
                    description='Set class data.')

@class_op.post()
def set_class(request):
    """sets the new class data into database returns true if success otherwise false"""

    new_class_data = request.json_body #!!!
    dataMapper = TeacherDataMapper()
    class_validator_schema = serialization_schema_validators.ValidationPutClass()

    try:
        new_class = class_validator_schema.deserialize(new_class_data)
        dataMapper.insert_clas(new_class)

    except Exception as e:
        return {'success': False, 'errors':e}

    return {'success': True}



learning_activities_info = Service(name='learning_activities',
                    path='/learning_activities/{teacherId}',
                    description='Get and set teaсher data.')

@learning_activities_info.get()
def get_learning_activities(request):
    """Returns the information about learning activities."""
    try:
        teacherId = int(request.matchdict['teacherId'])
    except ValueError:
        return {'success': False, 'errors': 'неверное значение teacherId'}

    dataMapper = TeacherDataMapper()
    activities= dataMapper.get_learningactivities_by_teacher(teacherId)

    activities_json = json.dumps(activities)
    return {'success': True, 'activities':activities_json}


