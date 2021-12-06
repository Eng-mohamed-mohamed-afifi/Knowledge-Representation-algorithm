[1]from logic import *
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge = And(
 (carrots,orange)
)
print(knowledge.formula())

#the English mean is [carrots color is orange]
-------------------------------------------------------------------------------------------
[2]from logic import *
Person = Symbol("Person")
carrots = Symbol("carrots")
knowledge = And(
 Implication(carrots,Person),
    (carrots,vegetarian),
    vegetarian
    
)
print(model_check(knowledge, carrots))
print(knowledge.formula())

#the English mean is [person likes carrot then if person is vegetarian]
-------------------------------------------------------------------------------------------
[3]from logic import *
student = Symbol("student")
study=symbol("study_hard")
knowledge = And(
 Implication(student, study_hard),
    (study_hard,pass),
    pass
    
)
print(model_check(knowledge, study))
print(knowledge.formula())

#the English mean is [if student study hard then he will pass]
-------------------------------------------------------------------------------------------
[4]from logic import *
student = Symbol("student")
study=symbol("study_hard")
knowledge = And(
 Implication(student, study_hard),
    (study_hard,pass),
    pass
    
)
print(model_check(knowledge, study))
print(knowledge.formula())

#the English mean is [who will pass?]
-------------------------------------------------------------------------------------------
[5]from logic import *
professor = Symbol("professor")
Course=symbol("Course")
knowledge = And(
 Implication(Course, professor),
    
)
print(knowledge.formula())

#the English mean is [which course professor teachecs?]
-------------------------------------------------------------------------------------------
[6]from logic import *
x= Symbol("x")
y=symbol("y")
knowledge = And(
 Implication(x, y),
	
    
)
print(knowledge.formula())

#the English mean is [if x and y are enemies then x hates y then y,x fight]
-------------------------------------------------------------------------------------------
[7]from logic import *
x= Symbol("x")
y=symbol("y")
knowledge = And(
 Implication(x, y),
	
    
)
print(knowledge.formula())

#the English mean is [if x and y are enemies then x hates y then y,x fight]
-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------
