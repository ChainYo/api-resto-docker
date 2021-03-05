from cassandra.cluster import Cluster

class DB():

    @classmethod
    def open_con(cls):
        cls.cluster = Cluster(['cassandra-c01'], port=9042)

        cls.session = cls.cluster.connect('resto', wait_for_all_pools=True)
        cls.session.execute('USE resto')

    @classmethod
    def close_con(cls):
        cls.cluster.shutdown()

    @classmethod
    def find_resto_by_id(cls, resto_id):
        cls.open_con()
        data = cls.session.execute(f"SELECT * FROM restaurant WHERE id={resto_id}")
        dictionaire={}
        for element in data:
            dictionnaire={'id':element[0], 'borough':element[1], 'buildingnum':element[2],
             'cuisinetype':element[3], 'name':element[4], 'phone':element[5], 'street':element[6], 'zipcode':element[7]}

        cls.close_con()
        return dictionnaire

    @classmethod
    def find_resto_by_type(cls, resto_type):
        cls.open_con()
        data = cls.session.execute(f"SELECT * FROM restaurant WHERE cuisinetype='{resto_type}'")
        liste=[]
        for element in data:
            dictionnaire={'id':element[0], 'borough':element[1], 'buildingnum':element[2],
             'cuisinetype':element[3], 'name':element[4], 'phone':element[5], 'street':element[6], 'zipcode':element[7]}
            liste.append(dictionnaire)
        dataReturn={'data':liste}
        cls.close_con()
        return dataReturn

    @classmethod
    def find_top_grade(cls, grade):
        cls.open_con()
        data = cls.session.execute(f"SELECT * FROM inspection WHERE grade='{grade}'")
        listeId=[]
        for element in data:
            listeId.append(element[0])

        liste=[]
        for id in listeId[:10]:
            resto=cls.find_resto_by_id(id)
            liste.append(resto)
        dataReturn={'data':liste}
        cls.close_con()
        return dataReturn

    @classmethod
    def find_nb_inspect(cls, resto_id):
        cls.open_con()
        data = cls.session.execute(f"SELECT * FROM inspection WHERE idrestaurant={resto_id}")
        liste=[]
        for element in data:
            liste.append(element)
        cls.close_con()
        dataReturn={'data':{f"nombre d'inspection du restaurant {resto_id}":len(liste)}}
        return dataReturn


