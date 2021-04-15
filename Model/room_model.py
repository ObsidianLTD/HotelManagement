from sqlalchemy.orm import sessionmaker
from Domain.rooms import Rooms

room_type = ["Double room", "Superior Double room", "Deluxe Double room", "Suite", "Deluxe suite", "Presidential Suite"]


class RoomsSQLModel:

    def __init__(self, engine):
        self.__engine = engine
        self.__my_session = sessionmaker(bind=engine)()

    def create_room(self, room_number, room_type, price_per_night, size_room, has_view):
        self.__my_session.add(
            Rooms(room_number=room_number, room_type=room_type, price_per_night=price_per_night, size_room=size_room,
                  has_view=has_view))
        self.__my_session.commit()

    def read_room(self):
        return self.__my_session.query(Rooms).all()

    def update_room(self, room_number, room_type=None, price_per_night=None, size_room=None, has_view=None):
        my_room = self.__my_session.query(Rooms).filter_by(room_number=room_number).first
        if my_room:
            self.__my_session.query(Rooms).filter_by(room_number=room_number).update({
                "room_type": f"{room_type or my_room.room_type}",
                "price_per_night": f"{price_per_night or my_room.price_per_night}",
                "size_room": f"{size_room or my_room.size_room}",
                "has_view": f"{has_view or my_room.has_view}",
            })
            self.__my_session.commit()

    def delete_room(self, room_number):
        self.__my_session.query(Rooms).filter_by(room_number=room_number).delete()
        self.__my_session.commit()

    def find_by_room_number(self, room_number):
        my_room = self.__my_session.query(Rooms).filter_by(room_number=room_number).first()
        return my_room

    def room_number_exists(self, room_number):
        my_room = self.__my_session.query(Rooms).filter_by(room_number=room_number).first()
        return True if my_room else False

    if __name__ == "__main__":
        from sqlalchemy import create_engine

        engine = create_engine('mysql+pymysql://root:@localhost:3306/Hotel_Management', echo=False)
        model = RoomSQLModel(engine=engine)

        model.create_room(123, "double", 100, 4, True)
        model.update_room(123, "double", "100", 4, False)

        for room in model.create_room():
            print(room)

        model.delete_room(123)
