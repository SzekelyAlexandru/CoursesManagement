from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
student = Table('student', pre_meta,
    Column('idStudent', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('surname', VARCHAR(length=64)),
    Column('username', VARCHAR(length=64)),
    Column('password', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('year', INTEGER),
    Column('group', VARCHAR(length=64)),
    Column('profile', VARCHAR(length=64)),
)

LabGrades = Table('LabGrades', post_meta,
    Column('lab_id', Integer),
    Column('student_id', Integer),
    Column('lab1', Integer),
    Column('lab2', Integer),
    Column('lab3', Integer),
    Column('lab4', Integer),
    Column('lab5', Integer),
    Column('lab6', Integer),
    Column('lab7', Integer),
    Column('lab8', Integer),
    Column('lab9', Integer),
    Column('lab10', Integer),
    Column('lab11', Integer),
    Column('lab12', Integer),
    Column('lab13', Integer),
    Column('lab14', Integer),
    Column('finalGrade', Integer),
)

StudyContracts = Table('StudyContracts', post_meta,
    Column('student_id', Integer),
    Column('subject_id', Integer),
)

TestAttendance = Table('TestAttendance', post_meta,
    Column('test_id', Integer),
    Column('student_id', Integer),
    Column('confirmedStud', Boolean),
)

TestGrades = Table('TestGrades', post_meta,
    Column('test_id', Integer),
    Column('student_id', Integer),
    Column('grade', Integer),
)

labs = Table('labs', post_meta,
    Column('lab_id', Integer, primary_key=True, nullable=False),
    Column('subject_id', Integer),
)

professors = Table('professors', post_meta,
    Column('professor_id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('surname', String(length=64)),
    Column('username', String(length=64)),
    Column('password', String(length=64)),
    Column('email', String(length=120)),
)

students = Table('students', post_meta,
    Column('student_id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('surname', String(length=64)),
    Column('username', String(length=64)),
    Column('password', String(length=64)),
    Column('email', String(length=120)),
    Column('year', Integer),
    Column('group', String(length=64)),
    Column('profile', String(length=64)),
)

subjects = Table('subjects', post_meta,
    Column('subject_id', Integer, primary_key=True, nullable=False),
    Column('professor_id', Integer),
    Column('name', String(length=64)),
    Column('semester', Integer),
    Column('year', Integer),
)

tests = Table('tests', post_meta,
    Column('test_id', Integer, primary_key=True, nullable=False),
    Column('subject_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['student'].drop()
    post_meta.tables['LabGrades'].create()
    post_meta.tables['StudyContracts'].create()
    post_meta.tables['TestAttendance'].create()
    post_meta.tables['TestGrades'].create()
    post_meta.tables['labs'].create()
    post_meta.tables['professors'].create()
    post_meta.tables['students'].create()
    post_meta.tables['subjects'].create()
    post_meta.tables['tests'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['student'].create()
    post_meta.tables['LabGrades'].drop()
    post_meta.tables['StudyContracts'].drop()
    post_meta.tables['TestAttendance'].drop()
    post_meta.tables['TestGrades'].drop()
    post_meta.tables['labs'].drop()
    post_meta.tables['professors'].drop()
    post_meta.tables['students'].drop()
    post_meta.tables['subjects'].drop()
    post_meta.tables['tests'].drop()
