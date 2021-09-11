from CSP import CSP as Mtz
from CurrentGenerator import CurrentGenerator
from CB import CircuitBreaker
from TT import Izmeritel

cb1 = CircuitBreaker('CB1')  # Создаем экземпляр класса выключателя
cb1.turn_breaker_on()  # Включаем выключатель
current_generator = CurrentGenerator()  # Создаем экзепляр класса генератора тока
current_generator.source = current_generator.create1stLevel(2)  # Выставляем режим КЗ
tt1 = Izmeritel('TT1', cb1, current_generator.source)  # Создаем ТТ
stupen1 = Mtz('stupen 1', 60, 1, tt1, cb1)  # Первая ступень ТСЗ
stupen2 = Mtz('stupen 2', 40, 5, tt1, cb1)  # Вторая ступень ТСЗ
stupen3 = Mtz('stupen 3', 10, 10, tt1, cb1)  # МТЗ
while cb1.get_state():
    tt1.measure()
    stupen1.run()
    stupen2.run()
    stupen3.run()
# Дз. 2 вариант
# Токовая защита еще делаем две ступени( всего 3 ступени)
# Уставки считать не надо.
