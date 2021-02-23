# Red neuronal para proyectar nuevos casos de diabetes
#### Créditos: Agragezco de ante mano a Jason Brownlee (compilador); al National Institute of Diabetes and Digestive and Kidney Diseases; y al investigador Vincent Sigillito de The John's Hopkins University por los datos y la ejemplificación de código.
#### NOTA: el archivo para entrenar esta red reuronal esta en la misma carpeta donde pertenece este script y se llama pima-indians-diabetes.csv


# Importar las librerías necesarias
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

#1- Número de embarazos
#2- Concentración de glucosa en la plasma sanguínea a 2 horas en una prueba oral
#3- Presión sanguínea diastólica (mm Hg)
#4- Espesor del pliegue cutáneo del tríceps (mm)
#5- Insulina sérica de 2 horas (mu U / ml)
#6- indíce de masa corporal (peso en kg/(altura en m)^2)
#7- Función del pedigrí de la diabetes (historial de prevalencia de diabetes en ascendencia consanguínea)
#8- Edad en años

#9- Variable dummy

# La última variable es dummy. Vamos a enseñarle a nuestro modelo a clasificar de acuerdo a dicha variable dicotomica

# Paso 1: cargar el dataset

# Carguemos el dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# (X) serán las variables explicativas y (y) la dicótomica
X = dataset[:,0:8]
y = dataset[:,8]

# Definamos el modelo de red neuronal más adecuado con la librería Keras
# El modelo espera columnas tal que tengamos 8 variables (input_dim=8),
# donde el primer layer oculto tiene 12 nodos y usa relu activation; el segundo layer oculto
# tiene 8 nodos y tambien usa relu actiation.
# El layer de salida tiene un nodo y usa la función simoide de activación

# definamos el modelo de keras
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilemos
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Hagamos el fit con el data que tenemos (training de la red neuronal)
model.fit(X, y, epochs=150, batch_size=10)

# Evaluemos la precisión del modelo
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# Juntemos todo y corramos

# Generemos nuestro llamado y seudonimos de las paqueterias a usar
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# carguemos el data set
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# Dividamos entre las variables input o explicativas y la y (binaria)
X = dataset[:,0:8]
y = dataset[:,8]
# Vamos a definir el modelo
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compilemos
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Hagamos el fit de la red neuronal con el dataset
model.fit(X, y, epochs=150, batch_size=10)
# Evaluemos la precisión del modelo
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))


# Limitemos a proyectar solo 5 casos
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
