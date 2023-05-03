## Task 3

This lab features usage of functions and classes in phyton.

First task was to create function that calculates average of
set of numbers. Numbers should be sent to the function both and as
positioned arguments which are separated with commas and as iterables
(e.g. list, set, tuple). Script average calc shows `average_calc()`
function in action. Function calculates average of 1, 2, 3 and 4.

```
[vit@vm task03]$ python3 average_calc.py 
Average of positioned arguments only: 2.5

Average of positioned and iterated arguments: 2.5

Average of iterated arguments only: 2.5

[vit@vm task03]$ 
```

Second task was modification of classes in module `animal.py`.
The modification were:
- addition of two "private" atributes `race` and `sex` to class `Human`;
- enhancement of class `Person` by insertion of two atributes `name` and `age`;
- addition of two new classes `Vaccine` and `Chip`

Example illustraring usage of ebove mentioned classes is showm below:

```
>>> 
>>> 
>>> from animal import *
>>> 
>>> me = Person('male', 'white', 'Bob', '22')
>>> dog = (me, Vaccine('vac1'), Chip(1234))
>>> me
Person(name='Bob', age='22')
>>> dog
(Person(name='Bob', age='22'), Vaccine(id_num=('vac1',)), Chip(id_num=1234))
>>> me.name('Mike')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> me.name = 'Mike'
>>> me
Person(name='Mike', age='22')
>>> dog
(Person(name='Mike', age='22'), Vaccine(vac_list=('vac1',)), Chip(id_num=1234))
>>> dog.vaccine
Vaccine(vac_list=('vac1',))
>>> dog.chip
Chip(id_num=1234)
>>> dog.owner
Person(name='Mike', age=22)
>>> 
```

Third task is about to create own classs. Module `entities.py` introduces
classes that represent behaviour of entities and player in game engine.
Example:

```
>>> from entities import *
>>> e = Entity('bob', [10,20,30])
>>> e.update(1,1,1)
"bob's position was updated"
>>> e.position
[11, 21, 31]
>>> 
>>> p = Player('mike', [0,0,0], 20)
>>> 
>>> p.update(2,-3,4,10)
'mike now has 30 health.'
>>> p.position
[2, -3, 4]
>>> p.health
30
>>> 
```
