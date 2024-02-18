"""
Módulo que contiene la clase Reservation para gestionar
las reservas de habitaciones en un hotel.
"""
import os
import json
import uuid


class Reservation:
    """
    Clase para gestionar reservas de habitaciones en un hotel.
    """

    def __init__(self, customer, hotel, reservation_data):

        self.customer = customer
        self.hotel = hotel
        self.room_number = reservation_data['room_number']
        self.check_in_date = reservation_data['check_in_date']
        self.check_out_date = reservation_data['check_out_date']
        # Generar un ID único para la reserva
        self.reservation_id = str(uuid.uuid4())

    def create_reservation(self):
        """
        Crea una nueva reserva y la guarda en un archivo JSON.

        Returns:
            str: Nombre del archivo de reserva creado.
        """
        self.hotel.reserve_room(self.room_number, self.customer.name,
                                self.check_in_date, self.check_out_date)
        try:
            reservation_data = {
                "reservation_id": self.reservation_id,
                "customer_name": self.customer.name,
                "customer_email": self.customer.email,
                "hotel_name": self.hotel.name,
                "room_number": self.room_number,
                "check_in_date": self.check_in_date,
                "check_out_date": self.check_out_date
            }
            filename = f"reservation_{self.reservation_id}.json"
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(reservation_data, file)
            print("Reserva creada correctamente.")
            return filename
        except FileNotFoundError as exception:
            print(f"Error al crear la reserva: {exception}")
            return None

    def cancel_reservation(self):
        """
        Cancela la reserva del cliente en el hotel.

        Returns:
            bool: True si la reserva se canceló correctamente,
            False en caso contrario.
        """
        try:
            # Elimina el archivo de reserva si existe
            filename = f"reservation_{self.reservation_id}.json"
            if os.path.exists(filename):
                os.remove(filename)
                print("Reserva cancelada correctamente.")

            return True
        except FileNotFoundError as exception:
            print(f"Error al cancelar la reserva: {exception}")
            return False
