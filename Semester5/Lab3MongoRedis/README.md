# Lab2Mongo
Sakharchuk Taras, KP-41
###Завдання:

1. Розробити схему бази даних на основі предметної галузі з ЛР№2-Ч1 у
спосіб, що застосовується в СУБД MongoDB.
2. Розробити модуль роботи з базою даних на основі пакету PyMongo.
3. Реалізувати дві операції на вибір із використанням паралельної обробки
даних Map/Reduce.
4. Реалізувати обчислення та виведення результату складного агрегативного
запиту до бази даних з використанням функції aggregate() сервера
MongoDB.

### Приклади коду
* Агрегація

```Python
    pipeline = [{"$unwind": "$diagnosis"},
                {"$group": {"_id": "$diagnosis", "count": {"$sum": 1}}},
                {"$sort": SON([("count", -1), ("_id", -1)])}]
    lst = list(db.surveys.aggregate(pipeline))
```

* MapReduce

```Python
    mapper = Code(
        """
        function(){
          emit(this.hospital.name, 1);
        }
        """)
    reducer = Code(
        """
          function(key, values){
            return values.length;
          };
        """)
    result = db.doctors.map_reduce(mapper, reducer, "myresults")
```