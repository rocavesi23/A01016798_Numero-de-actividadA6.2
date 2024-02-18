"""
Este módulo contiene pruebas unitarias para la clase Reservation.
"""
import unittest
import os
from customer import Customer
from hotel import Hotel
from reservation import Reservation


class TestReservation(unittest.TestCase):
    """
    Pruebas unitarias para la clase Reservation.
    """

    def setUp(self):
        """
        Prepara el contexto necesario para las pruebas.
        """
        # Crear instancias de Customer y Hotel para usar en las pruebas
        self.customer = Customer("Ed Baldwin", "ed_baldwin@nasa.gov.us",
                                 "1234567890", "666 Happy Valley St")
        self.hotel = Hotel("California", "123 Main St", "1234567890")

    def test_create_reservation(self):
        """
        Verifica que se pueda crear una reserva correctamente.
        """
        print("\nPrueba de crear una reservación: Verificando que se "
              "pueda crear una reservación correctamente")

        reservation_data = {
            'room_number': "203",
            'check_in_date': "2024-02-15",
            'check_out_date': "2024-02-20"
        }

        # Crear una instancia de Reservation
        reservation = Reservation(self.customer, self.hotel, reservation_data)

        # Agregar aserciones para verificar que la reserva se creó
        # correctamente
        self.assertIsInstance(reservation, Reservation)
        self.assertEqual(reservation.customer, self.customer)
        self.assertEqual(reservation.hotel, self.hotel)
        self.assertEqual(reservation.room_number, "203")
        self.assertEqual(reservation.check_in_date, "2024-02-15")
        self.assertEqual(reservation.check_out_date, "2024-02-20")

        reservation.create_reservation()
        filename = f"reservation_{reservation.reservation_id}.json"
        self.assertTrue(os.path.exists(filename),
                        f"La reservación {reservation.reservation_id}"
                        f"no se pudo crear.")

        print("Prueba de crear una reservación: Verificando que NO se "
              "pueda crear una reservación para una habitación no "
              "existente.")

        # Agregamps los casos negativos
        reservation_data = {
            'room_number': "203",
            'check_in_date': "2024-02-15",
            'check_out_date': "2024-02-20"
        }

        # Crear una instancia de Reservation
        reservation = Reservation(self.customer, self.hotel, reservation_data)
        reservation.create_reservation()

        print("Prueba de crear una reservación: Verificando que NO se "
              "pueda crear una reservación con fechas inválidas.")

        # Agregamps los casos negativos
        reservation_data = {
            'room_number': "103",
            'check_in_date': "2024-02-20",
            'check_out_date': "2024-02-15"
        }

        # Crear una instancia de Reservation
        reservation = Reservation(self.customer, self.hotel, reservation_data)
        reservation.create_reservation()

    def test_cancel_reservation(self):
        """
        Verifica que se pueda cancelar una reserva correctamente.
        """
        print("Prueba de cancelar una reservación: Verificando que se "
              "pueda cancelar una reservación correctamente.")

        reservation_data = {
            'room_number': "203",
            'check_in_date': "2024-02-15",
            'check_out_date': "2024-02-20"
        }

        # Crear una instancia de Reservation
        reservation = Reservation(self.customer, self.hotel, reservation_data)

        # Llamar al método cancel_reservation y agregar aserciones para
        # verificar que la reserva se canceló correctamente
        self.assertTrue(reservation.cancel_reservation())
        # Agregar más aserciones según sea necesario


if __name__ == "__main__":
    # Crear una instancia de TestSuite
    suite = unittest.TestSuite()

    # Agregar los métodos de prueba a la suite en el orden deseado
    suite.addTest(TestReservation('test_create_reservation'))
    suite.addTest(TestReservation('test_cancel_reservation'))

    # Crear un TextTestRunner personalizado
    runner = unittest.TextTestRunner()

    # Ejecutar las pruebas
    runner.run(suite)
