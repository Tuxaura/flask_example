from app import db, Puppy

##Create##
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

##Read##
all_puppies = Puppy.query.all()
print(all_puppies) #list of pupies objects in the table

##select##
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

##filters##
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

##update##
first_puppy = Puppy.query.get(1)
first_puppy.age = 22
db.session.add(first_puppy)
db.session.commit()


##delete##
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)