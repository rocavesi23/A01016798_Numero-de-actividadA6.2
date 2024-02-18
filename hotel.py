"""
Este módulo define la clase Hotel, que gestiona la información y operaciones
relacionadas con un hotel, como crear, eliminar, modificar y mostrar
información sobre el hotel, así como reservar y cancelar habitaciones.
"""
import json
import os
from datetime import datetime


class Hotel:
    """
    Clase para representar un hotel.

    Attributes:
        name (str): El nombre del hotel.
        location (str): La ubicación del hotel.
        rooms (list): La lista de habitaciones disponibles en el hotel.
        reservations (dict): Un diccionario que mapea el número de
        habitación con la información de reserva.
    """

    def __init__(self, name, location, phone):
        """
        Inicializa una instancia de la clase Hotel.

        Args:
            name (str): El nombre del hotel.
            location (str): La ubicación del hotel.
        """
        self.name = name
        self.location = location
        self.phone = phone
        self.rooms = ['101', '102', '103']
        self.reservations = {}

    def create_hotel(self):
        """
        Crea un archivo JSON con la información del hotel.
        """
        hotel_data = {
            'name': self.name,
            'location': self.location,
            'phone': self.phone,
            'rooms': self.rooms,
            'reservations': self.reservations
        }
        with open(f"{self.name}_hotel.json", 'w', encoding='utf-8') as file:
            json.dump(hotel_data, file)

    def delete_hotel(self):
        """
        Elimina el archivo JSON del hotel.
        """
        file_name = f"{self.name}_hotel.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print(f"El archivo {file_name} no existe.")

    def display_hotel_info(self):
        """
        Muestra la información del hotel.
        """
        print(f"\tHotel: {self.name}")
        print(f"\tlocation: {self.location}")
        print(f"\tPhone: {self.phone}")
        print("\tAvailable rooms:")
        for room in self.rooms:
            print(f"\t\t{room}")

    def modify_hotel_info(self, name=None, location=None, phone=None):
        """
        Modifica la información del hotel.

        Args:
            name (str): El nuevo nombre del hotel (opcional).
            location (str): La nueva ubicación del hotel (opcional).
        """
        if not name or not location or not phone:
            raise ValueError("Todos los campos son obligatorios.")

        filename = f"{self.name}_hotel.json"
        self.name = name
        self.location = location
        self.phone = phone

        if os.path.exists(filename):
            with open(filename, 'r+', encoding='utf-8') as file:
                hotel_data = json.load(file)
                if name:
                    hotel_data['name'] = name
                if location:
                    hotel_data['location'] = location
                if phone:
                    hotel_data['phone'] = phone
                file.seek(0)
                json.dump(hotel_data, file)
                file.truncate()
        else:
            print(f"Hotel {self.name}_hotel.json not found.")

    def reserve_room(self, room_number, guest_name,
                     check_in_date, check_out_date):
        """
        Reserva una habitación en el hotel.

        Args:
            room_number (str): El número de la habitación a reservar.
            guest_name (str): El nombre del huésped que realiza la reserva.
            check_in_date (str): La fecha de entrada a la habitación.
            check_out_date (str): La fecha de salida de la habitación.
        """
        if datetime.strptime(check_out_date, '%Y-%m-%d') <= \
           datetime.strptime(check_in_date, '%Y-%m-%d'):
            print(f"\tLas fechas de reservación del {check_in_date}"
                  f" al {check_out_date} son incorrectas.")
            return False
        if room_number not in self.rooms:
            print(f"No existe la habitación {room_number}.")
            return False
        if room_number in self.reservations:
            print(f"\tLa habitación {room_number} ya está reservada.")
            return False
        self.reservations[room_number] = {
            'guest_name': guest_name,
            'check_in_date': check_in_date,
            'check_out_date': check_out_date
        }
        print(f"\tSe ha reservado la habitación {room_number} "
              f"para {guest_name} del {check_in_date} "
              f"al {check_out_date}.")

        return True

    def cancel_reservation(self, room_number):
        """
        Cancela una reserva existente.

        Args:
            room_number (str): El número de la habitación de la reserva
            que se desea cancelar.

        Returns:
            bool: True si la reserva fue cancelada exitosamente,
            False de lo contrario.
        """
        print(f"Cancelando reserva {room_number}")
        if len(self.reservations) == 0 or not self.reservations[room_number]:
            print(f"No existe una reserva para la habitación {room_number}.")
            return False
        del self.reservations[room_number]
        print(f"La reserva para la habitación {room_number} "
              "ha sido cancelada.")
        return True
