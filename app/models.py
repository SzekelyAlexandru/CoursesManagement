from app import db


class Students(db.Model):
    __tablename__='Students'
    #!!!!!!! atentie aici
    id = db.Column(db.Integer,db.Sequence('Students_student_id_seq', start=1000, increment=1, minvalue=1000),primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), index=True)
    surname = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    year = db.Column(db.Integer, index=True)
    group = db.Column(db.String(64), index=True)
    profile = db.Column(db.String(64), index=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<Nume:  %r , %r>' % (self.name, self.surname)


class Professors(db.Model):
    __tablename__='Professors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True)
    surname = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<Nume:  %r , %r>' % (self.name, self.surname)

    def personal_subjects(self):
        return Professors.query.join(Subjects, Subjects.professor_id==Professors.id)


class Subjects(db.Model):
    __tablename__='Subjects'
    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('Professors.id'), index=True)
    name = db.Column(db.String(64), index=True)
    semester = db.Column(db.Integer, index=True)
    year = db.Column(db.Integer, index=True)


class Labs(db.Model):
    __tablename__='Labs'
    lab_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('Subjects.subject_id'), index=True)


class Tests(db.Model):
    __tablename__='Tests'
    test_id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('Subjects.subject_id'), index=True)


StudyContracts = db.Table('StudyContracts',
                          db.Column('student_id', db.Integer, db.ForeignKey('Students.id'), index=True),
                          db.Column('subject_id', db.Integer, db.ForeignKey('Subjects.subject_id'), index=True)
                          )

LabGrades = db.Table('LabGrades',
                     db.Column('lab_id', db.Integer, db.ForeignKey('Labs.lab_id'), index=True),
                     db.Column('student_id', db.Integer, db.ForeignKey('Students.id'), index=True),
                     db.Column('lab1', db.Integer),
                     db.Column('lab2', db.Integer),
                     db.Column('lab3', db.Integer),
                     db.Column('lab4', db.Integer),
                     db.Column('lab5', db.Integer),
                     db.Column('lab6', db.Integer),
                     db.Column('lab7', db.Integer),
                     db.Column('lab8', db.Integer),
                     db.Column('lab9', db.Integer),
                     db.Column('lab10', db.Integer),
                     db.Column('lab11', db.Integer),
                     db.Column('lab12', db.Integer),
                     db.Column('lab13', db.Integer),
                     db.Column('lab14', db.Integer),
                     db.Column('finalGrade', db.Integer)
                     )

TestGrades = db.Table('TestGrades',
                      db.Column('test_id', db.Integer, db.ForeignKey('Tests.test_id'), index=True),
                      db.Column('student_id', db.Integer, db.ForeignKey('Students.id'), index=True),
                      db.Column('grade', db.Integer)
                      )

TestAttendance = db.Table('TestAttendance',
                          db.Column('test_id', db.Integer, db.ForeignKey('Tests.test_id'), index=True),
                          db.Column('student_id', db.Integer, db.ForeignKey('Students.id'), index=True),
                          db.Column('confirmedStud', db.Boolean, index=True)
                          )

FinalGrades = db.Table('FinalGrades',
                       db.Column('subject_id', db.Integer, db.ForeignKey('Subjects.subject_id'), index=True),
                       db.Column('student_id', db.Integer, db.ForeignKey('Students.id'), index=True),
                       db.Column('grade', db.Integer, index=True)
                       )
