import json
import logging
from typing_extensions import Annotated, TypedDict
from langchain_core.tools import tool
from datetime import datetime, timedelta
import _3_db_service as db_service


class get_student_data(TypedDict):
    """get student details"""
    @staticmethod
    @tool
    def run():
        """get student details"""
        print("called")
        return db_service.get_student_data()

class add_student_data(TypedDict):
    """Add student details with student name and course"""

    name: Annotated[str, ..., "Student name"]
    course: Annotated[str, ..., "course name"]

    @staticmethod
    @tool
    def run(name: str, course: str):
        """Add student details with student name and course"""
        return db_service.add_student_data(name, course)

# NOTE: Update this list as more tool_calling feature need.
tools = [
    get_student_data,
    add_student_data,
]


def get_tool_desc():
    return {tool.__name__.lower(): tool.run for tool in tools}

