import random
import copy


def GenerateParity(information):
    parity = 0
    for i in range(len(information)):
        if information[i] == 1:
            parity = 1 - parity

    return parity


def ErrorChannel(coded):
    received = copy.copy(coded)
    flag = 0
    for i in range(len(coded) - 1):
        rand = random.random()
        x = rand
        if flag == 1:
            flag = 0
        elif (x <= 0.1) & (flag == 0):
            received[i] = 1 - received[i]
            received[i + 1] = 1 - received[i + 1]
            flag = 1
    return received

def CheckParity(received):
    parity = 0
    for i in range(len(received)):
        if received[i] == 1:
            parity = 1 - parity

    if parity == 0:
        return True
    else:
        return False


result = [0, 0, 0]

for tem in range(100000):
    print tem
    information = []
    infolength = 6
    for i in range(infolength):
        rand = random.randint(0, 1)
        information.append(rand)
    parity = GenerateParity(information)

    coded = copy.copy(information)
    coded.append(parity)
    received = ErrorChannel(coded)
    check = CheckParity(received)

    if (coded == received) & check:
        # If coded == received, no error happens. The count of event A is increased by 1
        result[0] = result[0] + 1
    elif (coded != received) & check:
        # If coded != received, and check==True (i.e., the parity check thinks that there is no error. ),
        # error happens but it is not detected by the parity check. The count of event C is increased by 1.
        result[1] = result[1] + 1
    elif (coded != received) & (not check):
        # If coded != received, and check==False (i.e., the parity check thinks that there is an error. ),
        # error happens and it is detected by the parity check. The count of event B is increased by 1.
        result[2] = result[2] + 1

print 'Event PA probability', float(result[0]) / float(sum(result))
# print 'Event PC probability', float(result[1]) / float(sum(result))
# print 'Event PB probability', float(result[2]) / float(sum(result))




