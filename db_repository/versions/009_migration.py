from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Students = Table('Students', pre_meta,
    Column('student_id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('surname', VARCHAR(length=64)),
    Column('username', VARCHAR(length=64)),
    Column('password', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('year', INTEGER),
    Column('group', VARCHAR(length=64)),
    Column('profile', VARCHAR(length=64)),
)

Students = Table('Students', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('surname', String(length=64)),
    Column('username', String(length=64)),
    Column('password', String(length=64)),
    Column('email', String(length=120)),
    Column('year', Integer),
    Column('group', String(length=64)),
    Column('profile', String(length=64)),
)

Professors = Table('Professors', pre_meta,
    Column('professor_id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('surname', VARCHAR(length=64)),
    Column('username', VARCHAR(length=64)),
    Column('password', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

Professors = Table('Professors', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('surname', String(length=64)),
    Column('username', String(length=64)),
    Column('password', String(length=64)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Students'].columns['student_id'].drop()
    post_meta.tables['Students'].columns['id'].create()
    pre_meta.tables['Professors'].columns['professor_id'].drop()
    post_meta.tables['Professors'].columns['id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Students'].columns['student_id'].create()
    post_meta.tables['Students'].columns['id'].drop()
    pre_meta.tables['Professors'].columns['professor_id'].create()
    post_meta.tables['Professors'].columns['id'].drop()
