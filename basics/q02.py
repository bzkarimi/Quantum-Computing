#!/usr/bin/env python 

'''
Quantum Teleportation
q0 ---> q2 using q1
'''

from qiskit import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from qiskit.visualization import plot_histogram

show = 'plot'

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3,3)
circuit.x(0)
circuit.barrier()
# q1 and q2 entanglement
circuit.h(1)
circuit.cx(1, 2)

circuit.cx(0, 1)
circuit.h(0)
circuit.barrier()
circuit.measure([0,1], [0,1])
circuit.barrier()

circuit.cx(1, 2)
circuit.cz(0, 2)

circuit.measure(2,2)
job = execute(circuit, simulator, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
plot_histogram(counts)
print(counts)
if (show == 'plot'):
    circuit.draw(output='mpl')
    plt.show()
elif (show == 'terminal'):
    print(circuit.draw())
