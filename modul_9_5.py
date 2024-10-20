class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.stop = stop
        self.start = start
        self.step = step
        self.pointer = self.start
        if self.step == 0:
            raise StepValueError("шаг не может быть равен 0")

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        if self.start > self.stop:
            if self.step < 0:
                if self.pointer + self.step >= self.stop:
                    self.pointer += self.step
                else:
                    raise StopIteration
            else:
                raise StopIteration
        else:
            if self.step > 0:
                if self.pointer + self.step <= self.stop:
                    self.pointer += self.step
                else:
                    raise StopIteration
            else:
                raise StopIteration
        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print(' ')
except StepValueError:
    print('Шаг указан неверно')
except StopIteration:
    print("данная итерация невозможна")

try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
    print(' ')
except StepValueError:
    print('Шаг указан неверно')
except StopIteration:
    print("данная итерация невозможна")

try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
    print(' ')
except StepValueError:
    print('Шаг указан неверно')
except StopIteration:
    print("данная итерация невозможна")

try:
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
    print(' ')
except StepValueError:
    print('Шаг указан неверно')
except StopIteration:
    print("данная итерация невозможна")

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
    print(' ')
except StepValueError:
    print('Шаг указан неверно')
except StopIteration:
    print("данная итерация невозможна")
