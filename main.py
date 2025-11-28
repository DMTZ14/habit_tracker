'''
from models import HabitTracker, Session
from validators import is_valid_date, is_valid_category
from stats import (
    get_minutes_by_habit,
    get_minutes_by_category,
    get_top_habits,
    get_global_stats,
)
import datetime
'''

def main():
      menu()

def menu():
    print("===HabitForge: Gestor de Hábitos===\n"
          "1. Registrar nueva sesión\n"
          "2. Ver resumen de hoy\n"
          "3. Ver resumen por rango de fechas\n"
          "4. Ver estadísticas globales\n"
          "5. Exportar resumen a archivo\n"
          "6. Salir\n"
          "Selecciona una opción: ", end="")
    return input()


if __name__ == "__main__":
      main()