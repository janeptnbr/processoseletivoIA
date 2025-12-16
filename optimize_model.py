import tensorflow as tf
import os

def main():
    # ===============================
    # 1. Verificar se o modelo existe
    # ===============================
    if not os.path.exists("model.h5"):
        raise FileNotFoundError(
            "Arquivo model.h5 não encontrado. "
            "Execute primeiro o script train_model.py."
        )

    # ===============================
    # 2. Carregar o modelo treinado
    # ===============================
    model = tf.keras.models.load_model("model.h5")

    # ===============================
    # 3. Criar o conversor TensorFlow Lite
    # ===============================
    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    # ===============================
    # 4. Aplicar otimização (Quantização)
    # ===============================
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    # ===============================
    # 5. Converter para formato TFLite
    # ===============================
    tflite_model = converter.convert()

    # ===============================
    # 6. Salvar o modelo otimizado
    # ===============================
    with open("model.tflite", "wb") as f:
        f.write(tflite_model)

    print("Modelo otimizado salvo com sucesso: model.tflite")

if __name__ == "__main__":
    main()
