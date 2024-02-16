class Guest:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone})"


class Room:
    def __init__(self, number, capacity, rate_per_night, is_occupied=False):
        self.number = number
        self.capacity = capacity
        self.rate_per_night = rate_per_night
        self.is_occupied = is_occupied
        self.guests = []

    def add_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            self.is_occupied = True
            print(f"Guest {guest.name} has been added to Room {self.number}.")
        else:
            print(f"Room {self.number} is already at full capacity.")

    def remove_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)
            if len(self.guests) == 0:
                self.is_occupied = False
            print(f"Guest {guest.name} has been removed from Room {self.number}.")
        else:
            print(f"Guest {guest.name} is not in Room {self.number}.")

    def __str__(self):
        status = "Occupied" if self.is_occupied else "Vacant"
        return f"Room {self.number}, Capacity: {self.capacity}, Status: {status}"


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.number] = room
        print(f"Room {room.number} has been added to {self.name}.")

    def remove_room(self, room_number):
        if room_number in self.rooms:
            del self.rooms[room_number]
            print(f"Room {room_number} has been removed from {self.name}.")
        else:
            print(f"Room {room_number} does not exist in {self.name}.")

    def check_in_guest(self, guest, room_number):
        room = self.rooms.get(room_number)
        if room:
            if not room.is_occupied:
                room.add_guest(guest)
            else:
                print(f"Room {room_number} is already occupied.")
        else:
            print(f"Room {room_number} does not exist in {self.name}.")

    def check_out_guest(self, guest, room_number):
        room = self.rooms.get(room_number)
        if room:
            room.remove_guest(guest)
        else:
            print(f"Room {room_number} does not exist in {self.name}.")

    def display_available_rooms(self):
        available_rooms = [room for room in self.rooms.values() if not room.is_occupied]
        if available_rooms:
            for room in available_rooms:
                print(room)
        else:
            print("No vacant rooms available.")

    def display_all_rooms(self):
        for room in self.rooms.values():
            print(room)


if __name__ == "__main__":
    hotel = Hotel("My Hotel")

    room101 = Room(101, 2, 100)
    hotel.add_room(room101)

    room102 = Room(102, 4, 150)
    hotel.add_room(room102)

    guest1 = Guest("John Doe", "john@example.com", "1234567890")
    guest2 = Guest("Jane Smith", "jane@example.com", "9876543210")

    hotel.check_in_guest(guest1, 101)
    hotel.check_in_guest(guest2, 102)

    hotel.display_available_rooms()

    hotel.check_out_guest(guest1, 101)

    hotel.display_all_rooms()
