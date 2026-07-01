from pydantic import BaseModel, ConfigDict


class CourseBase(BaseModel):
    course_name: str
    course_code: str
    semester: int
    branch: str
    university: str


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    course_name: str | None = None
    course_code: str | None = None
    semester: int | None = None
    branch: str | None = None
    university: str | None = None


class CourseRead(CourseBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )