from flask import Blueprint
from core.models.teachers import Teacher
from core.apis import decorators
from core.apis.responses import APIResponse
from .schema import TeacherSchema

principal_resources= Blueprint('principal_resources', __name__)

@principal_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal

def get_teachers(p):
    """Get all teachers"""
    teachers = Teacher.get_teachers()
    all_teacher_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=all_teacher_dump)