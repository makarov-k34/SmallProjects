# coding: utf-8
from sqlalchemy import Column, ForeignKey, SmallInteger, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Clas(Base):
    __tablename__ = 'class'

    name = Column(String(15))
    idclass = Column(SmallInteger, primary_key=True)


class Subject(Base):
    __tablename__ = 'subject'

    idsubject = Column(SmallInteger, primary_key=True)
    name = Column(String(20))


class Teacher(Base):
    __tablename__ = 'teacher'

    fullname = Column(String(20))
    qualification = Column(String(20))
    idteacher = Column(SmallInteger, primary_key=True)


class Learningactivity(Base):
    __tablename__ = 'learningactivities'

    idclass = Column(ForeignKey('class.idclass'), primary_key=True, nullable=False)
    idtechaer = Column(ForeignKey('teacher.idteacher'), primary_key=True, nullable=False)
    idsubject = Column(ForeignKey('subject.idsubject'), primary_key=True, nullable=False)

    clas = relationship('Clas')
    subject = relationship('Subject')
    teacher = relationship('Teacher')
