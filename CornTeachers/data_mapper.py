from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import models

class TeacherDataMapper():
    def __init__(self):       
        engine = create_engine('postgresql://scott:tiger@localhost/')

        # создание конфигурации класса Session
        Session = sessionmaker(bind=engine)

        # создание объекта Session        
        self.session =Session()
    
    def get_teacher_by_name(self, teacher_name):
        try:
            return self.session.query(models.Teacher).filter(models.Teacher.fullname == teacher_name).one_or_none()
        except Exception as e:
            return e

    def get_teachers(self):
        try:
            return self.session.query(models.Teacher).one_or_none()
        except e:
            return e

    def insert_clas(self, clas):
        try:
            self.session.add(clas)
            self.session.commit()

            
        except Exception as e:
            return e

    def get_classes_by_teacher(self, teacher_id):
        try:
            return self.session.query(models.Learningactivity).filter(models.Learningactivity.Teacher.idteacher == teacher_id).one_or_none()
           
        except Exception as e:
            return e


    def get_learningactivities_by_teacher(self, teacher_id):
        try:
            return self.session.query(models.Learningactivity).filter(
                models.Learningactivity.Teacher.idteacher == teacher_id).one_or_none()

        except Exception as e:
            return e