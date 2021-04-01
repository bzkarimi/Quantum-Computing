#!/usr/bin/env python 

'''
Visualization of state vector
'''

from qiskit import *
import matplotlib.pyplot as plt
from qiskit.tools.visualization import plot_bloch_multivector

circuit = QuantumCircuit(1,1)
circuit.x(0)
simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
print(statevector)
circuit.draw(output='mpl')
plt.show()
plot_bloch_multivector(statevector)
plt.show()
