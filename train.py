from tensorflow import keras

from get_data_azure_sql import get_data

iris_features, iris_label = get_data()

x = keras.utils.to_categorical(iris_label)

model = keras.models.Sequential()
model.add(keras.layers.Dense(32, activation='relu', input_shape=(4,)))
model.add(keras.layers.Dense(32, activation='relu'))
model.add(keras.layers.Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(iris_features, x, epochs=100, batch_size=32)

model.save('mymodel.h5')
