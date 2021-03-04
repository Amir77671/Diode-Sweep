import pyvisa
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager()
multimetr = rm.open_resource('GPIB0::10::INSTR')
zasilacz = rm.open_resource('GPIB0::9::INSTR')
multimetr.timeout = 1000
zasilacz.timeout = 1000

napiecie = []
prad = []
zasilacz.write('INST:SEL P6V')
zasilacz.write('VOLT 0')
zasilacz.write('OUTPUT ON')
for i in range(900):
    zasilacz.write(f'VOLT {i/20}')
    zasilacz.query('*OPC?')
    napiecie.append(float(multimetr.query('MEAS:VOLT?')))
    prad.append(float(zasilacz.query('MEAS:CURR?')))
    print(napiecie[-1], prad[-1])
zasilacz.write('VOLT 0')
zasilacz.write('OUTPUT OFF')




plt.plot(napiecie, prad)
plt.ylabel('prad')
plt.xlabel('napiecie')
plt.show()